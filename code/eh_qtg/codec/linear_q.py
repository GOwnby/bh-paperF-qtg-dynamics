"""Coefficient of the compact-data (k=3) tail in the linear problem: B_lin against 8 M |Q|, Q = int r^2 dphi along the ray u=u0 (the charge of the shift symmetry phi -> phi + c).
Angelopoulos-Aretakis-Gajic (2018): phi_H ~ -8 I_0^(1) v^-3; for l=0 data, I_0^(1) = -M Q is tested here.   usage: python3 linear_q.py model mass_factor hL vmax"""
import sys; sys.path.insert(0,'.')
import numpy as np, pipeline as P
from pipeline import *
from scipy.interpolate import interp1d
from scipy.optimize import least_squares
def a3fit(t,f,B0,lo,hi,npar):
    m=(t>=lo)&(t<=hi); x=t[m]; y=f[m]*x**3
    def res(p):
        q=1+p[1]/x
        if npar>=3: q=q+p[2]*np.log(x)/x
        if npar>=5: q=q+p[3]/x**2+p[4]*np.log(x)/x**2
        return p[0]*q-y
    return least_squares(res,[B0]+[0.0]*(npar-1),x_scale=[B0]+[10]*(npar-1)).x[0]
if __name__=='__main__':
    model=int(sys.argv[1]); fac=float(sys.argv[2]); hL=float(sys.argv[3]); vmaxrel=float(sys.argv[4])
    A=0.0300301*fac; m=None
    u,v,row0,col0,ph=rays(model,1.0,P.U0,P.UEND,P.V0,P.V0+vmaxrel,0.1,0.1,A,P.VA,P.VB)
    r=col0[0]; mm=ms_mass(model,1.0,col0[0],col0[1],col0[2],col0[3]); m=mm[-1]; bg=Static(model,m,1.0)
    Q=np.trapezoid(r**2*col0[7],v)
    x=bg.rstar_y(np.log(r-bg.rp)); ve=2*x; x0=x[0]; vstart=ve[0]
    nv=int(round((ve[-1]-vstart)/hL)); tl=vstart+hL*np.arange(nv)
    tl=tl[tl<=ve[-1]]; nv=len(tl)
    vof=interp1d(ve,v,kind='cubic'); phi_col=ph(vof(tl))
    rcol=interp1d(ve,r,kind='cubic')(tl); col=rcol*phi_col
    Lh=9.5/bg.kp/2; di=int(round(2*(x0+Lh)/hL)); nu=di+nv+2
    xrow=x0-hL/2*np.arange(nu); psirow=np.zeros(nu)
    t_,phiH,last=tail_L.run_L(bg,xrow,psirow,hL,hL*(nv-1),Lh,psi_col_val=col)
    print('model %d A/A0=%.2f m=%.5f Q=%.5f  8 m|Q|=%.4f'%(model,fac,m,Q,8*m*abs(Q)))
    for lo in (800,1600,3200):
        B=[a3fit(t_,phiH,8*m*abs(Q),lo,t_[-1]-5,n) for n in (2,3,5)]
        print('  window [%d,end]: B_lin (forms c1 | +ln | +1/t^2) = %s   ratio to 8m|Q| = %s'%(lo,' '.join('%.4f'%b for b in B),' '.join('%.5f'%(b/(8*m*abs(Q))) for b in B)),flush=True)
