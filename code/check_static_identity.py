"""(1) The double-null right-hand sides on the static interior: r_uv = f f'/4 and s_uv = f f''/4 (interior, f<0, W=|f|) for the Hayward h and for h = psi/sqrt(1-psi^2) (m=1).
   (2) The integrability identity c Q' - c = c' (Q + 2 psi), c = 4 pi/h', Q = 3h/h' - 2 psi, checked with numerical derivatives of h for both h (it is what makes
   the u- and v-Raychaudhuri equations compatible with the r_uv equation; derived analytically in the paper)."""
import sys,os,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from qtg_lib import *
print('(1) static interior')
for name,model,L2,bg in (('Hayward m=5',1,1.0,Bg()),('bounded h, m=1',2,1.0,Bg2(1.0,1.0))):
    fs=(lambda r:fstat(bg,r)) if model==1 else (lambda r:bg.f(r))
    worst=0
    for r in np.linspace(bg.rm*1.05,bg.rp*0.97,9):
        e=1e-4*r; f=fs(r); fp=(fs(r+e)-fs(r-e))/(2*e); fpp=(fs(r+e)-2*f+fs(r-e))/e**2
        W=abs(f); psi=(1+4*W/4)/r**2; Q,c1,c2,c3=coef(model,L2,psi)
        ruv=-0.25*W*r*Q; suv=0.5*W*psi-W*c2
        worst=max(worst,abs(ruv-f*fp/4)/max(abs(f*fp/4),1e-3),abs(suv-f*fpp/4)/max(abs(f*fpp/4),1e-3))
    print('  %-16s max relative deviation over 9 radii: %.1e'%(name,worst))
print('(2) integrability identity')
for name,model,L2,psis in (('Hayward',1,1.0,np.array([-3.0,-0.5,0.3,0.9,1.5,4.0])),('bounded h',2,1.0,np.array([-0.9,-0.4,0.2,0.7,0.95]))):
    e=1e-5; worst=0
    for p in psis:
        h0,hp0=hfun(model,L2,p); hm,hpm=hfun(model,L2,p-e); hP,hpP=hfun(model,L2,p+e)
        c=lambda x:4*np.pi/hfun(model,L2,x)[1]
        Q=lambda x:3*hfun(model,L2,x)[0]/hfun(model,L2,x)[1]-2*x
        cp=(c(p+e)-c(p-e))/(2*e); Qp=(Q(p+e)-Q(p-e))/(2*e)
        lhs=c(p)*Qp-c(p); rhs=cp*(Q(p)+2*p); worst=max(worst,abs(lhs-rhs)/max(abs(lhs),1e-8))
    print('  %-10s max relative violation: %.1e'%(name,worst))
