"""h-convergence of the BCR benchmark (Paper F, Sec. 'benchmark against Bizon et al.'): t^3 D(t) at r=5 for the eps pair (0.02,0.01) on the meshes h=0.1, 0.05, 0.025
(runs in base/, made by runtag.sh base ...), ratio of successive differences (4 = second order) and the Richardson value.  usage (from this directory): python3 convergence_h.py > convergence_h.log"""
import numpy as np
def L(h,e): d=np.load('base/h%s_%s.npz'%(h,e)); return d['t'],d['phi']
def D(h,hi,lo):
    t,a=L(h,hi); _,b=L(h,lo); e1,e2=float(hi),float(lo); return t,(a/e1-b/e2)/(e1**2-e2**2)
t,D1=D('0.1','0.02','0.01'); _,D2=D('0.05','0.02','0.01'); _,D3=D('0.025','0.02','0.01')
print('t^3 D at r=5, eps pair (0.02,0.01), h=0.1,0.05,0.025, ratio of differences (4 = second order), Richardson')
for T in (100,150,200,250):
    i=int(np.argmin(abs(t-T))); y=[t[i]**3*Dk[i,0] for Dk in (D1,D2,D3)]
    print(T,['%.3f'%v for v in y],'%.2f'%((y[0]-y[1])/(y[1]-y[2])),'%.3f'%(y[2]+(y[2]-y[1])/3))
