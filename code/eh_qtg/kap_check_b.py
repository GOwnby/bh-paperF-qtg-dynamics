import os, sys, numpy as np
import os, analyze_q as A
from static_gen import *
M0=float(sys.argv[2]); al=float(sys.argv[3])
rf=A.d['data'][list(A.d['data'].keys())[-1]]['rH_end']; psi=1/rf**2; m_f=0.5*rf**3*psi/np.sqrt(1-al**2*psi**2)
def hole(m):
    fm,fn,fpn=bounded(m,al); return StaticGen(fm,fn,fpn,(0.5,1.3),(1.4*m,2.6*m))
S0=hole(M0); S1=hole(m_f)
print('bounded alpha=%g M0=%g: static kappa- %.8f r- %.8f ; final m_f=%.8f kappa- %.8f r- %.8f ; kappa+ %.8f -> %.8f'%(al,M0,S0.km,S0.rm,m_f,S1.km,S1.rm,S0.kp,S1.kp))
for n,U in enumerate(A.d['Uq']):
    print(' U=%.3f'%U,' '.join('v=%d: %.6f'%(vv,A.top['sV'][n,int(np.argmin(abs(A.v-vv)))]) for vv in (20,30,40,50,60,70)))
