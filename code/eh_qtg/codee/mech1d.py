"""1D mechanism test: forward RK4 integration of the horizon Raychaudhuri equation  y'=sigma_v y - 4 pi r c1(psi) phi_v^2, psi=(1-2y)/r^2 (y=r_v on H+), using the exact column (r, sigma_v, phi_v) at the half-step grid, as code B does for every row near the horizon; compare with the exact y=r_v^H.  Usage: python mech1d.py hv v1"""
import sys,numpy as np,warnings; warnings.filterwarnings('ignore')
sys.path.insert(0,'..')
from dnU_qtg import *
hv=float(sys.argv[1]); v1=float(sys.argv[2]); B=3e-3;k=1.5;hs=0.05
S=StaticU(5.0); c=0.2*np.exp(-S.kp*v1)
d=build_eh_q(S,1,1.0,1.5,v1,hs,hv/2,B,k=k,c=c,vH=v1+300)
col=d['col0']; R,SG,RU,RV,SU,SVc,PU,PV=col
def c1of(psi): z=1-psi; return z*z
def f(j,y): 
    r=R[j]; psi=(1-2*y)/r**2; return SVc[j]*y-4*np.pi*r*c1of(psi)*PV[j]**2
y=RV[0]; nv=(col.shape[1]-1)//2
err=[]
for n in range(nv):
    j0,jh,j1=2*n,2*n+1,2*n+2
    k1=f(j0,y); k2=f(jh,y+0.5*hv*k1); k3=f(jh,y+0.5*hv*k2); k4=f(j1,y+hv*k3)
    y+=hv/6*(k1+2*k2+2*k3+k4); err.append(y-RV[j1])
err=np.array(err); v=hv*(np.arange(nv)+1)
print('kappa+ = ',S.kp)
for vv in [5,25,45,65,85,105,125,145,165,185,205,225,245]:
    i=int(round(vv/hv))-1
    print(vv,'exact r_v^H %.3e'%RV[2*(i+1)],' 1D RK4 error %.3e'%err[i])
