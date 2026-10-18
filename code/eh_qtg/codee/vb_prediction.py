"""Prediction of the blow-up advanced time v_b of code B from the one-dimensional model (Paper F, Sec. "Why the window closes").
Run first (cwd = this directory, QTG_CODE and PYTHONPATH as in the README):  python3 mech_vb.py 600 3e-3 1.5 ; python3 mech_vb.py 600 3e-2 1.5 ; python3 mech_vb.py 600 3e-4 1.5
(each writes mech_vb_B<B>_k1.5.npz, 3 MB, not shipped).  Then:  python3 vb_prediction.py
One constant is calibrated, the threshold |err| = delta* reached at the measured v_b of B=3e-3 (five values of h_v); the other columns are predictions."""
import numpy as np
meas={'0.003':{0.2:252,0.1:307,0.05:364,0.025:420,0.0125:477},'0.03':{0.2:158,0.1:214,0.05:270},'0.0003':{0.2:346}}   # first non-finite v of code B (hs=0.05); B=3e-3: cmp_table.log; others: first_nonfinite.py on the new runs (logs/vb_B3e-2_B3e-4.log)
f=lambda B: np.load('mech_vb_B%g_k1.5.npz'%float(B))
d=f('0.003'); e=lambda d,hv: (d['%g_4_v'%hv],np.abs(d['%g_4_e'%hv]))
print('1D RK4 error at the measured blow-up of code B (B=3e-3):')
ds=[]
for hv,v in meas['0.003'].items():
    vv,ee=e(d,hv); ds.append(ee[int(np.argmin(abs(vv-v)))]); print('  hv=%-7g v_b=%d  |err|=%.4f'%(hv,v,ds[-1]))
dstar=float(np.mean(ds)); print('delta* = %.4f +- %.4f'%(dstar,np.std(ds)))
for B in ('0.003','0.03','0.0003'):
    d=f(B); print('B=%s  predicted v_b (first v with |err|>delta*) vs measured:'%B)
    for hv in (0.2,0.1,0.05,0.025,0.0125):
        vv,ee=e(d,hv); i=np.argmax(ee>dstar); pv=vv[i] if ee[i]>dstar else float('nan')
        print('  hv=%-7g predicted %6.1f   measured %s'%(hv,pv,meas[B].get(hv,'-')))
