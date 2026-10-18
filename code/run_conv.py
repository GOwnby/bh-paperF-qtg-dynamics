"""Resolution study with the streaming solver: u in [-6,u1], columns u=0,2, QTG-Hayward, A=0.02.  usage: run_conv.py h vmax B tag"""
import sys,os,time,numpy as np,warnings
warnings.filterwarnings('ignore'); sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from qtg_lib import *
h=float(sys.argv[1]); vmax=float(sys.argv[2]); B=float(sys.argv[3]); tag=sys.argv[4]
u1=-6+h*int(round((8.0+10*h)/h)); bg=Bg(); t=time.time()
u,v,row0,col0=build_rays(bg,1,1.0,-6,u1,0,vmax,h,h,0.02,B)
cols=[int(round((x+6)/h)) for x in (0.0,2.0)]
out=run_stream(1,1.0,row0,col0,h,h,cols)
step=max(1,int(round(0.05/h)))
np.savez('conv_%s_h%g.npz'%(tag,h),v=v[::step],out=out[:,::step,:],h=h,B=B)
R,SG,RU,RV,SU,SV,PU,PV=[out[0,:,f] for f in range(8)]; psi=psi_of(R,SG,RU,RV)
print('h=%g  %.0fs:'%(h,time.time()-t),' '.join('v=%g: psi %.5f sv %+.4f;'%(vv,psi[int(round(vv/h))],SV[int(round(vv/h))]) for vv in (56,60,62,64,66,68)))
