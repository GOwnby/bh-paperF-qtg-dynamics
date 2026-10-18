"""Horizon table with an infalling pulse (Paper F, Sec. threshold): phi_H(v) = collapse tail table (m=5, k=3) + P sin^4(pi (v-ta)/(tb-ta)) on [ta,tb].
usage: python3 pulse_table.py P ta tb out.npz [base.npz]   (the file carries t, phiH, rg, g as Tail of gen_c.py expects; PU0MODE=zero is used for these runs)"""
import sys, numpy as np
P,ta,tb=float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]); out=sys.argv[4]; base=sys.argv[5] if len(sys.argv)>5 else 'data/tail_m1_v60_h1.npz'
d=dict(np.load(base)); t=d['t']; x=np.clip((t-ta)/(tb-ta),0,1)
d['phiH']=d['phiH']+P*np.sin(np.pi*x)**4; d['P']=P; d['ta']=ta; d['tb']=tb
np.savez_compressed(out,**d)
# horizon mass gain estimate: dm = 4 pi r+^2 int phi_v^2 dv (y=1/2 on the horizon)
from scipy.interpolate import CubicSpline
cs=CubicSpline(t,d['phiH']).derivative(); m=(t>=0)&(t<=ta+3*(tb-ta)); dm=4*np.pi*float(d['rp'])**2*np.trapezoid(cs(t[m])**2,t[m]); print('P=%g  horizon mass gain (crude, r_+ fixed) = %.4f'%(P,dm))
