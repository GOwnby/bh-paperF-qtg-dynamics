"""A priori estimates of the absorbed charge against the exact one (Paper F, Sec. collapse; logs/sp/eik_summary.log).  Reads the output of eik_test.py (sp/eik_test.log) and prints, per table,
F_abs = 1-Q_abs/Q_0 (horizon column of stage N), the measured F, the eikonal estimate F_eik (psi = r phi carried along the ingoing rays, true horizon radius), the Vaidya-eikonal estimate F_V
(horizon from dr/dv = f(r,m(v))/2 backwards) and the ratio of the horizon radii at the start, V/true.   usage: python3 eik_summary.py eik_test.log"""
import sys, re, numpy as np
rows = []
pend = {}
for l in open(sys.argv[1]):
    m = re.match(r'\s+Vaidya-eikonal: r_H\(v0\) (\S+) \(true (\S+)\);.*F_V=(\S+) ;', l)
    if m:
        pend = dict(rV=float(m.group(1)), rT=float(m.group(2)), FV=float(m.group(3)))
        continue
    m = re.match(r'\s+eikonal: .* F_eik=(\S+)', l)
    if m:
        pend['Feik'] = float(m.group(1))
        continue
    m = re.match(r'(\S+\.npz)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)', l)
    if m and pend:
        rows.append((m.group(1), float(m.group(2)), float(m.group(3)), float(m.group(10)), float(m.group(11)), pend['Feik'], pend['FV'], pend['rV'] / pend['rT']))
        pend = {}
print('A priori estimates of F from the initial data of the pulse (u0): F_eik (psi=r phi conserved along ingoing rays, true horizon radius), F_V (also the horizon from dr/dv=f(r,m(v))/2 backwards)')
print('%-24s %4s %6s %7s %7s %7s %7s %s' % ('table', 'm0', 'm_f', 'F_abs', 'F_meas', 'F_eik', 'F_V', 'rH0 V/true'))
for r in rows:
    print('%-24s %4g %6.2f %7.4f %7.4f %7.4f %7.4f %9.4f' % r)
a = np.array([r[3] for r in rows])
e = np.array([r[5] for r in rows]) / a - 1
v = np.array([r[6] for r in rows]) / a - 1
print('F_eik/F_abs-1: mean %.4f, max|.| %.4f ; F_V/F_abs-1: mean %.4f, max|.| %.4f, rms %.4f' % (e.mean(), abs(e).max(), v.mean(), abs(v).max(), np.sqrt((v ** 2).mean())))
