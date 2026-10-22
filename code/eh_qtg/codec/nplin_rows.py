"""Rows of logs/nplin.log (Paper F, Sec. collapse, k=2, linear test on the static exterior) from the saved horizon fields nplin_m{0,1}_M5_h0.2.npz of nplin.py:
phi_H t^2/(-4b) and the local index -d ln|phi_H| / d ln t (central, +-1) at t = 100 ... 6400.  The npz files hold phi_H at unit spacing in t, which are the samples nplin.py prints.
usage: python3 nplin_rows.py nplin_m0_M5_h0.2.npz nplin_m1_M5_h0.2.npz"""
import sys, numpy as np
for fn in sys.argv[1:]:
    d = np.load(fn); t = d['t']; f = d['phiH']; b = float(d['b'])
    ix = {int(round(x)): i for i, x in enumerate(t)}
    for T in (100, 200, 400, 800, 1600, 3200, 6400, 12800):
        if T + 1 in ix and T - 1 in ix:
            i = ix[T]
            print('t=%5d  phi_H t^2/(-4b)=%.5f' % (T, f[i] * T ** 2 / (-4 * b)), ' local index=%.4f' % (-np.log(abs(f[ix[T + 1]] / f[ix[T - 1]])) / np.log((T + 1) / (T - 1))))
