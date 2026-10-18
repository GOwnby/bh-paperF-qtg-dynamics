"""Mesh check of the scan: two code-E runs of the same pulse (e.g. hv=0.2 and hv=0.1, or hs=0.2 and hs=0.1) on every ray: max over the rays of the change of ln K, sigma_v,
r and ln m at v=100,200,400,800.   usage: pscan_conv.py coarse.json fine.json  (run from codec/sc)"""
import sys,json,os,numpy as np
sys.path.insert(0,os.environ['QTG_CODE']); from qtg_lib import coef
def fields(d,n):
    hv=list(d['data'].keys())[-1]
    F={a:np.array(b[n],float) for a,b in d['data'][hv].items() if a not in('nan','mon')}
    r,sg,rs,rv,Ps,PV,sV=[F[x] for x in ('r','sg','rs','rv','Ps','PV','sV')]
    W=np.exp(sg); y=-rs/W; rho=-rv; z=(r**2-1-4*y*rho)/r**2; psi=1-z
    Q,c1,c2,c3=[np.array(a) for a in coef(1,1.0,psi)]; g=Ps*PV/W
    Sig=psi/2-c2-8*np.pi*c1*g+64*np.pi**2*c3*g**2; H=128*np.pi**2*c1**2*g**2+Q**2/2
    return dict(K=(4*Sig)**2+8*H+4*psi**2,m=r**3*psi/(2*z),r=r,sV=sV)
A=json.load(open(sys.argv[1])); B=json.load(open(sys.argv[2])); vA=np.array(A['vq']); vB=np.array(B['vq'])
nr=min(len(list(A['data'].values())[-1]['r']),len(list(B['data'].values())[-1]['r']))
print('rays',nr,' columns: max over rays of |dlnK|, |dsigma_v|, |dr|, |dlnm|')
for vv in (100,200,400,800):
    iA=int(np.argmin(abs(vA-vv))); iB=int(np.argmin(abs(vB-vv))); out=[0,0,0,0]
    for n in range(nr):
        a=fields(A,n); b=fields(B,n)
        out=[max(out[0],abs(np.log(a['K'][iA]/b['K'][iB]))),max(out[1],abs(a['sV'][iA]-b['sV'][iB])),max(out[2],abs(a['r'][iA]-b['r'][iB])),max(out[3],abs(np.log(a['m'][iA]/b['m'][iB])))]
    print('v=%4d  %.2e %.2e %.2e %.2e'%(vv,*out))
