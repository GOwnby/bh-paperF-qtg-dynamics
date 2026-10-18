"""Slaving test for the bounded h (Paper F, Section 'slaving'): sigma_v against dln(rho)/dv and 2 dln|Phi|/dv on the ray U~1 of the extrapolated bounded-h runs (alpha=1, m=1.5, k=3/2).
usage: bounded_slaving.py json [json ...]"""
import sys, json, numpy as np
for fn in sys.argv[1:]:
    d=json.load(open(fn)); v=np.array(d['vq']); hl=sorted((float(h) for h in d['data']),reverse=True); n=2
    D={h:d['data'][repr(h) if repr(h) in d['data'] else str(h)] for h in hl}
    def rom(nm,K=4):
        lv=hl[-K:]; T=[[np.array(D[h][nm][n]) for h in lv]]
        for lev in range(1,K): T.append([(4**lev*T[-1][i+1]-T[-1][i])/(4**lev-1) for i in range(len(T[-1])-1)])
        return T[-1][0]
    print(fn,'levels',hl,'B',d['B'],'ray U=%.3f'%d['Uq'][n]); sV=rom('sV'); PV=rom('PV'); rv=rom('rv')
    print('    v   sigma_v   dln(rho)/dv   sigma_v-dln(rho)/dv   2dln|Phi|/dv')
    for vv in (60,65,70,75,80,85,90,95):
        j=int(np.argmin(abs(v-vv))); dl=(np.log(-rv[j+1])-np.log(-rv[j-1]))/2; dP=(np.log(abs(PV[j+1]))-np.log(abs(PV[j-1])))
        print('  %4d  %+.5f   %+.5f      %+.2e          %+.5f'%(vv,sV[j],dl,sV[j]-dl,dP))
