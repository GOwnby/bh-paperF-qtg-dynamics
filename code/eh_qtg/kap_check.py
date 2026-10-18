import os, json, sys, numpy as np
from scipy.optimize import brentq
import os, analyze_q as A
def hay(m,l2=1.0):
    P=lambda r:r**3-2*m*r*r+2*m*l2
    rr=np.linspace(0.3,2*m+2,200000); v=P(rr); idx=np.where(np.sign(v[:-1])*np.sign(v[1:])<0)[0]
    rm=brentq(P,rr[idx[0]],rr[idx[0]+1],xtol=1e-15); rp=brentq(P,rr[idx[1]],rr[idx[1]+1],xtol=1e-15)
    k=lambda r:abs(3*r*r-4*m*r)/(2*(r**3+2*m*l2))
    return rm,rp,k(rm),k(rp)
rf=A.d['data'][list(A.d['data'].keys())[-1]]['rH_end']; m_f=rf/(2*(1-1/rf**2))
print('B=%g r_H(v1)=%.8f  m_f=%.6f'%(A.d['B'],rf,m_f)); print(' static (m=5):',hay(5.0)); print(' final  (m_f):',hay(m_f))
for n,U in enumerate(A.d['Uq']):
    print(' U=%.3f'%U,' '.join('v=%d: %.6f'%(vv,A.top['sV'][n,int(np.argmin(abs(A.v-vv)))]) for vv in (40,50,60,70,80)))
