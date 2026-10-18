"""Blow-up law of the constrained evolution (Paper F, Sec. 'What limits the window'): first non-finite sample v on the ray U~1 against v_b = 205.25 + (2/kappa_+) ln(1.5e-4/(B h_v)).
usage: vb_law.py json [json ...]   (anisotropic runs; the first non-finite sample is at integer v)"""
import sys, json, math, numpy as np
kp=0.04896874208903945
for fn in sys.argv[1:]:
    d=json.load(open(fn)); v=np.array(d['vq']); B=d['B']
    print(fn,'B=%g'%B)
    for h in sorted((float(x) for x in d['data']),reverse=True):
        s=np.array(d['data'][repr(h) if repr(h) in d['data'] else str(h)]['sV'][2]); bad=np.where(~np.isfinite(s))[0]
        law=205.25+2/kp*math.log(1.5e-4/(B*h))
        print('   h_v=%-10g first non-finite sample: %s   law: %.1f'%(h,('%g'%v[bad[0]]) if len(bad) else '> %g (none)'%v[-1],law))
