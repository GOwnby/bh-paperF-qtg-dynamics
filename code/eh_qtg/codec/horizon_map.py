"""Map r_f -> r(0) of the horizon Raychaudhuri equation shot backward from v=vH with r_v=0, for the pulse tables P sin^4 on [10,30] added to the
collapse horizon field (run from codec/sc after pulse_table.py).  The root r(0)=r_+(5)=9.8979 exists on a monotone branch up to P=0.08; for P>=0.09 it does
not lie below r_f=16 (P=0.09) and the map is non-monotone at P=0.1 (Paper F, Sec. 14).  usage: horizon_map.py"""
import sys,numpy as np; sys.argv=['x']; sys.path.insert(0,'..')
from gen_c import *
S=StaticU(5.0); r0=S.rp; model=1; L2=1.0
d=np.load('pt_P0.0.npz'); t=d['t']
for P in (0.05,0.08,0.09,0.1,0.11,0.12):
    x=np.clip((t-10)/20,0,1); ph=d['phiH']+P*np.sin(np.pi*x)**4
    cs=CubicSpline(t,ph).derivative()
    def f(v,y):
        r,rv=y; psi=(1-2*rv)/r**2; Q,c1,_,_=[float(z) for z in coef(model,L2,psi)]
        return [rv, rv*(r*Q/2)-4*np.pi*r*c1*float(cs(min(v,t[-1])))**2]
    out=[(rf,solve_ivp(f,[310.,0.0],[rf,0.0],method='RK45',rtol=1e-9,atol=1e-12).y[0,-1]) for rf in (10,12,15,20,30,45,70,110,200)]
    print('P=%g  r(0) for r_f='%P,' '.join('%g:%.2f'%o for o in out),flush=True)
