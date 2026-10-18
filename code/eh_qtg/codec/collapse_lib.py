"""Collapse driver (Paper F, tails).  m0>0 (rays): the data on v=v0 are those of a static hole of mass m0 (sigma=0 gauge, r_u=-1/2, r_v=f/2, sigma_v=(f'(r)-f'(r_c))/2) and r_v=f(r_c)/2 on u=u0 before the pulse.  Double-null free evolution of a self-gravitating massless scalar in GR (model 0) or Hayward QTG (model 1),
ds^2=-W du dv+r^2 dOmega^2, from two characteristic rays: flat data on v=v0 (u0<=u<=uend<v0, no regular centre in the grid, cf. Burko-Ori) and an
ingoing compact scalar pulse on u=u0 (gauge sigma=0 on both rays)."""
import numpy as np, ctypes, os
from scipy.integrate import solve_ivp
_here=os.path.dirname(os.path.abspath(__file__))
lib=ctypes.CDLL(os.path.join(_here,'libqtgcol.so')); dp=ctypes.POINTER(ctypes.c_double); ip=ctypes.POINTER(ctypes.c_int)
lib.evolve_col.argtypes=[ctypes.c_int,ctypes.c_int,ctypes.c_double,ctypes.c_double,ctypes.c_int,ctypes.c_double,dp,dp,ctypes.c_int,ip,dp,ctypes.c_int,ctypes.c_int,ip,dp,dp]
def coef(model,L2,psi):
    if model==0: return psi,1.0
    z=1-L2*psi; return psi*(1-3*L2*psi), z*z
def Fs(model,L2,r,sg,ru,rv,pu,pv):
    W=np.exp(sg); psi=(1+4*ru*rv/W)/r**2
    if model==0: Q,c1,c2,c3=psi,1.0,0.0,0.0
    else: z=1-L2*psi; Q,c1,c2,c3=psi*(1-3*L2*psi),z*z,4.5*L2*psi**2*z,2*L2*z**3
    return (-0.25*W*r*Q, 0.5*W*psi-W*c2-8*np.pi*c1*pu*pv+64*np.pi**2*c3*pu**2*pv**2/W, -(ru*pv+rv*pu)/r)
def pulse(A,va,vb):
    def ph(v):
        x=np.clip((v-va)/(vb-va),0,1); return A*np.sin(np.pi*x)**4
    def dph(v):
        x=(v-va)/(vb-va); inside=(x>0)&(x<1); xx=np.clip(x,0,1)
        return np.where(inside,A*4*np.sin(np.pi*xx)**3*np.cos(np.pi*xx)*np.pi/(vb-va),0.0)
    return ph,dph
def static_profile(model,m,L2=1.0,rmax=1.0e5):
    """Static l=0 solution of the final exterior with phi -> 1/r:  g(r)=int_r^inf dr'/(r'^2 f(r')) = G(1/r), G(s)=int_0^s ds'/f(1/s'); g = 1/r + m/r^2 + ...  Returns (g, dg/dr=-1/(r^2 f))."""
    from scipy.interpolate import CubicSpline
    def f_of(r):
        return 1-2*m/r if model==0 else 1-2*m*r**2/(r**3+2*m*L2)
    s_=np.linspace(0.0,1.0/(2.5*m if m>0 else 10.0),4001); fs=np.array([1.0 if x==0 else f_of(1.0/x) for x in s_])
    G=CubicSpline(s_,1.0/fs).antiderivative()
    return (lambda r: G(1.0/r)), (lambda r: -1.0/(r**2*f_of(r)))
def np_tail(b,ra,dr,model=None,m=None,L2=1.0):
    """model=None: phi = b S((r-ra)/dr)/r^2 (see below).  With model,m: phi = b S((r-ra)/dr) g(r), g the static solution of mass m with g->1/r (scalar charge at infinity, r*phi -> b; I_0=-b m)."""
    if model is not None:
        g,gp=static_profile(model,m,L2)
        def T(r):
            x=np.clip((r-ra)/dr,0,1); return b*x**4*(35-84*x+70*x**2-20*x**3)*g(r)
        def dT(r):
            x=np.clip((r-ra)/dr,0,1); S=x**4*(35-84*x+70*x**2-20*x**3); Sp=140*x**3*(1-x)**3
            return b*(Sp/dr*g(r)+S*gp(r))
        return T,dT
    return _np_tail0(b,ra,dr)
def _np_tail0(b,ra,dr):
    """Non-compact addition to the data on u=u0 (nonzero Newman-Penrose constant): phi = b S((r-ra)/dr)/r^2 as a function of the areal radius r,
    S(x)=x^4(35-84x+70x^2-20x^3) (C^3 ramp, S'=140x^3(1-x)^3); I_0 = lim r^2 d_r(r phi) = -b.  Returns (phi(r), dphi/dr)."""
    def T(r):
        x=np.clip((r-ra)/dr,0,1); return b*x**4*(35-84*x+70*x**2-20*x**3)/r**2
    def dT(r):
        x=np.clip((r-ra)/dr,0,1); S=x**4*(35-84*x+70*x**2-20*x**3); Sp=140*x**3*(1-x)**3
        return b*(Sp/dr/r**2-2*S/r**3)
    return T,dT
def fstat(model,L2,m,r):
    """Static metric function f(r) and f'(r): Schwarzschild (model 0) or Hayward f=1-2 m r^2/(r^3+2 m L2) (model 1)."""
    if m==0: return np.ones_like(np.asarray(r,float)),np.zeros_like(np.asarray(r,float))
    if model==0: return 1-2*m/r, 2*m/r**2
    c=2*m*L2; return 1-2*m*r**2/(r**3+c), -2*m*(2*r*c-r**4)/(r**3+c)**2
def rays(model,L2,u0,uend,v0,vmax,hu,hv,A,va,vb,rtol=1e-13,tail=None,m0=0.0):
    nu=int(round((uend-u0)/hu))+1; nv=int(round((vmax-v0)/hv))+1
    u=u0+hu*np.arange(nu); v=v0+hv*np.arange(nv)
    ph,dph=pulse(A,va,vb)
    if tail is not None: Tf,dTf=np_tail(*tail)
    r00=(v0-u0)/2
    def rhs(t,Y):
        r,rv,ru,su,pu=Y; pv=dph(t)+(dTf(r)*rv if tail is not None else 0.0); a,b,c=Fs(model,L2,r,0.0,ru,rv,pu,pv)
        c1=coef(model,L2,(1+4*ru*rv)/r**2)[1]
        return [rv,-4*np.pi*r*c1*pv**2,a,b,c]
    fc,fpc=[float(x) for x in fstat(model,L2,m0,r00)]
    sol=solve_ivp(rhs,[v0,v[-1]],[r00,0.5*fc,-0.5,0.0,0.0],t_eval=v,method='DOP853',rtol=rtol,atol=1e-15,max_step=0.5)
    assert sol.success
    col0=np.zeros((8,nv)); Y=sol.y
    col0[0]=Y[0]; col0[1]=0; col0[2]=Y[2]; col0[3]=Y[1]; col0[4]=Y[3]; col0[5]=0; col0[6]=Y[4]; col0[7]=dph(v)+(dTf(Y[0])*Y[1] if tail is not None else 0.0)
    row0=np.zeros((8,nu)); row0[0]=(v0-u)/2; row0[2]=-0.5
    fr,fpr=fstat(model,L2,m0,row0[0]); row0[3]=0.5*fr; row0[5]=0.5*(fpr-fpc)
    return u,v,row0,col0,ph
def run(model,L2,row0,col0,hu,hv,cols,rows=(),niter=3):
    nu=row0.shape[1]; nv=col0.shape[1]; cols=np.ascontiguousarray(cols,dtype=np.int32); rws=np.ascontiguousarray(rows,dtype=np.int32)
    out=np.zeros((len(cols),nv,8)); snap=np.zeros((max(1,len(rws)),8,nu)); ah=np.zeros(nv)
    row0=np.ascontiguousarray(row0); col0=np.ascontiguousarray(col0)
    lib.evolve_col(nu,nv,hu,hv,model,L2,row0.ctypes.data_as(dp),col0.ctypes.data_as(dp),len(cols),cols.ctypes.data_as(ip),out.ctypes.data_as(dp),niter,len(rws),rws.ctypes.data_as(ip),snap.ctypes.data_as(dp),ah.ctypes.data_as(dp))
    return out,snap[:len(rws)],ah
def ms_mass(model,L2,R,SG,RU,RV):
    W=np.exp(SG); psi=(1+4*RU*RV/W)/R**2
    if model==0: return 0.5*R**3*psi
    return 0.5*R**3*psi/(1-L2*psi)    # generalized mass r^3 h/2
