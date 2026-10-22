#!/usr/bin/env python3
"""Exact / symbolic / multi-precision verification of the algebraic statements of Paper F (sympy + mpmath).  No numerical PDE solution is involved.
usage: python3 sym_checks.py > sym_checks.log            (about 20 s)

Statements checked (section of main.tex):
  S2  the static solution: h(psi) = 2m/r^3 with psi = (1-f)/r^2 for the Hayward metric f = 1 - 2 m r^2/(r^3 + 2 m l^2); 1 - l^2 psi = r^3/(r^3+2 m l^2); f' = r Q(psi) with
      Q = 3h/h' - 2 psi for the Hayward and the bounded h; Q = psi (1 - 3 l^2 psi) for Hayward; Misner-Sharp mass M = m r^3/(r^3 + 2 m l^2).
  S2  static numbers (50 digits): r_- = 1.057475, r_+ = 9.897927, kappa_- = 0.795649, Q(1/r_-^2) = -1.5048, Q'(1/r_-^2) = -4.36 (Hayward, m = 5, l = 1);
      psi(r_-) = 0.8376 for the bounded h (m = 1, alpha = 1).
  S4(c) integrability: c Q' - c = c' (Q + 2 psi), c = 4 pi/h', for a generic function h (symbolic), and both sides = 4 pi (1 - 3 h h''/h'^2)/h'.
  S5  the mass law  d/dv [ r^3 h(psi)/2 ] = 8 pi r^2 y phi_v^2  and the psi_v equation (generic h; derived from r' = -rho, rho' = sigma_v rho + 4 pi r phi_v^2/h',
      y' = r Q/4 - sigma_v y, psi = (1 + 4 y rho)/r^2); sigma_v cancels.
  S7  invariant manifolds: psi_v = 3 rho psi z/r + 16 pi y phi_v^2 z^2/r (Hayward, z = 1 - l^2 psi); psi_v = 3 rho psi s^2/r + 16 pi y phi_v^2 s^3/r (bounded, s = sqrt(1-alpha^2 psi^2)).
  S7  the negative-mass pole of the Hayward metric: r^3 = 2|m| l^2, |m| = r_-^3/(2 l^2) = 0.59 and the change of m by about 5.6; m_f = r_f/[2(1 - l^2/r_f^2)] = r_f^3 h(r_f^-2)/2.
"""
import sympy as sp
import mpmath as mp

mp.mp.dps = 50
ok_all = True


def report(name, ok, detail=''):
    global ok_all
    ok_all = ok_all and bool(ok)
    print('%-92s %s %s' % (name, 'OK' if ok else 'FAILED', detail))


psi, r, m, l, a = sp.symbols('psi r m l alpha', positive=True)
print('== static solution (Section 2) ==')
f = 1 - 2 * m * r ** 2 / (r ** 3 + 2 * m * l ** 2)
ps = sp.simplify((1 - f) / r ** 2)
hH = lambda p: p / (1 - l ** 2 * p)
hpH = lambda p: sp.diff(hH(psi), psi).subs(psi, p)
report('Hayward: h(psi) = 2m/r^3 with psi = (1-f)/r^2', sp.simplify(hH(ps) - 2 * m / r ** 3) == 0)
report('Hayward: 1 - l^2 psi = r^3/(r^3 + 2 m l^2)', sp.simplify(1 - l ** 2 * ps - r ** 3 / (r ** 3 + 2 * m * l ** 2)) == 0)
report('Hayward: h\'(psi) = 1/(1 - l^2 psi)^2', sp.simplify(sp.diff(hH(psi), psi) - 1 / (1 - l ** 2 * psi) ** 2) == 0)
Q = lambda hh: sp.simplify(3 * hh / sp.diff(hh, psi) - 2 * psi)
QH = Q(hH(psi))
report('Hayward: Q = 3h/h\' - 2 psi = psi (1 - 3 l^2 psi)', sp.simplify(QH - psi * (1 - 3 * l ** 2 * psi)) == 0)
report('Hayward: f\'(r) = r Q(psi(r))', sp.simplify(sp.diff(f, r) - r * QH.subs(psi, ps)) == 0)
report('Hayward: Misner-Sharp mass M = r^3 psi/2 = m r^3/(r^3 + 2 m l^2)', sp.simplify(r ** 3 * ps / 2 - m * r ** 3 / (r ** 3 + 2 * m * l ** 2)) == 0)
hB = psi / sp.sqrt(1 - a ** 2 * psi ** 2)
report('bounded h: h\'(psi) = (1 - alpha^2 psi^2)^(-3/2)', sp.simplify(sp.diff(hB, psi) - (1 - a ** 2 * psi ** 2) ** sp.Rational(-3, 2)) == 0)
XB = sp.symbols('X', positive=True)
psB = sp.simplify(sp.solve(sp.Eq(hB, XB), psi)[0])
report('bounded h: psi = X/sqrt(1 + alpha^2 X^2) for h(psi) = X (X = 2m/r^3)', sp.simplify(psB - XB / sp.sqrt(1 + a ** 2 * XB ** 2)) == 0 or sp.simplify(psB.subs(a, 1) - XB / sp.sqrt(1 + XB ** 2)) == 0)
fB = 1 - r ** 2 * psB.subs(XB, 2 * m / r ** 3)
report('bounded h: f\'(r) = r Q(psi(r))', sp.simplify((sp.diff(fB, r) - r * Q(hB).subs(psi, psB.subs(XB, 2 * m / r ** 3)))) == 0)
report('Einstein: h = psi gives Q = psi', sp.simplify(Q(psi) - psi) == 0)

print('== static numbers, 50 digits (Section 2) ==')
mm, ll = mp.mpf(5), mp.mpf(1)
F = lambda x: 1 - 2 * mm * x ** 2 / (x ** 3 + 2 * mm * ll ** 2)
rm = mp.findroot(F, 1.06, tol=1e-45)
rp = mp.findroot(F, 9.9, tol=1e-45)
dF = lambda x: mp.diff(F, x)
km, kp_ = abs(dF(rm)) / 2, abs(dF(rp)) / 2
print('r_- = %s  r_+ = %s  kappa_- = %s  kappa_+ = %s' % (mp.nstr(rm, 10), mp.nstr(rp, 10), mp.nstr(km, 10), mp.nstr(kp_, 10)))
Qn = lambda p: p * (1 - 3 * ll ** 2 * p)
Qpn = lambda p: 1 - 6 * ll ** 2 * p
print('Q(1/r_-^2) = %s   kappa_- = r_- |Q|/2 = %s   Q\'(1/r_-^2) = %s' % (mp.nstr(Qn(1 / rm ** 2), 6), mp.nstr(rm * abs(Qn(1 / rm ** 2)) / 2, 8), mp.nstr(Qpn(1 / rm ** 2), 5)))
report('r_- rounds to 1.057475', abs(rm - mp.mpf('1.057475')) < 5e-7)
report('r_+ rounds to 9.897927', abs(rp - mp.mpf('9.897927')) < 5e-7)
report('kappa_- rounds to 0.795649', abs(km - mp.mpf('0.795649')) < 5e-7)
report('Q(1/r_-^2) rounds to -1.5048', abs(Qn(1 / rm ** 2) - mp.mpf('-1.5048')) < 5e-5)
report('Q\'(1/r_-^2) = -4.3655 (main.tex writes -4.36: the correctly rounded value is -4.37)', abs(Qpn(1 / rm ** 2) - mp.mpf('-4.3655')) < 5e-5)
report('kappa_- = r_- |Q(psi_-)|/2 (the relation used in Section 2)', abs(rm * abs(Qn(1 / rm ** 2)) / 2 - km) < mp.mpf(10) ** -40)
c1II = (1 - 1 / rm ** 2) ** 2                # c_1 in the plateau (Section 9, slaving)
beta_inf = (rm ** 2 - 1) / 4
print('c1II = (1-1/r_-^2)^2 = %s  beta_inf = (r_-^2-1)/4 = %s   2 r_- beta_inf kappa_-/c1II = %s' % (mp.nstr(c1II, 8), mp.nstr(beta_inf, 8), mp.nstr(2 * rm * beta_inf * km / c1II, 6)))
report('limit of dm/dv in Eq. (dm) rounds to 4.45', abs(2 * rm * beta_inf * km / c1II - mp.mpf('4.45')) < 5e-3)
# bounded h, m = 1, alpha = 1: horizons at psi = 1/r^2 with psi = X/sqrt(1+X^2), X = 2m/r^3
mb = mp.mpf(1)
Gb = lambda x: 1 / x ** 2 - (2 * mb / x ** 3) / mp.sqrt(1 + (2 * mb / x ** 3) ** 2)
rmb = mp.findroot(Gb, 1.0, tol=1e-40)
print('bounded h, m = 1, alpha = 1: r_- = %s  psi(r_-) = %s' % (mp.nstr(rmb, 10), mp.nstr(1 / rmb ** 2, 8)))
report('bounded h: psi(r_-) = 0.8376 (m = 1, alpha = 1)', abs(1 / rmb ** 2 - mp.mpf('0.8376')) < 5e-5)
# bounded h, m = 1.5, alpha = 1 (Section 'The bounded characteristic function')
mb2 = mp.mpf('1.5')
psib = lambda x: (2 * mb2 / x ** 3) / mp.sqrt(1 + (2 * mb2 / x ** 3) ** 2)
fb = lambda x: 1 - x ** 2 * psib(x)
rmb2 = mp.findroot(fb, 1.03, tol=1e-40)
rpb2 = mp.findroot(fb, 2.98, tol=1e-40)
kmb2, kpb2 = abs(mp.diff(fb, rmb2)) / 2, abs(mp.diff(fb, rpb2)) / 2
print('bounded h, m = 1.5, alpha = 1: r_- = %s  r_+ = %s  kappa_- = %s  kappa_+ = %s  psi(r_-) = %s  1 - alpha psi(r_-) = %s' % tuple(mp.nstr(a, 7) for a in (rmb2, rpb2, kmb2, kpb2, psib(rmb2), 1 - psib(rmb2))))
report('bounded h m=1.5: r_- = 1.031986, r_+ = 2.980943, kappa_- = 0.797008, kappa_+ = 0.161359, psi(r_-) = 0.939, wall distance 0.061',
       abs(rmb2 - mp.mpf('1.031986')) < 5e-7 and abs(rpb2 - mp.mpf('2.980943')) < 5e-7 and abs(kmb2 - mp.mpf('0.797008')) < 5e-7 and abs(kpb2 - mp.mpf('0.161359')) < 5e-7
       and abs(psib(rmb2) - mp.mpf('0.939')) < 5e-4 and abs(1 - psib(rmb2) - mp.mpf('0.061')) < 5e-4)
print('Hayward negative-mass pole: |m| = r_-^3/(2 l^2) = %s ; m changes by %s' % (mp.nstr(rm ** 3 / 2, 6), mp.nstr(5 + rm ** 3 / 2, 4)))
report('|m| = r_-^3/(2 l^2) rounds to 0.59', abs(rm ** 3 / 2 - mp.mpf('0.59')) < 5e-3)
report('m changes by about 5.6 (5 + 0.59)', abs(5 + rm ** 3 / 2 - mp.mpf('5.6')) < 5e-2)
report('r_- ~ 1.06 as quoted in Section 7', abs(rm - mp.mpf('1.06')) < 5e-3)

print('== integrability identity, generic h (Section 4c) ==')
h = sp.Function('h')
h0, h1, h2 = h(psi), sp.diff(h(psi), psi), sp.diff(h(psi), psi, 2)
c = 4 * sp.pi / h1
Qg = 3 * h0 / h1 - 2 * psi
lhs = c * sp.diff(Qg, psi) - c
rhs = sp.diff(c, psi) * (Qg + 2 * psi)
report('c Q\' - c = c\' (Q + 2 psi), c = 4 pi/h\', generic h(psi)', sp.simplify(lhs - rhs) == 0)
report('both sides equal -12 pi h h\'\'/h\'^3  (main.tex writes 4 pi (1 - 3 h h\'\'/h\'^2)/h\', which is c Q\' alone)', sp.simplify(lhs + 12 * sp.pi * h0 * h2 / h1 ** 3) == 0 and sp.simplify(rhs + 12 * sp.pi * h0 * h2 / h1 ** 3) == 0 and sp.simplify(c * sp.diff(Qg, psi) - 4 * sp.pi * (1 - 3 * h0 * h2 / h1 ** 2) / h1) == 0)
report('c\' = -4 pi h\'\'/h\'^2, Q\' = 3 - 3 h h\'\'/h\'^2 - 2 (as used in the text)', sp.simplify(sp.diff(c, psi) + 4 * sp.pi * h2 / h1 ** 2) == 0 and sp.simplify(sp.diff(Qg, psi) - (3 - 3 * h0 * h2 / h1 ** 2 - 2)) == 0)

print('== mass law and psi_v equation, generic h (Sections 5, 7) ==')
rr, rho, y, sv, pv = sp.symbols('r rho y sigma_v phi_v', real=True)
H0, H1 = sp.symbols('h0 h1', real=True)          # h(psi) and h'(psi) at the point (Q = 3 H0/H1 - 2 psi)
ps_ = (1 + 4 * y * rho) / rr ** 2
Qs = 3 * H0 / H1 - 2 * ps_
rp_ = -rho
rhop = sv * rho + 4 * sp.pi * rr / H1 * pv ** 2
yp = rr * Qs / 4 - sv * y
psi_v = sp.diff(ps_, rr) * rp_ + sp.diff(ps_, rho) * rhop + sp.diff(ps_, y) * yp
report('psi_v = (rho/r) (Q + 2 psi) + 16 pi y phi_v^2/(r h\')  (sigma_v cancels)', sp.simplify(psi_v - (rho / rr) * (Qs + 2 * ps_) - 16 * sp.pi * y * pv ** 2 / (rr * H1)) == 0)
report('(Q + 2 psi) = 3 h/h\'', sp.simplify(Qs + 2 * ps_ - 3 * H0 / H1) == 0)
dm = sp.Rational(1, 2) * (3 * rr ** 2 * rp_ * H0 + rr ** 3 * H1 * psi_v)
report('d/dv [ r^3 h(psi)/2 ] = 8 pi r^2 y phi_v^2  (the generalized-mass law, every h)', sp.simplify(dm - 8 * sp.pi * rr ** 2 * y * pv ** 2) == 0)
report('sigma_v does not appear in d m/dv', sv not in sp.simplify(dm).free_symbols)
# Hayward / bounded: invariant manifolds
z = sp.symbols('z', positive=True)
psiH = 1 / l ** 2 - z / l ** 2          # z = 1 - l^2 psi
ysol = sp.solve(sp.Eq(psi, (1 + 4 * y * rho) / rr ** 2), y)[0]
zz = 1 - l ** 2 * psi
pv_psi = sp.simplify(psi_v.subs({H0: psi / zz, H1: 1 / zz ** 2}).subs(y, ysol))
target = 3 * rho * psi * zz / rr + 16 * sp.pi * ysol * pv ** 2 * zz ** 2 / rr
report('Hayward: psi_v = 3 rho psi z/r + 16 pi y phi_v^2 z^2/r, z = 1 - l^2 psi (vanishes at z = 0: invariant manifold)', sp.simplify(pv_psi - target) == 0)
ss = sp.sqrt(1 - a ** 2 * psi ** 2)
pv_psiB = sp.simplify(psi_v.subs({H0: psi / ss, H1: 1 / ss ** 3}).subs(y, ysol))
targetB = 3 * rho * psi * ss ** 2 / rr + 16 * sp.pi * ysol * pv ** 2 * ss ** 3 / rr
report('bounded: psi_v = 3 rho psi s^2/r + 16 pi y phi_v^2 s^3/r, s = sqrt(1 - alpha^2 psi^2) (walls invariant)', sp.simplify(pv_psiB - targetB) == 0)
# m_f formula
rf = sp.symbols('r_f', positive=True)
report('m_f = r_f^3 h(r_f^-2)/2 = r_f/[2 (1 - l^2/r_f^2)]  (Hayward)', sp.simplify(rf ** 3 * hH(rf ** -2) / 2 - rf / (2 * (1 - l ** 2 / rf ** 2))) == 0)
# horizon equation psi_H and sigma_v on H+ for y = 1/2: psi_H = (1 - 2 r_v)/r^2
rv = sp.symbols('r_v', real=True)
report('y = 1/2 on H+: psi = (1 + 4 y rho)/r^2 with rho = -r_v gives psi_H = (1 - 2 r_v)/r^2', sp.simplify(((1 + 4 * sp.Rational(1, 2) * (-rv)) / rr ** 2) - (1 - 2 * rv) / rr ** 2) == 0)
# sign theorem arithmetic: y>=1/2 gives dm/dv >= 4 pi r^2 phi_v^2
yge = sp.symbols('y', real=True)
report('y >= 1/2  =>  8 pi r^2 y phi_v^2 >= 4 pi r^2 phi_v^2', sp.simplify((8 * sp.pi * rr ** 2 * yge * pv ** 2 - 4 * sp.pi * rr ** 2 * pv ** 2) - 4 * sp.pi * rr ** 2 * pv ** 2 * (2 * yge - 1)) == 0)
print()
print('ALL OK' if ok_all else 'SOME CHECK FAILED')
raise SystemExit(0 if ok_all else 1)
