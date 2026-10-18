"""Constrained-y evolution on static EH-regular data: error of r, sigma_v, psi at fixed (U,v) against the exact static solution, per mesh and after Richardson-Romberg."""
import numpy as np, warnings, time, sys
warnings.filterwarnings('ignore')
from dnU_qtg import *
import os
from qtg_lib import run_stream_cy as _rs
MODE=int(os.environ.get("MODE","3"))
run_stream_cy=lambda *a,**k:run_stream_q(*a)
S=StaticU(); U1=3.0; v1=100.0; c=0.2*np.exp(-S.kp*v1); Uq=[0.3,0.6,1.0,1.2]; vq=[40,60,80,98]
sq=[np.round(np.log(1+x*S.kp/c)/S.kp/0.1)*0.1 for x in Uq]; Uact=[c*np.expm1(S.kp*s)/S.kp for s in sq]
hl=[0.1,0.05,0.025,0.0125]; res={}
for hs in hl:
    t=time.time(); d=build_eh_q(S,1,1.0,U1,v1,hs,hs,0.0,c=c,vH=v1+300)
    cols=[int(round(s/hs)) for s in sq]; out=run_stream_cy(1,1.0,d['row0'],d['col0'],hs,hs,cols)
    ii=[int(round(x/hs)) for x in vq]; res[hs]=np.array([[out[n][i,:] for i in ii] for n in range(len(cols))])  # (nU,nv,8)
    print('h=%g nu=%d %.0fs'%(hs,d['nu'],time.time()-t),flush=True)
def psi_of(a): return (1+4*a[...,2]*a[...,3]*np.exp(-a[...,1]))/a[...,0]**2
ex=np.array([[ [x[0] for x in S.fields(np.array([Uact[n]]),float(vq[m]))] for m in range(len(vq))] for n in range(len(Uq))])  # r,sig,rU,rV,sU,sV
gp=np.array([c*np.exp(S.kp*s) for s in sq])
exr=ex[...,0]; exsV=ex[...,5]; exps=(1+4*ex[...,2]*ex[...,3]/np.exp(ex[...,1]))/ex[...,0]**2
for name,get,ref in (('r',lambda a:a[...,0],exr),('sigma_v',lambda a:a[...,5],exsV),('psi',psi_of,exps)):
    print(name)
    for m,vv in enumerate(vq):
        row=[]
        for n in range(len(Uq)):
            e=[get(res[h])[n,m]-ref[n,m] for h in hl]
            # Romberg h^2: R_k
            T=[[get(res[h])[n,m] for h in hl]]
            for lev in range(1,len(hl)): T.append([(4**lev*T[-1][i+1]-T[-1][i])/(4**lev-1) for i in range(len(T[-1])-1)])
            row.append(' '.join('%+.1e'%x for x in e)+' | RR %+.1e'%(T[-1][0]-ref[n,m]))
        print('  v=%g:'%vv,' || '.join(row))
