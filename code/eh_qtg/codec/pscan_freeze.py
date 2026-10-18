"""r_inf of a code-E run against r_-(m_f), the mass m* with r_-(m*)=r_inf, and the ray mass at the first v with |r-r_inf|<3e-5 r_inf.  usage: pscan_freeze.py m_f json..."""
import sys,json,numpy as np
from scipy.optimize import brentq
def rminus(m):
    rt=np.roots([1,-2*m,0,2*m]); rt=rt[abs(rt.imag)<1e-9].real; return rt[rt>0].min()
mf=float(sys.argv[1])
for f in sys.argv[2:]:
    d=json.load(open(f)); v=np.array(d['vq']); F={a:np.array(b[2],float) for a,b in list(d['data'].values())[-1].items() if a not in('nan','mon')}
    r=F['r']; W=np.exp(F['sg']); y=-F['rs']/W; z=(r**2-1-4*y*(-F['rv']))/r**2; m=r**3*(1-z)/(2*z)
    ri=r[-1]; i=int(np.argmax(abs(r-ri)<3e-5*ri)); ms=brentq(lambda x:rminus(x)-ri,mf*0.5,mf*2)
    print('%s: m_f=%g r_-(m_f)=%.5f r_inf=%.5f (diff %.1e) m*=%.3f (%.2f%%) ray mass at freeze v=%.0f: %.3f (r_-=%.5f)'%(f.split('_')[1],mf,rminus(mf),ri,ri-rminus(mf),ms,100*(ms/mf-1),v[i],m[i],rminus(m[i])))
