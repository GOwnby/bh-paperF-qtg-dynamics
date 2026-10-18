"""Late-time table along the rays of a constrained QTG run (Romberg-extrapolated fields).  usage: late_q.py json model L2 [vlist]"""
import os, sys, numpy as np
sys.argv=[sys.argv[0]]+sys.argv[1:]
import analyze_q as A
sys.path.insert(0,os.environ.get('QTG_CODE',os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')))
from qtg_lib import coef, hfun
model=int(sys.argv[2]); L2=float(sys.argv[3]); vl=[float(x) for x in sys.argv[4:]] or [60,80,100,120,140,160,180,198]
def inv(lev):
    F=lambda nm:A.F[nm][lev]
    r,sg,rs,rv,Ps,PV,sV=[F(x) for x in ('r','sg','rs','rv','Ps','PV','sV')]
    W=np.exp(sg); y=-rs/W; rho=-rv; psi=(1+4*y*rho)/r**2; Q,c1,c2,c3=coef(model,L2,psi); g=Ps*PV/W
    Sig=psi/2-c2-8*np.pi*c1*g+64*np.pi**2*c3*g**2; h_,hp=hfun(model,L2,psi); m=0.5*r**3*h_
    K=(4*Sig)**2+8*(128*np.pi**2*c1**2*g**2+Q**2/2)+4*psi**2
    return dict(r=r,y=y,rho=rho,psi=psi,g=g,Sig=Sig,K=K,m=m,sV=sV,PV=PV,lnW=sg,c1=c1)
T=inv(len(A.hl)-1); P=inv(len(A.hl)-2)
print('model %d L2=%g B=%g k=%g; grids %s'%(model,L2,A.d['B'],A.d['k'],A.hl))
for n,U in enumerate(A.d['Uq']):
    print('--- ray U=%.3f   (columns: v, r, 1-psi (or wall gap), m, sigma_v, y, phi_v, g, Sigma, K, rel.diff(Sigma) top2 levels)'%U)
    for vv in vl:
        if vv>A.v[-1]: continue
        i=int(np.argmin(abs(A.v-vv)))
        print('%5.0f %.6f %.3e %.4e %+.5f %.3e %+.3e %.3e %.3e %.3e %.1e'%(A.v[i],T['r'][n,i],1-(T['psi'][n,i] if model==1 else abs(L2)**0.5*T['psi'][n,i]),T['m'][n,i],T['sV'][n,i],T['y'][n,i],T['PV'][n,i],T['g'][n,i],T['Sig'][n,i],T['K'][n,i],abs(T['Sig'][n,i]/P['Sig'][n,i]-1)))
