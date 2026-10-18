"""Multi-grid constrained-y QTG run with event-horizon-regular data (Paper F).  usage: gen_q.py model L2 B k v1 hs1 hs2 ...
Rays at s_q on grid points of 0.05 (U ~ 0.3, 0.6, 1.0, 1.2); stores the eight fields at v = 20, 21, ..., v1-2 for each grid -> genq_*.json"""
import os, sys, json, time, numpy as np, warnings
warnings.filterwarnings('ignore')
from dnU_qtg import *
from static_gen import StaticGen, bounded
from qtg_lib import run_stream_cy
model=int(sys.argv[1]); L2=float(sys.argv[2]); B=float(sys.argv[3]); k=float(sys.argv[4]); v1=float(sys.argv[5]); hl=[float(x) for x in sys.argv[6:]]
MASS=float(os.environ.get('MASS','5'))
if model==2:
    _fm,_fn,_fpn=bounded(MASS,np.sqrt(L2)); S=StaticGen(_fm,_fn,_fpn,(0.5,1.3),(1.4*MASS,2.6*MASS))
else: S=StaticU(MASS)
U1=1.5; c=0.2*np.exp(-S.kp*v1); Uq=[0.3,0.6,1.0,1.2]; vq=np.arange(20,v1-1.9,1.0)
sq=[float(np.round(np.log(1+x*S.kp/c)/S.kp/0.05)*0.05) for x in Uq]; Uact=[float(c*np.expm1(S.kp*s)/S.kp) for s in sq]
data={}
for hs in hl:
    t=time.time(); d=build_eh_q(S,model,L2,U1,v1,hs,hs,B,k=k,c=c,vH=v1+300)
    cols=[int(round(s/hs)) for s in sq]; out=run_stream_cy(model,L2,d['row0'],d['col0'],hs,hs,cols)
    ii=[int(round(x/hs)) for x in vq]
    data[str(hs)]={nm:[out[n][ii,f].tolist() for n in range(len(cols))] for f,nm in enumerate(['r','sg','rs','rv','sgs','sV','Ps','PV'])}
    rf=float(d['hz'].sol(v1)[0]); data[str(hs)]['rH_end']=rf; data[str(hs)]['nan']=int(np.isnan(out).sum())
    print('h=%g nu=%d nv=%d %.0fs nan=%d'%(hs,d['nu'],d['nv'],time.time()-t,np.isnan(out).sum()),flush=True)
json.dump(dict(model=model,L2=L2,Uq=Uact,sq=sq,vq=vq.tolist(),B=B,k=k,v1=v1,data=data),open('genq_m%d%s%s_B%g_k%g_v%g.json'%(model,('' if model!=2 else '_a%g'%np.sqrt(L2)),('' if MASS==5.0 else '_M%g'%MASS),B,k,v1),'w'))
print('done')
