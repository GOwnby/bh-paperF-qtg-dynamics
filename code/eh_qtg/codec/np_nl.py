"""k=2 collapse tail: stage N + L with a non-compact (nonzero NP constant) addition b S((r-ra)/dr)/r^2 on u=u0.  usage: python3 np_nl.py model b hN hL v1 vmax out.npz"""
import sys, numpy as np, time
import pipeline as P
from collapse_tail import make_table
model=int(sys.argv[1]); b=float(sys.argv[2]); hN=float(sys.argv[3]); hL=float(sys.argv[4]); v1=float(sys.argv[5]); vmax=float(sys.argv[6]); fn=sys.argv[7]
P.UEND=29.5; t0=time.time()
d=make_table(model,5.0,hN,hL,v1,vmax,tail=(b,25.3,1.8) if b!=0 else None)
np.savez_compressed(fn,**{k:np.asarray(v) for k,v in d.items()})
print('model %d b=%g A=%.8f mf=%.8f v1e=%.4f  %.0fs'%(model,b,d['A'],d['mf'],d['v1e'],time.time()-t0))
t=d['t']; f=d['phiH']
for T in (100,200,400,800,1600,3200,6400):
    if T<=vmax:
        i=int(round(T/hL)); print('t=%5d phi_H=%.4e  phi_H t^2/(-4b)=%s'%(T,f[i],('%.5f'%(f[i]*T**2/(-4*b)) if b else '-')))
