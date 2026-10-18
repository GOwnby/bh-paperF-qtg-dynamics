"""Prediction of sigma_v behind the front from the linear kernel (Paper F).  Behind the front rho=-r_v is independent of u and slaved to the interior flux Phi(v)=phi_v:
   rho_v = -kappa_- rho + S,  S = 4 pi r c1_II Phi^2   =>   G(v) = sigma_v = rho_v/rho = S/rho - kappa_-   (the amplitudes cancel).
Phi is the kernel flux of Paper G (kernel_lib.phi_v).  usage: gpred_q.py B k kappa_minus json [json ...]   (json: anisotropic runs; finest levels K=3 or 4)"""
import sys, json, numpy as np
B=float(sys.argv[1]); k=float(sys.argv[2]); kap=float(sys.argv[3]); fns=sys.argv[4:]
sys.argv=[sys.argv[0]]
import kernel_lib as KL
vs=np.arange(20,2000.5,0.5); dv=0.5
Phi=np.array([KL.phi_v(float(v),k,B) for v in vs]); S=Phi**2
rho=np.zeros_like(vs); r=0.0; e=np.exp(-kap*dv)
for i in range(1,len(vs)):
    a,b=S[i-1],S[i]; I=a*(1-e)/kap+(b-a)/dv*((dv-(1-e)/kap)/kap); r=r*e+I; rho[i]=r
Gk=S/np.maximum(rho,1e-300)-kap
print('B=%g k=%g kappa_-=%.4f   kappa_+=%.8f'%(B,k,kap,KL.kp))
print('asymptotics: G*v -> -(2k+2)=%.3f'%(-(2*k+2)))
def romb(arr):
    T=[arr]
    for lev in range(1,len(arr)): T.append([(4**lev*T[-1][i+1]-T[-1][i])/(4**lev-1) for i in range(len(T[-1])-1)])
    return T
rows={}
for fn in fns:
    d=json.load(open(fn)); v=np.array(d['vq']); hl=sorted((float(h) for h in d['data']),reverse=True)
    for K in (3,4):
        if len(hl)<K: continue
        lv=hl[-K:]; g=lambda nm:[np.array(d['data'][repr(h) if repr(h) in d['data'] else str(h)][nm][2]) for h in lv]
        T=romb(g('sV')); P=romb(g('PV'))
        rows[(fn,K)]=(v,T[-1][0],np.abs(T[-1][0]-T[-2][0]),P[-1][0])
print('   v    G_pde(K=4)  err    G_pde(K=3)  err    G_pred(kernel)   G_pred*v   Phi_pde/Phi_kernel')
for vv in (100,120,150,180,200,220,240,250,260,270,280,300,320,340,360,400,600,1000,2000):
    i=int(round((vv-20)/dv)); s='%5d '%vv
    cols=[]
    for K in (4,3):
        val=None
        for (fn,KK),(v,G,err,PV) in rows.items():
            if KK==K and vv<=v[-1]-1:
                j=int(np.argmin(abs(v-vv)))
                if np.isfinite(G[j]): val=(G[j],err[j],PV[j])
        cols.append(val)
    pdeS=''.join('%+.6f %.0e  '%(c[0],c[1]) if c else '   --         --  ' for c in cols)
    ph=[c[2] for c in cols if c]; rat=ph[0]/Phi[i] if ph else float('nan')
    print(s+pdeS+'%+.6f  %+.3f   %.5f'%(Gk[i],Gk[i]*vv,rat))
