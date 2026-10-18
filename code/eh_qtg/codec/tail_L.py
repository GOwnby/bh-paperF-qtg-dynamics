"""Stage L (Paper F, tails): linear l=0 scalar on the static exterior (GR: f=1-2m/r; Hayward QTG: f=1-2m r^2/(r^3+2 m l^2)) in Eddington null coordinates."""
import numpy as np, ctypes, os
_here=os.path.dirname(os.path.abspath(__file__))
libL=ctypes.CDLL(os.path.join(_here,'libqtgL.so')); dp=ctypes.POINTER(ctypes.c_double)
libL.evolve_L.argtypes=[ctypes.c_int,ctypes.c_int,ctypes.c_double,dp,dp,dp,ctypes.c_int,ctypes.c_int,dp,dp]
class Static:
    """Static background; model 0: GR, model 1: Hayward with l^2=L2.  Exterior r>r_+.  Tortoise r*(r) with an arbitrary additive constant."""
    def __init__(s,model,m,L2=1.0):
        s.model=model; s.m=m; s.L2=L2
        if model==0: s.rp=2*m; s.kp=1/(4*m); s.roots=None
        else:
            rt=np.sort(np.roots([1,-2*m,0,2*m*L2]).real)      # r^3-2m r^2+2 m l^2: roots r3<0<r-<r+
            s.r3,s.rm,s.rp=rt; s.roots=rt
            Pp=lambda r:3*r*r-4*m*r
            s.c=[2*m*r*r/Pp(r) for r in rt]                   # r* = r + sum c_i ln|r-r_i|, c_i=2m r_i^2/P'(r_i)
            s.kp=Pp(s.rp)/(2*(s.rp**3+2*m*L2))                # kappa_+ = f'(r_+)/2
    def f(s,r):
        if s.model==0: return 1-2*s.m/r
        return (r-s.rp)*(r-s.rm)*(r-s.r3)/(r**3+2*s.m*s.L2)
    def fp(s,r):
        if s.model==0: return 2*s.m/r**2
        m,L2=s.m,s.L2; P=r**3-2*m*r*r+2*m*L2; Q=r**3+2*m*L2
        return (3*r*r-4*m*r)/Q-(r-s.rp)*(r-s.rm)*(r-s.r3)*3*r*r/Q**2
    def V(s,r): return s.f(r)*s.fp(r)/r
    def rstar_y(s,y):
        """r* as a function of y=ln(r-r_+) (no cancellation near the horizon)."""
        r=s.rp+np.exp(y)
        if s.model==0: return r+2*s.m*(y-np.log(2*s.m))      # r* = r + 2m ln(r/2m-1)
        return r+s.c[2]*y+s.c[1]*np.log(np.abs(r-s.rm))+s.c[0]*np.log(np.abs(r-s.r3))
    def y_of_rstar(s,x):
        x=np.atleast_1d(np.asarray(x,float)); lo=np.full(x.shape,-745.0); hi=np.full(x.shape,np.log(1e9))
        for _ in range(200):
            mid=0.5*(lo+hi); up=s.rstar_y(mid)<x
            lo=np.where(up,mid,lo); hi=np.where(up,hi,mid)
        return 0.5*(lo+hi)
    def r_of_rstar(s,x): return s.rp+np.exp(s.y_of_rstar(x))
    def rstar(s,r): return s.rstar_y(np.log(r-s.rp))
def run_L(bg,x_row,psi_row,h,vmax_rel,Lh,psi_col_val=0.0):
    """x_row: r* of the row points (uniform spacing h/2 in r*, i.e. u_e spacing h), psi_row = r*phi on the row v=v1e, boundary ray u=u_e0 carries psi=psi_col_val.
    Returns v_rel (v-v1e), phi_H(v)=psi/r on the line r* = -Lh (horizon proxy), plus the final row."""
    nu=len(x_row); nv=int(round(vmax_rel/h))+1
    x0=x_row[0]                                   # r* at (u_e0, v1e)
    k=np.arange(-(nu+1),nv+1)                    # table index k -> r* = x0 + k h/2
    xt=x0+k*h/2; Vt=np.ascontiguousarray(bg.V(bg.r_of_rstar(xt)))
    # the horizon-proxy line r*=-Lh : x(i,j)=x0+(j-i)h/2 = -Lh -> i=j+di, di=round(2(x0+Lh)/h)
    di=int(round(2*(x0+Lh)/h))
    row=np.ascontiguousarray(psi_row,float); col=np.ascontiguousarray(np.full(nv,psi_col_val) if np.isscalar(psi_col_val) else psi_col_val,float); diag=np.zeros(nv); last=np.zeros(nu)
    libL.evolve_L(nu,nv,h,row.ctypes.data_as(dp),col.ctypes.data_as(dp),Vt.ctypes.data_as(dp),nu+1,di,diag.ctypes.data_as(dp),last.ctypes.data_as(dp))
    rH=bg.r_of_rstar(np.array([-Lh]))[0]
    return h*np.arange(nv),diag/rH,last
