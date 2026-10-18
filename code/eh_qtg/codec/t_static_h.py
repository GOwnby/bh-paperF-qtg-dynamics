"""Static-hole start (m0>0, A=0) must stay static: generalized mass r^3 h/2 and psi on the row v=v1 against m0 and the static psi(r); regression m0=0 against the old data.  usage: t_static_h.py h model m0"""
import sys; sys.path.insert(0,'.')
import numpy as np
from collapse_lib import *
h=float(sys.argv[1]); model=int(sys.argv[2]); m0=float(sys.argv[3]); v1=60.0
uend=float(sys.argv[4]) if len(sys.argv)>4 else 29.5
u,v,row0,col0,ph=rays(model,1.0,0.0,uend,40.0,v1,h,h,0.0,44.0,52.0,m0=m0)
out,snap,ah=run(model,1.0,row0,col0,h,h,[0],rows=[len(v)-1])
R,SG,RU,RV,SU,SV,PU,PV=snap[0]
psi=(1+4*RU*RV/np.exp(SG))/R**2; m=ms_mass(model,1.0,R,SG,RU,RV)
f,fp=fstat(model,1.0,m0,R); psis=(1-f)/R**2
print('h=%g model %d m0=%g: max|m-m0|=%.2e  max|psi-psi_s|/psi_s=%.2e  max|PU|=%.2e  finite %d/%d'%(h,model,m0,np.nanmax(abs(m-m0)),np.nanmax(abs(psi-psis)/np.maximum(abs(psis),1e-30)) if m0>0 else np.nanmax(abs(psi)),np.nanmax(abs(PU)),np.isfinite(R).sum(),len(R)))
i=int(np.argmin(abs(R-9.9)))
print('  at r=%.3f (row v1): m=%.8f  rv=%.5f  f/ (2*...)'%(R[i],m[i],RV[i]))
