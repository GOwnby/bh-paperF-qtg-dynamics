"""Trace of an isotropic run up to its first non-finite sample (Paper F, 'What limits the window'; generator of code/blow1.log-blow3.log).
usage: python3 blow_trace.py B v1 h [h ...]     e.g. python3 blow_trace.py 0.003 300 0.025   (blow1.log: first non-finite v = 233.575; h = 0.0125: 261.9, blow2.log; h = 0.00625: 290.20625, blow3.log)
Prints the first non-finite v and, every 5 units of v from 150, sigma_v, r, sigma and phi_v on the ray U ~ 1; saves blow_h<h>_B<B>.npy.  Cost ~ 1/h^2: 6 min, 25 min, 100 min (one core)."""
import sys, numpy as np, warnings
warnings.filterwarnings('ignore')
from dnU_qtg import *
from qtg_lib import run_stream_cy
B=float(sys.argv[1]); v1=float(sys.argv[2]); 
S=StaticU(5.0); c=0.2*np.exp(-S.kp*v1); Uq=[1.0]
sq=[float(np.round(np.log(1+x*S.kp/c)/S.kp/0.05)*0.05) for x in Uq]
for hs in [float(x) for x in sys.argv[3:]]:
    d=build_eh_q(S,1,1.0,1.5,v1,hs,hs,B,k=1.5,c=c,vH=v1+300)
    cols=[int(round(s/hs)) for s in sq]; out=run_stream_cy(1,1.0,d['row0'],d['col0'],hs,hs,cols)
    o=out[0]; fin=np.isfinite(o).all(axis=1); i=np.where(~fin)[0]
    print('h=%g first nonfinite v=%s'%(hs,(hs*i[0] if len(i) else None)),flush=True)
    for vv in range(150,int(v1),5):
        j=int(round(vv/hs))
        if j<len(o) and np.isfinite(o[j]).all(): print('   v=%d sV=%+.5f psi-res: r=%.8f  z? sg=%.3f PV=%.3e'%(vv,o[j,5],o[j,0],o[j,1],o[j,7]))
    np.save('blow_h%g_B%g.npy'%(hs,B),o)
