"""Near-extremal Hayward (Paper A endpoint M*=3 sqrt3/4 l): linear l=0 horizon field of an ingoing pulse, stage L (tail_L).  usage: nearext.py tmax h m1 m2 ..."""
import sys,numpy as np
sys.path.insert(0,'.')
from tail_L import Static,run_L
tmax=float(sys.argv[1]); h=float(sys.argv[2])
for ms in sys.argv[3:]:
    m=float(ms); bg=Static(1,m,1.0); Lh=9.5/(2*bg.kp)
    x0=0.0; di=int(round(2*(x0+Lh)/h)); nv=int(round(tmax/h))+1; nu=di+nv+2
    xrow=x0-h/2*np.arange(nu); v=h*np.arange(nv)
    col=np.exp(-((v-30)/6.0)**2)
    t,phiH,last=run_L(bg,xrow,np.zeros(nu),h,h*(nv-1),Lh,psi_col_val=col)
    out=[]
    for T in (50,100,200,400,800,1600,3200,6400,12800,25600):
        if T>tmax: break
        k=np.searchsorted(t,T); w=slice(max(k-int(0.1*T/h),0),k+int(0.1*T/h)); 
        out.append('%d: t2phi=%.2e t3phi=%.2e'%(T,np.mean(phiH[w])*T**2,np.mean(phiH[w])*T**3))
    print('m=%.4f kappa+=%.4f Lh=%.0f | '%(m,bg.kp,Lh)+' | '.join(out),flush=True)
