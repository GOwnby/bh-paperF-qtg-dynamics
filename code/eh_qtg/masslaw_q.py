"""Check of the exact mass law m_v = 8 pi r^2 y phi_v^2 on the extrapolated rays: m(v2)-m(v1) against the trapezoid integral of the right-hand side (samples every 1.0 in v)."""
import os, sys, numpy as np
import analyze_q as A
sys.path.insert(0,os.environ.get('QTG_CODE',os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')))
from qtg_lib import hfun
model=int(sys.argv[2]); L2=float(sys.argv[3])
r,sg,rs,PV=[A.F[n][-1] for n in ('r','sg','rs','PV')]; psi=A.top['psi']; h,_=hfun(model,L2,psi); m=0.5*r**3*h
y=A.top['y']; rhs=8*np.pi*r**2*y*PV**2
for n,U in enumerate(A.d['Uq']):
    out=[]
    for (a,b) in ((60,70),(70,80),(80,90),(90,100),(100,108)):
        i=int(np.argmin(abs(A.v-a))); j=int(np.argmin(abs(A.v-b)))
        I=np.trapezoid(rhs[n,i:j+1],A.v[i:j+1]); out.append('[%d,%d] dm=%.5e int=%.5e rel %.1e'%(a,b,m[n,j]-m[n,i],I,abs((m[n,j]-m[n,i])/I-1)))
    print('U=%.3f'%U,' | '.join(out))
