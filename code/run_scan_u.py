"""Ray classification: u-scan of psi, y=-r_u/W, sigma_v at several v for QTG-Hayward, A=0.02, B given.  usage: h vmax B"""
import sys,os,time,numpy as np,warnings
warnings.filterwarnings('ignore'); sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from qtg_lib import *
h=float(sys.argv[1]); vmax=float(sys.argv[2]); B=float(sys.argv[3]); bg=Bg()
us=[-5,-4,-3,-2,-1,0,1,2,4,6]; u1=-6+h*int(round((6.0+10*h+6)/h)); t=time.time()
u,v,row0,col0=build_rays(bg,1,1.0,-6,u1,0,vmax,h,h,0.02,B)
cols=[int(round((x+6)/h)) for x in us]; out=run_stream(1,1.0,row0,col0,h,h,cols)
print('h=%g B=%g (%.0fs)'%(h,B,time.time()-t))
for c,uu in enumerate(us):
    R,SG,RU,RV,SU,SV,PU,PV=[out[c,:,f] for f in range(8)]; W=np.exp(SG); psi=psi_of(R,SG,RU,RV)
    s=[]
    for vv in (40,50,56,60,64,vmax):
        j=int(round(vv/h)); s.append('v=%g:psi %+.4f y %+.2e sv %+.3f'%(vv,psi[j],-RU[j]/W[j],SV[j]))
    print(' u=%2g '%uu,' | '.join(s))
