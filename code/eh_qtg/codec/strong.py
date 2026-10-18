"""Collapse of a scalar pulse into an existing Hayward/Schwarzschild hole of mass m0 (Paper F, strong pulses): stage N with the static-hole start of
collapse_lib.rays(m0=...), stage L with the static exterior of the final mass.  The geometry scales with s=max(1,m_target/5): corner radius r_c=20 s
(v0=40 s, u0=0), pulse on v0+[4,12] s, v1=v0+20 s, h_N=h0 s; the data on v=v0 end at r_end=r_+(m0)+dr (exterior of the old hole only: deeper cells
are amplified by the interior instability of the static hole and are not needed).  m0=0 with uend=29.5 s is the earlier setup."""
import sys, os, numpy as np
from collapse_lib import *
from scipy.interpolate import CubicSpline
import tail_L
from tail_L import Static
L2=1.0
def geom(m0,mt,dr=None):
    dr=float(os.environ.get('STRONG_DR','0.1')) if dr is None else dr   # r_end=r_+(m0)+dr on the old-hole ray (negative: also cover an event horizon that lies inside r_+(m0)+0.1, weak pulses)
    s=max(1.0,mt/5.0); v0=40.0*s
    if m0>0:
        rp0=Static(1,m0,L2).rp; uend=2*(20.0*s-(rp0+dr))
    else: uend=29.5*s
    pa=float(os.environ.get('PULSE_A','4')); pb=float(os.environ.get('PULSE_B','12')); v1r=float(os.environ.get('PULSE_V1','20'))  # pulse window and v1-v0 in units of s (defaults: the Paper F setup)
    return dict(s=s,u0=0.0,uend=uend,v0=v0,va=v0+pa*s,vb=v0+pb*s,v1=v0+v1r*s)
def mass_after(model,m0,g,A,h=None,tail=None):
    h=0.05*g['s'] if h is None else h
    u,v,row0,col0,ph=rays(model,L2,g['u0'],g['uend'],g['v0'],g['v0']+60*g['s'],h,h,A,g['va'],g['vb'],m0=m0,tail=tail)
    return float(ms_mass(model,L2,col0[0][-1],col0[1][-1],col0[2][-1],col0[3][-1])), col0
def tune_A_m(model,m0,g,mt,A0,tail=None):
    f=lambda A:mass_after(model,m0,g,A,tail=tail)[0]-mt
    a,b=0.0,A0
    while f(b)<0: b*=1.5
    for _ in range(60):
        c=0.5*(a+b)
        if f(a)*f(c)<=0: b=c
        else: a=c
    return 0.5*(a+b)
def stageN_h(model,m0,g,A,h):
    u,v,row0,col0,ph=rays(model,L2,g['u0'],g['uend'],g['v0'],g['v1'],h,h,A,g['va'],g['vb'],m0=m0)
    nu=len(u); out,snap,ah=run(model,L2,row0,col0,h,h,[0],rows=[len(v)-1])
    return u,v,row0,col0,snap,ah
def make_table_h(model,m0,mt,h0,hL,vrel,Lh=None,A=None,verbose=True,tail=None):
    """Horizon table of the collapse of a pulse into a hole of mass m0 with final mass mt: h_N=h0*s, vmax=vrel*s (v-v1).  Returns a dict like collapse_tail.make_table plus Q=int r^2 phi_v dv on u0."""
    g=geom(m0,mt); s=g['s']
    if A is None: A=tune_A_m(model,m0,g,mt,0.03,tail=tail)
    hN=h0*s
    u,v,row0,col0,ph=rays(model,L2,g['u0'],g['uend'],g['v0'],g['v1'],hN,hN,A,g['va'],g['vb'],m0=m0,tail=tail)
    out,snap,ah=run(model,L2,row0,col0,hN,hN,[0],rows=[len(v)-1])
    mf=float(ms_mass(model,L2,col0[0][-1],col0[1][-1],col0[2][-1],col0[3][-1]))
    R,SG,RU,RV,SU,SV,PU,PV=snap[0]; ok=np.isfinite(R)&np.isfinite(PU)&np.isfinite(RU)
    bg=Static(model,mf,L2)
    phi=CubicSpline(u[ok],PU[ok]).antiderivative()(u[ok]); Rk=R[ok]
    if tail is not None: phi=phi+np_tail(*tail)[0](Rk[0])      # phi(u0,v1): the non-compact tail at the corner
    sel=Rk>bg.rp-1.0
    nb=np.where(~(np.diff(Rk)<0))[0]   # cut at the first non-monotone cell (garbage of the amplified deep cells)
    if len(nb): sel[nb[0]+1:]=False
    rr=Rk[sel][::-1]; csp=CubicSpline(rr,(Rk*phi)[sel][::-1])
    if Lh is None: Lh=9.5/bg.kp/2
    x0=bg.rstar_y(np.log(Rk[0]-bg.rp)); vmax=vrel*s
    di=int(round(2*(x0+Lh)/hL)); nv=int(round(vmax/hL))+1; nu=di+nv+2
    xrow=x0-hL/2*np.arange(nu); psirow=csp(bg.r_of_rstar(xrow))
    colv=0.0
    if tail is not None:
        rc=bg.r_of_rstar(x0+hL/2*np.arange(nv)); colv=rc*np_tail(*tail)[0](rc)
    t,phiH,last=tail_L.run_L(bg,xrow,psirow,hL,vmax,Lh,psi_col_val=colv)
    # charge on the ray u0 (pulse) from a fine ray integration
    uu,vv,r0_,c0,ph_=rays(model,L2,g['u0'],g['uend'],g['v0'],g['v0']+30*s,0.02*s,0.02*s,A,g['va'],g['vb'],m0=m0)
    Q=float(np.trapezoid(c0[0]**2*c0[7],vv)) if tail is None else float('nan')
    return dict(A=A,m0=m0,mt=mt,mf=mf,s=s,model=model,v1e=2*x0,t=t,phiH=phiH,x0=x0,rp=bg.rp,kp=bg.kp,Q=Q,ah=ah[-1],nu=len(u),rend=Rk[-1],rrow0=Rk[0])
