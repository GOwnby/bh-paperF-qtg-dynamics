"""PDE-only slaving test (Paper F): on the ray U~1 of an anisotropic run, sigma_v against dln(rho)/dv (rho=-r_v) and 2 dln|Phi|/dv (Phi=phi_v), Romberg in h_v^2 over the finest K<=4 levels
finite 30 units of v beyond the point; also y*rho/beta with beta=(psi r^2-1)/4 and z*m with m=r^3 psi/(2z).  usage: slaving_pde.py json"""
import os, sys, json, numpy as np
fn=sys.argv[1]; n=2; d=json.load(open(fn)); v=np.array(d['vq']); hl=sorted((float(h) for h in d['data']),reverse=True)
D={h:d['data'][repr(h) if repr(h) in d['data'] else str(h)] for h in hl}
vb={h:(v[np.where(~np.isfinite(np.array(D[h]['sV'][n])))[0][0]] if np.any(~np.isfinite(np.array(D[h]['sV'][n]))) else 1e9) for h in hl}
def rom(nm,K,j):
    lv=hl[-K:]; T=[[np.array(D[h][nm][n])[j] for h in lv]]
    for lev in range(1,K): T.append([(4**lev*T[-1][i+1]-T[-1][i])/(4**lev-1) for i in range(len(T[-1])-1)])
    return T[-1][0],T[-2][1]
print(fn,'levels',hl,'first non-finite per level',[vb[h] for h in hl],'ray U=%.3f'%d['Uq'][n])
print('   v  K  sigma_v     err     dln(rho)/dv  sigma_v-dln(rho)/dv   2dln|Phi|/dv     z        z*m     r')
for vv in range(60,int(v[-1]),10):
    K=next((K for K in (4,3,2) if all(vb[h]>=vv+30 for h in hl[-K:])),None)
    if K is None: continue
    j=np.array([int(np.argmin(abs(v-vv)))+o for o in (-1,0,1)]); F={nm:rom(nm,K,j) for nm in ('sV','rv','PV','r','sg','rs')}
    sV,e=F['sV']; rv=F['rv'][0]; PV=F['PV'][0]; r=F['r'][0]; W=np.exp(F['sg'][0]); y=-F['rs'][0]/W; psi=(1+4*y*(-rv))/r**2; z=1-psi; m=r**3*psi/(2*z)
    dl=(np.log(-rv[2])-np.log(-rv[0]))/2; dP=(np.log(abs(PV[2]))-np.log(abs(PV[0])))
    print('%4d  %d  %+.5f  %.0e   %+.5f      %+.2e         %+.5f   %.3e  %.4f  %.6f'%(vv,K,sV[1],abs(sV[1]-e[1]),dl,sV[1]-dl,dP,z[1],z[1]*m[1],r[1]))
