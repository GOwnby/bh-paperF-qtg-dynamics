"""Seed of the late-time departure of code E (Paper F, Sec. 'The seed of the late-time departure'): advanced time at which v*sigma_v departs from the unperturbed run
by 0.01, 0.05, 0.5 when a constant offset eps is added to Delta_0 at every s>0 (gen_e.py with env DELTA0_OFFSET=eps; B=3e-3, k=3/2, m=5, hs=0.2, hv=0.1, v1=1000; eps=3.55e-15, v1=950, is the
r_+ - r_H(0) of the former initial row).  Reference: eps=0, v1=1200.  Fit: v_dep = a - b ln(eps); expected b = 1/kappa_+ = 20.4.  usage: python3 seed_amplitude.py"""
import json,numpy as np
kp=0.0489687
def load(f):
    d=json.load(open(f)); v=np.array(d['vq']); return d,v,v*np.array([np.nan if t is None else t for t in d['data']['0.1']['sV'][0]])
_,vr,ar=load('data/gene_p1_hs0.2_m1_B0.003_k1.5_v1200_ray2.json')
E=['0','1e-15','3.55e-15','1e-14','1e-13','1e-12']; res={}
print('eps        v(dev>0.01) v(dev>0.05) v(dev>0.5)')
for e in E:
    d,v,a=load('data/seed_eps%s_v%d_ray2.json'%(e,950 if e=='3.55e-15' else 1000))
    dev=np.abs(a-np.interp(v,vr,ar)); dev[~np.isfinite(dev)]=1e9; dev[v>d['v1']-120]=0
    out=[]
    for th in (0.01,0.05,0.5):
        b=np.where(dev>th)[0]; out.append(v[b[0]] if len(b) else np.nan)
    res[e]=out; print('%-9s'%e,*['%9s'%('none' if np.isnan(o) else '%.0f'%o) for o in out])
x=np.log([float(e) for e in E[1:]])
for j,th in enumerate((0.01,0.05,0.5)):
    y=np.array([res[e][j] for e in E[1:]]); A=np.polyfit(x,y,1)
    print('threshold %-4g: dv/dln(eps) = %.2f (expected %.2f), rms residual %.2f'%(th,A[0],-1/kp,np.sqrt(np.mean((np.polyval(A,x)-y)**2))))
