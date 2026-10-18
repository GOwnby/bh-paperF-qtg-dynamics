"""Tail fits and production tables (Paper F, Sec. collapse).  usage: python3 fit_tables.py > logs/fit_tables.log ; writes data/tail_m{0,1}_v60_h05.npz"""
import numpy as np
from collapse_tail import *
from fit1 import fitwin
import pipeline as P
P.UEND=29.5
for model in (0,1):
    d=make_table(model,5.0,0.05,0.05,60.,2500.); ve=d['v1e']+d['t']; f=d['phiH']
    print('model',model,'A=%.8f v1e=%.3f'%(d['A'],d['v1e']))
    for a,b in ((600,1200),(1200,2400),(600,2400)):
        r=fitwin(ve,f,d['v1e']+a,d['v1e']+b); q=fitwin(ve,f,d['v1e']+a,d['v1e']+b,3.0)
        print('  t in [%d,%d]: free k=%.4f (B=%.3f, vs-vstart=%.2f) | k=3: B=%.4f vs-vstart=%.2f'%(a,b,r[2],r[0],r[1]-d['v1e'],q[0],q[1]-d['v1e']))
    np.savez_compressed('data/tail_m%d_v60_h05.npz'%model,**{k:np.asarray(v) for k,v in d.items()})
