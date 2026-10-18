"""Resolution dependence of a strong-pulse horizon table: usage strong_conv.py ref.npz other.npz ... ; relative difference max|dphi_H|/max|phi_H| in windows of t (same Eddington start), and of the Q, A, rp."""
import sys,numpy as np
from scipy.interpolate import CubicSpline
R=np.load(sys.argv[1]); rs=CubicSpline(R['v1e']+R['t'],R['phiH'])
for fn in sys.argv[2:]:
    d=np.load(fn); ve=float(d['v1e'])+d['t']; out=[]
    for lo,hi in ((0,100),(100,400),(400,1500),(1500,2900)):
        m=(d['t']>=lo)&(d['t']<hi)&(ve>R['v1e']+R['t'][0])&(ve<R['v1e']+R['t'][-1])
        if m.sum()==0: continue
        out.append('[%d,%d): %.1e'%(lo,hi,abs(d['phiH'][m]-rs(ve[m])).max()/abs(d['phiH'][m]).max()))
    print(fn.split('/')[-1],' '.join(out),' | dQ/Q=%.1e  dv1e=%.4f'%(abs(float(d['Q'])/float(R['Q'])-1),float(d['v1e'])-float(R['v1e'])))
