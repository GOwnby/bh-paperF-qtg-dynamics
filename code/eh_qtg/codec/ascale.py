import sys; sys.path.insert(0,'.')
import pipeline as P
from runL import *
from fit1 import fitwin
P.UEND=38.0
A0=0.030030088
rows=[]
for f in (0.8,0.9,1.0,1.1,1.2):
    A=f*A0; m=mass_u0(1,1.0,A)
    u,v,snap,out,ah=stageN(1,1.0,A,0.1,60.0)
    bg,t,phiH,x0,xmin=stageL(1,1.0,m,u,snap,0.1,2500.)
    ve=2*x0+t
    B,vs,k=fitwin(ve,phiH,1000,2500,3.0)[:3]; Bk,vsk,kk=fitwin(ve,phiH,1000,2500)
    # amplitude of late phi_H at fixed time after the collapse: use phi_H*(t)^3 at t=2000 relative to start of L
    rows.append((f,A,m,B,vs-2*x0,kk))
    print('A/A0=%.2f A=%.5f m=%.4f  B(k=3)=%.4f  vs-v1e=%.2f  free k=%.4f'%(f,A,m,B,vs-2*x0,kk),flush=True)
rows=np.array(rows)
print('d lnB/d lnA (successive):',np.diff(np.log(rows[:,3]))/np.diff(np.log(rows[:,1])))
print('d lnB/d lnm:',np.diff(np.log(rows[:,3]))/np.diff(np.log(rows[:,2])))
