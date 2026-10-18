"""Linearity of the horizon response to the non-compact tail and free fits (Paper F, Sec. collapse).  usage: python3 np_lin_b.py npdata/np_m1_b{0.0,0.5,1.0,-1.0,2.0}_h1.npz (b=0 first)"""
import numpy as np
D={b:np.load('npdata/np_m1_b%s_h1.npz'%b) for b in ('0.0','0.5','1.0','-1.0','2.0')}
t=D['0.0']['t']; f0=D['0.0']['phiH']; h=t[1]-t[0]
print('A (pulse amplitude re-tuned to m=5 at v=100):',{k:round(float(v['A']),8) for k,v in D.items()}); print('mass at the corner m_f:',{k:round(float(v['mf']),6) for k,v in D.items()})
print('E/b = (phi_H(b)-phi_H(0))/b  [units 1e-6]; spread over b = 0.5, 1, -1, 2:')
for T in (50,100,200,400,800,1600,3200,6400,12700):
    i=int(round(T/h)); e=[(D[b]['phiH'][i]-f0[i])/float(b) for b in ('0.5','1.0','-1.0','2.0')]
    print(' t=%5d  E/b(b=1)=%+.5f  max spread=%.1e  (relative %.1e)  phi_H(0)=%.3e'%(T,e[1]*1e6,max(e)-min(e),(max(e)-min(e))/abs(e[1]),f0[i]))
