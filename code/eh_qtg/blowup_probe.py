"""First non-finite sample of the constrained evolution on the ray U ~ 1 at the native resolution of the mesh (Paper F, Sec. 'What limits the window'; Eq. (vb)).
Same data and scheme as gen_q2.py (Hayward h, m = 5, k = 3/2, mode 3), no extrapolation; prints the first v at which sigma_v is not finite and sigma_v(150), sigma_v(190).
usage: blowup_probe.py B hs hv v1      examples: 0.003 0.05 0.05 250  and  0.003 0.05 0.05 400  (blow-up independent of v1: logs/vb1.log);
       0.003 0.0125 0.05 250 (independent of hs); 0.003 0.05 0.025 300, ... (shift by ln4/kappa_+ per halving of hv: logs/blow1.log-blow3.log)"""
import os, sys, numpy as np, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0,os.environ.get('QTG_CODE','..'))
from dnU_qtg import *
from qtg_lib import run_stream_cy
B=float(sys.argv[1]); hs=float(sys.argv[2]); hv=float(sys.argv[3]); v1=float(sys.argv[4])
S=StaticU(5.0); kp=S.kp; c=0.2*np.exp(-kp*v1); Uq=1.0
s_q=float(np.round(np.log(1+Uq*kp/c)/kp/0.05)*0.05)
d=build_eh_q(S,1,1.0,1.5,v1,hs,hv,B,k=1.5,c=c,vH=v1+300)
col=int(round(s_q/hs)); out=run_stream_cy(1,1.0,d['row0'],d['col0'],hs,hv,[col])[0]    # out[row, field]
sV=out[:,5]; v=np.arange(len(sV))*hv; bad=np.where(~np.isfinite(sV))[0]
fv=v[bad[0]] if len(bad) else float('nan')
at=lambda x: sV[int(round(x/hv))]
print('B=%g hs=%g hv=%g v1=%g  first nonfinite v=%.5g ; sV(190)=%.5f sV(150)=%.5f'%(B,hs,hv,v1,fv,at(190),at(150)))
