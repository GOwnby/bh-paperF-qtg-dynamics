"""Static check of the QTG EH-regular pipeline (B=0): evolved (r, sigma, sigma_v, r_U) against the exact static solution, and second-order convergence."""
import os, numpy as np, warnings, time, sys
warnings.filterwarnings('ignore')
from dnU_qtg import *
S=StaticU(); U1,v1=10.0,60.0; c=0.2*np.exp(-S.kp*v1)
for (hs,hv) in [(0.2,0.2),(0.1,0.1),(0.05,0.05)]:
    t=time.time(); d=build_eh_q(S,1,1.0,U1,v1,hs,hv,0.0,c=c)
    cols=list(range(0,d['nu'],max(1,d['nu']//8))); out=run_stream_q(1,1.0,d['row0'],d['col0'],hs,hv,cols)
    res=[]
    for n,j in enumerate(cols):
        U=d['U'][j]; gp=d['gp'][j]
        for vi in (20,50):
            i=int(round(vi/hv)); ex=S.fields(np.array([U]),vi); 
            r,sg,ru,rv,su,sv=[out[n][i,f] for f in range(6)]
            res.append((U,vi,sg-(ex[1][0]+np.log(gp)),sv-ex[5][0],r-ex[0][0]))
    res=np.array(res); print('h=%g nu=%d %.0fs  max|dsigma|=%.2e max|dsigma_v|=%.2e max|dr|=%.2e nan %d'%(hs,d['nu'],time.time()-t,abs(res[:,2]).max(),abs(res[:,3]).max(),abs(res[:,4]).max(),np.isnan(out).sum()),flush=True)
