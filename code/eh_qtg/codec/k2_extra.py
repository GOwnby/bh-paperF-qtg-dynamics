"""Numbers of the k=2 code-E runs quoted in the text of Paper F, Sec. collapse (not in an_k.py): front time on the four rays (first v with z below half its value at v=45), K and the local slope of K at v=1400 on U~1,
the fit  slope = a + c/v  to the slope of the b=1 run for 1000 <= v <= 1450 (ray U~1), and the interior at v=40 (generalized mass and radius, before the front).
usage: python3 k2_extra.py ce/genc_np1_hs0.2_hv0.2_v1500.json ce/genc_np01_hs0.2_hv0.2_v1500.json"""
import sys, os, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from front import load
for fn in sys.argv[1:]:
    print(os.path.basename(fn))
    for n in range(4):
        d, v, A = load(fn, n)
        zs = A['z'][np.argmin(abs(v - 45))]
        vf = v[np.argmax(A['z'] < 0.5 * zs)]
        j = np.argmin(abs(v - 1400))
        j40 = np.argmin(abs(v - 40))
        print('  ray %d U=%.4f front v=%.0f  K(1400)=%.3e  m(v=40)=%.4f r(v=40)=%.5f' % (n, d['Uq'][n], vf, A['K'][j], A['m'][j40], A['r'][j40]))
    d, v, A = load(fn, 2)
    sel = [j for j in range(50, len(v) - 50) if 1000 <= v[j] <= 1450]
    sl = np.array([np.log(A['K'][j + 50] / A['K'][j - 50]) / np.log(v[j + 50] / v[j - 50]) for j in sel])
    X = np.vstack([np.ones(len(sel)), 1.0 / v[sel]]).T
    a, c = np.linalg.lstsq(X, sl, rcond=None)[0]
    print('  fit slope = a + c/v on 1000<=v<=1450 (ray 2): a=%.3f c=%.0f' % (a, c))
