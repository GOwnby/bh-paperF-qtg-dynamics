"""Growth of the deviation of psi=(1-f)/r^2 from the pulse-only solution (B=0) on fixed rays u, QTG-Hayward, A=0.02, B=2e-3: slopes of ln|dpsi| in v.
   Also the same for the generalized-closure-free GR(additive) code is in Paper E Sec. below-threshold (kappa_- = 0.7956 / power law)."""
import sys,os,numpy as np,warnings
warnings.filterwarnings('ignore'); sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from qtg_lib import *
h=float(sys.argv[1]); vmax=float(sys.argv[2]); B=float(sys.argv[3]); bg=Bg()
res={}
for Bv in (B,0.0):
    u,v,arrs,_=build(bg,1,1.0,-6,8,0,vmax,h,h,0.02,Bv); run(1,1.0,arrs,h,h)
    R,SG,RU,RV=arrs[:4]; res[Bv]=(psi_of(R,SG,RU,RV),arrs)
d=res[B][0]-res[0.0][0]
print('h=%g B=%g: dpsi = psi(A,B)-psi(A,0)'%(h,B))
for uu in (-3,-1,0,1,2,4,6):
    i=int(round((uu+6)/h)); row=[]; sl=[]
    for vv in (20,30,36,40,44,48):
        if vv<=vmax: row.append('%.3e'%d[int(round(vv/h)),i])
    k=int(round(2/h))
    for vv in (30,36,40,44):
        j=int(round(vv/h)); 
        if vv+2<=vmax and d[j,i]*d[j+k,i]>0: sl.append('%.3f'%(np.log(abs(d[j+k,i]/d[j-k,i]))/(4)))
    print(' u=%2g dpsi(v=20,30,36,40,44,48): %s | dln|dpsi|/dv at 30,36,40,44: %s'%(uu,' '.join(row),' '.join(sl)))
