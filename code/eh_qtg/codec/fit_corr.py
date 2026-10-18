"""B with a 1/(v-v_s) correction: phi_H=B x^-3 (1+C/x), x=v_e-v_s, window [lo,hi] m_f/5; compared with B(k=3 fixed) and with F_abs from horizon_ray.log.  usage: fit_corr.py lo hi tables..."""
import sys,numpy as np
from scipy.optimize import least_squares
from fit1 import fitwin
lo,hi=float(sys.argv[1]),float(sys.argv[2]); Fabs={}
for ln in open('horizon_ray.log'):
    t=ln.split()
    if len(t)>=12 and t[0].endswith('.npz') and 'invalid' not in ln:
        try: Fabs[t[0]]=float(t[9])
        except ValueError: pass
print('%-26s %8s %8s %8s %8s %8s'%('table','F_abs','F(k=3)','F(corr)','k3/abs','corr/abs'))
for fn in sys.argv[3:]:
    d=np.load(fn); mf=float(d['mf']); s2=mf/5; ve=float(d['v1e'])+d['t']; ph=d['phiH']; Q=abs(float(d['Q']))
    m=(ve>=lo*s2)&(ve<=hi*s2); x0=ve[m]; y=ph[m]
    B3=fitwin(ve,ph,lo*s2,hi*s2,3.0)[0]
    f=lambda p:np.log(np.abs(y))-(np.log(p[0])-3*np.log(x0-p[1])+np.log(np.abs(1+p[2]/(x0-p[1]))))
    r=least_squares(f,[B3,0.,0.],x_scale=[10,50,50])
    Fc=r.x[0]/(8*mf*Q); F3=B3/(8*mf*Q); Fa=Fabs.get(fn.split('/')[-1],np.nan)
    print('%-26s %8.4f %8.4f %8.4f %8.4f %8.4f   C=%.1f'%(fn[:26],Fa,F3,Fc,F3/Fa,Fc/Fa,r.x[2]))
