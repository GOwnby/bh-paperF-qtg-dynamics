"""Convergence and robustness of code E after the correction of the initial row (Paper F, Sec. 'The seed of the late-time departure').  Reference: hs=0.2, hv=0.1, v1=1200, double (data/).
Compared: v1=1500; hv=0.05; hs=0.1; long double (genel_*).  Prints the relative change of K and r and the absolute change of sigma_v at several v (no growth like exp(kappa_+ v) is expected).  usage: python3 conv_e2.py"""
import os,sys,json,numpy as np
sys.path.insert(0,os.environ.get('QTG_CODE','../..'))
from qtg_lib import coef
def load(f):
    d=json.load(open(f)); x=d['data'][list(d['data'])[0]]; v=np.array(d['vq'])
    F={a:np.array([np.nan if t is None else t for t in b[0]],float) for a,b in x.items()}
    r,sg,rs,rv,Ps,PV=[F[a] for a in('r','sg','rs','rv','Ps','PV')]
    W=np.exp(sg); y=-rs/W; z=(r**2-1+4*y*rv)/r**2; psi=1-z
    Q,c1,c2,c3=[np.array(a) for a in coef(1,1.0,psi)]; g=Ps*PV/W
    Sig=psi/2-c2-8*np.pi*c1*g+64*np.pi**2*c3*g**2; H=128*np.pi**2*c1**2*g**2+Q**2/2
    return v,(4*Sig)**2+8*H+4*psi**2,r,F['sV']
ref='data/gene_p1_hs0.2_m1_B0.003_k1.5_v1200_ray2.json'
v,K0,r0,s0=load(ref)
print('change relative to the reference (K, r: relative; sigma_v: absolute)')
for nm,f in (('v1=1500','data/gene_p1_hs0.2_m1_B0.003_k1.5_v1500_ray2.json'),('hv/2','data/gene_p1_hs0.2_m1_B0.003_k1.5_v1200_hv0.05_ray2.json'),('hs/2','data/gene_p1_hs0.1_m1_B0.003_k1.5_v1200_ray2.json'),('long double','data/genel_p1_hs0.2_m1_B0.003_k1.5_v1200_ray2.json')):
    v2,K,r,s=load(f); n=min(len(v),len(v2))
    print('%-12s'%nm+'  '.join('v=%d: dK/K=%.1e dr/r=%.1e dsv=%.1e'%(V,abs(K[V-20]/K0[V-20]-1),abs(r[V-20]/r0[V-20]-1),abs(s[V-20]-s0[V-20])) for V in (100,300,650,1000,1100)))
