"""Metric-exponent plateau: median and spread of the extrapolated sigma_v over the points v>=vmin with sigma_v<-0.79 (static-interior regime, before the mass-inflation front), per ray, against -kappa_-(m_f).  usage: plateau_q.py json kappa_minus(m_f) [vmin]"""
import sys, numpy as np
import analyze_q as A
kap=float(sys.argv[2]); vmin=float(sys.argv[3]) if len(sys.argv)>3 else 45
print('B=%g  -kappa_-(m_f)=%.7f'%(A.d['B'],-kap))
for n,U in enumerate(A.d['Uq']):
    s=A.top['sV'][n]; m=(A.v>=vmin)&(s<-0.79)&np.isfinite(s)
    if m.sum()<3: print(' U=%.3f  (fewer than 3 plateau points)'%U); continue
    print(' U=%.3f  n=%2d  median %.7f  spread %.1e  median+kappa %+.1e'%(U,m.sum(),np.median(s[m]),s[m].max()-s[m].min(),np.median(s[m])+kap))
