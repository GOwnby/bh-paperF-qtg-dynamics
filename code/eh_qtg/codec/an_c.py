"""Analysis of code-E output (collapse-driven or prescribed): usage an_c.py json k [hvkey]  (ray n=2, U~1)."""
import sys,json,os,numpy as np
sys.path.insert(0,os.environ.get('QTG_CODE','../..')); sys.path.insert(0,'..')
from qtg_lib import coef
f=sys.argv[1]; k=float(sys.argv[2])
d=json.load(open(f)); v=np.array(d['vq']); hvs=list(d['data'].keys()); key=sys.argv[3] if len(sys.argv)>3 else hvs[-1]
NRAY=int(os.environ.get("NRAY","2"))
def fields(hv,n=None):
    n=NRAY if n is None else n
    n=min(n,len(d['data'][hv]['r'])-1)
    F={a:np.array(b[n],float) for a,b in d['data'][hv].items() if a not in('nan','mon')}
    r,sg,rs,rv,Ps,PV,sV=[F[x] for x in ('r','sg','rs','rv','Ps','PV','sV')]
    W=np.exp(sg); y=-rs/W; rho=-rv; z=(r**2-1-4*y*rho)/r**2; psi=1-z
    Q,c1,c2,c3=[np.array(a) for a in coef(1,1.0,psi)]; g=Ps*PV/W
    Sig=psi/2-c2-8*np.pi*c1*g+64*np.pi**2*c3*g**2; H=128*np.pi**2*c1**2*g**2+Q**2/2
    K=(4*Sig)**2+8*H+4*psi**2; m=r**3*psi/(2*z)
    return dict(z=z,m=m,K=K,sV=sV,r=r,psi=psi)
A=fields(key); 
print('file',os.path.basename(f),'hv keys',hvs,'using',key,'v range',v[0],v[-1])
print('   v        r          z          m        v*sV      K        slope')
for vv in list(range(20,100,10))+list(range(100,int(v[-1]),50)):
    if vv>v[-1]-12: break
    i=int(np.argmin(abs(v-vv))); a,b=max(i-10,0),min(i+10,len(v)-1)
    if not (np.isfinite(A['K'][b]) and A['K'][a]>0): print(vv,'nonfinite'); continue
    lk=(np.log(A['K'][b])-np.log(A['K'][a]))/(np.log(v[b])-np.log(v[a]))
    print('%6.0f  %.5f  %.3e  %.6f  %8.3f  %.3e  %6.3f'%(v[i],A['r'][i],A['z'][i],A['m'][i],v[i]*A['sV'][i],A['K'][i],lk))
if len(hvs)>1:
    B=fields(hvs[0]); 
    for vv in (100,200,400,800,1200):
        if vv>v[-1]-12: continue
        i=int(np.argmin(abs(v-vv))); print('hv-conv at v=%d: dlnK=%.1e dsV=%.1e dr=%.1e'%(vv,abs(np.log(A['K'][i]/B['K'][i])),abs(A['sV'][i]-B['sV'][i]),abs(A['r'][i]-B['r'][i])))
