"""Sensitivity of the consistency of the constrained evolution to the c_3 term (Paper F).  Mode 1 projects only r_u on the u-Raychaudhuri integral and evolves r_v with r_uv, sigma_uv (the v-Raychaudhuri equation is then a constraint); mode 3 integrates both Raychaudhuri equations. They differ by O(h^2) only if sigma_uv is compatible (propagates the constraint). 
both integrate the Raychaudhuri equations.  If sigma_uv has the wrong c_3 coefficient the evolution of (r, r_u, r_v) from the three equations is inconsistent and the modes differ at O(1) of the c_3 effect.
Rebuilds libqtg with c3 -> FAC * c3 (Hayward model).  usage: c3_sensitivity.py B v1 h FAC1 FAC2 ..."""
import os, sys, subprocess, ctypes, numpy as np, warnings
warnings.filterwarnings('ignore')
code=os.environ.get('QTG_CODE','..'); sys.path.insert(0,code)
import qtg_lib
from dnU_qtg import *
B=float(sys.argv[1]); v1=float(sys.argv[2]); h=float(sys.argv[3]); facs=[float(x) for x in sys.argv[4:]]
S=StaticU(5.0); kp=S.kp; c=0.2*np.exp(-kp*v1); Uq=[0.3,0.6,1.0,1.2]; vq=np.arange(20,v1-1.9,1.0)
sq=[float(np.round(np.log(1+x*kp/c)/kp/0.05)*0.05) for x in Uq]
d=build_eh_q(S,1,1.0,1.5,v1,h,h,B,k=1.5,c=c,vH=v1+300); cols=[int(round(s/h)) for s in sq]; ii=[int(round(x/h)) for x in vq]
src=open(os.path.join(code,'qtg_dn.c')).read(); assert '*c3=2*L2*z*z*z;' in src
dp=ctypes.POINTER(ctypes.c_double)
res={}
import tempfile; tmpd=tempfile.mkdtemp(prefix='qtg_c3_')   # scratch directory for the modified C sources/libraries
for fac in facs:
    f=os.path.join(tmpd,'qtg_c3_%g.c'%fac); open(f,'w').write(src.replace('*c3=2*L2*z*z*z;','*c3=%r*2*L2*z*z*z;'%fac)); so=os.path.join(tmpd,'libqtg_c3_%g.so'%fac)
    subprocess.check_call(['gcc','-O3','-shared','-fPIC','-o',so,f,'-lm'])
    lib2=ctypes.CDLL(so); lib2.evolve_stream_qtg_cy.argtypes=qtg_lib.lib.evolve_stream_qtg_cy.argtypes; qtg_lib.lib=lib2
    for mode in (1,3):
        out=qtg_lib.run_stream_cy(1,1.0,d['row0'],d['col0'],h,h,cols,mode=mode); res[(fac,mode)]=out[:,ii,:]
names=['r','sg','rs','rv','sgs','sV','Ps','PV']
print('B=%g h=%g, ray U~1: difference mode1-mode3 (sigma_v, z=1-psi relative) for c3 -> FAC*c3'%(B,h))
def zz(a):
    r,sg,rs,rv=a[2,:,0],a[2,:,1],a[2,:,2],a[2,:,3]; W=np.exp(sg); return 1-(1+4*(-rs/W)*(-rv))/r**2
print('   v    '+'   '.join('FAC=%g: dsV  dz/z  sV(m3)'%f for f in facs))
for vv in (60,70,80,90,100,105):
    j=int(np.argmin(abs(vq-vv))); s=''
    for fac in facs:
        a2=res[(fac,1)]; a3=res[(fac,3)]; z2=zz(a2); z3=zz(a3)
        s+='   %+.1e %+.1e %+.4f'%(a2[2,j,5]-a3[2,j,5],(z2[j]-z3[j])/z3[j],a3[2,j,5])
    print('%4d'%vv+s)
