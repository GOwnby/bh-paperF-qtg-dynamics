"""Fit of the horizon tables of strong_table.py: B (k=3 fixed and free k) in the window [1000,2900] m_f/5 of Eddington time, B/m_f^3, B/(8 m_f|Q|).  usage: strong_fit.py tables..."""
import sys,numpy as np
from fit1 import fitwin
print('%-26s %4s %7s %8s %9s %8s %7s %9s %8s'%('table','m0','m_f','A','Q','B(k=3)','k free','B/(8mf|Q|)','B/mf^3'))
for fn in sys.argv[1:]:
    d=np.load(fn); mf=float(d['mf']); s2=mf/5.0; ve=float(d['v1e'])+d['t']; ph=d['phiH']
    B,vs=fitwin(ve,ph,1000*s2,2900*s2,3.0)[:2]; Bf,vsf,kf=fitwin(ve,ph,1000*s2,2900*s2)
    Q=float(d['Q'])
    print('%-26s %4g %7.3f %8.5f %9.5f %8.3f %7.4f %9.4f %8.4f'%(fn.split('/')[-1][:26],float(d['m0']),mf,float(d['A']),Q,B,kf,B/(8*mf*abs(Q)),B/mf**3))
