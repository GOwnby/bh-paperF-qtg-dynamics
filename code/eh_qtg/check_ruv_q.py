"""Independent end-to-end check of the evolved solution (constrained scheme, EH-regular data): the r_uv equation r_sv = -(W_s r/4) Q(psi) is NOT used to update r in mode 3
(r follows from r_v = -rho along the column), so its finite-difference residual on a stored row v=const tests sigma_uv (in particular the c3 phi_u^2 phi_v^2 term) together with the
Raychaudhuri integrals.  Relative L2 residual over the stored row on s in [s_lo, s_hi] vs mesh.  usage: check_ruv_q.py B v1 hs1 hs2 ... -- v1 v2 ..."""
import numpy as np, warnings, sys
warnings.filterwarnings('ignore')
from dnU_qtg import *
from qtg_lib import run_stream_cy, coef
B=float(sys.argv[1]); v1=float(sys.argv[2]); i=sys.argv.index('--'); hl=[float(x) for x in sys.argv[3:i]]; vs=[float(x) for x in sys.argv[i+1:]]
S=StaticU(); c=0.2*np.exp(-S.kp*v1); res={}
for hs in hl:
    d=build_eh_q(S,1,1.0,1.5,v1,hs,hs,B,k=1.5,c=c,vH=v1+300)
    out,snap=run_stream_cy(1,1.0,d['row0'],d['col0'],hs,hs,[0],rows=[int(round(x/hs)) for x in vs]); U=d['U']; s=d['s']
    for k,vv in enumerate(vs):
        r,sg,rs,rv,sgs,sV,Ps,PV=snap[k]; W=np.exp(sg); y=-rs/W; rho=-rv; psi=(1+4*y*rho)/r**2; Q=coef(1,1.0,psi)[0]
        rsv=(rv[2:]-rv[:-2])/(2*hs); rhs=-(W[1:-1]*r[1:-1]/4)*Q[1:-1]; m=(s[1:-1]>0.0); m2=(np.abs(rhs)>=1e-3*np.abs(rhs).max())   # m: whole row; m2: points where the r_uv term is >= 1e-3 of its maximum (behind the front r_uv ~ 1e-15 is below the roundoff of the finite difference)
        res[(hs,vv)]=(np.sqrt(np.sum((rsv-rhs)[m]**2)/np.sum(rhs[m]**2)), np.sqrt(np.sum(rhs[m]**2)/m.sum()), np.sqrt(np.sum((rsv-rhs)[m2]**2)/np.sum(rhs[m2]**2)))
    print('h=%g done'%hs,flush=True)
for vv in vs: print('v=%g  rel L2 residual of r_uv equation per mesh: '%vv+'  '.join('%.2e'%res[(h,vv)][0] for h in hl)+'   | points with |r_uv|>=1e-3 max: '+'  '.join('%.2e'%res[(h,vv)][2] for h in hl))
