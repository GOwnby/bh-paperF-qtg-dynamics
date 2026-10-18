"""Bounded h (alpha=1, m=1.5, B=3e-4, k=3/2) from the anisotropic run (h_s=0.05, h_v halved; Paper F Sec. 'bounded'): first non-finite sample per level (shift per halving = ln4/kappa_+ = 8.59),
sigma_v on U~1 (Romberg in h_v^2 over the finest K<=4 levels finite 10 units of v beyond the point), dln(rho)/dv, 2dln|Phi|/dv.  usage: bounded_aniso.py json"""
import sys, json, numpy as np
fn=sys.argv[1]; d=json.load(open(fn)); v=np.array(d['vq']); hl=sorted((float(h) for h in d['data']),reverse=True); n=2
D={h:d['data'][repr(h) if repr(h) in d['data'] else str(h)] for h in hl}; vb={}
for h in hl:
    s=np.array(D[h]['sV'][n]); bad=np.where(~np.isfinite(s))[0]; vb[h]=v[bad[0]] if len(bad) else 1e9; print('h_v=%-10g first non-finite sample v=%g'%(h,vb[h]))
def rom(nm,K,j):
    lv=hl[-K:]; T=[[np.array(D[h][nm][n])[j] for h in lv]]
    for lev in range(1,K): T.append([(4**lev*T[-1][i+1]-T[-1][i])/(4**lev-1) for i in range(len(T[-1])-1)])
    return T[-1][0],T[-2][1]
print('   v  K  sigma_v     err    dln(rho)/dv  sigma_v-dln(rho)/dv  2dln|Phi|/dv')
for vv in range(60,int(v[-1]),5):
    K=next((K for K in (4,3,2) if all(vb[h]>=vv+10 for h in hl[-K:])),None)
    if K is None: continue
    j=np.array([int(np.argmin(abs(v-vv)))+o for o in (-1,0,1)])
    sV,e=rom('sV',K,j); rv,_=rom('rv',K,j); PV,_=rom('PV',K,j)
    dl=(np.log(-rv[2])-np.log(-rv[0]))/2; dP=(np.log(abs(PV[2]))-np.log(abs(PV[0])))
    print('%4d  %d  %+.5f  %.0e   %+.5f      %+.2e          %+.5f'%(vv,K,sV[1],abs(sV[1]-e[1]),dl,sV[1]-dl,dP))
