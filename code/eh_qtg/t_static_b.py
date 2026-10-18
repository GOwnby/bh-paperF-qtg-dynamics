"""Static check for the bounded characteristic function (model 2, alpha=1, m=5) with the constrained EH-regular pipeline."""
import numpy as np, warnings, time, sys
warnings.filterwarnings('ignore')
from dnU_qtg import *
from static_gen import *
from qtg_lib import run_stream_cy
al=float(sys.argv[1]) if len(sys.argv)>1 else 1.0
import os
MASS=float(os.environ.get("MASS","5"))
fm,fn,fpn=bounded(MASS,al); S=StaticGen(fm,fn,fpn,(0.5,1.3),(1.4*MASS,2.6*MASS))
print('alpha=%g r-=%.8f r+=%.8f kappa-=%.8f kappa+=%.8f'%(al,S.rm,S.rp,S.km,S.kp))
U1=3.0; v1=100.0; c=0.2*np.exp(-S.kp*v1); Uq=[0.3,0.6,1.0,1.2]; vq=[40,60,80,98]
sq=[np.round(np.log(1+x*S.kp/c)/S.kp/0.1)*0.1 for x in Uq]; Uact=[c*np.expm1(S.kp*s)/S.kp for s in sq]
hl=[0.1,0.05,0.025,0.0125]; res={}
for hs in hl:
    d=build_eh_q(S,2,al**2,U1,v1,hs,hs,0.0,c=c,vH=v1+300)
    cols=[int(round(s/hs)) for s in sq]; out=run_stream_cy(2,al**2,d['row0'],d['col0'],hs,hs,cols)
    ii=[int(round(x/hs)) for x in vq]; res[hs]=np.array([[out[n][i,:] for i in ii] for n in range(len(cols))])
ex=np.array([[ [x[0] for x in S.fields(np.array([Uact[n]]),float(vq[m]))] for m in range(len(vq))] for n in range(len(Uq))])
exps=(1+4*ex[...,2]*ex[...,3]/np.exp(ex[...,1]))/ex[...,0]**2
def psi_of(a): return (1+4*a[...,2]*a[...,3]*np.exp(-a[...,1]))/a[...,0]**2
for name,get,ref in (('r',lambda a:a[...,0],ex[...,0]),('sigma_v',lambda a:a[...,5],ex[...,5]),('psi',psi_of,exps)):
    print(name)
    for m,vv in enumerate(vq):
        row=[]
        for n in range(len(Uq)):
            e=[get(res[h])[n,m]-ref[n,m] for h in hl]; T=[[get(res[h])[n,m] for h in hl]]
            for lev in range(1,len(hl)): T.append([(4**lev*T[-1][i+1]-T[-1][i])/(4**lev-1) for i in range(len(T[-1])-1)])
            row.append(' '.join('%+.1e'%x for x in e)+' | RR %+.1e'%(T[-1][0]-ref[n,m]))
        print('  v=%g:'%vv,' || '.join(row))
