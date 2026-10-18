"""Row v=v1 after the pulse against the static hole of final mass: generalized mass and psi.  usage: sp_interior.py model m0 mt h0"""
import sys; sys.path.insert(0,'.')
from strong import *
model=int(sys.argv[1]); m0=float(sys.argv[2]); mt=float(sys.argv[3]); h0=float(sys.argv[4])
g=geom(m0,mt); A=tune_A_m(model,m0,g,mt,0.03); h=h0*g['s']
u,v,row0,col0,snap,ah=stageN_h(model,m0,g,A,h); R,SG,RU,RV,SU,SV,PU,PV=snap[0]
m=ms_mass(model,L2,R,SG,RU,RV); bg=Static(model,mt,L2)
f,fp=fstat(model,L2,mt,R); psis=(1-f)/R**2 if model==0 else (1-f)/R**2
psi=(1+4*RU*RV/np.exp(SG))/R**2
print('model %d m0=%g mt=%g s=%.2f h=%.3f rp=%.4f'%(model,m0,mt,g['s'],h,bg.rp))
for lo,hi in ((1.5*bg.rp,3*bg.rp),(1.1*bg.rp,1.5*bg.rp),(1.01*bg.rp,1.1*bg.rp),(0.9*bg.rp,1.01*bg.rp)):
    k=np.isfinite(m)&(R>=lo)&(R<hi)
    if k.sum(): print('  r in [%.2f,%.2f): max|m-mt|=%.2e  max|psi/psi_s-1|=%.2e  (%d pts)'%(lo,hi,np.nanmax(abs(m[k]-mt)),np.nanmax(abs(psi[k]/psis[k]-1)),k.sum()))
