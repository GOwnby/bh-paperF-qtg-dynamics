"""Free evolution (evolve_stream_qtg, r_u and r_v evolved) versus the constrained evolution on EH-regular data at B=0.003, early times (before the noise of the free scheme grows)."""
import os, numpy as np, warnings
warnings.filterwarnings('ignore')
from dnU_qtg import *
from qtg_lib import run_stream_cy, run_stream
S=StaticU(); B=0.003; v1=60.0; c=0.2*np.exp(-S.kp*v1); Uq=[0.3,0.6,1.0]
sq=[float(np.round(np.log(1+x*S.kp/c)/S.kp/0.05)*0.05) for x in Uq]
rows=[]
for hs in (0.05,0.025,0.0125,0.00625):
    d=build_eh_q(S,1,1.0,1.5,v1,hs,hs,B,k=1.5,c=c,vH=v1+300); cols=[int(round(s/hs)) for s in sq]
    a=run_stream(1,1.0,d['row0'],d['col0'],hs,hs,cols); b=run_stream_cy(1,1.0,d['row0'],d['col0'],hs,hs,cols)
    ii=[int(round(x/hs)) for x in (10,20,30,40)]
    rows.append(np.array([[[ (a[n][i,f]-b[n][i,f]) for f in (0,1,5,7)] for i in ii] for n in range(len(cols))]))
    print('h=%g done'%hs,flush=True)
names=['r','sigma','sigma_v','phi_v']
for n,U in enumerate(Uq):
    for m,vv in enumerate((10,20,30,40)):
        print('ray U~%.1f v=%d: |free-constrained| per h (0.05..0.00625):'%(U,vv),' ; '.join('%s '%nm+' '.join('%.1e'%abs(rows[k][n,m,f]) for k in range(4)) for f,nm in enumerate(names)))
