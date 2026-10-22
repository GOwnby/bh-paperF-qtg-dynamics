import sys, json, numpy as np
import os; sys.path.insert(0,os.environ.get('QTG_CODE',os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')))
from qtg_lib import coef
fn=sys.argv[1]; Kl=int(sys.argv[2]) if len(sys.argv)>2 else 4
d=json.load(open(fn)); v=np.array(d['vq']); hl=sorted((float(h) for h in d['data']),reverse=True)
def top(nm,n,K):
    lv=hl[-K:]; arr=[np.array(d['data'][repr(h) if repr(h) in d['data'] else str(h)][nm][n]) for h in lv]
    T=[arr]
    for lev in range(1,K): T.append([(4**lev*T[-1][i+1]-T[-1][i])/(4**lev-1) for i in range(len(T[-1])-1)])
    return T[-1][0]
n=int(sys.argv[3]) if len(sys.argv)>3 else 2
F={nm:top(nm,n,Kl) for nm in ('r','sg','rs','rv','Ps','PV','sV')}
r,sg,rs,rv,Ps,PV=[F[x] for x in ('r','sg','rs','rv','Ps','PV')]
W=np.exp(sg); y=-rs/W; rho=-rv; psi=(1+4*y*rho)/r**2; Q,c1,c2,c3=[np.array(a) for a in coef(1,1.0,psi)]; g=Ps*PV/W
Sig=psi/2-c2-8*np.pi*c1*g+64*np.pi**2*c3*g**2; K=(4*Sig)**2+8*(128*np.pi**2*c1**2*g**2+Q**2/2)+4*psi**2
z=1-psi
print('ray U=%.3f, K=%d finest levels'%(d['Uq'][n],Kl))
print('   v      z          g=phiu phiv/W    Sigma        K       dlnK/dlnv  dln|g|/dlnv  dlnz/dlnv  dlnW/dv')
for vv in range(100,int(sys.argv[4]) if len(sys.argv)>4 else 241,10):
    i=int(np.argmin(abs(v-vv))); a=i-5; b=i+5
    lk=(np.log(K[b])-np.log(K[a]))/(np.log(v[b])-np.log(v[a])); lg=(np.log(abs(g[b]))-np.log(abs(g[a])))/(np.log(v[b])-np.log(v[a])); lz=(np.log(z[b])-np.log(z[a]))/(np.log(v[b])-np.log(v[a]))
    dW=(sg[b]-sg[a])/(v[b]-v[a])
    print(' %5.0f  %.3e  %+.4e   %.4e  %.4e   %.2f   %.2f   %.2f   %+.4f'%(v[i],z[i],g[i],Sig[i],K[i],lk,lg,lz,dW))
print('\ncheck of the structural scaling: K z^-6 Phi^4 (-> const (1+G/kappa)^4 phi_u^4) and g*Phi/(1+G/kappa)/phi_u')
kap=0.795
for vv in range(100,int(sys.argv[4]) if len(sys.argv)>4 else 241,20):
    i=int(np.argmin(abs(v-vv)))
    print(' %5.0f  K z^-6 Phi^4=%.4e   g*Phi/((1+G/kap)*phi_u*...)=%.4e   phi_u(s)=%.4e  Phi=%.4e'%(v[i],K[i]/z[i]**6*PV[i]**4,g[i]*PV[i]/((1+F['sV'][i]/kap)*Ps[i]),Ps[i],PV[i]))
