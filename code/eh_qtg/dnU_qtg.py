"""Event-horizon-regular data for the double-null evolution in 4D quasi-topological gravity (Paper F).

Same static Hayward exterior/interior in (U,v) as Paper E/G (dnU.StaticU; the static metric of the Hayward h is the Hayward metric), but
the teleological horizon data and the transverse integrations use the QTG equations of Paper F:
   r_UU - s_U r_U = -(4 pi r c1) phi_U^2 ,  r_vv - s_v r_v = -(4 pi r c1) phi_v^2 ,  c1 = 1/h'(psi)
   r_Uv = -(W r/4) Q(psi),  s_Uv, phi_Uv as in qtg_lib.F,  psi = (1+4 r_U r_v/W)/r^2.
On H+ = {U=0} in the EF gauge r_U = -W/2 (so y = -r_U/W = 1/2):
   psi_H = (1-2 r_v)/r^2,   s_v = r Q(psi_H)/2,   r_vv = s_v r_v - 4 pi r c1(psi_H) phi_v^2 ,
which for h = psi is the horizon equation of Paper E.  Backward shooting from (r_f, r_v=0) at late v fixes r(0)=r_+.
"""
import os, sys, numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
_here=os.path.dirname(os.path.abspath(__file__))
import dnU
from dnU import StaticU, PHVF, V0
sys.path.insert(0,os.environ.get('QTG_CODE',os.path.join(_here,'..')))
import qtg_lib
from qtg_lib import coef, F as Fq, run_stream as run_stream_q

def horizon_q(S,model,L2,B,k,vH,r0=None):
    r0=S.rp if r0 is None else r0
    phv=lambda v:PHVF(k,B,v)
    def f(v,y):
        r,rv=y; psi=(1-2*rv)/r**2; Q,c1,_,_=[float(x) for x in coef(model,L2,psi)]
        return [rv, rv*(r*Q/2)-4*np.pi*r*c1*phv(v)**2]
    def shoot(rf,dense=False): return solve_ivp(f,[vH,0.0],[rf,0.0],method='DOP853',rtol=1e-13,atol=1e-300,dense_output=dense)
    g=lambda rf: shoot(rf).y[0,-1]-r0
    if B==0: rf=r0
    else:
        a=r0; b=r0+1e-12
        while g(b)<0: b=r0+2*(b-r0)
        rf=brentq(g,a,b,xtol=1e-16,rtol=1e-15)
    so=shoot(rf,True)
    class H: pass
    h=H(); h.rf=rf; h.sol=lambda v: so.sol(v); return h

def build_eh_q(S,model,L2,U1,v1,hs,hv,B,k=1.5,vH=None,rtol=1e-12,c=None):
    """Grid uniform in s with U=c(e^{kp s}-1)/kp (c=None: uniform U).  Returns dict(row0 (8,nu) on v=0, col0 (8,nv) on U=0, ...) in (s,v) variables:
    sigma_s=sigma~+ln g', r_s=r_U g', sigma_s(derivative)=sigma~_U g'+kp, phi_s=phi_U g'  (g'=c e^{kp s})."""
    nv=int(round(v1/hv))+1; v=hv*np.arange(nv)
    if c is None:
        nu=int(round(U1/hs))+1; U=hs*np.arange(nu); gp=np.ones(nu); sg_=U
    else:
        smax=np.log(1+U1*S.kp/c)/S.kp; nu=int(round(smax/hs))+1; sg_=hs*np.arange(nu); U=c*np.expm1(S.kp*sg_)/S.kp; gp=c*np.exp(S.kp*sg_)
    vH=v1+150.0 if vH is None else vH
    hz=horizon_q(S,model,L2,B,k,vH); phv=lambda t:PHVF(k,B,t)
    sQ=lambda r,rv: r*float(coef(model,L2,(1-2*rv)/r**2)[0])/2          # sigma_v on H+
    r_,rv_,_,_,sU0,_=[a[0] for a in S.fields(np.array([0.0]),0.0)]
    def rhsH(t,Y):
        sg,sU,pU=Y; r,rv=hz.sol(t); rU=-0.5*np.exp(sg)
        _,b,c_=Fq(model,L2,r,sg,rU,rv,pU,phv(t))
        return [sQ(r,rv),float(b),float(c_)]
    sH=solve_ivp(rhsH,[0,v1],[np.log(2.0),sU0,0.0],t_eval=v,method='DOP853',rtol=rtol,atol=1e-14); assert sH.success
    Rs,Sg,RUs,_,SUs,_=S.fields(U,0.0)
    r0h,rv0=hz.sol(0); sgv0=sQ(r0h,rv0)
    def rhsT(t,Y):
        r,sg,rU,_,sUt,_=[a[0] for a in S.fields(np.array([t]),0.0)]
        a,b,c_=Fq(model,L2,r,sg,rU,Y[0],0.0,Y[2]); return [float(a),float(b),float(c_)]
    sT=solve_ivp(rhsT,[0,U[-1]],[rv0,sgv0,phv(0)],t_eval=U,method='DOP853',rtol=rtol,atol=1e-14); assert sT.success
    R0,SG0,RU0,RV0,SU0,SV0,PU0,PV0=[np.zeros(nu) for _ in range(8)]
    R0[:]=Rs; SG0[:]=Sg; RU0[:]=RUs; SU0[:]=SUs; RV0[:]=sT.y[0]; SV0[:]=sT.y[1]; PV0[:]=sT.y[2]
    rH=np.array([hz.sol(t)[0] for t in v]); rvH=np.array([hz.sol(t)[1] for t in v])
    Rc=rH; SGc=sH.y[0].copy(); RUc=-0.5*np.exp(sH.y[0]); RVc=rvH; SVc=np.array([sQ(a,b) for a,b in zip(rH,rvH)])
    SUc=sH.y[1].copy(); PUc=sH.y[2].copy(); PVc=phv(v)
    for a,bv in ((R0,Rc),(SG0,SGc),(RU0,RUc),(RV0,RVc),(SU0,SUc),(SV0,SVc),(PU0,PUc),(PV0,PVc)): a[0]=bv[0]
    if c is not None:
        SG0=SG0+np.log(gp); RU0=RU0*gp; SU0=SU0*gp+S.kp; PU0=PU0*gp
        SGc=SGc+np.log(gp[0]); RUc=RUc*gp[0]; SUc=SUc*gp[0]+S.kp; PUc=PUc*gp[0]
    row0=np.ascontiguousarray(np.vstack([R0,SG0,RU0,RV0,SU0,SV0,PU0,PV0])); col0=np.ascontiguousarray(np.vstack([Rc,SGc,RUc,RVc,SUc,SVc,PUc,PVc]))
    return dict(s=sg_,v=v,U=U,gp=gp,row0=row0,col0=col0,hz=hz,nu=nu,nv=nv)
