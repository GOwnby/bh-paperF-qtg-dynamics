import os, sys, numpy as np
import os, analyze_q as A
sys.path.insert(0,os.environ.get('QTG_CODE',os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')))
from qtg_lib import coef
def inv(lev,n,i):
    F=lambda nm:A.F[nm][lev][n,i]
    r,sg,rs,rv,Ps,PV,sV=[F(x) for x in ('r','sg','rs','rv','Ps','PV','sV')]
    W=np.exp(sg); y=-rs/W; rho=-rv; psi=(1+4*y*rho)/r**2; Q,c1,c2,c3=coef(1,1.0,psi); g=Ps*PV/W
    Sig=psi/2-c2-8*np.pi*c1*g+64*np.pi**2*c3*g**2
    return psi,g,Sig,sV,np.log(W)
for n in (2,3):
  for vv in (70,90,100,108):
    i=int(np.argmin(abs(A.v-vv)))
    print('ray',n,'v=%d'%vv,' '.join('L%d: psi=%.6f g=%.4e Sig=%.4e sV=%.5f lnW=%.3f |'%((lev,)+inv(lev,n,i)) for lev in range(len(A.hl))))
