"""Mass-inflation front: advanced time v_f(U) at which sigma_v (Romberg-extrapolated) crosses the midpoint between -kappa_-(m_f) and -0.1, and the Kruskal variable x_f = U e^{kappa_+ v_f}.  usage: front_q.py json kappa_+"""
import sys, numpy as np
import analyze_q as A
kp=float(sys.argv[2]); thr=float(sys.argv[3]) if len(sys.argv)>3 else -0.4
print('B=%g  threshold sigma_v=%g'%(A.d['B'],thr))
print('   U       v_f     x_f=U e^{kp v_f}   ln x_f')
for n,U in enumerate(A.d['Uq']):
    s=A.top['sV'][n]; v=A.v; idx=None
    for i in range(len(v)-1):
        if s[i]<thr<=s[i+1] and np.all(np.isfinite(s[i:i+2])): idx=i
    if idx is None: print(' %.4f  not reached'%U); continue
    i=idx; vf=v[i]+(thr-s[i])/(s[i+1]-s[i])*(v[i+1]-v[i]); xf=U*np.exp(kp*vf)
    print(' %.4f  %7.2f   %8.2f   %6.3f'%(U,vf,xf,np.log(xf)))
