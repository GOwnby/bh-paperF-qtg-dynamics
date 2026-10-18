"""Curvature K along U~1 from code B (hs=0.05). usage: kstudy.py json hv [hv2]  ; Richardson (hv^4) if hv2 given (hv2=2*hv)"""
import sys,json,os,numpy as np
sys.path.insert(0,os.environ['QTG_CODE'])
from qtg_lib import coef
d=json.load(open(sys.argv[1])); hv=sys.argv[2]; n=2
def fld(hv): return {k:np.array(v[n],float) for k,v in d['data'][hv].items() if k not in('nan','mon')}
F=fld(hv)
if len(sys.argv)>3:
    G=fld(sys.argv[3]); F={k:(16*F[k]-G[k])/15 for k in F}
v=np.array(d['vq']); r,sg,rs,rv,Ps,PV,sV=[F[x] for x in ('r','sg','rs','rv','Ps','PV','sV')]
W=np.exp(sg); y=-rs/W; rho=-rv; psi=(1+4*y*rho)/r**2; Q,c1,c2,c3=[np.array(a) for a in coef(1,1.0,psi)]; g=Ps*PV/W
Sig=psi/2-c2-8*np.pi*c1*g+64*np.pi**2*c3*g**2; H=128*np.pi**2*c1**2*g**2+Q**2/2
K=(4*Sig)**2+8*H+4*psi**2; z=1-psi
np.save('kst_%s.npy'%os.path.basename(sys.argv[1]).replace('.json',''),np.array([v,r,sg,y,rho,psi,z,g,Sig,K,PV,Ps,sV]))
print('v   z   W   K   dlnK/dlnv  (finite-difference over +-10)   Sigma-term share   sig_v(=sV)  -(2k+2)/v')
for vv in list(range(100,361,20)):
    i=int(np.argmin(abs(v-vv))); a=i-10; b=i+10
    if b>=len(v) or not np.isfinite(K[b]): break
    lk=(np.log(K[b])-np.log(K[a]))/(np.log(v[b])-np.log(v[a]))
    print('%4d  %.3e  %.3e  %.4e  %5.2f   S16=%.2f%%  H8=%.2f%%  psi4=%.2f%%   sV=%+.4f  -(5)/v=%+.4f'%(vv,z[i],W[i],K[i],lk,100*(4*Sig[i])**2/K[i],100*8*H[i]/K[i],100*4*psi[i]**2/K[i],sV[i],-5/vv))

# terms of Sigma and the exact generalized mass m=r^3 psi/(2 z) (h=psi/z, l=1), v0 from m/(dm/dv)
m=r**3*psi/(2*z)
print('\nv   psi/2   -c2   -8pi c1 g   64pi^2 c3 g^2   c3term/Sigma   H-term share   m   dm/dv   v0=v-m/(dm/dv)   dlnz/dlnv   v*sV')
for vv in (100,200,300,340,380):
    i=int(np.argmin(abs(v-vv))); dm=(m[i+5]-m[i-5])/10; dz=(np.log(z[i+10])-np.log(z[i-10]))/(np.log(v[i+10])-np.log(v[i-10]))
    t=(psi[i]/2,-c2[i],-8*np.pi*c1[i]*g[i],64*np.pi**2*c3[i]*g[i]**2)
    print('%4d  %.5f  %.2e  %.3e  %.3e  %.10f  %.1e  %.1f  %.3f  %.1f  %.3f  %.3f'%(vv,t[0],t[1],t[2],t[3],t[3]/Sig[i],8*H[i]/K[i],m[i],dm,vv-m[i]/dm,dz,vv*sV[i]))
