"""Static background for h(psi)=psi/sqrt(1-alpha^2 psi^2) (Bueno et al. 2509.19016 eq. 51):  psi = x/sqrt(1+alpha^2 x^2), x = 2m/r^3, f = 1 - r^2 psi.
f(r) = P(r) / ( r^6 s (s + r^2 x) ),  s = sqrt(1+alpha^2 x^2),  P(r) = r^6 - 4 m^2 r^4 + 4 m^2 alpha^2   (roots r_-, r_+ of f).  Relative precision near r_- via the shifted polynomial."""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
class Bg2:
    def __init__(s,m=5.0,alpha=1.0,tmax=60.0):
        s.m=m; s.al=alpha; s.a2=alpha**2
        a=np.zeros(7); a[6]=1; a[4]=-4*m*m; a[0]=4*m*m*alpha**2; s.coef=a
        P=lambda r:np.polyval(a[::-1],r)
        rr=np.linspace(0.3,2*m,40000); v=P(rr); idx=np.where(np.sign(v[:-1])*np.sign(v[1:])<0)[0]
        s.rm=brentq(P,rr[idx[0]],rr[idx[0]+1],xtol=1e-15,rtol=1e-15); s.rp=brentq(P,rr[idx[1]],rr[idx[1]+1],xtol=1e-15,rtol=1e-15)
        # shifted coefficients about r_-:  P(r_-+y) = sum_k c_k y^k, c_0 := 0
        from math import comb
        c=np.array([sum(a[j]*comb(j,k)*s.rm**(j-k) for j in range(k,7)) for k in range(7)]); c[0]=0.0; s.c=c
        s.kap=-0.5*s.df(s.rm); s.kap_p=0.5*abs(s.df(s.rp))
        y0=0.5*(s.rp-s.rm)
        A=solve_ivp(lambda t,y:[s.fy(y[0])],[0,tmax],[y0],method='DOP853',rtol=1e-13,atol=1e-300,dense_output=True)
        Bk=solve_ivp(lambda t,y:[s.fy(y[0])],[0,-30],[y0],method='DOP853',rtol=1e-13,atol=1e-300,dense_output=True)
        s.a_,s.b_=A,Bk
    def f(s,r):
        r=np.asarray(r)
        x=2*s.m/r**3; sq=np.sqrt(1+s.a2*x*x); return 1-r*r*x/sq
    def df(s,r,h=1e-20):
        r=np.asarray(r,float); out=np.imag(s.f(r+1j*h))/h
        return float(out) if out.ndim==0 else out
    def fy(s,y):
        r=s.rm+y; x=2*s.m/r**3; sq=np.sqrt(1+s.a2*x*x)
        Py=sum(s.c[k]*y**k for k in range(1,7))
        return Py/(r**6*sq*(sq+r*r*x))
    def y(s,rs):
        rs=np.asarray(rs,float); out=np.empty_like(rs); pos=rs>=0
        out[pos]=s.a_.sol(rs[pos])[0] if pos.any() else 0
        out[~pos]=s.b_.sol(rs[~pos])[0] if (~pos).any() else 0
        return out
if __name__=='__main__':
    b=Bg2(); print('r-=%.8f r+=%.8f kappa-=%.8f kappa+=%.8f'%(b.rm,b.rp,b.kap,b.kap_p))
    for r in (1.5,2.0,5.0): print(r, b.f(r), b.fy(r-b.rm), b.df(r), (b.f(r+1e-6)-b.f(r-1e-6))/2e-6)
