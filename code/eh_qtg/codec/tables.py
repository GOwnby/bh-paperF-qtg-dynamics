"""Switching-time and resolution dependence of the horizon tables (Paper F, Sec. collapse).  usage: python3 tables.py > logs/tables.log"""
import sys, numpy as np
from collapse_tail import *
from scipy.interpolate import CubicSpline
import pipeline as P
def cmp(a,b,lab):
    ra=CubicSpline(a['v1e']+a['t'],a['phiH']); ve=b['v1e']+b['t']; m=(ve>a['v1e']+a['t'][0])&(ve<a['v1e']+1400)&(ve>b['v1e'])
    out=[]
    for lo,hi in ((0,50),(50,150),(150,400),(400,1400)):
        mm=m&(ve-b['v1e']>=lo)&(ve-b['v1e']<hi)
        out.append(abs(b['phiH'][mm]-ra(ve[mm])).max()/abs(b['phiH'][mm]).max())
    print(lab,'max|diff|/max|phi_H| in windows of v-v_start [0,50),[50,150),[150,400),[400,1400):',['%.1e'%x for x in out])
for model in (0,1):
    P.UEND=29.5
    t60=make_table(model,5.0,0.1,0.1,60.,1500.); t70=make_table(model,5.0,0.1,0.1,70.,1500.); t80=make_table(model,5.0,0.1,0.1,80.,1500.); t60f=make_table(model,5.0,0.05,0.05,60.,1500.)
    cmp(t60,t70,'model %d v1 60->70'%model); cmp(t60,t80,'model %d v1 60->80'%model); cmp(t60,t60f,'model %d (hN,hL) 0.1->0.05'%model)
