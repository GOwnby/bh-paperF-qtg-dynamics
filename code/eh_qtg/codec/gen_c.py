"""Code E driven by a collapse-generated horizon tail (Paper F, Sec. "collapse-generated tails").
usage: python3 gen_c.py tail.npz v1 hs:hv [hs:hv ...] ; env MASS (5), PU0MODE (profile|zero), TAILMODE (table|fit)
Same equations, scheme and data construction as gen_e.py (code E), but
  * phi_v^H(v) on the horizon is the derivative of the tabulated phi_H(v_E), v_E = v_e - v_e(start)  (stage L of collapse_tail.py), instead of B(1+v)^-k;
  * phi_U on the starting row is the profile dphi/dr|row (stage N) times the static r_U (PU0MODE=profile), instead of 0.
Data on the horizon column and the row are otherwise built exactly as in dnU_qtg.build_eh_q / gen_e.py (Delta_0 = z(U), D_0 integrated in the difference variable)."""
import os, sys, json, time, ctypes, bisect, numpy as np, warnings
warnings.filterwarnings('ignore')
here=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(here,'..'))
from dnU_qtg import *
from scipy.interpolate import CubicSpline
dp=ctypes.POINTER(ctypes.c_double); ip=ctypes.POINTER(ctypes.c_int)
lib=ctypes.CDLL(os.path.join(here,'..','codee','libqtge.so'))    # built by setup.sh
lib.evolve_E.argtypes=[ctypes.c_int,ctypes.c_int,ctypes.c_double,ctypes.c_double,ctypes.c_int,ctypes.c_double,dp,dp,ctypes.c_int,ctypes.c_int,ip,dp]
def run_E(model,L2,row0,col,hs,hv,cols):
    nu=row0.shape[1]; ncolt=col.shape[1]; nv=(ncolt-1)//2+1
    cols=np.ascontiguousarray(cols,dtype=np.int32); out=np.zeros((len(cols),nv,8))
    row0=np.ascontiguousarray(row0); col=np.ascontiguousarray(col)
    lib.evolve_E(nu,nv,hs,hv,model,L2,row0.ctypes.data_as(dp),col.ctypes.data_as(dp),ncolt,len(cols),cols.ctypes.data_as(ip),out.ctypes.data_as(dp))
    return out
class Tail:
    """phi_H(v_E) table -> callables phi(v), phi_v(v)"""
    def __init__(s,fn,vmax_use=None):
        d=np.load(fn); t=d['t']; f=d['phiH']
        s.cs=CubicSpline(t,f); s.ds=s.cs.derivative(); s.tmax=t[-1]; s.d=d
        s.x=s.ds.x.tolist(); s.c=[s.ds.c[:,i].tolist() for i in range(len(s.x)-1)]      # coefficients of the piecewise-cubic derivative (pure-python Horner evaluation: smooth and fast)
        if 'rg' in d.files: s.rg=d['rg']; s.g=d['g']; s.gs=CubicSpline(s.rg,s.g)      # row profile (tables of collapse_tail.make_table); the tables of strong.py have none: PU0MODE=zero
    def phv(s,v):
        i=bisect.bisect_right(s.x,v)-1; i=min(max(i,0),len(s.c)-1); d=v-s.x[i]; c=s.c[i]
        return (c[0]*d+c[1])*d+c[2]
    def pu0(s,r):  # dphi/dU on the row, U-gauge: (dphi/dr)(r) * r_U
        return float(s.gs(r))
def horizon_c(S,model,L2,phv,vH,r0=None):
    """Event horizon column: r_v = r_v r Q/2 - 4 pi r c1 phi_v^2 with r_v=0 at v=vH (teleological), r(0)=r0.  Backward shooting on r(vH); the integration is stopped by events if r leaves [0.2 r0, 40 r0]
    (that happens for a bracket value of r(vH) that is too large or too small when the horizon grows a lot, e.g. a strong infalling pulse) and the sign of g is taken from the event."""
    r0=S.rp if r0 is None else r0
    def f(v,y):
        r,rv=y; psi=(1-2*rv)/r**2; Q,c1,_,_=[float(x) for x in coef(model,L2,psi)]
        return [rv, rv*(r*Q/2)-4*np.pi*r*c1*phv(v)**2]
    big=lambda v,y: y[0]-40*r0
    small=lambda v,y: y[0]-0.2*r0
    big.terminal=True; small.terminal=True
    def shoot(rf,dense=False): return solve_ivp(f,[vH,0.0],[rf,0.0],method='DOP853',rtol=1e-13,atol=1e-300,dense_output=dense,events=(big,small))
    def g(rf):
        s_=shoot(rf)
        if s_.status==1: return (1.0 if s_.t_events[0].size else -1.0)*1e6
        return s_.y[0,-1]-r0
    a=r0; b=r0+1e-12
    while g(b)<0: b=r0+2*(b-r0)
    rf=brentq(g,a,b,xtol=1e-16,rtol=1e-15)
    so=shoot(rf,True)
    class H: pass
    h=H(); h.rf=rf; h.sol=lambda v: so.sol(v); return h
def build_c(S,model,L2,U1,v1,hs,hv,T,c,vH,pumode='profile'):
    nv=int(round(v1/hv))+1; v=hv*np.arange(nv)
    smax=np.log(1+U1*S.kp/c)/S.kp; nu=int(round(smax/hs))+1; sg_=hs*np.arange(nu); U=c*np.expm1(S.kp*sg_)/S.kp; gp=c*np.exp(S.kp*sg_)
    hz=horizon_c(S,model,L2,T.phv,vH); phv=T.phv
    Rs,Sg,RUs,_,SUs,_=S.fields(U,0.0)
    pu0=(np.array([T.pu0(r) for r in Rs])*RUs) if pumode=='profile' else np.zeros(nu)     # phi_U on the row (U gauge)
    pu0f=CubicSpline(U[:min(nu,2000)] if False else U,pu0) if False else None
    sQ=lambda r,rv: r*float(coef(model,L2,(1-2*rv)/r**2)[0])/2
    r_,rv_,_,_,sU0,_=[a[0] for a in S.fields(np.array([0.0]),0.0)]
    pc0=float(pu0[0])
    def rhsH(t,Y):
        sg,sU,pU=Y; r,rv=hz.sol(t); rU=-0.5*np.exp(sg)
        _,b,c_=Fq(model,L2,r,sg,rU,rv,pU,phv(t))
        return [sQ(r,rv),float(b),float(c_)]
    sH=solve_ivp(rhsH,[0,v1],[np.log(2.0),sU0,pc0],t_eval=v,method='DOP853',rtol=1e-12,atol=1e-14); assert sH.success
    r0h,rv0=hz.sol(0); sgv0=sQ(r0h,rv0)
    # row ODEs: phi_U(U) by interpolation of the profile in U (r(U) and r_U(U) are known on the grid; use a spline of pu0 in U)
    pus=CubicSpline(U,pu0) if pumode=='profile' else (lambda x:0.0)
    def rhsT(t,Y):
        r,sg,rU,_,sUt,_=[a[0] for a in S.fields(np.array([t]),0.0)]
        a,b,c_=Fq(model,L2,r,sg,rU,Y[0],float(pus(t)),Y[2]); return [float(a),float(b),float(c_)]
    sT=solve_ivp(rhsT,[0,U[-1]],[rv0,sgv0,phv(0)],t_eval=U,method='DOP853',rtol=1e-12,atol=1e-14); assert sT.success
    R0,SG0,RU0,RV0,SU0,SV0,PU0,PV0=[np.zeros(nu) for _ in range(8)]
    R0[:]=Rs; SG0[:]=Sg; RU0[:]=RUs; SU0[:]=SUs; RV0[:]=sT.y[0]; SV0[:]=sT.y[1]; PV0[:]=sT.y[2]; PU0[:]=pu0
    rH=np.array([hz.sol(t)[0] for t in v]); rvH=np.array([hz.sol(t)[1] for t in v])
    Rc=rH; SGc=sH.y[0].copy(); RUc=-0.5*np.exp(sH.y[0]); RVc=rvH; SVc=np.array([sQ(a,b) for a,b in zip(rH,rvH)])
    SUc=sH.y[1].copy(); PUc=sH.y[2].copy(); PVc=np.array([phv(t) for t in v])
    for a,bv in ((R0,Rc),(SG0,SGc),(RU0,RUc),(RV0,RVc),(SU0,SUc),(SV0,SVc),(PU0,PUc),(PV0,PVc)): a[0]=bv[0]
    SG0=SG0+np.log(gp); RU0=RU0*gp; SU0=SU0*gp+S.kp; PU0=PU0*gp
    SGc=SGc+np.log(gp[0]); RUc=RUc*gp[0]; SUc=SUc*gp[0]+S.kp; PUc=PUc*gp[0]
    row0=np.ascontiguousarray(np.vstack([R0,SG0,RU0,RV0,SU0,SV0,PU0,PV0])); col0=np.ascontiguousarray(np.vstack([Rc,SGc,RUc,RVc,SUc,SVc,PUc,PVc]))
    return dict(s=sg_,v=v,U=U,gp=gp,row0=row0,col0=col0,hz=hz,nu=nu,nv=nv,pus=pus)
if __name__=='__main__':
    fn=sys.argv[1]; v1=float(sys.argv[2]); pairs=[tuple(float(t) for t in x.split(':')) for x in sys.argv[3:]]
    model=1; L2=1.0; MASS=float(os.environ.get('MASS','5')); pumode=os.environ.get('PU0MODE','profile')
    T=Tail(fn); S=StaticU(MASS)
    U1=1.5; c=0.2*np.exp(-S.kp*v1); Uq=[0.3,0.6,1.0,1.2]; vq=np.arange(20,v1-1.9,1.0)
    sq=[float(np.round(np.log(1+x*S.kp/c)/S.kp/0.2)*0.2) for x in Uq]; Uact=[float(c*np.expm1(S.kp*s)/S.kp) for s in sq]
    data={}
    for hs,hv in pairs:
        t=time.time(); d=build_c(S,model,L2,U1,v1,hs,hv/2,T,c,v1+300.0,pumode)
        row0=d['row0'].copy(); Ux=d['U']; zz=np.where(Ux<1.0,-Ux*S.w(Ux),row0[0]-S.rp); row0[0]=zz     # Delta_0 = z(U), continuous at s=0
        hz=d['hz']; r0h,rv0=hz.sol(0); sQ=lambda r,rv: r*float(coef(model,L2,(1-2*rv)/r**2)[0])/2; sgv0=sQ(r0h,rv0)
        pus=d['pus']
        def rhsD(t,Y):
            r,sg,rU,_,sUt,_=[a[0] for a in S.fields(np.array([t]),0.0)]
            a,b,c_=Fq(model,L2,r,sg,rU,rv0+Y[0],float(pus(t)),Y[2]); return [float(a),float(b),float(c_)]
        sD=solve_ivp(rhsD,[0,d['U'][-1]],[0.0,sgv0,T.phv(0)],t_eval=d['U'],method='DOP853',rtol=1e-13,atol=[1e-26,1e-14,1e-300]); assert sD.success
        row0[3]=sD.y[0]
        cols=[int(round(s/hs)) for s in sq]; out=run_E(model,L2,row0,d['col0'],hs,hv,cols)
        ii=[int(round(x/hv)) for x in vq]
        data[str(hv)]={nm:[out[n][ii,f].tolist() for n in range(len(cols))] for f,nm in enumerate(['r','sg','rs','rv','sgs','sV','Ps','PV'])}
        data[str(hv)]['nan']=int(np.isnan(out).sum())
        print('C: hs=%g hv=%g nu=%d nv=%d %.0fs nan=%d'%(hs,hv,d['nu'],len(out[0]),time.time()-t,np.isnan(out).sum()),flush=True)
        tag=os.environ.get('TAG','c')
        json.dump(dict(model=model,L2=L2,Uq=Uact,sq=sq,vq=vq.tolist(),v1=v1,tail=os.path.basename(fn),pumode=pumode,data=data),open('genc_%s_hs%g_hv%g_v%g.json'%(tag,hs,hv,v1),'w'))
