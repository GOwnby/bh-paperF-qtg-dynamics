"""Horizon tail of collapse data with scalar charge at infinity (rphi -> c): a0 = phi_H t^2/(4 I0), I0=-c m_t (the 1/r^2 coefficient of r phi on u0), fits of np_fit.  usage: tc_fit.py tc_*.npz"""
import sys,numpy as np
from np_fit import a0fit,kfit
for fn in sys.argv[1:]:
    d=np.load(fn); t=d['t']; f=d['phiH']; b=float(d['b']); s=float(d['s'])
    print(fn,'c=%g  I0=-c m_t=%g  m_f(stage N)=%.5f  m_t=%g  tmax=%.0f'%(float(d['c']),-b,float(d['mf']),float(d['mt']),t[-1]))
    for lo in (800,1600,3200):
        hi=t[-1]
        print('  window [%d,%d]: a0 = '%(lo,hi)+'  '.join('%.5f'%a0fit(t,f,b,lo,hi,n) for n in (2,3,5)),'   (c1 | +c2 ln t/t | +c3,c4 at 1/t^2)')
    for lo in (800,1600,3200):
        B,sh,k=kfit(t,f,lo,t[-1]); print('  free (B,s,k) window [%d,%.0f]: B/(4|I0|)=%.4f  s=%.1f  k=%.4f'%(lo,t[-1],B/(4*abs(b)),sh,k))
