"""Compatibility check of sigma_uv (Eq. (10) of Paper F) at states like those behind the front, in 80-digit decimal arithmetic (no mpmath needed):
Hayward h (h'=1/z^2, h''=2/z^3, z=1-psi, exact), psi within 1e-1..1e-6 of the pole, W down to 1e-30, g=phi_u phi_v/W up to 1e12.  Same identity as check_compat.py:
sigma_uv from d_v(r_uu) = d_u(r_uv) with r_uu, r_vv (Raychaudhuri), r_uv, phi_uv from the field equations, against Eq. (10).  Prints the max relative defect per range of z."""
import random
from decimal import Decimal as D, getcontext
getcontext().prec=80
random.seed(7)
PI=D('3.14159265358979323846264338327950288419716939937510582097494459230781640628620899')
def u(a,b): return D(repr(random.uniform(a,b)))
def lg(a,b): return D(10)**D(repr(random.uniform(a,b)))
def one(z,W,r,g):
    psi=1-z; ru=-u(0.2,1)*D('1e-8'); rv=(psi*r*r-1)*W/(4*ru)
    su=u(-1,1); sv=u(-1,1); pu=u(0.2,1)*D('1e-2'); pv=g*W/pu*random.choice([-1,1])
    hp=1/(z*z); hpp=2/(z**3); h=psi/z
    Q=3*h/hp-2*psi; c=4*PI*r/hp
    ruu=su*ru-c*pu**2; rvv=sv*rv-c*pv**2; ruv=-W*r*Q/4; puv=-(ru*pv+rv*pu)/r
    psi_u=(4*(ruu*rv+ru*ruv)/W-4*ru*rv*su/W)/r**2-2*psi*ru/r
    psi_v=(4*(ruv*rv+ru*rvv)/W-4*ru*rv*sv/W)/r**2-2*psi*rv/r
    Qp=3-3*h*hpp/hp**2-2
    d_u_ruv=-(W*su*r+W*ru)/4*Q-(W*r/4)*Qp*psi_u
    dvc=4*PI*(rv/hp-r*hpp*psi_v/hp**2)
    suv=(d_u_ruv-su*ruv+dvc*pu**2+2*c*pu*puv)/ru
    c2=9*h**2*hpp/(4*hp**3); c3=hpp/hp**3
    suv10=W*psi/2-W*c2-8*PI*pu*pv/hp+64*PI**2*c3*pu**2*pv**2/W
    return suv, suv10
print('z range            max rel defect of sigma_uv   [W in 1e-30..1e-5, g in 1e3..1e12, r in 1.04..1.07; 2000 states per range; 80-digit arithmetic]')
for z0,z1 in ((-1,-2),(-2,-3),(-3,-4),(-4,-5),(-5,-6)):
    worst=D(0)
    for _ in range(2000):
        z=D(10)**D(repr(random.uniform(z1,z0))); W=lg(-30,-5); r=u(1.04,1.07); g=lg(3,12)
        a,b=one(z,W,r,g); worst=max(worst,abs(a-b)/abs(b))
    print(' 1e%d..1e%d      %.2e'%(z1,z0,float(worst)))
