"""Exact static black-hole solution in event-horizon-regular coordinates for an arbitrary smooth f(r) with simple zeros r_- < r_+ (Paper F).

Generalises dnU.StaticU (written for the Hayward polynomial) to f(r) = 1 - r^2 psi(r), h(psi) = 2m/r^3, in particular the bounded characteristic function.
Coordinates: x = U e^{kappa_+ v} = e^{2 kappa_+ r_*},  r = r(x),  x dr/dx = f(r)/(2 kappa_+),  W~ = -f/(kappa_+ U),  r_U = -W~/2,  r_v = f/2,
sigma~_v = f'/2,  sigma~_U = (f'/(2 kappa_+) - 1)/U ;  x<1: r = r_+ + z, z = -x w(x) ;  x>=1: r = r_- + exp(L), L integrated without cancellation.
Divided differences D1(z)=f(r_+ + z)/z, D2(z)=(f'(r_+ + z)-f'(r_+))/z, E1(rho)=f(r_- + rho)/rho are evaluated from Taylor series (truncated-Taylor "jet" arithmetic in float64)
near the zeros and directly elsewhere, so every quantity keeps full relative precision down to x ~ 1e-12 and rho ~ 1e-76.
"""
import os, numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

class Jet:
    """Truncated Taylor series (coefficients c_0..c_{N-1} in eps) with +,-,*,/, sqrt: automatic differentiation without sympy/mpmath."""
    N=16
    def __init__(s,c): s.c=np.zeros(Jet.N); c=np.atleast_1d(np.asarray(c,float)); s.c[:len(c)]=c[:Jet.N]
    @staticmethod
    def _j(x): return x if isinstance(x,Jet) else Jet([x])
    def __add__(s,o): o=Jet._j(o); return Jet(s.c+o.c)
    __radd__=__add__
    def __sub__(s,o): o=Jet._j(o); return Jet(s.c-o.c)
    def __rsub__(s,o): return Jet._j(o)-s
    def __neg__(s): return Jet(-s.c)
    def __mul__(s,o): o=Jet._j(o); return Jet(np.convolve(s.c,o.c)[:Jet.N])
    __rmul__=__mul__
    def __truediv__(s,o):
        o=Jet._j(o); q=np.zeros(Jet.N)
        for n in range(Jet.N): q[n]=(s.c[n]-sum(q[k]*o.c[n-k] for k in range(n)))/o.c[0]
        return Jet(q)
    def __rtruediv__(s,o): return Jet._j(o)/s
    def __pow__(s,n):
        out=Jet([1.0])
        for _ in range(n): out=out*s
        return out
    def sqrt(s):
        q=np.zeros(Jet.N); q[0]=np.sqrt(s.c[0])
        for n in range(1,Jet.N): q[n]=(s.c[n]-sum(q[k]*q[n-k] for k in range(1,n)))/(2*q[0])
        return Jet(q)

class StaticGen:
    def __init__(s,fmp,fnp,fpnp,rlo,rhi,order=14,cut=0.25):
        """fmp: mpmath callable f(r); fnp, fpnp: numpy callables f, f'; (rlo,rhi): brackets containing r_- in [rlo[0],rlo[1]] and r_+ in [rhi[0],rhi[1]]."""
        s.f=fnp; s.fp=fpnp; s.cut=cut
        s.rm=brentq(fnp,*rlo,xtol=1e-16,rtol=1e-15); s.rp=brentq(fnp,*rhi,xtol=1e-16,rtol=1e-15)
        s.kp=0.5*fpnp(s.rp); s.km=-0.5*fpnp(s.rm)
        Jet.N=order+1
        s.cp=fmp(Jet([s.rp,1.0])).c; s.cm=fmp(Jet([s.rm,1.0])).c; s.cp[0]=0.0; s.cm[0]=0.0
        s.kp=0.5*s.cp[1]
        s.tmin=np.log(1e-12)
        g=lambda t,w:[w[0]*(s.D1(-np.exp(t)*w[0])/(2*s.kp)-1)]
        s.sol=solve_ivp(g,[s.tmin,0.0],[1.0],method='DOP853',rtol=1e-13,atol=1e-300,dense_output=True)
        z1=-s.sol.sol(0.0)[0]; s.d0=s.rp-s.rm; L0=np.log(s.d0+z1)
        h=lambda t,L:[s.E1(np.exp(L[0]))/(2*s.kp)]
        s.solL=solve_ivp(h,[0,np.log(5e4)],[L0],method='DOP853',rtol=1e-13,atol=1e-14,dense_output=True)
    # divided differences
    def D1(s,z):
        z=np.asarray(z,float); k=np.arange(1,len(s.cp)); small=np.abs(z)<s.cut
        ser=np.polynomial.polynomial.polyval(z,s.cp[1:]); out=np.where(small,ser,s.f(s.rp+z)/np.where(z==0,1,z)); return out
    def D2(s,z):
        z=np.asarray(z,float); small=np.abs(z)<s.cut
        co=np.array([k*s.cp[k] for k in range(2,len(s.cp))]); ser=np.polynomial.polynomial.polyval(z,co)
        return np.where(small,ser,(s.fp(s.rp+z)-s.fp(s.rp))/np.where(z==0,1,z))
    def E1(s,rho):
        rho=np.asarray(rho,float); small=np.abs(rho)<s.cut
        ser=np.polynomial.polynomial.polyval(rho,s.cm[1:]); return np.where(small,ser,s.f(s.rm+rho)/np.where(rho==0,1,rho))
    def w(s,x):
        x=np.asarray(x,float); out=np.ones_like(x); m=x>1e-12
        if m.any(): out[m]=s.sol.sol(np.log(x[m]))[0]
        return out
    def fields(s,U,v):
        U=np.asarray(U,float); U,vv=np.broadcast_arrays(U,np.asarray(v,float)); ev=np.exp(s.kp*vv); x=U*ev; small=x<1.0
        # exterior-side branch (x<1)
        Ua=np.where(small,U,0.5*np.exp(-s.kp*vv)); xa=Ua*ev; w=s.w(xa); z=-xa*w; r=s.rp+z; D1=s.D1(z); fr=D1*z
        Wt=-fr/(s.kp*np.where(Ua>0,Ua,1.0)); Wt=np.where(Ua>0,Wt,D1*w*ev/s.kp)       # U=0: W~ = D1 w e^{kp v}/kp
        sig=np.log(Wt); rU=-0.5*Wt; rV=0.5*fr; fp=s.fp(r); sV=0.5*fp; sU=ev*(-w)*s.D2(z)/(2*s.kp)
        a=(r,sig,rU,rV,sU,sV)
        # interior branch (x>=1)
        xb=np.where(small,2.0,x); rho=np.exp(s.solL.sol(np.log(xb).ravel())[0]).reshape(xb.shape); r2=s.rm+rho; fr2=s.E1(rho)*rho
        Ub=np.where(small,1.0,U); Wt2=-fr2/(s.kp*Ub); fp2=s.fp(r2)
        b=(r2,np.log(Wt2),-0.5*Wt2,0.5*fr2,(fp2/(2*s.kp)-1)/Ub,0.5*fp2)
        return tuple(np.where(small,A,B) for A,B in zip(a,b))

def bounded(m=5.0,alpha=1.0):
    """f = 1 - 2 m r^2/sqrt(r^6 + 4 alpha^2 m^2)   (h = psi/sqrt(1-alpha^2 psi^2) = 2m/r^3)."""
    fm=lambda r: 1-2*m*(r*r)/((r*r*r*r*r*r)+4*alpha**2*m**2).sqrt()
    fn=lambda r: 1-2*m*r**2/np.sqrt(r**6+4*alpha**2*m**2)
    fpn=lambda r: -4*m*r/np.sqrt(r**6+4*alpha**2*m**2)+6*m*r**7/(r**6+4*alpha**2*m**2)**1.5
    return fm,fn,fpn
def hayward(m=5.0,l2=1.0):
    fm=lambda r: 1-2*m*(r*r)/(r*r*r+2*m*l2)
    fn=lambda r: 1-2*m*r**2/(r**3+2*m*l2)
    fpn=lambda r: -4*m*r/(r**3+2*m*l2)+6*m*r**4/(r**3+2*m*l2)**2
    return fm,fn,fpn
if __name__=='__main__':
    import dnU
    S0=dnU.StaticU(); fm,fn,fpn=hayward(); S=StaticGen(fm,fn,fpn,(0.8,1.2),(9.0,11.0))
    print('Hayward: r- %.12f vs %.12f, r+ %.12f vs %.12f, kp %.12f vs %.12f, km %.9f'%(S.rm,S0.rm,S.rp,S0.rp,S.kp,S0.kp,S.km))
    for U,v in ((0.0,0.0),(1e-9,20.),(0.3,20.),(1.0,0.),(0.6,50.),(1.2,98.)):
        a=np.array([x[0] for x in S.fields(np.array([U]),float(v))]); b=np.array([x[0] for x in S0.fields(np.array([U]),float(v))])
        print(' U=%g v=%g max rel diff %.2e'%(U,v,np.max(np.abs(a-b)/(np.abs(b)+1e-300))))
    fm,fn,fpn=bounded(5.0,1.0); T=StaticGen(fm,fn,fpn,(0.9,1.1),(9.0,11.0))
    print('bounded m=5 alpha=1: r- %.10f r+ %.10f kappa+ %.8f kappa- %.8f'%(T.rm,T.rp,T.kp,T.km))
