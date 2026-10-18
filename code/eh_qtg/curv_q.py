"""Curvature invariants along the rays of a constrained QTG run (Hayward h, L2=1): Kretschmann K = (4 Sigma)^2 + 8 H_ab H^ab / r^2 + 4 psi^2,
Sigma = sigma_uv/W = psi/2 - c2 - 8 pi c1 g + 64 pi^2 c3 g^2, g = phi_u phi_v / W,  H_abH^ab / r^2 = 128 pi^2 c1^2 g^2 + Q^2/2   (derivation in Paper F)."""
import os, sys, numpy as np
import analyze_q as A
sys.path.insert(0,os.environ.get('QTG_CODE',os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')))
from qtg_lib import coef
L2=1.0; v=A.v
r,sg,rs,rv,Ps,PV=[A.F[n][-1] for n in ('r','sg','rs','rv','Ps','PV')]
W=np.exp(sg); y=-rs/W; rho=-rv; psi=(1+4*y*rho)/r**2; Q,c1,c2,c3=coef(1,L2,psi); g=Ps*PV/W
Sig=psi/2-c2-8*np.pi*c1*g+64*np.pi**2*c3*g**2; K=(4*Sig)**2+8*(128*np.pi**2*c1**2*g**2+Q**2/2)+4*psi**2
Mms=0.5*r**3*psi
print('B=%g'%A.d['B'])
for n,U in enumerate(A.d['Uq']):
    print('--- U=%.3f'%U); print(' v    1-psi       g=phi_u phi_v/W   c1*g        Sigma      K          K_{GR-like}=16M^2/r^6*3  max(|z^1.5 g|)')
    for vv in (40,50,60,70,80,90,100,108):
        i=int(np.argmin(abs(v-vv)))
        print('%4d %.3e %+.3e %+.3e %+.4f %.4e %.4e'%(v[i],1-psi[n,i],g[n,i],c1[n,i]*g[n,i],Sig[n,i],K[n,i],48*Mms[n,i]**2/r[n,i]**6))
