"""Weighted-mass hypotheses for the tail coefficient B = 8 m_eff |Q| of a collapse pulse into a hole: along the pulse ray u0, m(v) is the generalized mass, q(v)=-2 r r_v phi the charge density
(Q=int q dv, equal to int r^2 phi_v dv after integration by parts), m_eff candidates compared with the measured B/(8|Q|).  usage: weight_test.py PULSE_A PULSE_B PULSE_V1 table.npz ..."""
import sys,os,numpy as np
os.environ['PULSE_A'],os.environ['PULSE_B'],os.environ['PULSE_V1']=sys.argv[1:4]
from strong import *
from fit1 import fitwin
for fn in sys.argv[4:]:
    d=np.load(fn); model=int(d['model']); m0=float(d['m0']); mt=float(d['mt']); A=float(d['A']); mf=float(d['mf']); g=geom(m0,mt); s=g['s']
    uu,vv,r0,c0,ph=rays(model,L2,g['u0'],g['uend'],g['v0'],g['v0']+max(30.0,float(sys.argv[3])+10)*s,0.02*s,0.02*s,A,g['va'],g['vb'],m0=m0)
    r,sg,ru,rv,su,sv,pu,pv=[np.asarray(x) for x in c0]
    m=np.array([ms_mass(model,L2,r[i],sg[i],ru[i],rv[i]) for i in range(len(vv))])
    phi=np.concatenate([[0],np.cumsum(0.5*(pv[1:]+pv[:-1])*np.diff(vv))])
    q=-2*r*rv*phi; Q=np.trapezoid(q,vv); Q2=np.trapezoid(r**2*pv,vv)
    qa=np.trapezoid(r**2*abs(pv),vv)
    s2=mf/5.0; ve=float(d['v1e'])+d['t']; B=fitwin(ve,d['phiH'],1000*s2,2900*s2,3.0)[0]
    meff=B/(8*abs(Q2)); wm=np.trapezoid(m*q,vv)/Q
    # candidates: charge-weighted mass; mass weighted by q, evaluated with m shifted to the pulse centre
    cum=np.concatenate([[0],np.cumsum(0.5*(q[1:]+q[:-1])*np.diff(vv))])/Q   # cumulative charge fraction
    from scipy.optimize import brentq
    vv0=vv; mfun=lambda x: np.interp(x,vv0,m,left=m0,right=m[-1])
    g_=lambda D: np.trapezoid(mfun(vv0-D)*q,vv0)/Q-meff
    try: Dl=brentq(g_,0,60*s)
    except Exception: Dl=float('nan')
    # centroid of charge and mass-weighted quantities
    vc=np.trapezoid(vv*q,vv)/Q
    print('  retardation D(solves <m(v-D)>_q=meff)=%.3f = %.3f s ; q-centroid v-v0=%.3f s; pulse width %.1f s'%(Dl,Dl/s,(vc-g['v0'])/s,(g['vb']-g['va'])/s))
    print('%-28s m0=%-4g mf=%-3g  Q=%9.4f Q(q)=%9.4f  int|r2phiv|/|Q|=%6.1f  meff=B/8Q=%7.4f (F=%.4f)  <m>_q=%7.4f (/mf %.4f)  m(end)=%.4f'%(fn[:28],m0,mf,Q2,Q,qa/abs(Q2),meff,meff/mf,wm,wm/mf,m[-1]))
