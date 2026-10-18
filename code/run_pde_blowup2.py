"""PDE (Hayward h): detect the blow-up curve.  Runs to v_end = v_*(u0) - margin; prints per ray u the first v with |psi|>1e3 and the sign of psi there, plus the maximum of |psi|."""
import sys,os,numpy as np,warnings
warnings.filterwarnings('ignore'); sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from qtg_lib import *
h=float(sys.argv[1]); vmax=float(sys.argv[2]); A=float(sys.argv[3]); B=float(sys.argv[4])
bg=Bg(); model,L2=1,1.0
u,v,arrs,_=build(bg,model,L2,-6,8,0,vmax,h,h,A,B); run(model,L2,arrs,h,h)
R,SG,RU,RV=arrs[:4]; psi=psi_of(R,SG,RU,RV)
print('A=%g B=%g h=%g vmax=%g  finite: %s'%(A,B,h,vmax,bool(np.isfinite(psi).all())))
for uu in (-6,-5,-4,-3,-2,-1,0,1,2,4,6,8):
    i=int(round((uu+6)/h)); col=psi[:,i]; bad=np.where(~np.isfinite(col)|(np.abs(col)>1e3))[0]
    j=bad[0] if len(bad) else None
    print(' u=%3g: %s  max|psi|=%.3e at v=%.1f  psi(v=vmax-1)=%.3e'%(uu,('first |psi|>1e3 at v=%.2f sign %+d'%(v[j],np.sign(col[j-1]))) if j is not None else 'no blow-up         ',np.nanmax(np.abs(col[np.isfinite(col)])),v[np.nanargmax(np.where(np.isfinite(col),np.abs(col),0))],col[int(round((vmax-1)/h))]))
