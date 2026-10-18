"""a0 of the linear test (nplin.py output) : python3 nplin_fit.py nplin_m0_M5_h0.2.npz ..."""
import sys, numpy as np
from np_fit import a0fit, kfit
for fn in sys.argv[1:]:
    d=np.load(fn); t=d['t']; f=d['phiH']; b=float(d['b']); print(fn,'b=%g'%b)
    for lo in (800,1600,3200): print('  window [%d,12700]: a0 = '%lo+'  '.join('%.5f'%a0fit(t,f,b,lo,12700,n) for n in (2,3,5)))
    B,s,k=kfit(t,f,1600,12700); print('  free fit [1600,12700]: k=%.4f B/(4|b|)=%.4f'%(k,B/(4*abs(b))))
