"""Snapshots of the unextrapolated run B = 3e-3, k = 3/2, v1 = 300, h_s = 0.05, h_v = 0.0125 on the rows v = 100, 150, 200 (code A, streamed): writes prof2_U.npy, prof2_gp.npy,
prof2_snap.npy into the current directory; slaving_prof.py (logs/slaving_prof.log) reads them.  About 3 min on one core.  usage: python3 prof2.py && python3 slaving_prof.py"""
import numpy as np, warnings, sys
warnings.filterwarnings('ignore')
from dnU_qtg import *
from qtg_lib import run_stream_cy, coef
B=0.003; v1=300.0; hs=0.05; hv=0.0125; vs=[100.,150.,200.]
S=StaticU(5.0); c=0.2*np.exp(-S.kp*v1); kp=S.kp
d=build_eh_q(S,1,1.0,1.5,v1,hs,hv,B,k=1.5,c=c,vH=v1+300)
out,snap=run_stream_cy(1,1.0,d['row0'],d['col0'],hs,hv,[0],rows=[int(round(x/hv)) for x in vs])
U=d['U']; gp=d['gp']
np.save('prof2_U.npy',U); np.save('prof2_gp.npy',gp); np.save('prof2_snap.npy',snap)
