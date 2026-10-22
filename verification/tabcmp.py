"""Compare the regenerated collapse tables tail_m{0,1}_v60_h05.npz with the shipped ones (maximum relative difference of every array).  usage: python3 tabcmp.py <new dir> <shipped dir>"""
import sys, os, numpy as np
for m in (0, 1):
    fn = 'tail_m%d_v60_h05.npz' % m
    a, b = np.load(os.path.join(sys.argv[1], fn)), np.load(os.path.join(sys.argv[2], fn))
    for k in sorted(set(a.files) & set(b.files)):
        x, y = np.asarray(a[k], float), np.asarray(b[k], float)
        sc = np.max(np.abs(y)) or 1.0
        if x.dtype.kind not in 'fiu':
            continue
        print('%s %-8s max |new - shipped| / max|shipped| = %.2e' % (fn, k, np.max(np.abs(x - y)) / sc if x.size else 0.0))
    print('%s arrays only in the regenerated table: %s; only in the shipped table: %s' % (fn, sorted(set(a.files) - set(b.files)), sorted(set(b.files) - set(a.files))))
