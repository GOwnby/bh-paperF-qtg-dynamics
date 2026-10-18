"""usage: strong_table.py model m0 mt h0 hLf vrel out.npz  (s=max(1,mt/5); h_N=h0*s, h_L=hLf*s; stage L to t=vrel*s; see strong.py)"""
import sys,time,numpy as np
from strong import *
model=int(sys.argv[1]); m0=float(sys.argv[2]); mt=float(sys.argv[3]); h0=float(sys.argv[4]); hL=float(sys.argv[5]); vrel=float(sys.argv[6]); fn=sys.argv[7]
import os
sc=max(1.0,mt/5.0); tail=None
if os.environ.get('TAIL_C'):   # scalar charge at infinity: phi = c S((r-ra)/dr) g(r), g the static solution of mass mt with g->1/r (ra, dr in units of s)
    tail=(float(os.environ['TAIL_C']),float(os.environ.get('TAIL_RA','26.8'))*sc,float(os.environ.get('TAIL_DR','2.4'))*sc,model,mt,1.0)
t0=time.time(); d=make_table_h(model,m0,mt,h0,hL*sc,vrel,tail=tail)
if tail is not None: d['b']=float(os.environ['TAIL_C'])*mt; d['c']=float(os.environ['TAIL_C'])
np.savez_compressed(fn,**{k:np.asarray(v) for k,v in d.items()})
print('model %d m0=%g mt=%g: A=%.6f mf=%.6f s=%.3f Q=%.5f 8 mf|Q|=%.3f rp=%.5f ah=%.1f/%d  %.0fs'%(model,m0,mt,d['A'],d['mf'],d['s'],d['Q'],8*d['mf']*abs(d['Q']),d['rp'],d['ah'],d['nu'],time.time()-t0))
