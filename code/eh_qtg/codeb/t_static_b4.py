"""Code B on exact static EH-regular data (Hayward m=5 -> StaticU(), B=0): error of r, sigma_v, psi vs the exact static solution; observed order for h_s=h_v=h."""
import sys,os,numpy as np,warnings,time; warnings.filterwarnings('ignore')
sys.path.insert(0,'..'); from dnU_qtg import *
from gen_b import run_B
S=StaticU(); U1=3.0; v1=100.0; c=0.2*np.exp(-S.kp*v1); Uq=[0.3,0.6,1.0,1.2]; vq=[40,60,80,98]
hl=[0.2,0.1,0.05,0.025]
sq=[np.round(np.log(1+x*S.kp/c)/S.kp/0.1)*0.1 for x in Uq]; Uact=[c*np.expm1(S.kp*s)/S.kp for s in sq]
res={}
for h in hl:
    t=time.time(); d=build_eh_q(S,1,1.0,U1,v1,h,h/2,0.0,c=c,vH=v1+300)
    cols=[int(round(s/h)) for s in sq]; out,mon=run_B(1,1.0,d['row0'],d['col0'],h,h,cols,1)
    ii=[int(round(x/h)) for x in vq]; res[h]=np.array([[out[n][i,:] for i in ii] for n in range(len(cols))]); print('h=%g nu=%d %.0fs'%(h,d['nu'],time.time()-t),flush=True)
ex=np.array([[ [x[0] for x in S.fields(np.array([Uact[n]]),float(vq[m]))] for m in range(len(vq))] for n in range(len(Uq))])
exps=(1+4*ex[...,2]*ex[...,3]/np.exp(ex[...,1]))/ex[...,0]**2
psi=lambda a:(1+4*a[...,2]*a[...,3]*np.exp(-a[...,1]))/a[...,0]**2
# B stores (r,sg,rs,rv,sgs,sV,Ps,PV): same layout as code A fields? fields order in A: r,sg,rs(=r_s),rv,.. ; take r (0), sigma_v (5), psi
for name,get,ref in (('r',lambda a:a[...,0],ex[...,0]),('sigma_v',lambda a:a[...,5],ex[...,5]),('psi',psi,exps)):
    print(name,'(errors for h=',hl,'; max over the 4 rays at v=40,60,80,98; observed order from last two)')
    for m,vv in enumerate(vq):
        e=[np.max(np.abs(get(res[h])[:,m]-ref[:,m])) for h in hl]
        print('  v=%g:'%vv,' '.join('%.2e'%x for x in e),' order(last)=%.2f'%(np.log2(e[-2]/e[-1]) if e[-1]>0 else 0))
