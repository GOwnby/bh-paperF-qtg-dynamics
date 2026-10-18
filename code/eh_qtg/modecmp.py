"""Two discretisations of the same equations (Paper F, independent check of the constrained scheme).  Mode 2 updates r with the r_uv equation (Q(psi)), mode 3 does not use it (r from r_v=-rho along each column);
both integrate the Raychaudhuri equations for r_u, r_v.  If both converge to the same limit the r_uv equation is satisfied by the solution that the Raychaudhuri-integrals produce.
Hayward h, B, k=3/2, m=5, rays U~0.3,0.6,1.0,1.2, isotropic meshes h_s=h_v; Romberg in h^2.  usage: modecmp.py B v1 h1 h2 ..."""
import os, sys, numpy as np, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0,os.environ.get('QTG_CODE','..'))
from dnU_qtg import *
from qtg_lib import run_stream_cy, coef
B=float(sys.argv[1]); v1=float(sys.argv[2]); hs_=[float(x) for x in sys.argv[3:]]
S=StaticU(5.0); kp=S.kp; c=0.2*np.exp(-kp*v1); Uq=[0.3,0.6,1.0,1.2]; vq=np.arange(20,v1-1.9,1.0)
sq=[float(np.round(np.log(1+x*kp/c)/kp/0.05)*0.05) for x in Uq]
res={}
for mode in (2,3):
    for h in hs_:
        d=build_eh_q(S,1,1.0,1.5,v1,h,h,B,k=1.5,c=c,vH=v1+300)
        cols=[int(round(s/h)) for s in sq]; out=run_stream_cy(1,1.0,d['row0'],d['col0'],h,h,cols,mode=mode)
        ii=[int(round(x/h)) for x in vq]; res[(mode,h)]=out[:,ii,:]; print('mode',mode,'h',h,'nan',int(np.isnan(out).sum()),flush=True)
def rom(mode):
    T=[[res[(mode,h)] for h in hs_]]
    for lev in range(1,len(hs_)): T.append([(4**lev*T[-1][i+1]-T[-1][i])/(4**lev-1) for i in range(len(T[-1])-1)])
    return T
T2=rom(2); T3=rom(3)
names=['r','sg','rs','rv','sgs','sV','Ps','PV']
print('\nRay U~1.0 (index 2): extrapolated sigma_v, z=1-psi and r, mode 2 vs mode 3 (top Romberg level); differences; inter-level error of mode 3')
print('  v    sV(mode3)     sV(m2)-sV(m3)   z(mode3)    z(m2)/z(m3)-1   r(m3)-r_-    r(m2)-r(m3)   err_sV(m3)')
def zr(a):
    r,sg,rs,rv=a[2,:,0],a[2,:,1],a[2,:,2],a[2,:,3]; W=np.exp(sg); psi=(1+4*(-rs/W)*(-rv))/r**2; return 1-psi,r
a3=T3[-1][0]; a2=T2[-1][0]; z3,r3=zr(a3); z2,r2=zr(a2); e3=np.abs(T3[-1][0][2,:,5]-T3[-2][-1][2,:,5])
for vv in (30,40,50,60,70,80,90,100,105):
    j=int(np.argmin(abs(vq-vv)))
    print('%4d  %+.7f   %+.2e      %.4e   %+.2e       %+.2e   %+.2e   %.1e'%(vv,a3[2,j,5],a2[2,j,5]-a3[2,j,5],z3[j],z2[j]/z3[j]-1,r3[j]-1.057475,r2[j]-r3[j],e3[j]))
