"""Comparison of code E with the independent code B (Paper F).  Reads data/ (this directory) and ../codeb/data/.  usage: python3 conv_e.py
E: hs=0.1, hv=0.05, ray U=0.99684 (v1=500, corrected initial row); B: hs=0.05, hv=0.0125, ray U=0.99928.  (The convergence of E in hs, hv, v1 and arithmetic is in conv_e2.py.)"""
import json,numpy as np
ld=lambda f: json.load(open(f))
Eb=ld('data/gene_p1_hs0.1_m1_B0.003_k1.5_v500_ray2.json'); Bj=ld('../codeb/data/genb_hs0.05_v600.json')
vE=np.array(Eb['vq']); vB=np.array(Bj['vq'])
g=lambda J,hv,nm,v,vv,n=0: np.array(J['data'][hv][nm][n])[int(np.argmin(abs(v-vv)))]
for vv in (100,140,180,220,260,300,340,380):
    out=[]
    for nm in ('sV','r','PV'):
        e=g(Eb,'0.05',nm,vE,vv); b=g(Bj,'0.0125',nm,vB,vv,2); out.append('%s: E=%.7g B=%.7g rel.diff=%.1e'%(nm,e,b,abs(e-b)/abs(b)))
    print('v=%3d  '%vv+' | '.join(out))
