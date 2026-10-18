"""Compatibility check: sigma_uv of Eq. (10) is the value for which d_v(r_uu) = d_u(r_uv) holds, with r_uu and r_vv from the Raychaudhuri equations (8), r_uv from (9), phi_uv from (11).
Random values of (r, r_u, r_v, sigma, sigma_u, sigma_v, phi_u, phi_v) at a point; derivatives of the fields are obtained from the equations themselves (no finite differences in the fields);
the derivatives of h are exact (Hayward) or by complex-step-free finite differences (bounded).  Prints max relative defect."""
import numpy as np,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from qtg_lib import hfun,coef
rng=np.random.default_rng(1)
def check(model,L2,psi_range,n=2000):
    worst=0
    for _ in range(n):
        r=rng.uniform(0.5,3); ru,rv=rng.uniform(-1,1,2); sg=rng.uniform(-2,1); su,sv=rng.uniform(-2,2,2); pu,pv=rng.uniform(-1,1,2)
        W=np.exp(sg); psi=(1+4*ru*rv/W)/r**2
        if not (psi_range[0]<psi<psi_range[1]): continue
        h,hp=hfun(model,L2,psi); e=1e-6*max(1,abs(psi)); hp_p=hfun(model,L2,psi+e)[1]; hp_m=hfun(model,L2,psi-e)[1]; hpp=(hp_p-hp_m)/(2*e)
        Q=3*h/hp-2*psi; c=4*np.pi*r/hp                         # r_uu = su ru - c pu^2 ; r_vv = sv rv - c pv^2
        ruu=su*ru-c*pu**2; rvv=sv*rv-c*pv**2; ruv=-W*r*Q/4; puv=-(ru*pv+rv*pu)/r
        # psi_u, psi_v from psi=(1+4 ru rv/W)/r^2
        psi_u=(4*(ruu*rv+ru*ruv)/W-4*ru*rv*su/W)/r**2-2*psi*ru/r
        psi_v=(4*(ruv*rv+ru*rvv)/W-4*ru*rv*sv/W)/r**2-2*psi*rv/r
        Qp=3-3*h*hpp/hp**2-2                                  # dQ/dpsi
        d_u_ruv=-(W*su*r+W*ru)/4*Q-(W*r/4)*Qp*psi_u
        # d_v of r_uu:  sigma_uv r_u + su ruv - d_v(c) pu^2 - 2 c pu puv ; d_v c = 4pi[(rv)/hp - r hpp psi_v/hp^2]
        dvc=4*np.pi*(rv/hp-r*hpp*psi_v/hp**2)
        # solve sigma_uv from  d_v(r_uu) = d_u(r_uv)
        suv=(d_u_ruv-su*ruv+dvc*pu**2+2*c*pu*puv)/ru
        # formula (10)
        c2=9*h**2*hpp/(4*hp**3); c3=hpp/hp**3
        suv10=0.5*W*psi-W*c2-8*np.pi*pu*pv/hp+64*np.pi**2*c3*pu**2*pv**2/W
        worst=max(worst,abs(suv-suv10)/max(1e-3,abs(suv10)))
    return worst
print('Hayward  max relative defect of sigma_uv (compatibility vs Eq.(10)): %.2e'%check(1,1.0,(-5,0.95)))
print('bounded  max relative defect of sigma_uv (compatibility vs Eq.(10)): %.2e'%check(2,1.0,(-0.95,0.95)))
