import sys, numpy as np, time
from scipy.interpolate import CubicSpline
from collapse_lib import *
import tail_L
from tail_L import Static
U0,UEND,V0,VA,VB=0.0,29.5,40.0,44.0,52.0
def mass_u0(model,L2,A,n=4000,tail=None):
    """generalized mass on the ray u=u0 after the pulse (ray ODE only)"""
    u,v,row0,col0,ph=rays(model,L2,U0,UEND,V0,V0+1.5*V0,0.05*V0/40,0.05*V0/40,A,VA,VB,tail=tail)
    R,SG,RU,RV=col0[0][-1],col0[1][-1],col0[2][-1],col0[3][-1]
    return ms_mass(model,L2,R,SG,RU,RV)
def tune_A(model,L2,m_target,A0=0.03,tail=None):
    f=lambda A:mass_u0(model,L2,A,tail=tail)-m_target
    a,b=0.8*A0,1.2*A0
    for _ in range(60):
        c=0.5*(a+b)
        if f(a)*f(c)<=0: b=c
        else: a=c
    return 0.5*(a+b)
def stageN(model,L2,A,h,v1,rows=None,tail=None):
    u,v,row0,col0,ph=rays(model,L2,U0,UEND,V0,v1,h,h,A,VA,VB,tail=tail)
    nu=len(u); out,snap,ah=run(model,L2,row0,col0,h,h,[0,nu//2],rows=[len(v)-1] if rows is None else rows)
    return u,v,snap,out,ah
def row_to_psi(model,L2,u,snap,mf):
    R,SG,RU,RV,SU,SV,PU,PV=snap[0]
    phi=CubicSpline(u,PU).antiderivative()(u)       # phi(u0,v1)=0
    bg=Static(model,mf,L2)
    return bg,R,phi
def build_L_row(bg,R,phi,h_L,nu_extra=0):
    ok=R>bg.rp*(1+1e-12)
    x=np.array([bg.rstar_y(np.array([np.log(R[i]-bg.rp)]))[0] for i in range(len(R))]) if False else None
    x=bg.rstar_y(np.log(R[ok]-bg.rp)); psi=R[ok]*phi[ok]
    x0=x[0]; xs=x[::-1]; ps=psi[::-1]                   # increasing x
    cs=CubicSpline(xs,ps)
    return x0,xs[0],cs
def stageL(model,L2,mf,u,snap,hL,vmax_rel,Lh=None,A=None,tail=None):
    R,SG,RU,RV,SU,SV,PU,PV=snap[0]
    ok=np.isfinite(R)&np.isfinite(PU)
    bg=Static(model,mf,L2)
    phi=CubicSpline(u[ok],PU[ok]).antiderivative()(u[ok]); Rok=R[ok]
    if tail is not None:
        from collapse_lib import np_tail
        phi=phi+np_tail(*tail)[0](Rok[0])         # phi(u0,v1): value of the non-compact tail at the corner
    ex=Rok>bg.rp*(1+1e-9)
    x=bg.rstar_y(np.log(Rok[ex]-bg.rp)); psi=Rok[ex]*phi[ex]
    xs=x[::-1]; ps=psi[::-1]; cs=CubicSpline(xs,ps)
    x0=x[0]                                      # r* at the boundary ray u0 (largest r*)
    if Lh is None: Lh=9.5/bg.kp/2*1.0           # e^{2 kappa r*} ~ 5e-9
    di=int(round(2*(x0+Lh)/hL)); nv=int(round(vmax_rel/hL))+1; nu=di+nv+2
    xrow=x0-hL/2*np.arange(nu)
    psirow=np.where(xrow>=xs[0],cs(np.maximum(xrow,xs[0])),ps[0])   # constant (horizon-regular) extension beyond the last data point
    colv=0.0
    if tail is not None:
        from collapse_lib import np_tail
        nvv=int(round(vmax_rel/hL))+1; rc=bg.r_of_rstar(x0+hL/2*np.arange(nvv)); colv=rc*np_tail(*tail)[0](rc)
    t,phiH,last=tail_L.run_L(bg,xrow,psirow,hL,vmax_rel,Lh,psi_col_val=colv)
    stageL.last=(xrow,last)
    return bg,t,phiH,x0,xs[0]
