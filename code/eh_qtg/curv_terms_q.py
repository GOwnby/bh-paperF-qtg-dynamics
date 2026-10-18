"""Kretschmann invariant of the evolved metric (Hayward h, L2=1) per ray: maximum over the sampled v, and the decomposition of Sigma=sigma_uv/W = psi/2 - c2 - 8 pi c1 g + 64 pi^2 c3 g^2 at selected v (converged window).  usage: curv_terms_q.py json v1 v2 ..."""
import os, sys, numpy as np
sys.path.insert(0,os.environ.get('QTG_CODE',os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')))
import analyze_q as A
from qtg_lib import coef
vl=[float(x) for x in sys.argv[2:]]
L=len(A.hl)-1; F=lambda nm:A.F[nm][L]
r,sg,rs,rv,Ps,PV=[F(n) for n in ('r','sg','rs','rv','Ps','PV')]
W=np.exp(sg); y=-rs/W; rho=-rv; psi=(1+4*y*rho)/r**2; Q,c1,c2,c3=coef(1,1.0,psi); g=Ps*PV/W
t1=psi/2; t2=-c2; t3=-8*np.pi*c1*g; t4=64*np.pi**2*c3*g**2; Sig=t1+t2+t3+t4; K=(4*Sig)**2+8*(128*np.pi**2*c1**2*g**2+Q**2/2)+4*psi**2
print('B=%g: max of K over sampled v (v>=20) per ray, and K(v) in the converged window'%A.d['B'])
for n,U in enumerate(A.d['Uq']):
    k=np.where(np.isfinite(K[n]),K[n],0); i=int(np.argmax(k)); print(' U=%.3f  max K=%.2e at v=%g'%(U,k[i],A.v[i]))
print('decomposition of Sigma on the ray U=%.3f:  v   psi/2   -c2   -8pi c1 g   64pi^2 c3 g^2   K'%A.d['Uq'][2])
for vv in vl:
    i=int(np.argmin(abs(A.v-vv))); print('  %5.0f  %.3f  %.2e  %.3e  %.3e   %.3e'%(A.v[i],t1[2,i],t2[2,i],t3[2,i],t4[2,i],K[2,i]))
