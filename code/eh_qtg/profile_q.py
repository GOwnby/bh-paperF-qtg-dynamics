"""Profile in U at fixed v along a constrained QTG run (single grid): sigma_v, 1-psi, r-r_CH, y, ln W, g, Sigma vs U and x = U e^{kappa_+ v}."""
import os, numpy as np, warnings, sys
warnings.filterwarnings('ignore')
from dnU_qtg import *
from qtg_lib import run_stream_cy, coef
B=float(sys.argv[1]); hs=float(sys.argv[2]); v1=float(sys.argv[3]); vs=[float(x) for x in sys.argv[4:]]
S=StaticU(); c=0.2*np.exp(-S.kp*v1)
d=build_eh_q(S,1,1.0,1.5,v1,hs,hs,B,k=1.5,c=c,vH=v1+300)
out,snap=run_stream_cy(1,1.0,d['row0'],d['col0'],hs,hs,[0],rows=[int(round(x/hs)) for x in vs])
U=d['U']; kp=S.kp
for k,vv in enumerate(vs):
    r,sg,rs,rv,sgs,sV,Ps,PV=snap[k]; W=np.exp(sg); y=-rs/W; rho=-rv; psi=(1+4*y*rho)/r**2; Q,c1,c2,c3=coef(1,1.0,psi); g=Ps*PV/W
    Sig=psi/2-c2-8*np.pi*c1*g+64*np.pi**2*c3*g**2; x=U*np.exp(kp*vv)
    print('=== v=%g (h=%g)'%(vv,hs)); print('    U        x=Ue^{k+v}   r          1-psi      sigma_v   y          g          Sigma     W*Sigma(sigma_uv per U)')
    idx=[int(round(t)) for t in np.linspace(1,len(U)-1,26)]
    idx=sorted(set(idx+[int(np.argmin(abs(x-xx))) for xx in (0.1,0.3,1,3,10,30,100,300,1000)]))
    for i in idx: print(' %.3e %.3e %.6f %.3e %+.5f %.3e %.3e %.3e %.3e'%(U[i],x[i],r[i],1-psi[i],sV[i],y[i],g[i],Sig[i],W[i]*Sig[i]*d['gp'][i]))
