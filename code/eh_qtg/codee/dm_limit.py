"""Closed form of the late growth rate of the generalized mass, dm/dv -> 2 r_- beta_inf kappa_- / c1^II, beta_inf=(r_-^2-1)/4, c1^II=(1-1/r_-^2)^2 (Eq. (dm) of Paper F), and z*m -> r_-^3/2, for the three inner masses (l=1)."""
import sys,os
sys.path.insert(0,os.environ.get('QTG_CODE','../..')); sys.path.insert(0,'..')
from dnU_qtg import StaticU
print('mass   r_-       kappa_-   closed-form dm/dv   r_-^3/2')
for m in (3,5,10):
    S=StaticU(m); rm=S.rm; psi=1/rm**2; km=rm*abs(psi*(1-3*psi))/2; b=(rm**2-1)/4; c1=(1-1/rm**2)**2
    print('%4d   %.6f  %.6f  %.4f              %.5f'%(m,rm,km,2*rm*b*km/c1,0.5*rm**3))
