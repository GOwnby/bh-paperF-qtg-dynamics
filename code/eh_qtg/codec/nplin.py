"""Linear test of the nonzero-Newman-Penrose-constant tail on a static exterior (Paper F, Sec. collapse, k=2).
Data: psi=0 on v=v1, psi=b*w(r)/r on the outgoing ray u=u0 (w a C^3 ramp from 0 to 1 over [r_a,r_b]); NP constant I0=lim r^2 d_r(r phi)=-b.
Angelopoulos-Aretakis-Gajic (2018): phi|_H ~ 4 I0 v^-2.   usage: python3 nplin.py model mass h vmax [b]"""
import sys, numpy as np
from tail_L import Static, run_L
import tail_L
def smooth(x):
    x=np.clip(x,0,1); return x**4*(35-84*x+70*x**2-20*x**3)
def run(model,m,h,vmax,b=1.0,ra=None,dr=10.0,x0=None):
    bg=Static(model,m,1.0)
    if x0 is None: x0=bg.rstar(np.array([25.0]))[0]
    r0=bg.r_of_rstar(np.array([x0]))[0]; ra=r0 if ra is None else ra
    Lh=9.5/bg.kp/2; di=int(round(2*(x0+Lh)/h)); nv=int(round(vmax/h))+1; nu=di+nv+2
    xrow=x0-h/2*np.arange(nu); psirow=np.zeros(nu)
    rc=bg.r_of_rstar(x0+h/2*np.arange(nv)); col=b*smooth((rc-ra)/dr)/rc
    t,phiH,last=run_L(bg,xrow,psirow,h,vmax,Lh,psi_col_val=col)
    return bg,2*x0,t,phiH
if __name__=='__main__':
    model=int(sys.argv[1]); m=float(sys.argv[2]); h=float(sys.argv[3]); vmax=float(sys.argv[4]); b=float(sys.argv[5]) if len(sys.argv)>5 else 1.0
    bg,v1e,t,phiH=run(model,m,h,vmax,b)
    np.savez_compressed('nplin_m%d_M%g_h%g.npz'%(model,m,h),t=t[::int(round(1/h))],phiH=phiH[::int(round(1/h))],v1e=v1e,b=b)
    for T in (100,200,400,800,1600,3200,6400,12800):
        if T+2<=vmax:
            i=int(round(T/h)); print('t=%5d  phi_H t^2/(-4b)=%.5f'%(T,phiH[i]*T**2/(-4*b)), ' local index=%.4f'%(-np.log(abs(phiH[i+int(1/h)]/phiH[i-int(1/h)]))/np.log((T+1)/(T-1))))
