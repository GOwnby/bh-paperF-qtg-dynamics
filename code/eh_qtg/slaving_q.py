"""Structure behind the front (Paper F, Section 'Behind the front'): snapshots of the constrained QTG run (Hayward h, B, k=3/2, m=5) at rows v=const.
Tests (a) u-independence of phi_v, rho=-r_v and sigma_v behind/ahead of the front, (b) the plateau balance  rho_v = -kappa_- rho + S,  S = 4 pi r c1 phi_v^2,
(c) y rho = beta = (psi r^2 - 1)/4 (exact), (d) the closed form  dm/dv = 2 r beta (kappa_- + G)/c1_II  against the direct 8 pi r^2 y phi_v^2.
usage: slaving_q.py B hs hv v1 v_1 v_2 ...   (QTG_CODE = directory with qtg_lib.py)"""
import os, sys, numpy as np, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0,os.environ.get('QTG_CODE','..'))
from dnU_qtg import *
from qtg_lib import run_stream_cy, coef
B=float(sys.argv[1]); hs=float(sys.argv[2]); hv=float(sys.argv[3]); v1=float(sys.argv[4]); vs=[float(x) for x in sys.argv[5:]]
S=StaticU(5.0); kp=S.kp; c=0.2*np.exp(-kp*v1)
d=build_eh_q(S,1,1.0,1.5,v1,hs,hv,B,k=1.5,c=c,vH=v1+300)
out,snap=run_stream_cy(1,1.0,d['row0'],d['col0'],hs,hv,[0],rows=[int(round(x/hv)) for x in vs])
U=d['U']; print('B=%g hs=%g hv=%g v1=%g  kappa_+=%.8f'%(B,hs,hv,v1,kp))
for k,vv in enumerate(vs):
    r,sg,rs,rv,sgs,sV,Ps,PV=snap[k]; W=np.exp(sg); y=-rs/W; rho=-rv; psi=(1+4*y*rho)/r**2; z=1-psi; x=U*np.exp(kp*vv)
    c1=np.array([float(coef(1,1.0,p)[1]) for p in psi]); Sx=4*np.pi*r*c1*PV**2
    def rng(a,m): return (np.nanmax(a[m])-np.nanmin(a[m]))/abs(np.nanmean(a[m]))
    mPh=(x>=10)&(x<=2e4); mRh=(x>=40)&(x<=2e4)
    iP=int(np.argmin(abs(x-25))); iIII=int(np.argmin(abs(x-3000))); kap=-sV[iP]; G=sV[iIII]
    beta=(psi[iIII]*r[iIII]**2-1)/4; c1II=c1[iP]
    pred=2*r[iIII]*beta*(kap+G)/c1II; direct=8*np.pi*r[iIII]**2*y[iIII]*PV[iIII]**2
    print('--- v=%g: front at x_f ~ %.0f (sigma_v=-0.4); plateau sigma_v(x=25)=%.5f z_II=%.5f ; behind: G=sigma_v(x=3000)=%.5f z=%.3e'%(vv,x[np.argmax(sV[x>5]>-0.4)+np.argmax(x>5)],sV[iP],z[iP],G,z[iIII]))
    print('    u-independence (max-min)/mean: phi_v over 10<=x<=2e4: %.2e ; rho over 40<=x<=2e4 (x>=x_f only: %.2e) ; sigma_v over x>=2 x_f: %.2e'%(rng(PV,mPh),rng(rho,mRh),rng(sV,x>=2*x[np.argmax(sV[x>5]>-0.4)+np.argmax(x>5)])))
    print('    y*rho/beta behind the front = %.6f ; plateau balance S/((kappa+G) rho) = %.5f (-> 1 if rho_v = -kappa rho + S and rho_v/rho = G)'%(y[iIII]*rho[iIII]/beta,Sx[iP]/((kap+G)*rho[iP])))
    print('    dm/dv: closed form 2 r beta (kappa+G)/c1_II = %.4f ; direct 8 pi r^2 y phi_v^2 = %.4f'%(pred,direct))
