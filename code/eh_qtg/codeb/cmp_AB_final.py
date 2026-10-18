"""Code A (2nd order, Richardson-Romberg in hv^2, hs->0 by 2-point extrapolation) vs code B (4th order, hs=0.05, hv=0.05 [and 0.1]) at U~1 (ray 2), v1=400 data."""
import json,numpy as np
n=2
def Aseries(fn,nm):
    d=json.load(open(fn)); v=np.array(d['vq']); hl=sorted((float(h) for h in d['data']),reverse=True)
    D={h:d['data'][repr(h) if repr(h) in d['data'] else str(h)] for h in hl}
    vb={h:(v[np.where(~np.isfinite(np.array(D[h]['sV'][n])))[0][0]] if np.any(~np.isfinite(np.array(D[h]['sV'][n]))) else 1e9) for h in hl}
    out=np.full(len(v),np.nan)
    for j,vv in enumerate(v):
        for K in (4,3,2):
            lv=hl[-K:]
            if len(lv)==K and all(vb[h]>=vv+30 for h in lv):
                T=[[np.array(D[h][nm][n])[j] for h in lv]]
                for lev in range(1,K): T.append([(4**lev*T[-1][i+1]-T[-1][i])/(4**lev-1) for i in range(len(T[-1])-1)])
                out[j]=T[-1][0]; break
    return v,out
B=json.load(open('data/genb_hs0.05_v400.json')); vB=np.array(B['vq'])
print('A hs=0.05/0.025 Uq',json.load(open('../data/genq2_hs0.05_m1_B0.003_k1.5_v400.json'))['Uq'][n],'B Uq',B['Uq'][n])
for nm in ['r','sV','PV','Ps','rs','rv']:
    v1,g1=Aseries('../data/genq2_hs0.05_m1_B0.003_k1.5_v400.json',nm); v2,g2=Aseries('../data/genq2_hs0.025_m1_B0.003_k1.5_v400.json',nm)
    g0=g2+(g2-g1)/3
    row=[]
    for v in (40,60,100,150,200,250,300):
        i=np.argmin(abs(v1-v)); j=np.argmin(abs(vB-v)); b=np.array(B['data']['0.05'][nm][n])[j]; b2=np.array(B['data']['0.1'][nm][n])[j]
        row.append('%d: A05=%.1e A0=%.1e B.1-B.05=%.0e'%(v,abs(g1[i]-b)/abs(b),abs(g0[i]-b)/abs(b),abs(b2-b)/abs(b)))
    print(nm); print('   '+'\n   '.join(row))
