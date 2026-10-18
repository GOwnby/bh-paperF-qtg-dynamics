"""Balance rho_v = -kappa_- rho + S on the evolved solution (Paper F): from the extrapolated ray data (U~1) form rho=-r_v, Phi=phi_v, S=4 pi r c1(psi) Phi^2 and compare
dln(rho)/dv (central difference, dv=2) with S/rho - kappa_-  and with sigma_v and with 2 dln|Phi|/dv.  usage: balance_check.py json kappa_minus [ray]"""
import os, sys, json, numpy as np
sys.path.insert(0,os.environ.get('QTG_CODE','..')); from qtg_lib import coef
fn=sys.argv[1]; kap=float(sys.argv[2]); n=int(sys.argv[3]) if len(sys.argv)>3 else 2
d=json.load(open(fn)); v=np.array(d['vq']); hl=sorted((float(h) for h in d['data']),reverse=True)
D={h:d['data'][repr(h) if repr(h) in d['data'] else str(h)] for h in hl}
vb={h:(v[np.where(~np.isfinite(np.array(D[h]['sV'][n])))[0][0]] if np.any(~np.isfinite(np.array(D[h]['sV'][n]))) else 1e9) for h in hl}
def rom(nm,K):
    lv=hl[-K:]; T=[[np.array(D[h][nm][n]) for h in lv]]
    for lev in range(1,K): T.append([(4**lev*T[-1][i+1]-T[-1][i])/(4**lev-1) for i in range(len(T[-1])-1)])
    return T[-1][0]
print('file',fn,'kappa_-=',kap,'ray U=%.3f'%d['Uq'][n])
print('   v   K  dln(rho)/dv  S/rho-kappa   diff      sigma_v     2dln|Phi|/dv   ')
for vv in range(100,int(v[-1])-6,20):
    K=next((K for K in (4,3,2) if all(vb[h]>=vv+30 for h in hl[-K:])),None)
    if K is None: continue
    F={nm:rom(nm,K) for nm in ('r','sg','rs','rv','PV','sV')}
    j=int(np.argmin(abs(v-vv))); W=np.exp(F['sg']); y=-F['rs']/W; rho=-F['rv']; psi=(1+4*y*rho)/F['r']**2
    c1=np.array([float(coef(1,1.0,p)[1]) for p in psi[j-2:j+3]]); Sx=4*np.pi*F['r'][j-2:j+3]*c1*F['PV'][j-2:j+3]**2
    dl=(np.log(rho[j+1])-np.log(rho[j-1]))/2; bal=Sx[2]/rho[j]-kap; dP=(np.log(abs(F['PV'][j+1]))-np.log(abs(F['PV'][j-1])))
    print('%5d  %d  %+.6f   %+.6f   %+.1e   %+.6f   %+.6f'%(vv,K,dl,bal,dl-bal,F['sV'][j],dP))
