"""Mechanism of the window law (Paper F): forward integration of the horizon Raychaudhuri equation  y'=sigma_v^H y - S(y,r,phi_v)  (y=r_v on H+), the equation that every row next to the horizon integrates in code B,
with the exact column (r_H, sigma_v^H, phi_v^H) at the half-step grid, by RK4 with step h_v  (order p=4) or by midpoint RK2 (p=2).  The error against the exact y = r_v^H is  eps(h_v) e^{kappa_+ v}.
Usage: python mech_vb.py v1 B k   -> table of the error and the advanced time at which it reaches a threshold, for h_v = 0.2 ... 0.0125 (RK4) and 0.2 ... 0.0125 (RK2)."""
import sys,numpy as np,warnings; warnings.filterwarnings('ignore')
sys.path.insert(0,'..')
from dnU_qtg import *
v1=float(sys.argv[1]); B=float(sys.argv[2]); k=float(sys.argv[3]); hs=0.05
S=StaticU(5.0); c=0.2*np.exp(-S.kp*v1)
def c1of(psi): z=1-psi; return z*z
res={}
for hv in [0.2,0.1,0.05,0.025,0.0125]:
    d=build_eh_q(S,1,1.0,1.5,v1,hs,hv/2,B,k=k,c=c,vH=v1+300); R,SG,RU,RV,SU,SVc,PU,PV=d['col0']
    def f(j,y):
        r=R[j]; psi=(1-2*y)/r**2; return SVc[j]*y-4*np.pi*r*c1of(psi)*PV[j]**2
    nv=(d['col0'].shape[1]-1)//2
    for p in (4,2):
        y=RV[0]; err=np.zeros(nv)
        for n in range(nv):
            j0,jh,j1=2*n,2*n+1,2*n+2
            if p==4:
                k1=f(j0,y); k2=f(jh,y+0.5*hv*k1); k3=f(jh,y+0.5*hv*k2); k4=f(j1,y+hv*k3); y+=hv/6*(k1+2*k2+2*k3+k4)
            else:
                k1=f(j0,y); k2=f(jh,y+0.5*hv*k1); y+=hv*k2
            err[n]=y-RV[j1]
        res[(hv,p)]=(hv*(np.arange(nv)+1),err)
    print('hv=%g done'%hv,flush=True)
np.savez('mech_vb_B%g_k%g.npz'%(B,k),**{('%g_%d_v'%key):val[0] for key,val in res.items()},**{('%g_%d_e'%key):val[1] for key,val in res.items()})
print('kappa+ = %.7f'%S.kp)
for p in (4,2):
    print('--- order p=%d: error at v=100,150,200,250 and ratio to the previous h_v'%p)
    prev=None
    for hv in [0.2,0.1,0.05,0.025,0.0125]:
        v,e=res[(hv,p)]; vals=[abs(e[int(round(x/hv))-1]) for x in (100,150,200,250)]
        print('hv=%-7g'%hv,' '.join('%.3e'%x for x in vals),'' if prev is None else ' ratio '+' '.join('%.1f'%(a/b) for a,b in zip(prev,vals)))
        prev=vals
