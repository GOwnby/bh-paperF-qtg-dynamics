"""Resolution diagnostic: the exact identity psi_v = (rho/r)(Q+2 psi) + 16 pi y phi_v^2/(r h') [Eq. (psiv) of the paper] evaluated on the stored columns u=0
of run_conv.py (spacing 0.05 in v; central differences).  Prints the maximum relative defect over v in [lo,hi]."""
import numpy as np,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from qtg_lib import psi_of,coef
for h in ('0.01','0.005','0.0025','0.00125','0.000625'):
    d=np.load('conv_B2e-4_h%s.npz'%h); v=d['v']; o=d['out']; R,SG,RU,RV,SU,SV,PU,PV=[o[0,:,f] for f in range(8)]
    W=np.exp(SG); psi=psi_of(R,SG,RU,RV); Q,c1,c2,c3=coef(1,1.0,psi); rho=-RV; y=-RU/W
    rhs=rho/R*(Q+2*psi)+16*np.pi*c1*y*PV**2/R; lhs=np.gradient(psi,v)
    out=[]
    for lo,hi in ((40,56),(56,62),(62,66)):
        m=(v>=lo)&(v<=hi); out.append(np.max(np.abs(lhs[m]-rhs[m]))/np.max(np.abs(rhs[m])))
    print('h=%-8s max|psi_v - rhs|/max|rhs| for v in [40,56],[56,62],[62,66]: %s'%(h,' '.join('%.1e'%x for x in out)))
