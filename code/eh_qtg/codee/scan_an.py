"""Scan analysis for code E output (Paper F).  usage: scan_an.py json k MASS [vmax]   (ray n=2, U~1).
Prints, at advanced times v = x/kappa_+ (x = 2,4,...), the slaving quantities, hv-convergence (two hv in the file), m*z, v*sigma_v vs -(2k+2), the K slope and the generalized slope formula."""
import sys,json,os,numpy as np
sys.path.insert(0,os.environ.get('QTG_CODE','../..')); sys.path.insert(0,'..')
from qtg_lib import coef
from dnU_qtg import StaticU
f=sys.argv[1]; k=float(sys.argv[2]); mass=float(sys.argv[3]); vmax=float(sys.argv[4]) if len(sys.argv)>4 else 1e9
S=StaticU(mass); kp=S.kp
d=json.load(open(f)); v=np.array(d['vq']); hvs=list(d['data'].keys())
def fields(hv,n=2):
    n=min(n,len(d['data'][hv]['r'])-1)   # thinned files (data/) carry the single ray U=0.9968
    F={a:np.array(b[n],float) for a,b in d['data'][hv].items() if a not in('nan','mon')}
    r,sg,rs,rv,Ps,PV,sV=[F[x] for x in ('r','sg','rs','rv','Ps','PV','sV')]
    W=np.exp(sg); y=-rs/W; rho=-rv; z=(r**2-1-4*y*rho)/r**2; psi=1-z
    Q,c1,c2,c3=[np.array(a) for a in coef(1,1.0,psi)]; g=Ps*PV/W
    Sig=psi/2-c2-8*np.pi*c1*g+64*np.pi**2*c3*g**2; H=128*np.pi**2*c1**2*g**2+Q**2/2
    K=(4*Sig)**2+8*H+4*psi**2; m=r**3*psi/(2*z)
    return dict(z=z,m=m,K=K,sV=sV,r=r)
A=fields(hvs[0]); Bf=fields(hvs[-1])
print('file',os.path.basename(f),'k=%g mass=%g kappa+=%.6f  hv: %s'%(k,mass,kp,hvs))
print(' x=k+v   v      z         m*z       v*sV     -(2k+2)  dm/dv   v0     K          slope  formula  corr    dsV(hv)   dlnK(hv)')
for x in [1,2,3,4,6,8,10,12,14,16,18,20,22,24,26,28,30,35,40,45,50,55,60,65]:
    vv=x/kp
    if vv>vmax or vv<60: continue
    i=int(np.argmin(abs(v-vv)))
    if i+12>=len(v) or not np.isfinite(A['K'][i+10]): break
    a,b=i-10,i+10
    lk=(np.log(A['K'][b])-np.log(A['K'][a]))/(np.log(v[b])-np.log(v[a])); dm=(A['m'][i+5]-A['m'][i-5])/10; v0=v[i]-A['m'][i]/dm
    vs=v[i]*A['sV'][i]; form=(4*k-2)-6*v0/(v[i]-v0)+2*(abs(vs)-(2*k+2))
    corr=lk+6*v0/(v[i]-v0)-2*(abs(vs)-(2*k+2))   # -> 4k-2 as v -> infinity (Eq. kslopek with the two correction terms removed)
    print('%5.1f %7.1f  %.3e  %.5f  %8.4f  %6.2f  %.4f  %6.1f  %.3e  %6.3f  %6.3f  %6.3f  %.1e  %.1e'%(x,v[i],A['z'][i],A['m'][i]*A['z'][i],vs,-(2*k+2),dm,v0,A['K'][i],lk,form,corr,abs(A['sV'][i]-Bf['sV'][i]),abs(np.log(A['K'][i]/Bf['K'][i]))))
