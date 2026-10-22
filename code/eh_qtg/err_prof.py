"""Profiles of the difference between meshes across x = U e^{kappa_+ v} at v = 100, 150, 180 (Paper F, 'What limits the window'; generator of code/errprof.log).
B = 3e-3, k = 3/2, v1 = 300, h_s = h_v = h = 0.05, 0.025, 0.0125 (code A, constrained, streamed); prints sigma_v (finest), the relative differences of rho = -r_v between the meshes
and the differences of r.  usage: python3 err_prof.py > ../errprof.log   (about 6 min on one core; the h = 0.0125 run dominates)"""
import numpy as np, warnings, sys
warnings.filterwarnings('ignore')
from dnU_qtg import *
from qtg_lib import run_stream_cy, coef
B=0.003; v1=300.0; vs=[100.,150.,180.]
S=StaticU(5.0); c=0.2*np.exp(-S.kp*v1); res={}
for hs in (0.05,0.025,0.0125):
    d=build_eh_q(S,1,1.0,1.5,v1,hs,hs,B,k=1.5,c=c,vH=v1+300)
    out,snap=run_stream_cy(1,1.0,d['row0'],d['col0'],hs,hs,[0],rows=[int(round(x/hs)) for x in vs])
    res[hs]=(d['U'],snap)
    print('done',hs,flush=True)
U1,s1=res[0.05]; U2,s2=res[0.025]; U3,s3=res[0.0125]
kp=S.kp
for k,vv in enumerate(vs):
    print('=== v=%g   columns: s-index(coarse) U  x  sV(0.0125)  d(0.05-0.025)  d(0.025-0.0125) for sigma_v, rho_rel, and r'%vv)
    n1=len(U1)
    for i in sorted(set(list(range(0,n1,max(1,n1//30)))+[n1-1])):
        j=2*i; l=4*i
        if l>=len(U3): continue
        x=U1[i]*np.exp(kp*vv)
        f=lambda s,idx: s[k][5][idx]
        rho=lambda s,idx: -s[k][3][idx]
        print(' %4d %.3e %.3e %+.5f  %+.2e %+.2e   rho: %.3e %+.2e %+.2e  r: %+.1e'%(i,U1[i],x,f(s3,l),f(s1,i)-f(s2,j),f(s2,j)-f(s3,l),rho(s3,l),(rho(s1,i)-rho(s2,j))/(abs(rho(s3,l))+1e-300),(rho(s2,j)-rho(s3,l))/(abs(rho(s3,l))+1e-300),s2[k][0][j]-s3[k][0][l]))
