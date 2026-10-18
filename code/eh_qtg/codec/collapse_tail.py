"""Collapse-generated horizon tail (Paper F): stage N (nonlinear double-null collapse to v1) + stage L (linear l=0 scalar on the static exterior to large v).
usage: python3 collapse_tail.py model mass h_N h_L v1 vmax out.npz        (A is tuned so that the generalised mass on u=u0 after the pulse equals `mass`)"""
import sys, numpy as np, time
from scipy.interpolate import CubicSpline
import pipeline as P
from pipeline import *
import tail_L
def make_table(model,mass,hN,hL,v1,vmax,Lh=None,A=None,verbose=True,tail=None):
    L2=1.0
    if A is None: A=tune_A(model,L2,mass,tail=tail)
    u,v,row0,col0,ph=rays(model,L2,P.U0,P.UEND,P.V0,v1,hN,hN,A,P.VA,P.VB,tail=tail)
    out,snap,ah=run(model,L2,row0,col0,hN,hN,[0],rows=[len(v)-1])
    R,SG,RU,RV,SU,SV,PU,PV=snap[0]; ok=np.isfinite(R)&np.isfinite(PU)&np.isfinite(RU)
    bg=Static(model,mass,L2)
    phi=CubicSpline(u[ok],PU[ok]).antiderivative()(u[ok]); Rk=R[ok]; PUk=PU[ok]; RUk=RU[ok]
    if tail is not None:                             # phi(u0,v1) is the value of the non-compact tail at the corner (0 for a compact pulse)
        from collapse_lib import np_tail
        phi=phi+np_tail(*tail)[0](Rk[0])
    sel=Rk>bg.rp-1.0                                 # exterior plus a layer inside the horizon: phi(r), psi(r) are smooth across r_+
    rr=Rk[sel][::-1]; csp=CubicSpline(rr,(Rk*phi)[sel][::-1])
    if Lh is None: Lh=9.5/bg.kp/2
    x0=bg.rstar_y(np.log(Rk[0]-bg.rp))
    di=int(round(2*(x0+Lh)/hL)); nv=int(round(vmax/hL))+1; nu=di+nv+2
    xrow=x0-hL/2*np.arange(nu); rrow=bg.r_of_rstar(xrow)
    psirow=csp(rrow)
    if tail is None: colv=0.0
    else:                                            # non-compact part of the data on u=u0 beyond v1: psi=r*phi=r*T(r), r(r*) of the static exterior
        from collapse_lib import np_tail
        assert tail[1]+tail[2]<=Rk[0]+1e-9, 'ramp of the tail must end before r(u0,v1)'
        Tf=np_tail(*tail)[0]; rc=bg.r_of_rstar(x0+hL/2*np.arange(nv)); colv=rc*Tf(rc)
    t,phiH,last=tail_L.run_L(bg,xrow,psirow,hL,vmax,Lh,psi_col_val=colv)
    v1e=2*x0
    # row profile for the interior layer (phi_r on the row v1): g(r)=PU/RU
    ex=(Rk<bg.rp+0.5)&(Rk>6.0); g=(PUk/RUk)[ex][::-1]; rg=Rk[ex][::-1]
    return dict(b=0.0 if tail is None else tail[0],A=A,mass=mass,model=model,v1e=v1e,t=t,phiH=phiH,x0=x0,rp=bg.rp,kp=bg.kp,rg=rg,g=g,mf=ms_mass(model,L2,R[0],SG[0],RU[0],RV[0]))
if __name__=='__main__':
    model=int(sys.argv[1]); mass=float(sys.argv[2]); hN=float(sys.argv[3]); hL=float(sys.argv[4]); v1=float(sys.argv[5]); vmax=float(sys.argv[6]); fn=sys.argv[7]
    t0=time.time(); d=make_table(model,mass,hN,hL,v1,vmax)
    np.savez_compressed(fn,**{k:np.asarray(v) for k,v in d.items()})
    print('A=%.8f mf=%.8f v1e=%.4f rp=%.6f kp=%.7f  phiH(0)=%.5e  %.0fs'%(d['A'],d['mf'],d['v1e'],d['rp'],d['kp'],d['phiH'][0],time.time()-t0))
