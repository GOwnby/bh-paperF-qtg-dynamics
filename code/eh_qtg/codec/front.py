import sys,json,numpy as np,os
sys.path.insert(0,os.environ['QTG_CODE'])
from qtg_lib import coef
def load(fn,n,hv=None):
    d=json.load(open(fn)); hv=hv or list(d['data'])[-1]; F={a:np.array(b[n],float) for a,b in d['data'][hv].items() if a not in('nan','mon')}
    v=np.array(d['vq']); r,sg,rs,rv,Ps,PV,sV=[F[x] for x in ('r','sg','rs','rv','Ps','PV','sV')]
    W=np.exp(sg); y=-rs/W; rho=-rv; z=(r**2-1-4*y*rho)/r**2; psi=1-z
    Q,c1,c2,c3=[np.array(a) for a in coef(1,1.0,psi)]; g=Ps*PV/W
    Sig=psi/2-c2-8*np.pi*c1*g+64*np.pi**2*c3*g**2; H=128*np.pi**2*c1**2*g**2+Q**2/2
    K=(4*Sig)**2+8*H+4*psi**2; m=r**3*psi/(2*z)
    return d,v,dict(z=z,m=m,K=K,sV=sV,r=r,Ps=Ps,PV=PV)
if __name__=='__main__':
    for fn in sys.argv[1:]:
        for n in range(4):
            d,v,A=load(fn,n); zs=A['z'][np.argmin(abs(v-45))]
            i=np.argmax(A['z']<0.5*zs) ; vf=v[i]
            j=np.argmin(abs(v-1400)); a,b=j-50,j+50
            lk=np.log(A['K'][b]/A['K'][a])/np.log(v[b]/v[a])
            print(os.path.basename(fn)[:22],'ray',n,'U=%.3f'%d['Uq'][n],'front(z<half of v=45 value) v=%.0f'%vf,' v*sV(1400)=%.3f'%(v[j]*A['sV'][j]),' K(1400)=%.3e slope=%.3f m(1400)=%.1f'%(A['K'][j],lk,A['m'][j]))
