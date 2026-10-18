"""Pulse-strength scan, late-time diagnostics: usage pscan_an.py json... ; prints r_inf, v*sigma_v and dlnK/dlnv (20-point window) at v=300,600,900 times env VS (default 1)."""
import sys,json,os,numpy as np
sys.path.insert(0,os.environ.get('QTG_CODE','../..')); from qtg_lib import coef
def rminus(m):
    rt=np.roots([1,-2*m,0,2*m]); rt=rt[abs(rt.imag)<1e-9].real; return rt[rt>0].min()
def fields(d,hv,n):
    F={a:np.array(b[n],float) for a,b in d['data'][hv].items() if a not in('nan','mon')}
    r,sg,rs,rv,Ps,PV,sV=[F[x] for x in ('r','sg','rs','rv','Ps','PV','sV')]
    W=np.exp(sg); y=-rs/W; rho=-rv; z=(r**2-1-4*y*rho)/r**2; psi=1-z
    Q,c1,c2,c3=[np.array(a) for a in coef(1,1.0,psi)]; g=Ps*PV/W
    Sig=psi/2-c2-8*np.pi*c1*g+64*np.pi**2*c3*g**2; H=128*np.pi**2*c1**2*g**2+Q**2/2
    K=(4*Sig)**2+8*H+4*psi**2
    return dict(r=r,m=r**3*psi/(2*z),K=K,sV=sV)
print('%-30s %6s %9s %9s %9s'%('run','v','r_inf','v*sV','dlnK/dlnv'))
for f in sys.argv[1:]:
    d=json.load(open(f)); v=np.array(d['vq']); hv=list(d['data'].keys())[-1]
    A=fields(d,hv,2)
    VS=float(os.environ.get('VS','1'))
    for vv in [int(x*VS) for x in (300,600,900)]:
        if vv>v[-1]-12: continue
        i=int(np.argmin(abs(v-vv))); a,b=i-10,i+10
        lk=(np.log(A['K'][b])-np.log(A['K'][a]))/(np.log(v[b])-np.log(v[a]))
        print('%-30s %6.0f %9.5f %9.3f %9.3f'%(os.path.basename(f)[:30],v[i],A['r'][i],v[i]*A['sV'][i],lk))
