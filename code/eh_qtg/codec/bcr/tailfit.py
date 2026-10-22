"""tailfit.py TAG : continuum (h, eps -> 0, t -> inf) estimate of c = lim t^3 phi_3 at fixed r, and candidate formulas.
 phi_3 estimated by D(eps_hi,eps_lo)=[phi_hi/eps_hi - phi_lo/eps_lo]/(eps_hi^2-eps_lo^2).
 h: Richardson (2nd order; verified for the base pulse with h=0.1,0.05,0.025: ratio of differences 3.9)
 eps: slope in eps_hi^2 from the (0.04,0.02) and (0.02,0.01) pairs at h=0.1 (relative correction applied to the h-converged value)
 t: fit c + a/t + b/t^2 over t in [t1,t2]."""
import sys,os,numpy as np; sys.path.insert(0,'.')
tag=sys.argv[1]; j=int(sys.argv[2]) if len(sys.argv)>2 else 0
# amplitude asymmetry of the pulse a(s) (the integrals X1, X2, M_ADM below are those of the data of the run): 'base' is symmetric, 'asym1' needs B_ASYM = 1.5 (documented default, also exported by verify.sh)
os.environ['B_ASYM']='0' if tag=='base' else os.environ.get('B_ASYM','1.5')
import bcr
def L(h,e): d=np.load('%s/h%s_%s.npz'%(tag,h,e)); return d['t'],d['phi']
def D(h,hi,lo):
    t,a=L(h,hi); _,b=L(h,lo); e1,e2=float(hi),float(lo); return t,(a/e1-b/e2)/(e1**2-e2**2)
t,D1=D('0.1','0.02','0.01'); _,D2=D('0.05','0.02','0.01')
Dh=D2+(D2-D1)/3.0                                   # h->0 at eps pair (0.02,0.01)
_,Da=D('0.1','0.04','0.02'); 
rel=(D1/Da-1)                                       # eps shift between pairs (ratio of pair values), h=0.1
# D(eps_hi)=D0+s*eps_hi^2: D0 = D(0.02) + (D(0.02)-D(0.04))*(0.0004)/(0.0016-0.0004)
D0fac=1+(D1-Da)/D1*0.0004/(0.0016-0.0004)
Dc=Dh*D0fac
s=np.linspace(-20,60,800001); a=bcr.a_of(s); da=np.gradient(a,s)
cs=np.concatenate([[0],np.cumsum(0.5*(da[1:]**2+da[:-1]**2)*np.diff(s))]); Mtot=4*np.pi*cs[-1]
MB=4*np.pi*(cs[-1]-cs); MIN=4*np.pi*cs
w=lambda f: np.trapezoid(f,s)
Q=w(a)
X1=-8*w(MB*a); X4=-8*w(MIN*a); X2=-8*Mtot*Q
print('Madm %.5f Q %.5f | X1=-8 int M_B a %.3f  X4=-8 int M_in a %.3f  X2=-8 M Q %.3f'%(Mtot,Q,X1,X4,X2))
m=(t>=100)&(t<=300)
for k,r in enumerate((5,10,20)):
    y=t**3*Dc[:,k]; A=np.vstack([np.ones(m.sum()),1/t[m],1/t[m]**2]).T
    c=np.linalg.lstsq(A,y[m],rcond=None)[0]
    A2=np.vstack([np.ones(m.sum()),1/t[m]]).T; c2=np.linalg.lstsq(A2,y[m],rcond=None)[0]
    print('r=%g  t^3D(t=100,150,200,300)= %s  fit(3par) c=%.2f  fit(2par) c=%.2f   c/X1=%.3f c/X2=%.3f'%(r,' '.join('%.1f'%y[np.argmin(abs(t-T))] for T in (100,150,200,300)),c[0],c2[0],c[0]/X1,c[0]/X2))
