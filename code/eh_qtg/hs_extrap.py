"""h_s-error of sigma_v (Paper F): sigma_v on U~1 from two anisotropic families (h_s = 0.05 and 0.025), each Romberg-extrapolated in h_v^2 over the finest levels that are finite
30 units of v beyond the point; then G(h_s->0) = G(0.025) + (G(0.025)-G(0.05))/3 (error O(h_s^2)).  Compared with the kernel prediction G_pred (Paper G kernel, kappa_-(m_f)).
usage: hs_extrap.py json_hs0.05 json_hs0.025 B k kappa_minus"""
import os, sys, json, numpy as np
f1,f2=sys.argv[1],sys.argv[2]; B=float(sys.argv[3]); k=float(sys.argv[4]); kap=float(sys.argv[5]); n=2
def series(fn,nm='sV'):
    d=json.load(open(fn)); v=np.array(d['vq']); hl=sorted((float(h) for h in d['data']),reverse=True)
    D={h:d['data'][repr(h) if repr(h) in d['data'] else str(h)] for h in hl}
    vb={h:(v[np.where(~np.isfinite(np.array(D[h]['sV'][n])))[0][0]] if np.any(~np.isfinite(np.array(D[h]['sV'][n]))) else 1e9) for h in hl}
    out=np.full(len(v),np.nan); Ks=np.zeros(len(v),int)
    for j,vv in enumerate(v):
        for K in (4,3,2):
            lv=hl[-K:]
            if len(lv)==K and all(vb[h]>=vv+30 for h in lv):
                T=[[np.array(D[h][nm][n])[j] for h in lv]]
                for lev in range(1,K): T.append([(4**lev*T[-1][i+1]-T[-1][i])/(4**lev-1) for i in range(len(T[-1])-1)])
                out[j]=T[-1][0]; Ks[j]=K; break
    return v,out,Ks
v1,G1,K1=series(f1); v2,G2,K2=series(f2)
import kernel_lib as KL
vs=np.arange(20,3000.5,0.5); dv=0.5; Phi=np.array([KL.phi_v(float(x),k,B) for x in vs]); S=Phi**2
rho=np.zeros_like(vs); r_=0.0; e=np.exp(-kap*dv)
for i in range(1,len(vs)):
    a,b=S[i-1],S[i]; I=a*(1-e)/kap+(b-a)/dv*((dv-(1-e)/kap)/kap); r_=r_*e+I; rho[i]=r_
Gk=S/np.maximum(rho,1e-300)-kap
print('B=%g k=%g kappa_-=%g'%(B,k,kap)); print('   v   G(hs=.05)   G(hs=.025)   G(hs->0)    G_kernel    G(hs->0)-G_kernel   rel      v*G(hs->0)  Ks')
for vv in range(100,int(min(v1[-1],v2[-1]))-5,10):
    j1=int(np.argmin(abs(v1-vv))); j2=int(np.argmin(abs(v2-vv)))
    if not (np.isfinite(G1[j1]) and np.isfinite(G2[j2])): continue
    G0=G2[j2]+(G2[j2]-G1[j1])/3; gk=Gk[int(round((vv-20)/dv))]
    print('%5d  %+.6f  %+.6f  %+.6f  %+.6f   %+.2e   %+.4f   %+.3f   %d/%d'%(vv,G1[j1],G2[j2],G0,gk,G0-gk,(G0-gk)/gk,vv*G0,K1[j1],K2[j2]))
