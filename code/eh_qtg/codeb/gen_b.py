"""Code B driver: python gen_b.py model L2 B k v1 hs:hv [hs:hv ...] ; env PROJ=0/1 (default 1), MASS.  Writes genb_*.json in the format of gen_q2.py (fields r, sg, rs, rv, sgs(NaN), sV, Ps, PV on the same four rays)."""
import os, sys, json, time, ctypes, numpy as np, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0,'..')
from dnU_qtg import *
from static_gen import StaticGen, bounded
dp=ctypes.POINTER(ctypes.c_double); ip=ctypes.POINTER(ctypes.c_int)
lib=ctypes.CDLL(os.path.abspath('libqtgb.so'))
lib.evolve_B.argtypes=[ctypes.c_int,ctypes.c_int,ctypes.c_double,ctypes.c_double,ctypes.c_int,ctypes.c_double,dp,dp,ctypes.c_int,ctypes.c_int,ip,dp,ctypes.c_int,ctypes.c_int,dp]
def run_B(model,L2,row0,col,hs,hv,cols,proj=1):
    nu=row0.shape[1]; ncolt=col.shape[1]; nv=(ncolt-1)//2+1
    cols=np.ascontiguousarray(cols,dtype=np.int32); out=np.zeros((len(cols),nv,8)); mon=np.zeros(nv)
    row0=np.ascontiguousarray(row0); col=np.ascontiguousarray(col)
    lib.evolve_B(nu,nv,hs,hv,model,L2,row0.ctypes.data_as(dp),col.ctypes.data_as(dp),ncolt,len(cols),cols.ctypes.data_as(ip),out.ctypes.data_as(dp),proj,1,mon.ctypes.data_as(dp))
    return out,mon
if __name__=='__main__':
    model=int(sys.argv[1]); L2=float(sys.argv[2]); B=float(sys.argv[3]); k=float(sys.argv[4]); v1=float(sys.argv[5]); pairs=[tuple(float(t) for t in x.split(':')) for x in sys.argv[6:]]
    MASS=float(os.environ.get('MASS','5')); proj=int(os.environ.get('PROJ','1'))
    if model==2:
        _fm,_fn,_fpn=bounded(MASS,np.sqrt(L2)); S=StaticGen(_fm,_fn,_fpn,(0.5,1.3),(1.4*MASS,2.6*MASS))
    else: S=StaticU(MASS)
    U1=1.5; c=0.2*np.exp(-S.kp*v1); Uq=[0.3,0.6,1.0,1.2]; vq=np.arange(20,v1-1.9,1.0)
    sq=[float(np.round(np.log(1+x*S.kp/c)/S.kp/0.05)*0.05) for x in Uq]; Uact=[float(c*np.expm1(S.kp*s)/S.kp) for s in sq]
    data={}
    for hs,hv in pairs:
        t=time.time(); d=build_eh_q(S,model,L2,U1,v1,hs,hv/2,B,k=k,c=c,vH=v1+300)
        cols=[int(round(s/hs)) for s in sq]; out,mon=run_B(model,L2,d['row0'],d['col0'],hs,hv,cols,proj)
        ii=[int(round(x/hv)) for x in vq]
        data[str(hv)]={nm:[out[n][ii,f].tolist() for n in range(len(cols))] for f,nm in enumerate(['r','sg','rs','rv','sgs','sV','Ps','PV'])}
        data[str(hv)]['nan']=int(np.isnan(out).sum()); data[str(hv)]['mon']=mon[::max(1,int(1/hv))].tolist()
        print('B: hs=%g hv=%g proj=%d nu=%d nv=%d %.0fs nan=%d'%(hs,hv,proj,d['nu'],len(out[0]),time.time()-t,np.isnan(out).sum()),flush=True)
    json.dump(dict(model=model,L2=L2,Uq=Uact,sq=sq,vq=vq.tolist(),B=B,k=k,v1=v1,data=data),open('genb_p%d_hs%g_m%d_B%g_k%g_v%g.json'%(proj,pairs[0][0],model,B,k,v1),'w'))
