"""Threshold-scan summary (Paper F, pulse strength).  usage: pscan_summary.py P1 P2 ...  (run from codec/sc; needs pt_P*.npz and genc_P*_hs0.2_hv0.2_v1000.json)
For each P: (i) r_inf of the collapse ray (horizon ODE shot from v=1300 = v1+300 as in gen_c) (code E), (ii) r_-(m) inverted to the implied mass m*, (iii) the ray mass just before inflation
(first v with |r-r_inf|<3e-5 r_inf),  (iv) the final horizon radius r_f from the horizon ODE (the root that makes r(0)=r_+(5)), converted to
a mass via r_+(m_f)=r_f (static Hayward),  (v) the crude horizon mass gain 4 pi r_+^2 int phi_v^2."""
import sys,json,os,glob,numpy as np
sys.argv_save=sys.argv[:]; Ps=sys.argv[1:]; sys.argv=['x']; sys.path.insert(0,'..')
from gen_c import *
from scipy.optimize import brentq
sys.path.insert(0,os.environ['QTG_CODE'])
def rminus(m):
    rt=np.roots([1,-2*m,0,2*m]); rt=rt[abs(rt.imag)<1e-9].real; return rt[rt>0].min()
def rplus(m):
    rt=np.roots([1,-2*m,0,2*m]); rt=rt[abs(rt.imag)<1e-9].real; return rt[rt>0].max()
S=StaticU(5.0); r0=S.rp; model=1; L2=1.0
for P in Ps:
    tb=np.load('pt_P%s.npz'%P); t=tb['t']; cs=CubicSpline(t,tb['phiH']).derivative()
    def f(v,y):
        r,rv=y; psi=(1-2*rv)/r**2; Q,c1,_,_=[float(z) for z in coef(model,L2,psi)]
        return [rv, rv*(r*Q/2)-4*np.pi*r*c1*float(cs(min(v,t[-1])))**2]
    g=lambda rf: solve_ivp(f,[1300.,0.0],[rf,0.0],method='DOP853',rtol=1e-12,atol=1e-14).y[0,-1]-r0
    rf=brentq(g,r0*1.0001,40,xtol=1e-10) if float(P)>0 else r0
    mf=brentq(lambda m: rplus(m)-rf,4.9,60) if float(P)>0 else 5.0
    tt=t[t<=200]; crude=4*np.pi*r0**2*np.trapezoid(cs(tt)**2,tt)
    fn=glob.glob('genc_P%s_hs0.2_hv0.2_v1000.json'%P)
    if not fn: print(P,'rf=%.4f m_f=%.4f crude=%.3f (no run)'%(rf,mf,crude)); continue
    d=json.load(open(fn[0])); v=np.array(d['vq']); F={a:np.array(b[2],float) for a,b in d['data']['0.2'].items() if a not in('nan','mon')}
    r=F['r']; rinf=r[-1]; i=int(np.argmax(abs(r-rinf)<3e-5*rinf))
    W=np.exp(F['sg']); y=-F['rs']/W; z=(r**2-1-4*y*(-F['rv']))/r**2; mray=(r**3*(1-z)/(2*z))
    mstar=brentq(lambda m: rminus(m)-rinf,4.0,80)
    print('P=%s  crude dm=%.3f  r_f=%.4f -> m_f=%.4f (r_-=%.5f) | r_inf=%.5f -> m*=%.4f | ray mass at freeze m=%.4f (r_-=%.5f) | v_freeze=%.1f'%(P,crude,rf,mf,rminus(mf),rinf,mstar,mray[i],rminus(mray[i]),v[i]))
