"""Python side of the QTG double-null experiments (Paper F).  Static background = Hayward interior with m=5, l=1 (same f as the additive-closure runs at mu=0)."""
import numpy as np, ctypes, os, sys
from scipy.integrate import solve_ivp
_here=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(_here,'..','..','paperE_inner_horizon','code','nonlinear'))   # Bg class (static Hayward interior) from Paper E
from dn2lib import Bg, dfr, fr as fstat      # background class (static Hayward interior, relative precision near r_-)
from qtg_bg2 import Bg2
def bgdf(bg,r): return bg.df(r) if hasattr(bg,'df') else dfr(bg,r)
lib=ctypes.CDLL(os.path.join(_here,'libqtg.so')); dp=ctypes.POINTER(ctypes.c_double)
lib.evolve_qtg.argtypes=[ctypes.c_int,ctypes.c_int,ctypes.c_double,ctypes.c_double,ctypes.c_int,ctypes.c_double]+[dp]*8+[ctypes.c_int]

def coef(model,L2,psi):
    psi=np.asarray(psi,float)
    if model==0: return psi, 1+0*psi, 0*psi, 0*psi
    if model==1:
        z=1-L2*psi; return psi*(1-3*L2*psi), z*z, 4.5*L2*psi**2*z, 2*L2*z**3
    s2=np.maximum(1-L2*psi**2,1e-30); s=np.sqrt(s2); return 3*psi*s2-2*psi, s*s2, 6.75*L2*psi**3*s2, 3*L2*psi*s2*s2
def hfun(model,L2,psi):
    psi=np.asarray(psi,float)
    if model==0: return psi, 1+0*psi
    if model==1: z=1-L2*psi; return psi/z, 1/z**2
    s=np.sqrt(1-L2*psi**2); return psi/s, 1/s**3
def F(model,L2,r,sg,ru,rv,pu,pv):
    W=np.exp(sg); psi=(1+4*ru*rv/W)/r**2; Q,c1,c2,c3=coef(model,L2,psi)
    return (-0.25*W*r*Q, 0.5*W*psi-W*c2-8*np.pi*c1*pu*pv+64*np.pi**2*c3*pu**2*pv**2/W, -(ru*pv+rv*pu)/r)
def psi_of(r,sg,ru,rv): return (1+4*ru*rv/np.exp(sg))/r**2

def build(bg,model,L2,u0,u1,v0,v1,hu,hv,A,B,rtol=1e-12,width=1.0,k=1.5):
    """Characteristic data as in Paper E (phi=B+A e^{-(u/w)^2} on v=0, phi=B(1+v)^-k on u=u0; sigma = static background on both rays; r, r_t from the (modified) Raychaudhuri and r_uv equations)."""
    nu=int(round((u1-u0)/hu))+1; nv=int(round((v1-v0)/hv))+1
    u=u0+hu*np.arange(nu); v=v0+hv*np.arange(nv)
    ph1=lambda x: B+A*np.exp(-(x/width)**2); dph1=lambda x:-2*x/width**2*A*np.exp(-(x/width)**2)
    ph2=lambda x: B*(1+x)**(-k);    dph2=lambda x:-k*B*(1+x)**(-k-1)
    yc=bg.y(np.array([(u0+v0)/2]))[0]; rc=bg.rm+yc; fc=bg.fy(yc)
    out={}
    for name,(s0,s1,n,h,t0,dph,dpt) in {'u':(u0,u1,nu,hu,v0,dph1,dph2(v0)),'v':(v0,v1,nv,hv,u0,dph2,dph1(u0))}.items():
        def rhs(s,Y,t0=t0,dph=dph,name=name):
            r,rs,rt,st,pt=Y
            y=bg.y(np.array([(s+t0)/2]))[0]; rb=bg.rm+y; f=bg.fy(y)
            sg=np.log(abs(f)); ss=bgdf(bg,rb)/2
            ps=dph(s)
            W=np.exp(sg); psi=(1+4*rs*rt/W)/r**2; c1=coef(model,L2,psi)[1]
            rss=ss*rs-4*np.pi*r*c1*ps**2
            if name=='u': a,b,c=F(model,L2,r,sg,rs,rt,ps,pt)
            else:         a,b,c=F(model,L2,r,sg,rt,rs,pt,ps)
            return [rs,rss,a,b,c]
        Y0=[rc,fc/2,fc/2,bgdf(bg,rc)/2,dpt]
        sol=solve_ivp(rhs,[s0,s1],Y0,t_eval=np.minimum(s0+h*np.arange(n),s1),method='DOP853',rtol=rtol,atol=1e-300)
        assert sol.success and sol.y.shape[1]==n,(name,sol.message)
        out[name]=sol.y
    Z=lambda:np.zeros((nv,nu))
    R,SG,RU,RV,SU,SV,PU,PV,PH=[Z() for _ in range(9)]
    Y=out['u']; yb=bg.y((u+v0)/2); rb=bg.rm+yb
    R[0,:]=Y[0]; SG[0,:]=np.log(np.abs(bg.fy(yb))); RU[0,:]=Y[1]; RV[0,:]=Y[2]; SU[0,:]=bgdf(bg,rb)/2; SV[0,:]=Y[3]; PU[0,:]=dph1(u); PV[0,:]=Y[4]; PH[0,:]=ph1(u)
    Y=out['v']; yb=bg.y((u0+v)/2); rb=bg.rm+yb
    R[:,0]=Y[0]; SG[:,0]=np.log(np.abs(bg.fy(yb))); RV[:,0]=Y[1]; RU[:,0]=Y[2]; SV[:,0]=bgdf(bg,rb)/2; SU[:,0]=Y[3]; PV[:,0]=dph2(v); PU[:,0]=Y[4]; PH[:,0]=ph2(v)
    return u,v,[R,SG,RU,RV,SU,SV,PU,PV],PH

lib.evolve_stream_qtg.argtypes=[ctypes.c_int,ctypes.c_int,ctypes.c_double,ctypes.c_double,ctypes.c_int,ctypes.c_double,dp,dp,ctypes.c_int,ctypes.POINTER(ctypes.c_int),dp,ctypes.c_int]
def run_stream(model,L2,row0,col0,hu,hv,cols,niter=3):
    """row0: (8,nu) data on v=v0, col0: (8,nv) data on u=u0; returns out (ncol,nv,8): fields R,SG,RU,RV,SU,SV,PU,PV at u-indices cols for all v."""
    nu=row0.shape[1]; nv=col0.shape[1]; cols=np.ascontiguousarray(cols,dtype=np.int32); out=np.zeros((len(cols),nv,8))
    row0=np.ascontiguousarray(row0); col0=np.ascontiguousarray(col0)
    lib.evolve_stream_qtg(nu,nv,hu,hv,model,L2,row0.ctypes.data_as(dp),col0.ctypes.data_as(dp),len(cols),cols.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),out.ctypes.data_as(dp),niter)
    return out
def run(model,L2,arrs,hu,hv,niter=3):
    nv,nu=arrs[0].shape; p=lambda a:a.ctypes.data_as(dp)
    lib.evolve_qtg(nu,nv,hu,hv,model,L2,*[p(a) for a in arrs],niter); return arrs

def fields(model,L2,arrs):
    """MS mass M=(r/2)(1-f)=r^3 psi/2, generalized mass m=r^3 h(psi)/2, psi."""
    R,SG,RU,RV=arrs[:4]; psi=psi_of(R,SG,RU,RV); h,hp=hfun(model,L2,psi)
    return 0.5*R**3*psi, 0.5*R**3*h, psi

def build_rays(bg,model,L2,u0,u1,v0,v1,hu,hv,A,B,rtol=1e-12,width=1.0,k=1.5):
    """Like build() but returns only the two data rays: row0 (8,nu) on v=v0 and col0 (8,nv) on u=u0 (field order R,SG,RU,RV,SU,SV,PU,PV)."""
    nu=int(round((u1-u0)/hu))+1; nv=int(round((v1-v0)/hv))+1
    u=u0+hu*np.arange(nu); v=v0+hv*np.arange(nv)
    ph1=lambda x: B+A*np.exp(-(x/width)**2); dph1=lambda x:-2*x/width**2*A*np.exp(-(x/width)**2)
    dph2=lambda x:-k*B*(1+x)**(-k-1)
    yc=bg.y(np.array([(u0+v0)/2]))[0]; rc=bg.rm+yc; fc=bg.fy(yc); out={}
    for name,(s0,s1,n,h,t0,dph,dpt) in {'u':(u0,u1,nu,hu,v0,dph1,dph2(v0)),'v':(v0,v1,nv,hv,u0,dph2,dph1(u0))}.items():
        def rhs(s,Y,t0=t0,dph=dph,name=name):
            r,rs,rt,st,pt=Y
            y=bg.y(np.array([(s+t0)/2]))[0]; rb=bg.rm+y; f=bg.fy(y)
            sg=np.log(abs(f)); ss=bgdf(bg,rb)/2; ps=dph(s)
            W=np.exp(sg); psi=(1+4*rs*rt/W)/r**2; c1=coef(model,L2,psi)[1]
            rss=ss*rs-4*np.pi*r*c1*ps**2
            if name=='u': a,b,c=F(model,L2,r,sg,rs,rt,ps,pt)
            else:         a,b,c=F(model,L2,r,sg,rt,rs,pt,ps)
            return [rs,rss,a,b,c]
        sol=solve_ivp(rhs,[s0,s1],[rc,fc/2,fc/2,bgdf(bg,rc)/2,dpt],t_eval=np.minimum(s0+h*np.arange(n),s1),method='DOP853',rtol=rtol,atol=1e-300)
        assert sol.success and sol.y.shape[1]==n,(name,sol.message)
        out[name]=sol.y
    row0=np.zeros((8,nu)); col0=np.zeros((8,nv))
    Y=out['u']; yb=bg.y((u+v0)/2); rb=bg.rm+yb
    row0[0]=Y[0]; row0[1]=np.log(np.abs(bg.fy(yb))); row0[2]=Y[1]; row0[3]=Y[2]; row0[4]=bgdf(bg,rb)/2; row0[5]=Y[3]; row0[6]=dph1(u); row0[7]=Y[4]
    Y=out['v']; yb=bg.y((u0+v)/2); rb=bg.rm+yb
    col0[0]=Y[0]; col0[1]=np.log(np.abs(bg.fy(yb))); col0[3]=Y[1]; col0[2]=Y[2]; col0[5]=bgdf(bg,rb)/2; col0[4]=Y[3]; col0[7]=dph2(v); col0[6]=Y[4]
    return u,v,row0,col0

lib.evolve_stream_qtg_cy.argtypes=[ctypes.c_int,ctypes.c_int,ctypes.c_double,ctypes.c_double,ctypes.c_int,ctypes.c_double,dp,dp,ctypes.c_int,ctypes.POINTER(ctypes.c_int),dp,ctypes.c_int,ctypes.c_double,ctypes.c_int,ctypes.c_int,ctypes.POINTER(ctypes.c_int),dp]
def run_stream_cy(model,L2,row0,col0,hu,hv,cols,niter=3,y0=0.5,mode=3,rows=None):
    """Constrained streaming evolution for event-horizon-regular data (grid uniform in s, hu = ds): r_u = -y W with y from the u-Raychaudhuri constraint
    (y=y0 on the horizon column) and, for mode 2, r_v = -q W with q from the v-Raychaudhuri constraint started from the data on v=0."""
    nu=row0.shape[1]; nv=col0.shape[1]; cols=np.ascontiguousarray(cols,dtype=np.int32); out=np.zeros((len(cols),nv,8))
    row0=np.ascontiguousarray(row0); col0=np.ascontiguousarray(col0)
    rws=np.ascontiguousarray([] if rows is None else rows,dtype=np.int32); snap=np.zeros((max(1,len(rws)),8,nu))
    lib.evolve_stream_qtg_cy(nu,nv,hu,hv,model,L2,row0.ctypes.data_as(dp),col0.ctypes.data_as(dp),len(cols),cols.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),out.ctypes.data_as(dp),niter,y0,mode,len(rws),rws.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),snap.ctypes.data_as(dp))
    if rows is not None: return out,snap[:len(rws)]
    return out
