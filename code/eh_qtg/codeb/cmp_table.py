"""Paper F, Sec. 'A second implementation': (1) sigma_v of code A (Table of Sec. endpoint, merged 8-level Romberg, h_s=0.05) vs code B (h_s=0.05, h_v=0.0125) with the h_s correction;
(2) first non-finite v of code B for each h_v (constrained, and the unconstrained PROJ=0 version)."""
import json,numpy as np
B=json.load(open('data/genb_hs0.05_v600.json')); vB=np.array(B['vq']); sB=np.array(B['data']['0.0125']['sV'][2])
B25=json.load(open('data/genb_hs0.05_v480.json')); s25=np.array(B25['data']['0.025']['sV'][2])
tab={100:-0.094251,120:-0.087733,140:-0.079755,160:-0.068968,180:-0.056255,200:-0.043998,220:-0.034253,240:-0.027494,260:-0.023090,280:-0.020206,300:-0.018223}  # Table 'tab:end' (endpoint_B0.003_merged.log)
print(' v   sigma_v(A)   A+1.6e-4   sigma_v(B,hv=.0125)   B-(A+1.6e-4)   B(.0125)-B(.025)')
for v,a in tab.items():
    i=int(np.argmin(abs(vB-v))); print('%4d  %+.6f   %+.6f   %+.6f   %+.1e   %+.1e'%(v,a,a+1.6e-4,sB[i],sB[i]-(a+1.6e-4),sB[i]-s25[i]))
print('first non-finite v of sigma_v on ray 2 (constrained):')
for f in ['data/genb_hs0.05_v360_hv.json','data/genb_hs0.05_v400.json','data/genb_hs0.05_v480.json','data/genb_hs0.05_v600.json']:
    d=json.load(open(f)); v=np.array(d['vq'])
    for hv,dd in d['data'].items():
        s=np.array(dd['sV'][2],float); bad=np.where(~np.isfinite(s))[0]; print('  %s hv=%s : %s (grid end %g)'%(f.split('/')[-1],hv,v[bad[0]] if len(bad) else 'none',v[-1]))
print('unconstrained (PROJ=0):')
for f in ['data/genb_p0_a.json','data/genb_p0_b.json']:
    d=json.load(open(f)); v=np.array(d['vq'])
    for hv,dd in d['data'].items():
        s=np.array(dd['sV'][2],float); bad=np.where(~np.isfinite(s))[0]; print('  hv=%s : %s'%(hv,v[bad[0]] if len(bad) else 'none'))
