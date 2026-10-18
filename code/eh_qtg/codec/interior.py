import sys; sys.path.insert(0,'.')
import pipeline as P
from pipeline import *
P.UEND=float(sys.argv[2]); import collapse_lib
A=tune_A(1,1.0,5.0); h=float(sys.argv[1]); v1=float(sys.argv[3])
u,v,row0,col0,ph=rays(1,1.0,P.U0,P.UEND,P.V0,v1,h,h,A,P.VA,P.VB)
out,snap,ah=run(1,1.0,row0,col0,h,h,[0],rows=[len(v)-1])
R,SG,RU,RV,SU,SV,PU,PV=snap[0]
print('nan',(~np.isfinite(R)).sum(),'of',len(u))
psi=(1+4*RU*RV/np.exp(SG))/R**2
m=5.0; psis=2*m/(R**3+2*m)
for i in range(0,len(u),max(1,len(u)//30)): print('u=%6.2f r=%9.4f psi=%.6e static=%.6e rel=%.1e rv=%.3e'%(u[i],R[i],psi[i],psis[i],(psi[i]-psis[i])/psis[i],RV[i]))
