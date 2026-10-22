"""Charges behind two statements of Sec. 'Collapse-generated horizon tails' (Paper F).  NEW FILE (not in the author's original archive): a thin driver that calls
only functions of the original modules (pipeline.py, collapse_lib.py, runL.py, linear_q.py conventions) and reads B from logs/ascale.log.

 (1) B/(8 m |Q|) for A/A0 = 0.8 ... 1.2, with the charge of the data Q = int r^2 phi_v dv on the ray u = u0 and the mass m of the hole,
     computed exactly as linear_q.py does (Q and m do not need an evolution).  At A/A0 = 0.8, 1.0, 1.2 these are the numbers of logs/linear_q.log
     (Q = -1.49525, -1.70606, -1.81036); A/A0 = 0.9 and 1.1 are not in that log.
 (2) the charge Q_row = int r^2 phi_u du of the exterior part (r > r_+(m)) of the row v = 60 of stage N (pulse of A/A0 on the default grid U_END = 29.5, h = 0.1),
     and B/(8 m |Q_row|).
usage: python3 ascale_q.py            (about 10 s)   Output: logs/ascale_q.log"""
import sys, re, os
sys.path.insert(0, '.')
import numpy as np
import pipeline as P
from pipeline import *
from runL import *
A0 = 0.030030088            # the value used by ascale.py
A0Q = 0.0300301             # the value used by linear_q.py
Bs = {}
for ln in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs', 'ascale.log')):
    mt = re.match(r'A/A0=([0-9.]+) A=([0-9.]+) m=([0-9.]+)\s+B\(k=3\)=([0-9.]+)', ln)
    if mt: Bs[round(float(mt.group(1)), 2)] = float(mt.group(4))
print('(1) data charge, linear_q.py convention (model 1, h = 0.1, U_END = %.1f)' % P.UEND)
print('%6s %10s %9s %10s %12s %10s %14s' % ('A/A0', 'A', 'm', 'Q', '8m|Q|', 'B(ascale)', 'B/(8m|Q|)'))
res = {}
for f in (0.8, 0.9, 1.0, 1.1, 1.2):
    A = A0Q * f
    u, v, row0, col0, ph = rays(1, 1.0, P.U0, P.UEND, P.V0, P.V0 + 2000.0, 0.1, 0.1, A, P.VA, P.VB)   # as linear_q.py (vmax = 2000; Q does not depend on it)
    r = col0[0]; m = ms_mass(1, 1.0, col0[0], col0[1], col0[2], col0[3])[-1]
    Q = np.trapezoid(r ** 2 * col0[7], v)
    res[f] = (m, Q)
    print('%6.2f %10.7f %9.5f %10.5f %12.4f %10.4f %14.4f' % (f, A, m, Q, 8 * m * abs(Q), Bs[f], Bs[f] / (8 * m * abs(Q))))
print()
print('(2) charge of the exterior part of the row v = 60 (stage N, h = 0.1, U_END = %.1f); r > r_+(m)' % P.UEND)
print('%6s %9s %9s %10s %14s' % ('A/A0', 'm', 'r_+', 'Q_row', 'B/(8m|Q_row|)'))
for f in (0.8, 0.9, 1.0, 1.1, 1.2):
    A = A0 * f
    m = mass_u0(1, 1.0, A)
    u, v, snap, out, ah = stageN(1, 1.0, A, 0.1, 60.0)
    R, SG, RU, RV, SU, SV, PU, PV = [np.asarray(x) for x in snap[0]]
    bg = Static(1, m, 1.0)
    ok = np.isfinite(R) & np.isfinite(PU) & (R > bg.rp)
    Qrow = np.trapezoid((R ** 2 * PU)[ok], u[ok])
    print('%6.2f %9.4f %9.4f %10.4f %14.3f' % (f, m, bg.rp, Qrow, Bs[f] / (8 * m * abs(Qrow))))
