"""Search for the seed of the late-time departure of code E (Paper F, Sec. 'The seed of the late-time departure, and the range of code E').
Regenerates the experiments of codee/logs/seed_search.log with the shipped gen_e.py construction: v1 = 950, B = 3e-3, k = 3/2, m = 5, hs = 0.2, hv = 0.1, ray U = 0.9968;
the printed entries are v*sigma_v at v = 500, 600, 650, 700, 740, 780.

  (1) integrator tolerances of the horizon column (shooting DOP853 rtol / rtol of sigma, sigma_U, phi_U and of the transverse integration): default (1e-13 / 1e-12),
      loose (1e-11 / 1e-10), tight (2.3e-14 / 2.3e-14), each with the former initial row  Delta_0 = zz + (r_+ - r_H(0));
  (2) the fields of the horizon column of the default run replaced, one group at a time, by those of the tight run;
  (3) the initial row of the tight run with the default column (= the tight run);
  (4) Delta_0 = zz + EPS with EPS = 0 (the corrected row of gen_e.py), 3e-15 and 3.55e-15;
  (5) perturbation of sigma_U^H or phi_U^H by 1e-12 (these channels are not used by the evolution).
usage: python3 seed_search.py [v1]            (about 20 runs of code E, 1-5 min each: part of --full of verify.py)
Run it in this directory (needs libqtge.so from ../setup.sh)."""
import os, sys, numpy as np, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0, '..')
import dnU_qtg
from dnU_qtg import *
from gen_e import run_B

_orig_solve = dnU_qtg.solve_ivp
_R1 = [1e-13]


def _solve(*a, **k):                      # the shooting integration of horizon_q has rtol = 1e-13 hard-wired: redirect it
    if k.get('rtol') == 1e-13:
        k = dict(k, rtol=_R1[0])
    return _orig_solve(*a, **k)


dnU_qtg.solve_ivp = _solve

v1 = float(sys.argv[1]) if len(sys.argv) > 1 else 950.0
model, L2, B, k, hs, hv = 1, 1.0, 3e-3, 1.5, 0.2, 0.1
S = StaticU(5.0)
c = 0.2 * np.exp(-S.kp * v1)
U1 = 1.5
sq = [float(np.round(np.log(1 + x * S.kp / c) / S.kp / 0.2) * 0.2) for x in [0.3, 0.6, 1.0, 1.2]]
cols = [int(round(s / hs)) for s in sq]
VS = [500, 600, 650, 700, 740, 780]
phv = lambda t: PHVF(k, B, t)
sQ = lambda r, rv: r * float(coef(model, L2, (1 - 2 * rv) / r ** 2)[0]) / 2


def build(R1, R2):
    _R1[0] = R1
    d = build_eh_q(S, model, L2, U1, v1, hs, hv / 2, B, k=k, c=c, vH=v1 + 300, rtol=R2)
    _R1[0] = 1e-13
    return d


def make_row(d, eps):
    """initial row of gen_e.py with Delta_0 = zz + eps (eps=None: the former construction eps = r_+ - r_H(0))"""
    row0 = d['row0'].copy()
    Ux = d['U']
    zz = np.where(Ux < 1.0, -Ux * S.w(Ux), row0[0] - S.rp)
    hz = d['hz']
    r0h, rv0 = hz.sol(0)
    off = (S.rp - r0h) if eps is None else eps
    row0[0] = zz + off
    sgv0 = sQ(r0h, rv0)

    def rhsD(t, Y):
        r, sg, rU, _, sUt, _ = [a[0] for a in S.fields(np.array([t]), 0.0)]
        a, b, c_ = Fq(model, L2, r, sg, rU, rv0 + Y[0], 0.0, Y[2])
        return [float(a), float(b), float(c_)]
    sD = _orig_solve(rhsD, [0, d['U'][-1]], [0.0, sgv0, phv(0)], t_eval=d['U'], method='DOP853', rtol=1e-13, atol=[1e-26, 1e-14, 1e-300])
    assert sD.success
    row0[3] = sD.y[0]
    return row0, off


def ev(row0, col0):
    out, mon = run_B(model, L2, np.ascontiguousarray(row0), np.ascontiguousarray(col0), hs, hv, cols)
    sv = out[2][:, 5]
    return [float(v * sv[int(round(v / hv))]) for v in VS]


def show(label, vals, nd=5):
    print('    %-34s: %s' % (label, ' '.join(('%.*f' % (nd, x)) for x in vals)), flush=True)


print('Search for the seed of the late-time departure of code E (Paper F); v1=%g, B=3e-3, k=3/2, m=5, hs=0.2, hv=0.1, ray U=0.9968.' % v1)
print('Entries: v*sigma_v at v = ' + ', '.join(str(v) for v in VS) + '.')
print()
print('(1) Integrator tolerances of the horizon column (shooting DOP853 rtol / sigma,sigma_U,phi_U rtol), former initial row:')
dD = build(1e-13, 1e-12)
rowD, offD = make_row(dD, None)
rD = ev(rowD, dD['col0'])
show('default (1e-13 / 1e-12)', rD)
dL = build(1e-11, 1e-10)
rowL, offL = make_row(dL, None)
show('loose   (1e-11 / 1e-10)', ev(rowL, dL['col0']), 4)
dT = build(2.3e-14, 2.3e-14)
rowT, offT = make_row(dT, None)
rT = ev(rowT, dT['col0'])
show('tight   (2.3e-14 / 2.3e-14)', rT)
cD, cT = dD['col0'], dT['col0']
rel = lambda a, b: float(np.max(np.abs(a - b) / np.maximum(np.abs(a), 1e-300)))
print('    r_+ - r_H(0): default %.3e, loose %.3e, tight %.3e' % (offD, offL, offT))
print('    Largest relative difference of the column fields between default and tight: r_H %.0e, sigma_H %.0e, sigma_v^H %.0e; r_v^H (absolute): %.0e at v=0, %.0e elsewhere; phi_v^H %.0e' % (
    rel(cD[0], cT[0]), rel(cD[1], cT[1]), rel(cD[5], cT[5]), abs(cD[3][0] - cT[3][0]), float(np.max(np.abs(cD[3][1:] - cT[3][1:]))), rel(cD[7], cT[7])))
print('(2) Replacing, one group at a time, the column channels of the default run by those of the tight run (default initial row):')
for lab, idx in (('r_H', [0]), ('sigma_H', [1]), ('r_U^H, sigma_U^H, phi_U^H', [2, 4, 6]), ('r_v^H', [3]), ('sigma_v^H', [5])):
    col = cD.copy()
    for i in idx:
        col[i] = cT[i]
    show(lab, ev(rowD, col))
print('(3) Initial row of the tight run with the default column; and of the default run with the tight column:')
show('tight row + default column', ev(rowT, cD))
show('default row + tight column', ev(rowD, cT))
print('    perturbing sigma_U^H or phi_U^H of the default column by 1e-12 (relative): largest change of v*sigma_v')
for i, nm in ((4, 'sigma_U^H'), (6, 'phi_U^H')):
    col = cD.copy()
    col[i] = col[i] * (1 + 1e-12)
    r = ev(rowD, col)
    print('    %-12s %.1e' % (nm, max(abs(a - b) for a, b in zip(r, rD))), flush=True)
print('(4) Delta_0 = zz + EPS, zz the static r - r_+ without cancellation, EPS = r_+ - r_H(0) (%.3e for the default run, 2 ulps of r_+ = %.3f):' % (offD, S.rp))
for eps, lab in ((0.0, 'EPS = 0       (corrected row)'), (3e-15, 'EPS = 3e-15'), (3.55e-15, 'EPS = 3.55e-15')):
    row, _ = make_row(dD, eps)
    show(lab, ev(row, cD))
