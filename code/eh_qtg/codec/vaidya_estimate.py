"""Vaidya-like estimate of the horizon mass for the pulse tables: dm/dv = 4 pi r_+(m)^2 phi_v^2 (r_+ of the static Hayward hole, or 2m for GR), m(0)=5.
It has a pole at a finite pulse strength (the horizon area grows with the mass); run from codec/sc.  usage: vaidya_estimate.py"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline
d=np.load('pt_P0.0.npz'); t=d['t']
def rplus(m):
    rt=np.roots([1,-2*m,0,2*m]); rt=rt[abs(rt.imag)<1e-9].real; return rt.max()
for model,rp in (('Hayward',rplus),('GR',lambda m:2*m)):
    def mf(P):
        x=np.clip((t-10)/20,0,1); cs=CubicSpline(t,d['phiH']+P*np.sin(np.pi*x)**4).derivative()
        ev=lambda v,m: m[0]-1e4; ev.terminal=True
        s=solve_ivp(lambda v,m:[4*np.pi*rp(m[0])**2*float(cs(v))**2],[0,300],[5.0],rtol=1e-10,events=ev)
        return s.y[0,-1] if s.status!=1 else np.inf
    print(model,' '.join('P=%g:m_f=%.3f'%(P,mf(P)) for P in (0.01,0.03,0.05,0.07,0.08,0.09,0.1,0.12)))
