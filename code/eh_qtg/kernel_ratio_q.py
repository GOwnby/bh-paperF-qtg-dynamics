"""QTG flux phi_v (Romberg, EH-regular data) divided by the linear-response kernel prediction of Paper G, on the ray U~1 (ray index 2) and U~0.6 (1)."""
import os, sys, numpy as np
fn=sys.argv[1]; sys.argv=[sys.argv[0],fn]
import analyze_q as A
import kernel_lib as KL
k=A.d['k']; B=A.d['B']
print('B=%g k=%g'%(B,k)); print('   v   kernel_phi_v    ratio U=0.6   ratio U=1.0   ratio U=1.2')
for vv in (40,50,60,70,80,90,100,108):
    i=int(np.argmin(abs(A.v-vv))); kv=KL.phi_v(float(A.v[i]),k,B)
    print('%4d  %.5e   %.6f   %.6f   %.6f'%(A.v[i],kv,A.top['PV'][1,i]/kv,A.top['PV'][2,i]/kv,A.top['PV'][3,i]/kv))
