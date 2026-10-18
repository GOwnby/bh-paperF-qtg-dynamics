"""Exact generalized-mass law m_v = 8 pi r^2 y phi_v^2 (m = r^3 h(psi)/2, y = -r_u/W) tested on the converged PDE columns (needs conv_B2e-4_h0.000625.npz from run_conv.py).
Central differences on the stored v-samples (spacing 0.05) limit the agreement."""
import numpy as np,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from qtg_lib import psi_of,hfun
d=np.load('conv_B2e-4_h0.000625.npz'); v=d['v']; o=d['out']
for c,uu in ((0,0.0),(1,2.0)):
    R,SG,RU,RV,SU,SV,PU,PV=[o[c,:,f] for f in range(8)]; W=np.exp(SG); psi=psi_of(R,SG,RU,RV); h,_=hfun(1,1.0,psi); m=R**3*h/2; y=-RU/W
    dm=np.gradient(m,v); rhs=8*np.pi*R**2*y*PV**2
    for vv in (5,45,55,60,64):
        i=int(round(vv/0.05)); print('u=%g v=%g m=%.6f dm/dv=%.6e 8pi r^2 y phi_v^2=%.6e rel.diff=%.1e  y=%+.3e psi=%.5f'%(uu,vv,m[i],dm[i],rhs[i],abs(dm[i]-rhs[i])/abs(rhs[i]),y[i],psi[i]))
