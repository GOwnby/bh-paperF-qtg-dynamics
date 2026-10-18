"""Code E driver (Paper F, Sec. "Removing the exponential"): python3 gen_e.py model L2 B k v1 hs:hv [hs:hv ...] ; env MASS (default 5).  Writes gene_*.json in the format of gen_q2.py (fields r, sg, rs, rv, sgs(NaN), sV, Ps, PV on the same four rays)."""
import os, sys, json, time, ctypes, numpy as np, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0,'..')
from dnU_qtg import *
from static_gen import StaticGen, bounded
dp=ctypes.POINTER(ctypes.c_double); ip=ctypes.POINTER(ctypes.c_int)
lib=ctypes.CDLL(os.path.abspath('libqtge.so'))
lib.evolve_E.argtypes=[ctypes.c_int,ctypes.c_int,ctypes.c_double,ctypes.c_double,ctypes.c_int,ctypes.c_double,dp,dp,ctypes.c_int,ctypes.c_int,ip,dp]
def run_B(model,L2,row0,col,hs,hv,cols,proj=1):
    nu=row0.shape[1]; ncolt=col.shape[1]; nv=(ncolt-1)//2+1
    cols=np.ascontiguousarray(cols,dtype=np.int32); out=np.zeros((len(cols),nv,8)); mon=np.zeros(nv)
    row0=np.ascontiguousarray(row0); col=np.ascontiguousarray(col)
    lib.evolve_E(nu,nv,hs,hv,model,L2,row0.ctypes.data_as(dp),col.ctypes.data_as(dp),ncolt,len(cols),cols.ctypes.data_as(ip),out.ctypes.data_as(dp))
    return out,mon
if __name__=='__main__':
    model=int(sys.argv[1]); L2=float(sys.argv[2]); B=float(sys.argv[3]); k=float(sys.argv[4]); v1=float(sys.argv[5]); pairs=[tuple(float(t) for t in x.split(':')) for x in sys.argv[6:]]
    MASS=float(os.environ.get('MASS','5')); proj=int(os.environ.get('PROJ','1'))
    if model==2:
        _fm,_fn,_fpn=bounded(MASS,np.sqrt(L2)); S=StaticGen(_fm,_fn,_fpn,(0.5,1.3),(1.4*MASS,2.6*MASS))
    else: S=StaticU(MASS)
    U1=1.5; c=0.2*np.exp(-S.kp*v1); Uq=[0.3,0.6,1.0,1.2]; vq=np.arange(20,v1-1.9,1.0)
    sq=[float(np.round(np.log(1+x*S.kp/c)/S.kp/0.2)*0.2) for x in Uq]; Uact=[float(c*np.expm1(S.kp*s)/S.kp) for s in sq]
    data={}
    for hs,hv in pairs:
        t=time.time(); d=build_eh_q(S,model,L2,U1,v1,hs,hv/2,B,k=k,c=c,vH=v1+300)
        row0=d['row0'].copy(); Ux=d['U']; zz=np.where(Ux<1.0,-Ux*S.w(Ux),row0[0]-S.rp)   # Delta_0 = r - r_+ without cancellation (x=U at v=0)
        row0[0]=zz+float(os.environ.get('DELTA0_OFFSET','0'))     # Delta_0 = r - r_H(0) = z(U): continuous at s=0 (Delta_0(0)=0). The former zz+(r_+ - r_H(0)) had a ~3.6e-15 step at s=0 that seeded exp(kappa_+ v) growth (Paper F, Sec. seed). DELTA0_OFFSET: test only.
        hz=d['hz']; r0h,rv0=hz.sol(0); sQ=lambda r,rv: r*float(coef(model,L2,(1-2*rv)/r**2)[0])/2; sgv0=sQ(r0h,rv0); phv=lambda t:PHVF(k,B,t)
        def rhsD(t,Y):
            r,sg,rU,_,sUt,_=[a[0] for a in S.fields(np.array([t]),0.0)]
            a,b,c_=Fq(model,L2,r,sg,rU,rv0+Y[0],0.0,Y[2]); return [float(a),float(b),float(c_)]
        sD=solve_ivp(rhsD,[0,d['U'][-1]],[0.0,sgv0,phv(0)],t_eval=d['U'],method='DOP853',rtol=1e-13,atol=[1e-26,1e-14,1e-300]); assert sD.success
        row0[3]=sD.y[0]                        # D_0 = r_v - r_v^H at v=0, integrated in the difference variable (relative accuracy, no cancellation)
        cols=[int(round(s/hs)) for s in sq]; out,mon=run_B(model,L2,row0,d['col0'],hs,hv,cols,proj)
        ii=[int(round(x/hv)) for x in vq]
        data[str(hv)]={nm:[out[n][ii,f].tolist() for n in range(len(cols))] for f,nm in enumerate(['r','sg','rs','rv','sgs','sV','Ps','PV'])}
        data[str(hv)]['nan']=int(np.isnan(out).sum()); data[str(hv)]['mon']=mon[::max(1,int(1/hv))].tolist()
        print('B: hs=%g hv=%g proj=%d nu=%d nv=%d %.0fs nan=%d'%(hs,hv,proj,d['nu'],len(out[0]),time.time()-t,np.isnan(out).sum()),flush=True)
    json.dump(dict(model=model,L2=L2,Uq=Uact,sq=sq,vq=vq.tolist(),B=B,k=k,v1=v1,data=data),open('gene_p%d_hs%g_m%d_B%g_k%g_v%g.json'%(proj,pairs[0][0],model,B,k,v1),'w'))
