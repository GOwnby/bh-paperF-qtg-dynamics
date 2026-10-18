"""Curvature K, slaved quantities and the slope formula along U~1 to large v (v up to 1400 if the file reaches it). usage: kstudy2.py json hv [vmax] [ray]; ray index 0 for thinned files (single ray)."""
import sys,json,os,numpy as np
sys.path.insert(0,os.environ.get('QTG_CODE','../..'))
from qtg_lib import coef
d=json.load(open(sys.argv[1])); hv=sys.argv[2]; vmax=float(sys.argv[3]) if len(sys.argv)>3 else 1e9; n=int(sys.argv[4]) if len(sys.argv)>4 else 2
n=min(n,len(d['data'][hv]['r'])-1)   # thinned files carry the single ray U=0.9968
F={k:np.array(v[n],float) for k,v in d['data'][hv].items() if k not in('nan','mon')}
v=np.array(d['vq']); r,sg,rs,rv,Ps,PV,sV=[F[x] for x in ('r','sg','rs','rv','Ps','PV','sV')]
W=np.exp(sg); y=-rs/W; rho=-rv; z=(r**2-1-4*y*rho)/r**2; psi=1-z
Q,c1,c2,c3=[np.array(a) for a in coef(1,1.0,psi)]; g=Ps*PV/W
Sig=psi/2-c2-8*np.pi*c1*g+64*np.pi**2*c3*g**2; H=128*np.pi**2*c1**2*g**2+Q**2/2
K=(4*Sig)**2+8*H+4*psi**2
m=r**3*psi/(2*z)
print('v      z          m        dm/dv   v0       K            dlnK/dlnv  formula  slope+terms  v*sV     dlnz/dlnv   c3share')
for vv in [100,150,200,250,300,340,380,420,460,500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200,1250,1300,1350,1400]:
    if vv>vmax: break
    i=int(np.argmin(abs(v-vv))); a=i-10; b=i+10
    if b>=len(v) or not np.isfinite(K[b]): break
    lk=(np.log(K[b])-np.log(K[a]))/(np.log(v[b])-np.log(v[a])); dm=(m[i+5]-m[i-5])/10; v0=vv-m[i]/dm
    dz=(np.log(z[b])-np.log(z[a]))/(np.log(v[b])-np.log(v[a])); vs=vv*sV[i]
    form=4-6*v0/(vv-v0)+2*(abs(vs)-5)
    corr=lk+6*v0/(vv-v0)-2*(abs(vs)-5)     # -> 4 (k=3/2); add back the two 1/v terms of the formula
    print('%4d  %.4e  %8.1f  %.4f  %6.1f  %.5e  %7.3f   %7.3f  %7.3f   %7.3f  %7.3f   %.9f'%(vv,z[i],m[i],dm,v0,K[i],lk,form,corr,vs,dz,64*np.pi**2*c3[i]*g[i]**2/Sig[i]))
