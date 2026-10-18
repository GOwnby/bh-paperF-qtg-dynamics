"""Spherically symmetric Einstein-massless-scalar field with a regular centre (polar-areal gauge, G_ab = 8 pi T_ab,
T_ab = d_a phi d_b phi - 1/2 g_ab (d phi)^2), method of lines (RK4, 2nd-order centred differences), for the third-order late-time
tail of Bizon, Chmaj and Rostworowski (arXiv:0812.4333): data phi(0,r)=eps (a(-r)-a(r))/r, phi_t(0,r)=eps (a'(-r)-a'(r))/r, a(s)=A b((s-s0)/w).
The tail phi_3 is extracted by eps-differencing: D = [phi_eps/eps - phi_{eps/2}/(eps/2)]/(3 eps^2/4) = phi_3 + O(eps^2), which removes the
(linear) truncation error of the scheme.  usage: bcr.py eps h tmax Rout out.npz"""
import sys,numpy as np
def bump(x):
    y=np.zeros_like(x); m=(x>0)&(x<1); y[m]=(x[m]*(1-x[m]))**6*4.0**6   # max 1
    return y
def dbump(x):
    y=np.zeros_like(x); m=(x>0)&(x<1); xm=x[m]; y[m]=4.0**6*6*(xm*(1-xm))**5*(1-2*xm)
    return y
import os
S0,W,AMP=float(os.environ.get('B_S0',2.0)),float(os.environ.get('B_W',6.0)),1.0
ASYM=float(os.environ.get('B_ASYM',0.0))
def a_of(s):
    x=(s-S0)/W; return AMP*bump(x)*(1+ASYM*(x-0.5))
def da_of(s):
    x=(s-S0)/W; return AMP*(dbump(x)*(1+ASYM*(x-0.5))+bump(x)*ASYM)/W
def cumtrapz(y,h):
    c=np.zeros_like(y); c[1:]=np.cumsum(0.5*(y[1:]+y[:-1]))*h; return c
def metric(r,h,Phi,Pi):
    """a, alpha from the constraints (lapse normalised alpha(R)=1/a(R))."""
    Fm=2*np.pi*r**2*(Pi**2+Phi**2)                    # m' = F (1-2m/r)
    g=np.zeros_like(r); g[1:]=2*Fm[1:]/r[1:]          # 2F/r  (-> 0 at r=0)
    I=cumtrapz(g,h); m=np.exp(-I)*cumtrapz(Fm*np.exp(I),h)
    a2=np.ones_like(r); a2[1:]=1.0/(1-2*m[1:]/r[1:]); a=np.sqrt(a2)
    s=np.zeros_like(r); s[1:]=2*np.pi*r[1:]*(Pi[1:]**2+Phi[1:]**2)+(a2[1:]-1)/(2*r[1:])
    la=cumtrapz(s,h); al=np.exp(la); al=al/(al[-1]*a[-1])
    return a,al,m
def gridPhi(phi,h):
    Ph=(phi[1:]-phi[:-1])/h                      # half points j+1/2
    P=np.zeros_like(phi); P[1:-1]=0.5*(Ph[1:]+Ph[:-1]); P[-1]=Ph[-1]; P[0]=0.0
    return Ph,P
def rhs(r,h,phi,Pi):
    Ph,Phi=gridPhi(phi,h); a,al,m=metric(r,h,Phi,Pi)
    dphi=al/a*Pi
    q=al/a; qh=0.5*(q[1:]+q[:-1]); rh=0.5*(r[1:]+r[:-1])
    flux=rh**2*qh*Ph                              # r^2 alpha Phi / a at j+1/2
    vol=(rh[1:]**3-rh[:-1]**3)/3.0                # interior j=1..N-1
    dPi=np.zeros_like(Pi)
    dPi[1:-1]=(flux[1:]-flux[:-1])/vol
    dPi[0]=flux[0]/(rh[0]**3/3.0)
    dphi[-1]=0.0; dPi[-1]=0.0
    return dphi,dPi,m
def run(eps,h,tmax,R,robs=(5.0,10.0,20.0),dtf=0.5,rfar=(100.0,200.0,300.0)):
    N=int(round(R/h)); r=h*np.arange(N+1); rs=r.copy(); rs[0]=1.0
    f=np.zeros_like(r); g=np.zeros_like(r)
    m=r>0
    f[m]=eps*(a_of(-r[m])-a_of(r[m]))/r[m]; g[m]=eps*(da_of(-r[m])-da_of(r[m]))/r[m]
    f[0]=eps*(-2*da_of(np.array([0.0]))[0]); g[0]=eps*(-2*0.0)   # both vanish for this a (a'(0)=a''(0)=0)
    phi=f.copy(); Pi=g.copy()
    for it in range(8):                                 # Pi=(a/alpha) phi_t exactly
        Phi=gridPhi(phi,h)[1]; a,al,mm=metric(r,h,Phi,Pi); Pi=a/al*g
    dt=dtf*h; nst=int(round(tmax/dt)); ob=[int(round(x/h)) for x in robs]
    out=[]; ts=[]; farm=[]; farp=[]; jf=[int(round(x/h)) for x in rfar]
    for n in range(nst+1):
        if n%int(round(0.5/dt))==0:
            ts.append(n*dt); out.append([phi[j] for j in ob])
            Phi_=gridPhi(phi,h)[1]; _,_,mm_=metric(r,h,Phi_,Pi)
            farm.append([mm_[j] for j in jf]); farp.append([r[j]*phi[j] for j in jf])
        k1p,k1P,_=rhs(r,h,phi,Pi)
        k2p,k2P,_=rhs(r,h,phi+0.5*dt*k1p,Pi+0.5*dt*k1P)
        k3p,k3P,_=rhs(r,h,phi+0.5*dt*k2p,Pi+0.5*dt*k2P)
        k4p,k4P,_=rhs(r,h,phi+dt*k3p,Pi+dt*k3P)
        phi=phi+dt/6*(k1p+2*k2p+2*k3p+k4p); Pi=Pi+dt/6*(k1P+2*k2P+2*k3P+k4P)
    Phi=gridPhi(phi,h)[1]; a,al,mm=metric(r,h,Phi,Pi)
    run.far=(np.array(farm),np.array(farp))
    return np.array(ts),np.array(out),mm[-1]
if __name__=='__main__':
    eps=float(sys.argv[1]); h=float(sys.argv[2]); tmax=float(sys.argv[3]); R=float(sys.argv[4])
    ts,out,mR=run(eps,h,tmax,R)
    np.savez(sys.argv[5],t=ts,phi=out,eps=eps,h=h,R=R,mR=mR,mfar=run.far[0],psifar=run.far[1])
    print('done eps',eps,'m(R) at end',mR)
