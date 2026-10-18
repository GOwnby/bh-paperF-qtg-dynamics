"""Killing-energy budget of the stage-L row.  The row v=v1 (ingoing null, parametrised by u, spacing h_L) carries the field that is left outside the
horizon after the pulse has fallen in; on the static exterior of mass m_f
   E_row = 4 pi Int r^2 (phi_u)^2 du   (flux through v = v1; T_uv = 0 for the spherical massless scalar)
splits into the horizon uptake E_H = 4 pi r_+^2 Int phi_v^2 dv (from the stage-L horizon table) and the energy sent to scri+, E_scri = E_row - E_H
(the ray u0 beyond v1 carries no field for compact data).  Einstein-type fluxes (h' ~ 1 at these masses).
usage: rowflux.py model m0 mt h0 hLf table.npz"""
import sys,time,numpy as np
from strong import *
model=int(sys.argv[1]); m0=float(sys.argv[2]); mt=float(sys.argv[3]); h0=float(sys.argv[4]); hLf=float(sys.argv[5]); tab=sys.argv[6]
g=geom(m0,mt); s=g['s']; L2=1.0
A=tune_A_m(model,m0,g,mt,0.03)
hN=h0*s; hL=hLf*s
u,v,row0,col0,ph=rays(model,L2,g['u0'],g['uend'],g['v0'],g['v1'],hN,hN,A,g['va'],g['vb'],m0=m0)
out,snap,ah=run(model,L2,row0,col0,hN,hN,[0],rows=[len(v)-1])
mf=float(ms_mass(model,L2,col0[0][-1],col0[1][-1],col0[2][-1],col0[3][-1]))
R,SG,RU,RV,SU,SV,PU,PV=snap[0]; ok=np.isfinite(R)&np.isfinite(PU)&np.isfinite(RU)
bg=Static(model,mf,L2)
phi=CubicSpline(u[ok],PU[ok]).antiderivative()(u[ok]); Rk=R[ok]
sel=Rk>bg.rp-1.0
nb=np.where(~(np.diff(Rk)<0))[0]
if len(nb): sel[nb[0]+1:]=False
rr=Rk[sel][::-1]; csp=CubicSpline(rr,(Rk*phi)[sel][::-1])
Lh=9.5/bg.kp/2
x0=bg.rstar_y(np.log(Rk[0]-bg.rp)); d=np.load(tab); vmax=float(d['t'][-1]); 
di=int(round(2*(x0+Lh)/hL)); nv=int(round(vmax/hL))+1; nu=di+nv+2
xrow=x0-hL/2*np.arange(nu); r=bg.r_of_rstar(xrow); psi=csp(r)
ex=xrow>=-Lh                                       # outside the horizon proxy
ph_=psi/r; phiU=np.gradient(ph_,hL)                # row index i <-> u = u0 + i hL
Erow=4*np.pi*np.trapezoid((r**2*phiU**2)[ex],dx=hL)
t=d['t']; f=d['phiH']; rp=float(d['rp']); EH=4*np.pi*rp**2*np.trapezoid(np.gradient(f,t)**2,t)
# energy of the pulse on u0 (mass added) for scale: mf-m0
print('model %d m0=%g mt=%g mf=%.5f : E_row=%.4e  E_H=%.4e  E_scri=E_row-E_H=%.4e  (E_row/mf=%.3e, E_scri/mf=%.3e, E_scri/E_row=%.3f)'%(model,m0,mt,mf,Erow,EH,Erow-EH,Erow/mf,(Erow-EH)/mf,(Erow-EH)/Erow))

# direct check: stage L to V=V1+vchk, read the final row (psi at the largest x ~ scri signal a(U)), Q_scri=Int a dU, E_scri(direct)=4 pi Int a_U^2 dU
import os,tail_L
vchk=float(os.environ.get('VCHK',1500.0))
nv2=int(round(vchk/hL))+1; nu2=di+nv2+2
xrow2=x0-hL/2*np.arange(nu2); psirow2=csp(bg.r_of_rstar(xrow2))
t2,phiH2,last=tail_L.run_L(bg,xrow2,psirow2,hL,vchk,Lh,psi_col_val=0.0)
xl=x0+vchk/2-hL/2*np.arange(len(last))           # x of the points of the final row
sel=(xl>x0+200)                                  # far from the hole: psi ~ a(U)
a=last[sel]; Ui=hL*np.arange(len(last))[sel]
Es=4*np.pi*np.trapezoid(np.gradient(a,Ui)**2,Ui); Qs=np.trapezoid(a,Ui)
print('   direct: E_scri=%.4e (E_scri/mf=%.3e)  Q_scri=Int a dU=%.4e  max|a|=%.3e  U-extent of signal %.1f..%.1f (final-row points with x>x0+200: %d)'%(Es,Es/mf,Qs,np.abs(a).max(),Ui[0],Ui[-1],sel.sum()))
