"""Monotonicity of the kernel flux (Paper F, Sec. 'Behind the front', Asymptotics of the slaved description, item (i)).
Phi(v) = phi_v(v) = int K(v-v') j(v') dv' for the horizon tail phi_H = B (1+v)^-k, with the interior kernel K of Paper E/G (kernel_lib.phi_v, m_N = 5).
Prints, for k = 1/2, 1, 3/2, 2, 3, the largest value of Phi(v+1)/Phi(v) on the grid v = 20, 21, ..., 1200 (|Phi| strictly decreasing  <=>  all ratios < 1) and writes
Phi_kernel.npy = array [v, Phi(v)/B] for k = 3/2 (B = 1).  usage: python3 phi_monotone.py > logs/phi_monotone.log   (36 s measured, see code/README.md)"""
import numpy as np, kernel_lib as KL
v=np.arange(20,1201,1.0)
out={}
for k in (0.5,1.0,1.5,2.0,3.0):
    P=np.array([KL.phi_v(float(x),k,1.0) for x in v]); out[k]=P
    r=P[1:]/P[:-1]
    print('k=%-4g  Phi(20)=%.6e  Phi(1200)=%.6e  max Phi(v+1)/Phi(v)=%.9f  at v=%g   strictly decreasing |Phi|: %s'%(k,P[0],P[-1],r.max(),v[np.argmax(r)],bool(np.all(np.abs(P[1:])<np.abs(P[:-1])))))
np.save('Phi_kernel.npy',np.vstack([v,out[1.5]]))
