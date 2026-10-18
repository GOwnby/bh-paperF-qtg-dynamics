import sys; sys.path.insert(0,'.')
import pipeline as P
from runL import *
from fit1 import fitwin
from scipy.interpolate import interp1d
model=1; m=5.0; A=tune_A(model,1.0,m); bg=Static(model,m,1.0)
hL=0.1; vmaxrel=2600.
u,v,row0,col0,ph=rays(model,1.0,P.U0,P.UEND,P.V0,P.V0+vmaxrel,0.1,0.1,A,P.VA,P.VB)
r=col0[0]; x=bg.rstar_y(np.log(r-bg.rp))             # r*(r(u0,v)) along the ray
ve=2*x                                              # v_e = u_e0 + 2 r*, u_e0=0
x0=x[0]; vstart=ve[0]
nv=int(round((ve[-1]-vstart)/hL)); tl=vstart+hL*np.arange(nv)
vof=interp1d(ve,v,kind='cubic'); phi_col=np.array([float(ph(vof(t))) if t<=ve[-1] else 0. for t in tl])
Lh=9.5/bg.kp/2; di=int(round(2*(x0+Lh)/hL)); nu=di+nv+2
xrow=x0-hL/2*np.arange(nu); psirow=np.zeros(nu)
rb=bg.r_of_rstar(np.array([x0]))[0]
col=r[0]*phi_col*0+bg.r_of_rstar(x0+0*tl/2+ (0))[0]*0   # placeholder
# boundary ray u_e0: psi = r(u0, v_e) phi ; r from the ray values interpolated on the lattice
rint=interp1d(ve,r,kind='cubic'); rcol=np.array([float(rint(t)) for t in tl]); col=rcol*phi_col
t_,phiH,last=tail_L.run_L(bg,xrow,psirow,hL,hL*(nv-1),Lh,psi_col_val=col)
vee=vstart+t_
B,vs,k=fitwin(vee,phiH,vstart+1100,vstart+2500,3.0)[:3]; Bk,vsk,kk=fitwin(vee,phiH,vstart+1100,vstart+2500)
print('linear pulse on static Hayward m=5: A=%.5f  B(k=3)=%.4f  vs-vstart=%.2f free k=%.4f (B_nonlinear=25.434)'%(A,B,vs-vstart,kk))
print('ratio B_nl/B_lin = %.3f'%(25.434/B))
