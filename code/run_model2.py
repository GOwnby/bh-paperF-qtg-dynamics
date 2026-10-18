import sys,os,numpy as np,warnings
warnings.filterwarnings('ignore'); sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from qtg_lib import *
h=float(sys.argv[1]); vmax=float(sys.argv[2]); B=float(sys.argv[3]); A=float(sys.argv[4]); mass=float(sys.argv[5]) if len(sys.argv)>5 else 1.0
bg=Bg2(mass,1.0); print('m=%g r-=%.5f kappa-=%.5f'%(mass,bg.rm,bg.kap))
u,v,arrs,_=build(bg,2,1.0,-6,8,0,vmax,h,h,A,B); run(2,1.0,arrs,h,h)
R,SG,RU,RV,SU,SV,PU,PV=arrs; W=np.exp(SG); psi=psi_of(R,SG,RU,RV)
print('A=%g B=%g h=%g vmax=%g finite %s  psi range [%.5f, %.5f] (wall +-1)'%(A,B,h,vmax,np.isfinite(psi).all(),np.nanmin(psi),np.nanmax(psi)))
for uu in (-6,-3,-1,0,2,4,6):
    i=int(round((uu+6)/h)); print(' u=%2g  psi at v=20,40,60,80,%g:'%(uu,vmax),' '.join('%.5f'%psi[int(round(vv/h)),i] for vv in (20,40,60,80,vmax) if vv<=vmax),'| sigma_v:',' '.join('%+.3f'%SV[int(round(vv/h)),i] for vv in (20,40,60,80,vmax) if vv<=vmax),'| y=-r_u/W at vmax: %+.3e'%(-RU[-1,i]/W[-1,i]))
