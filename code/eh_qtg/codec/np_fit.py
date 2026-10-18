"""Coefficient and exponent of the k=2 collapse tail (Paper F, Sec. collapse).  usage: python3 np_fit.py file.npz [file2.npz ...]
  y(t)=phi_H t^2/(-4b) with t=v-v_start; fit  y = a0 [1 + c1/t + c2 ln t/t + (c3 + c4 ln t)/t^2]  (a0=1 is the Angelopoulos-Aretakis-Gajic coefficient 4 I0, I0=-b) in windows [lo, 12700];
  free-index fit phi_H = B (t - s)^-k."""
import sys, numpy as np
from scipy.optimize import least_squares
def a0fit(t,f,b,lo,hi,npar):
    m=(t>=lo)&(t<=hi); x=t[m]; y=f[m]/(-4*b)*x**2
    def res(p):
        q=1+p[1]/x
        if npar>=3: q=q+p[2]*np.log(x)/x
        if npar>=5: q=q+p[3]/x**2+p[4]*np.log(x)/x**2
        return p[0]*q-y
    return least_squares(res,[1.0]+[0.0]*(npar-1),x_scale=[1]+[10]*(npar-1)).x[0]
def kfit(t,f,lo,hi):
    m=(t>=lo)&(t<=hi); x=t[m]; y=np.log(np.abs(f[m]))
    r=lambda p:(np.log(p[0])-p[2]*np.log(x-p[1]))-y
    return least_squares(r,[4.,0.,2.],x_scale=[1,50,1]).x
if __name__=='__main__':
    for fn in sys.argv[1:]:
        d=np.load(fn); t=d['t']; f=d['phiH']; b=float(d['b']); 
        if b==0: continue
        print(fn,'b=%g A=%.8f'%(b,float(d['A'])))
        for lo in (800,1600,3200):
            print('  window [%d,12700]: a0 = '%lo+'  '.join('%.5f'%a0fit(t,f,b,lo,12700,n) for n in (2,3,5)),'   (forms: c1 | +c2 ln t/t | +c3,c4 at 1/t^2)')
        for lo in (800,1600,3200):
            B,s,k=kfit(t,f,lo,12700); print('  free (B,s,k) window [%d,12700]: B/(4|b|)=%.4f  s=%.1f  k=%.4f'%(lo,B/(4*abs(b)),s,k))
