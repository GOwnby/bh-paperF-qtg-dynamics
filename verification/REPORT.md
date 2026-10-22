# Verification report: bh-paperF-qtg-dynamics (quick)

**Result: 2170 PASS, 0 FAIL, 0 SKIPPED** of 2170 checks.  Total wall time 108.2 min.

## Environment

- python: 3.13.16
- numpy: 2.5.3
- scipy: 1.18.1
- sympy: not installed
- mpmath: not installed
- matplotlib: 3.11.2
- gcc: gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0
- platform: Linux-6.18.44-fc-v139-x86_64-with-glibc2.39
- machine: x86_64
- cpus: 2
- date: 2026-10-21 15:16 UTC

Jobs whose log was imported from `verification/imported/` (they need sympy/mpmath, which are not installed on this machine; the logs were produced by the same scripts on another machine, see `verification/imported/PROVENANCE.txt`): sym_checks.

## Checks

Each row: a quantity quoted in `main.tex`, its location, the value in the manuscript, the tolerance (with the reason), the value computed from the regenerated log, PASS/FAIL. Tolerance rule unless stated: half a unit of the last quoted digit of the manuscript value plus half a unit of the last printed digit of the log (rounding only); for bounds ("at most", "below") the computed value must satisfy the bound.

| status | id | location | paper | tolerance (reason) | computed |
|---|---|---|---|---|---|
| PASS | gr_limit | Sec. 4 Checks (a) | 9.7e-17 | 5.5e-19 | 9.71e-17 |
| PASS | gr_limit_scale | Sec. 4 Checks (a) | 3.4 | 0.05 (paper rounds 3.43 to 3.4) | 3.43 |
| PASS | static_identity_hay | Sec. 4 Checks (b) | 1.3e-7 | 1e-08 | 1.3e-07 |
| PASS | static_identity_bnd | Sec. 4 Checks (b) | 1.1e-6 | 1e-07 | 1.1e-06 |
| PASS | integrab_hay | Sec. 4 Checks (c) | 1.8e-11 | 1e-12 | 1.8e-11 |
| PASS | integrab_bnd | Sec. 4 Checks (c) | 2.1e-9 | 1e-10 | 2.1e-09 |
| PASS | compat_hay | Sec. 4 Checks (e) | 3.4e-12 | 5.5e-14 | 3.41e-12 |
| PASS | compat_bnd | Sec. 4 Checks (e) | 3.3e-10 | 5.5e-12 | 3.3e-10 |
| PASS | val1_w1.1 | Sec. 4 Checks(d) table row "1, v in [0,20]" | 4.0e-3 | 5.5e-05 | 0.004 |
| PASS | val1_w1.2 | Sec. 4 Checks(d) table row "1, v in [0,20]" | 3.0e-3 | 5.5e-05 | 0.003 |
| PASS | val1_w1.3 | Sec. 4 Checks(d) table row "1, v in [0,20]" | 9.9e-4 | 5.5e-06 | 0.000995 |
| PASS | val1_w1.4 | Sec. 4 Checks(d) table row "1, v in [0,20]" | 7.5e-4 | 5.5e-06 | 0.000747 |
| PASS | val1_w1.5 | Sec. 4 Checks(d) table row "1, v in [0,20]" | 2.5e-4 | 5.5e-06 | 0.000249 |
| PASS | val1_w1.6 | Sec. 4 Checks(d) table row "1, v in [0,20]" | 1.9e-4 | 5.5e-06 | 0.000187 |
| PASS | val1_w1.7 | Sec. 4 Checks(d) table row "1, v in [0,20]" | 2.0 | 0.055 | 2 |
| PASS | val1_w1.8 | Sec. 4 Checks(d) table row "1, v in [0,20]" | 2.0 | 0.055 | 2 |
| PASS | val1_w2.1 | Sec. 4 Checks(d) table row "1, v in [20,55.2]" | 5.9e-1 | 0.0055 | 0.591 |
| PASS | val1_w2.2 | Sec. 4 Checks(d) table row "1, v in [20,55.2]" | 6.8e-4 | 5.5e-06 | 0.000675 |
| PASS | val1_w2.3 | Sec. 4 Checks(d) table row "1, v in [20,55.2]" | 1.4e-1 | 0.0055 | 0.138 |
| PASS | val1_w2.4 | Sec. 4 Checks(d) table row "1, v in [20,55.2]" | 1.7e-4 | 5.5e-06 | 0.000169 |
| PASS | val1_w2.5 | Sec. 4 Checks(d) table row "1, v in [20,55.2]" | 3.4e-2 | 0.00055 | 0.0341 |
| PASS | val1_w2.6 | Sec. 4 Checks(d) table row "1, v in [20,55.2]" | 4.2e-5 | 5.5e-07 | 4.22e-05 |
| PASS | val1_w2.7 | Sec. 4 Checks(d) table row "1, v in [20,55.2]" | 2.0 (manuscript: $4.2\!\times\!10^{-5}$ & $2.1$; $2.0$) | 0.055 | 2.01 |
| PASS | val1_w2.8 | Sec. 4 Checks(d) table row "1, v in [20,55.2]" | 2.0 | 0.055 | 2 |
| PASS | val2_w1.1 | Sec. 4 Checks(d) table row "2, v in [0,20]" | 1.2e-3 | 5.5e-05 | 0.00116 |
| PASS | val2_w1.2 | Sec. 4 Checks(d) table row "2, v in [0,20]" | 6.1e-4 | 5.5e-06 | 0.000605 |
| PASS | val2_w1.3 | Sec. 4 Checks(d) table row "2, v in [0,20]" | 2.9e-4 | 5.5e-06 | 0.000293 |
| PASS | val2_w1.4 | Sec. 4 Checks(d) table row "2, v in [0,20]" | 1.6e-4 | 5.5e-06 | 0.000155 |
| PASS | val2_w1.5 | Sec. 4 Checks(d) table row "2, v in [0,20]" | 7.4e-5 | 5.5e-07 | 7.42e-05 |
| PASS | val2_w1.6 | Sec. 4 Checks(d) table row "2, v in [0,20]" | 4.1e-5 | 5.5e-07 | 4.09e-05 |
| PASS | val2_w1.7 | Sec. 4 Checks(d) table row "2, v in [0,20]" | 2.0 | 0.055 | 1.98 |
| PASS | val2_w1.8 | Sec. 4 Checks(d) table row "2, v in [0,20]" | 1.9 | 0.055 | 1.93 |
| PASS | val2_w2.1 | Sec. 4 Checks(d) table row "2, v in [20,60]" | 2.4e-2 | 0.00055 | 0.0237 |
| PASS | val2_w2.2 | Sec. 4 Checks(d) table row "2, v in [20,60]" | 2.7e-4 | 5.5e-06 | 0.000272 |
| PASS | val2_w2.3 | Sec. 4 Checks(d) table row "2, v in [20,60]" | 5.9e-3 | 5.5e-05 | 0.00589 |
| PASS | val2_w2.4 | Sec. 4 Checks(d) table row "2, v in [20,60]" | 6.8e-5 | 5.5e-07 | 6.79e-05 |
| PASS | val2_w2.5 | Sec. 4 Checks(d) table row "2, v in [20,60]" | 1.5e-3 | 5.5e-05 | 0.00147 |
| PASS | val2_w2.6 | Sec. 4 Checks(d) table row "2, v in [20,60]" | 1.7e-5 | 5.5e-07 | 1.7e-05 |
| PASS | val2_w2.7 | Sec. 4 Checks(d) table row "2, v in [20,60]" | 2.0 | 0.055 | 2 |
| PASS | val2_w2.8 | Sec. 4 Checks(d) table row "2, v in [20,60]" | 2.0 | 0.055 | 2 |
| PASS | static_conv.1 | Sec. 4 Checks(d) static background, max relative error in r, h = 0.08 ... 0.01 (model 1) | 9.3e-4 | 5.5e-06 | 0.000932 |
| PASS | static_conv.2 | Sec. 4 Checks(d) static background, max relative error in r, h = 0.08 ... 0.01 (model 1) | 2.3e-4 | 5.5e-06 | 0.000233 |
| PASS | static_conv.3 | Sec. 4 Checks(d) static background, max relative error in r, h = 0.08 ... 0.01 (model 1) | 5.8e-5 | 5.5e-07 | 5.82e-05 |
| PASS | static_conv.4 | Sec. 4 Checks(d) static background, max relative error in r, h = 0.08 ... 0.01 (model 1) | 1.5e-5 | 5.5e-07 | 1.46e-05 |
| PASS | val1_u_resid_big | Sec. 4 Checks(d) text: u-residual of model 1, second window, coarsest mesh | 0.59 | 0.005 (paper quotes 0.59 for 5.91e-1) | 0.591 |
| PASS | val1_u_resid_mid | Sec. 4 Checks(d) text: ... next mesh | 0.14 | 0.005 (1.38e-1 rounded) | 0.138 |
| PASS | val1_u_resid_fine | Sec. 4 Checks(d) text: ... finest mesh | 0.034 | 0.00055 | 0.0341 |
| PASS | masslaw_u0_v5 | Sec. 5, check_mass_law: relative difference of dm/dv and 8 pi r^2 y phi_v^2 at u=0, v=5 | 2e-4 | 5.5e-05 | 0.00021 |
| PASS | masslaw_u0_v45 | Sec. 5, check_mass_law: relative difference of dm/dv and 8 pi r^2 y phi_v^2 at u=0, v=45 | 3e-4 | 5.5e-05 | 0.00027 |
| PASS | masslaw_u0_v55 | Sec. 5, check_mass_law: relative difference of dm/dv and 8 pi r^2 y phi_v^2 at u=0, v=55 | 1.5e-4 | 1e-05 | 0.00015 |
| PASS | masslaw_u0_v60 | Sec. 5, check_mass_law: relative difference of dm/dv and 8 pi r^2 y phi_v^2 at u=0, v=60 | 3e-4 | 5.5e-05 | 0.00032 |
| PASS | masslaw_u0_v64 | Sec. 5, check_mass_law: relative difference of dm/dv and 8 pi r^2 y phi_v^2 at u=0, v=64 | 2e-2 | 0.0055 | 0.021 |
| PASS | action_n_tests | Sec. 4 Checks(f): number of tests with c = 4 pi/h, h of degree 4 and 6 (d_v C_u = 0 exactly) | 30 | 0 (integer count of exact-zero tests) | 30 |
| PASS | action2_n_exact | Sec. 4 Checks(f): tests with a_2 = 0, difference exactly zero (action_check2.py) | 12 | 0 (integer count) | 12 |
| PASS | action3_n_tests | Sec. 4 Checks(f): tests with a_2 != 0 (action_check3.py) | 8 | 0 (integer count) | 8 |
| PASS | action3_maxdiff | Sec. 4 Checks(f): at most 1.3e-14 in the 8 tests with a_2 != 0 | 1.3e-14 | bound: <= paper | 1.24e-14 |
| PASS | action_control_11 | Sec. 4 Checks(f): for a Raychaudhuri coefficient 1.1 times larger the difference is 6e-3 or more (the a_2 != 0 tests, action_check3.py; action_check2.py: 3.0e-3) | 6e-3 | bound: >= paper | 0.00612 |
| PASS | action_control_psi5 | Sec. 4 Checks(f): for c(1+psi/5) the difference is not zero (smallest value over the three logs; bound 1e-4) | 1e-4 | bound: >= paper | 0.0001365 |
| PASS | action_c3_min | Sec. 4 Checks(f): without the c3 term the difference is 1e-5 ... 1e-1 (action_check3.py, a_2 != 0): smallest c3 term | 1e-5 | bound: >= paper | 2.25e-05 |
| PASS | action_c3_max | Sec. 4 Checks(f): ... largest c3 term (action_check2.py, a_2 = 0, reaches 1.7) | 1e-1 | bound: <= paper | 0.0921 |
| PASS | lift_reduced | Sec. 4 Checks(g)(i): reductions R, I_C2, I_C3, I_Rh2, I_Rh3, I_R2C agree to | 9e-11 | bound: <= paper | 8.1e-11 |
| PASS | lift_lifts | Sec. 4 Checks(g)(ii): lifts P, H, T, K reproduce psi, eta, tau, calR to | 3e-11 | bound: <= paper | 2.8e-11 |
| PASS | lift_gr | Sec. 4 Checks(g)(iii): density with H2 = 2P, H3 = 4, H4 = 1 equals the Ricci scalar to | 3e-13 | bound: <= paper | 2.5e-13 |
| PASS | lift_control | Sec. 4 Checks(g): the control (the wrong fourth term) must fail: smallest control difference > 1 | 1 | bound: >= paper | 31 |
| PASS | tab_static_U0.3_free_v40 | Table tab:static, ray U~0.3, free, v=40 | 2.5e-9 | 1e-10 | 2.5e-09 |
| PASS | tab_static_U0.3_free_v60 | Table tab:static, ray U~0.3, free, v=60 | 2.1e-5 | 1e-06 | 2.1e-05 |
| PASS | tab_static_U0.3_free_v80 | Table tab:static, ray U~0.3, free, v=80 | 2.0 | 0.1 | 2 |
| PASS | tab_static_U0.3_free_v98 | Table tab:static, ray U~0.3, free, v=98 | 1 | 0 (1 = value is non-finite in the log) | 1 |
| PASS | tab_static_U0.3_con_v40 | Table tab:static, ray U~0.3, constrained, v=40 | 1.3e-9 | 1e-10 | 1.3e-09 |
| PASS | tab_static_U0.3_con_v60 | Table tab:static, ray U~0.3, constrained, v=60 | 5.7e-5 | 1e-06 | 5.7e-05 |
| PASS | tab_static_U0.3_con_v80 | Table tab:static, ray U~0.3, constrained, v=80 | 5.8e-5 | 1e-06 | 5.8e-05 |
| PASS | tab_static_U0.3_con_v98 | Table tab:static, ray U~0.3, constrained, v=98 | 5.8e-5 | 1e-06 | 5.8e-05 |
| PASS | tab_static_U0.3_ext_v40 | Table tab:static, ray U~0.3, constrained, extrapolated, v=40 | 4e-14 | 5.5e-15 | 3.9e-14 |
| PASS | tab_static_U0.3_ext_v60 | Table tab:static, ray U~0.3, constrained, extrapolated, v=60 | 2.5e-12 | 1e-13 | 2.5e-12 |
| PASS | tab_static_U0.3_ext_v80 | Table tab:static, ray U~0.3, constrained, extrapolated, v=80 | 2.9e-12 | 1e-13 | 2.9e-12 |
| PASS | tab_static_U0.3_ext_v98 | Table tab:static, ray U~0.3, constrained, extrapolated, v=98 | 2.9e-12 | 1e-13 | 2.9e-12 |
| PASS | tab_static_U1.0_free_v40 | Table tab:static, ray U~1.0, free, v=40 | 2.9e-5 | 1e-06 | 2.9e-05 |
| PASS | tab_static_U1.0_free_v60 | Table tab:static, ray U~1.0, free, v=60 | 5.6e1 | 1 | 56 |
| PASS | tab_static_U1.0_free_v80 | Table tab:static, ray U~1.0, free, v=80 | 1 | 0 (1 = value is non-finite in the log) | 1 |
| PASS | tab_static_U1.0_free_v98 | Table tab:static, ray U~1.0, free, v=98 | 1 | 0 (1 = value is non-finite in the log) | 1 |
| PASS | tab_static_U1.0_con_v40 | Table tab:static, ray U~1.0, constrained, v=40 | 5.4e-5 | 1e-06 | 5.4e-05 |
| PASS | tab_static_U1.0_con_v60 | Table tab:static, ray U~1.0, constrained, v=60 | 5.4e-5 | 1e-06 | 5.4e-05 |
| PASS | tab_static_U1.0_con_v80 | Table tab:static, ray U~1.0, constrained, v=80 | 5.4e-5 | 1e-06 | 5.4e-05 |
| PASS | tab_static_U1.0_con_v98 | Table tab:static, ray U~1.0, constrained, v=98 | 5.4e-5 | 1e-06 | 5.4e-05 |
| PASS | tab_static_U1.0_ext_v40 | Table tab:static, ray U~1.0, constrained, extrapolated, v=40 | 1.9e-12 | 1e-13 | 1.9e-12 |
| PASS | tab_static_U1.0_ext_v60 | Table tab:static, ray U~1.0, constrained, extrapolated, v=60 | 1.9e-12 | 1e-13 | 1.9e-12 |
| PASS | tab_static_U1.0_ext_v80 | Table tab:static, ray U~1.0, constrained, extrapolated, v=80 | 1.9e-12 | 1e-13 | 1.9e-12 |
| PASS | tab_static_U1.0_ext_v98 | Table tab:static, ray U~1.0, constrained, extrapolated, v=98 | 1.9e-12 | 1e-13 | 1.9e-12 |
| PASS | free_psi_v40_ext_U0.3 | Sec. 8 Constrained evolution free evolution, extrapolated error in psi at v=40, U~0.3 | 6e-14 | 5e-15 (paper writes 6e-14 for 5.9e-14) | 5.9e-14 |
| PASS | free_psi_v40_ext_U0.6 | Sec. 8 Constrained evolution ... U~0.6 | 8e-11 | 5.5e-12 | 8e-11 |
| PASS | free_psi_v40_ext_U1.0 | Sec. 8 Constrained evolution ... U~1.0 | 2e-8 | 5.5e-09 | 2e-08 |
| PASS | free_psi_v40_ext_U1.2 | Sec. 8 Constrained evolution ... U~1.2 | 1.3e-6 | 1e-07 | 1.3e-06 |
| PASS | free_psi_U0.6_v60_mesh0 | Sec. 8 Constrained evolution error in psi on U~0.6 at v=60, mesh 0 | 1.3e2 | 10 | 130 |
| PASS | free_psi_U0.6_v60_mesh1 | Sec. 8 Constrained evolution error in psi on U~0.6 at v=60, mesh 1 | 3.5 | 0.1 | 3.5 |
| PASS | free_psi_U0.6_v60_mesh2 | Sec. 8 Constrained evolution error in psi on U~0.6 at v=60, mesh 2 | 0.21 | 0.01 | 0.21 |
| PASS | free_psi_U0.6_v60_mesh3 | Sec. 8 Constrained evolution error in psi on U~0.6 at v=60, mesh 3 | 1.3e-2 | 0.001 | 0.013 |
| PASS | free_nf_U0.6_v80 | Sec. 8 Constrained evolution non-finite on U~0.6 at v=80 (finest mesh) | 1 | 0 (1 = non-finite) | 1 |
| PASS | free_nf_v98_ray0 | Sec. 8 Constrained evolution non-finite at v=98 on every ray (finest mesh) | 1 | 0 (1 = non-finite) | 1 |
| PASS | free_nf_v98_ray1 | Sec. 8 Constrained evolution non-finite at v=98 on every ray (finest mesh) | 1 | 0 (1 = non-finite) | 1 |
| PASS | free_nf_v98_ray2 | Sec. 8 Constrained evolution non-finite at v=98 on every ray (finest mesh) | 1 | 0 (1 = non-finite) | 1 |
| PASS | free_nf_v98_ray3 | Sec. 8 Constrained evolution non-finite at v=98 on every ray (finest mesh) | 1 | 0 (1 = non-finite) | 1 |
| PASS | mode3_maxext | Sec. 8 Constrained evolution largest extrapolated error over 4 rays, 4 times, 3 variables, mode 3 | 4.7e-11 | 5e-13 | 4.7e-11 |
| PASS | mode1_maxext | Sec. 8 Constrained evolution mode 1: extrapolated errors at most | 1.1e-9 | bound: <= paper | 1.1e-09 |
| PASS | mode2_maxext | Sec. 8 Constrained evolution mode 2: extrapolated errors at most | 1.1e-8 | bound: <= paper | 1.1e-08 |
| PASS | static_leq3e-12 | Sec. 8 Constrained evolution (i) <= 3e-12 after extrapolation (the two rays of the table) | 3e-12 | bound: <= paper | 2.9e-12 |
| PASS | bounded_M1.5_maxext | Sec. 8 Constrained evolution (iv) bounded h, m = 1.5, alpha = 1: extrapolated error at most | 4.1e-11 | bound: <= paper | 4.1e-11 |
| PASS | bounded_M5_sv_v98 | Sec. 8 Constrained evolution (iv) m = 5, alpha = 1: extrapolated error in sigma_v at v=98 | 6.5e-3 | 0.0001 | 0.0065 |
| PASS | freecon_v30.1 | Sec. 8 Constrained evolution (ii) /free - constrained/ in sigma on U~1, v=30, h=0.05 ... 0.00625 | 4.8e-4 | 1e-05 | 0.00048 |
| PASS | freecon_v30.2 | Sec. 8 Constrained evolution (ii) /free - constrained/ in sigma on U~1, v=30, h=0.05 ... 0.00625 | 1.2e-4 | 1e-05 | 0.00012 |
| PASS | freecon_v30.3 | Sec. 8 Constrained evolution (ii) /free - constrained/ in sigma on U~1, v=30, h=0.05 ... 0.00625 | 3.0e-5 | 1e-06 | 3e-05 |
| PASS | freecon_v30.4 | Sec. 8 Constrained evolution (ii) /free - constrained/ in sigma on U~1, v=30, h=0.05 ... 0.00625 | 7.5e-6 | 1e-07 | 7.5e-06 |
| PASS | freecon_v40.1 | Sec. 8 Constrained evolution (ii) /free - constrained/ in sigma on U~1, v=40, h=0.05 ... 0.00625 | 1.0e-2 | 0.001 | 0.01 |
| PASS | freecon_v40.2 | Sec. 8 Constrained evolution (ii) /free - constrained/ in sigma on U~1, v=40, h=0.05 ... 0.00625 | 2.5e-3 | 0.0001 | 0.0025 |
| PASS | freecon_v40.3 | Sec. 8 Constrained evolution (ii) /free - constrained/ in sigma on U~1, v=40, h=0.05 ... 0.00625 | 6.3e-4 | 1e-05 | 0.00063 |
| PASS | freecon_v40.4 | Sec. 8 Constrained evolution (ii) /free - constrained/ in sigma on U~1, v=40, h=0.05 ... 0.00625 | 1.6e-4 | 1e-05 | 0.00016 |
| PASS | ruv_v40.1 | Sec. 8 Constrained evolution (iii) relative L2 residual of the r_uv equation, v=40, h=0.05, 0.025, 0.0125 | 1.1e-3 | 5.5e-05 | 0.00106 |
| PASS | ruv_v40.2 | Sec. 8 Constrained evolution (iii) relative L2 residual of the r_uv equation, v=40, h=0.05, 0.025, 0.0125 | 2.7e-4 | 5.5e-06 | 0.000266 |
| PASS | ruv_v40.3 | Sec. 8 Constrained evolution (iii) relative L2 residual of the r_uv equation, v=40, h=0.05, 0.025, 0.0125 | 6.7e-5 | 5.5e-07 | 6.7e-05 |
| PASS | ruv_v100.1 | Sec. 8 Constrained evolution (iii) ... v=100 | 3.3e-3 | 5.5e-05 | 0.00325 |
| PASS | ruv_v100.2 | Sec. 8 Constrained evolution (iii) ... v=100 | 8.9e-4 | 5.5e-06 | 0.000894 |
| PASS | ruv_v100.3 | Sec. 8 Constrained evolution (iii) ... v=100 | 2.6e-4 | 5.5e-06 | 0.000259 |
| PASS | static_gen_maxdiff | Sec. 7 Event-horizon-regular data(a): max relative difference over six points up to v=98 against the Paper E implementation | 5.8e-13 | 5e-15 (maximum of the printed values (5.82e-13)) | 5.82e-13 |
| PASS | m_f_B0.0003 | Sec. 7 Event-horizon-regular data(b): m_f for B=0.0003 (Hayward, m=5) | 5.000001 | 1e-06 | 5 |
| PASS | m_f_B0.003 | Sec. 7 Event-horizon-regular data(b): m_f for B=0.003 (Hayward, m=5) | 5.000099 | 1e-06 | 5.0001 |
| PASS | m_f_B0.03 | Sec. 7 Event-horizon-regular data(b): m_f for B=0.03 (Hayward, m=5) | 5.00996 | 5.5e-06 | 5.00996 |
| PASS | sym_all_ok | Sec. 2/4/5/7: every symbolic and 50-digit identity of code/sym_checks.py holds (number of failed identities) | 0 | 0 (count; sympy/mpmath/rational arithmetic) | 0 |
| PASS | sym_r_minus | Sec. 2: r_- of the Hayward interior, m=5, l=1 | 1.057475 | 1e-06 (log prints 10 significant digits; 1.057474507 rounds to 1.057475) | 1.05747 |
| PASS | sym_r_plus | Sec. 2: r_+ | 9.897927 | 1e-06 (9.897926849 rounds to 9.897927) | 9.89793 |
| PASS | sym_kappa_minus | Sec. 2: kappa_- | 0.795649 | 1e-06 (0.7956492739 rounds to 0.795649) | 0.795649 |
| PASS | sym_Q_inner | Sec. 2: Q(1/r_-^2) | -1.5048 | 5e-05 (-1.50481) | -1.50481 |
| PASS | sym_Qprime_inner | Sec. 2: Q'(1/r_-^2) = 1 - 6 l^2 psi_-; manuscript writes -4.36, correctly rounded -4.37 (-4.36552) | -4.37 | 0.005 (-4.3655 is within 0.005 of -4.37 and 0.0055 of -4.36: see the proposed correction in the report) | -4.3655 |
| PASS | sym_psi_bounded | Sec. 2: psi(r_-) of the bounded model (m=1, alpha=1) | 0.8376 | 5e-05 (0.83756544 rounds to 0.8376) | 0.837565 |
| PASS | sym_pole_mass | Sec. 7: /m/ = r_-^3/(2 l^2) at the negative-mass pole | 0.59 | 0.005 (0.591262) | 0.591262 |
| PASS | sym_pole_change | Sec. 7: m has changed by about 5.6 | 5.6 | 0.05 (5.591) | 5.591 |
| PASS | tab_kernel_B0.0003_v60 | Table tab:kernel, B=0.0003, v=60 (ratio on U~1) | 0.999244 | 1e-06 | 0.999244 |
| PASS | tab_kernel_B0.0003_v80 | Table tab:kernel, B=0.0003, v=80 (ratio on U~1) | 0.999331 | 1e-06 | 0.999331 |
| PASS | tab_kernel_B0.0003_v100 | Table tab:kernel, B=0.0003, v=100 (ratio on U~1) | 0.999383 | 1e-06 | 0.999383 |
| PASS | tab_kernel_B0.0003_v108 | Table tab:kernel, B=0.0003, v=108 (ratio on U~1) | 0.999399 | 1e-06 | 0.999399 |
| PASS | tab_kernel_B0.003_v60 | Table tab:kernel, B=0.003, v=60 (ratio on U~1) | 0.999328 | 1e-06 | 0.999328 |
| PASS | tab_kernel_B0.003_v80 | Table tab:kernel, B=0.003, v=80 (ratio on U~1) | 0.999428 | 1e-06 | 0.999428 |
| PASS | tab_kernel_B0.003_v100 | Table tab:kernel, B=0.003, v=100 (ratio on U~1) | 0.999492 | 1e-06 | 0.999492 |
| PASS | tab_kernel_B0.003_v108 | Table tab:kernel, B=0.003, v=108 (ratio on U~1) | 0.999512 | 1e-06 | 0.999512 |
| PASS | tab_kernel_B0.03_v60 | Table tab:kernel, B=0.03, v=60 (ratio on U~1) | 1.007802 | 1e-06 | 1.0078 |
| PASS | tab_kernel_B0.03_v80 | Table tab:kernel, B=0.03, v=80 (ratio on U~1) | 1.009181 | 1e-06 | 1.00918 |
| PASS | tab_kernel_B0.03_v100 | Table tab:kernel, B=0.03, v=100 (ratio on U~1) | 1.010465 | 1e-06 | 1.01046 |
| PASS | tab_kernel_B0.03_v108 | Table tab:kernel, B=0.03, v=108 (ratio on U~1) | 1.010849 | 1e-06 | 1.01085 |
| PASS | kernel_small_min | Sec. 9 Hayward text: ratio 0.9992-0.9995 for v >= 60 (B = 3e-4 and 3e-3): minimum | 0.9992 | 5e-05 (range quoted to 4 digits) | 0.999244 |
| PASS | kernel_small_max | Sec. 9 Hayward text: ... maximum | 0.9995 | 5e-05 (range quoted to 4 digits) | 0.999512 |
| PASS | kernel_large_min | Sec. 9 Hayward text: B=3e-2 ratio 1.0078-1.0108: minimum | 1.0078 | 5e-05 (range quoted to 4 digits) | 1.0078 |
| PASS | kernel_large_max | Sec. 9 Hayward text: ... maximum | 1.0108 | 5e-05 (range quoted to 4 digits) | 1.01085 |
| PASS | kernel_offset_diff | Sec. 9 Hayward text: offsets from unity at the two small amplitudes differ by at most | 1.1e-4 | 5e-06 (1.09e-4 rounds to 1.1e-4) | 0.000113 |
| PASS | kernel_offset_min | Sec. 9 Hayward text: offset of 5-8e-4 at small B: smallest 1-ratio | 5e-4 | 5e-05 (range quoted to one digit (4.9e-4)) | 0.000488 |
| PASS | kernel_offset_max | Sec. 9 Hayward text: ... largest 1-ratio | 8e-4 | 5e-05 (range quoted to one digit (7.6e-4)) | 0.000756 |
| PASS | cmp_add_U1_v60 | Sec. 9 Hayward text: difference between the two evolutions on U~1, B=3e-3 | -3.2e-4 | 1e-05 | -0.00032 |
| PASS | cmp_add_range_min | Sec. 9 Hayward text: QTG flux differs from the additive by -2.4e-4 ... (smallest /./ for v=60-80 on the four rays; manuscript: -2.4e-4) | 2.4e-4 | 1.5e-05 (smallest /difference/ over v=60,70,80 and the four rays is 2.3e-4 (ray 0, v=60; 2.4e-4 for v>=70): see report) | 0.00023 |
| PASS | cmp_add_range_max | Sec. 9 Hayward text: ... -3.7e-4 (largest /./ for v=60-80; manuscript: -3.7e-4) | 3.7e-4 | 1.5e-05 (largest /difference/ over v=60,70,80 is 3.6e-4 (ray 3, v=60); 3.7e-4 occurs at v=50 (ray 3): see report) | 0.00036 |
| PASS | cmp_add_scaling | Sec. 9 Hayward text: exactly 1e-2 of that at B=3e-4 (ratio of the differences, ray 2, v=60) | 0.01 | 0.001 (ratio of two 2-digit numbers (3.2e-6/3.2e-4)) | 0.01 |
| PASS | cmp_add_sigma_v80 | Sec. 9 Hayward text: at v=80 on U~1 the metric exponents of the two evolutions differ by | 0.68 | 0.01 | 0.68 |
| PASS | tab_exp_kappa_B0.0003 | Table tab:exp, B=0.0003: -kappa_-(m_f) | -0.7956493 | 1e-07 | -0.795649 |
| PASS | tab_exp_plateau_B0.0003 | Table tab:exp, B=0.0003: plateau of sigma_v on U~0.3 | -0.7956493 | 1e-07 | -0.795649 |
| PASS | tab_exp_diff_B0.0003 | Table tab:exp, B=0.0003: difference | -1.5e-10 | 1e-11 | -1.5e-10 |
| PASS | tab_exp_kappa_B0.003 | Table tab:exp, B=0.003: -kappa_-(m_f) | -0.7956534 | 1e-07 | -0.795653 |
| PASS | tab_exp_plateau_B0.003 | Table tab:exp, B=0.003: plateau of sigma_v on U~0.3 | -0.7956534 | 1e-07 | -0.795653 |
| PASS | tab_exp_diff_B0.003 | Table tab:exp, B=0.003: difference | -4.1e-9 | 1e-10 | -4.1e-09 |
| PASS | tab_exp_kappa_B0.03 | Table tab:exp, B=0.03: -kappa_-(m_f) | -0.7960656 | 1e-07 | -0.796066 |
| PASS | tab_exp_plateau_B0.03 | Table tab:exp, B=0.03: plateau of sigma_v on U~0.3 | -0.7960643 | 1e-07 | -0.796064 |
| PASS | tab_exp_diff_B0.03 | Table tab:exp, B=0.03: difference | 1.3e-6 | 1e-07 | 1.3e-06 |
| PASS | exp_shift_B0.03 | Sec. 9 Hayward text: at B=3e-2 the shift from the static value -kappa_-(5) = -0.7956493 | 4.2e-4 | 5e-06 (0.7960656-0.7956493 = 4.163e-4) | 0.0004163 |
| PASS | width_min | Sec. 9 Hayward text: 10%-90% rise of sigma_v over 7.2-7.6 units of v: smallest width | 7.2 | 0.1 | 7.2 |
| PASS | width_max | Sec. 9 Hayward text: ... largest width | 7.6 | 0.1 | 7.6 |
| PASS | vf_B0.003_ray0 | Sec. 9 Hayward front v_f (sigma_v=-0.4), B=3e-3, ray 0 | 102.3 | 0.055 | 102.25 |
| PASS | xf_B0.003_ray0 | Sec. 9 Hayward front x_f = U exp(kappa_+ v_f), B=3e-3, ray 0 | 45 | 0.5 (x_f rounded to integer) | 44.8 |
| PASS | vf_B0.003_ray1 | Sec. 9 Hayward front v_f (sigma_v=-0.4), B=3e-3, ray 1 | 84.0 | 0.055 | 84.03 |
| PASS | xf_B0.003_ray1 | Sec. 9 Hayward front x_f = U exp(kappa_+ v_f), B=3e-3, ray 1 | 37 | 0.5 (x_f rounded to integer) | 36.74 |
| PASS | vf_B0.003_ray2 | Sec. 9 Hayward front v_f (sigma_v=-0.4), B=3e-3, ray 2 | 70.4 | 0.055 | 70.38 |
| PASS | xf_B0.003_ray2 | Sec. 9 Hayward front x_f = U exp(kappa_+ v_f), B=3e-3, ray 2 | 31 | 0.5 (x_f rounded to integer) | 31.4 |
| PASS | vf_B0.003_ray3 | Sec. 9 Hayward front v_f (sigma_v=-0.4), B=3e-3, ray 3 | 65.4 | 0.055 | 65.44 |
| PASS | xf_B0.003_ray3 | Sec. 9 Hayward front x_f = U exp(kappa_+ v_f), B=3e-3, ray 3 | 30 | 0.5 (x_f rounded to integer) | 29.57 |
| PASS | vf_U1_B0.0003 | Sec. 9 Hayward v_f on U~1, B=0.0003 | 83.5 | 0.055 | 83.54 |
| PASS | vf_U1_B0.003 | Sec. 9 Hayward v_f on U~1, B=0.003 | 70.4 | 0.055 | 70.38 |
| PASS | vf_U1_B0.03 | Sec. 9 Hayward v_f on U~1, B=0.03 | 57.3 | 0.055 | 57.29 |
| PASS | xf_U1_B0.0003 | Sec. 9 Hayward x_f on U~1, B=0.0003 | 60 | 0.5 (quoted to integer) | 59.82 |
| PASS | xf_U1_B0.003 | Sec. 9 Hayward x_f on U~1, B=0.003 | 31 | 0.5 (quoted to integer) | 31.4 |
| PASS | xf_U1_B0.03 | Sec. 9 Hayward x_f on U~1, B=0.03 | 16.5 | 0.05 (16.54 rounds to 16.5) | 16.54 |
| PASS | delay_per_decade | Sec. 9 Hayward text: delay of 13.1 per decade of 1/B (v_f(3e-4) - v_f(3e-2))/2 on U~1 | 13.1 | 0.05 ((83.54-57.29)/2 = 13.1) | 13.125 |
| PASS | delay_per_efold | Sec. 9 Hayward text: ... i.e. 5.7 per e-fold | 5.7 | 0.05 (13.1/ln 10 = 5.7) | 5.70012 |
| PASS | tab_front_v80_sigma_v | Table tab:front, v=80, sigma_v | -0.1159 | 5.5e-05 | -0.1159 |
| PASS | tab_front_v80_dsigma_v | Table tab:front, v=80, dsigma_v | 1.9e-9 | 1e-10 | 1.9e-09 |
| PASS | tab_front_v80_z | Table tab:front, v=80, z | 1.77e-2 | 5.05e-05 | 0.017709 |
| PASS | tab_front_v80_dz/z | Table tab:front, v=80, dz/z | 5.5e-8 | 1e-09 | 5.5e-08 |
| PASS | tab_front_v80_m | Table tab:front, v=80, m | 32.8 | 0.0505 | 32.796 |
| PASS | tab_front_v80_dm/dv | Table tab:front, v=80, dm/dv | 3.21 | 0.0055 | 3.205 |
| PASS | tab_front_v80_zm | Table tab:front, v=80, zm | 0.581 | 0.00055 | 0.5808 |
| PASS | tab_front_v80_y phi_v^2 | Table tab:front, v=80, y phi_v^2 | 0.116 | 0.00055 | 0.1158 |
| PASS | tab_front_v100_sigma_v | Table tab:front, v=100, sigma_v | -0.0941 | 5.5e-05 | -0.09408 |
| PASS | tab_front_v100_dsigma_v | Table tab:front, v=100, dsigma_v | 2.3e-10 | 1e-11 | 2.3e-10 |
| PASS | tab_front_v100_z | Table tab:front, v=100, z | 5.65e-3 | 5.05e-06 | 0.005646 |
| PASS | tab_front_v100_dz/z | Table tab:front, v=100, dz/z | 2.6e-7 | 1e-08 | 2.6e-07 |
| PASS | tab_front_v100_m | Table tab:front, v=100, m | 104.1 | 0.055 | 104.13 |
| PASS | tab_front_v100_dm/dv | Table tab:front, v=100, dm/dv | 3.72 | 0.0055 | 3.722 |
| PASS | tab_front_v100_zm | Table tab:front, v=100, zm | 0.588 | 0.00055 | 0.5879 |
| PASS | tab_front_v100_y phi_v^2 | Table tab:front, v=100, y phi_v^2 | 0.133 | 0.00055 | 0.1325 |
| PASS | tab_front_v120_sigma_v | Table tab:front, v=120, sigma_v | -0.0876 | 5.5e-05 | -0.08757 |
| PASS | tab_front_v120_dsigma_v | Table tab:front, v=120, dsigma_v | 4.0e-9 | 1e-10 | 4e-09 |
| PASS | tab_front_v120_z | Table tab:front, v=120, z | 3.28e-3 | 5.05e-06 | 0.0032757 |
| PASS | tab_front_v120_dz/z | Table tab:front, v=120, dz/z | 1.3e-7 | 1e-08 | 1.3e-07 |
| PASS | tab_front_v120_m | Table tab:front, v=120, m | 179.9 | 0.055 | 179.91 |
| PASS | tab_front_v120_dm/dv | Table tab:front, v=120, dm/dv | 3.84 | 0.0055 | 3.84 |
| PASS | tab_front_v120_zm | Table tab:front, v=120, zm | 0.589 | 0.00055 | 0.5893 |
| PASS | tab_front_v120_y phi_v^2 | Table tab:front, v=120, y phi_v^2 | 0.137 | 0.00055 | 0.1366 |
| PASS | tab_front_v140_sigma_v | Table tab:front, v=140, sigma_v | -0.0796 | 5.5e-05 | -0.07959 |
| PASS | tab_front_v140_dsigma_v | Table tab:front, v=140, dsigma_v | 6.9e-8 | 1e-09 | 6.9e-08 |
| PASS | tab_front_v140_z | Table tab:front, v=140, z | 2.29e-3 | 5.05e-06 | 0.0022908 |
| PASS | tab_front_v140_dz/z | Table tab:front, v=140, dz/z | 4.1e-6 | 1e-07 | 4.1e-06 |
| PASS | tab_front_v140_m | Table tab:front, v=140, m | 257.5 | 0.055 | 257.51 |
| PASS | tab_front_v140_dm/dv | Table tab:front, v=140, dm/dv | 3.92 | 0.0055 | 3.919 |
| PASS | tab_front_v140_zm | Table tab:front, v=140, zm | 0.590 | 0.00055 | 0.5899 |
| PASS | tab_front_v140_y phi_v^2 | Table tab:front, v=140, y phi_v^2 | 0.139 | 0.00055 | 0.1394 |
| PASS | tab_front_v160_sigma_v | Table tab:front, v=160, sigma_v | -0.0688 | 5.5e-05 | -0.06881 |
| PASS | tab_front_v160_dsigma_v | Table tab:front, v=160, dsigma_v | 1.4e-6 | 1e-07 | 1.4e-06 |
| PASS | tab_front_v160_z | Table tab:front, v=160, z | 1.75e-3 | 5.05e-06 | 0.0017531 |
| PASS | tab_front_v160_dz/z | Table tab:front, v=160, dz/z | 2.2e-4 | 1e-05 | 0.00022 |
| PASS | tab_front_v160_m | Table tab:front, v=160, m | 336.7 | 0.055 | 336.67 |
| PASS | tab_front_v160_dm/dv | Table tab:front, v=160, dm/dv | 4.00 | 0.0055 | 3.998 |
| PASS | tab_front_v160_zm | Table tab:front, v=160, zm | 0.590 | 0.00055 | 0.5902 |
| PASS | tab_front_v160_y phi_v^2 | Table tab:front, v=160, y phi_v^2 | 0.142 | 0.00055 | 0.1422 |
| PASS | tab_front_v180_sigma_v | Table tab:front, v=180, sigma_v | -0.0561 | 5.5e-05 | -0.05609 |
| PASS | tab_front_v180_dsigma_v | Table tab:front, v=180, dsigma_v | 3.4e-5 | 1e-06 | 3.4e-05 |
| PASS | tab_front_v180_z | Table tab:front, v=180, z | 1.41e-3 | 5.05e-06 | 0.0014144 |
| PASS | tab_front_v180_dz/z | Table tab:front, v=180, dz/z | 8.6e-3 | 0.0001 | 0.0086 |
| PASS | tab_front_v180_m | Table tab:front, v=180, m | 417.4 | 0.055 | 417.43 |
| PASS | tab_front_v180_dm/dv | Table tab:front, v=180, dm/dv | 4.07 | 0.0055 | 4.073 |
| PASS | tab_front_v180_zm | Table tab:front, v=180, zm | 0.590 | 0.00055 | 0.5904 |
| PASS | tab_front_v180_y phi_v^2 | Table tab:front, v=180, y phi_v^2 | 0.145 | 0.00055 | 0.1452 |
| PASS | front_zm_limit | Sec. 9 Hayward text: (1 - l^2 psi) m -> r_-^3/(2 l^2) = 0.59 (zm at v=180) | 0.59 | 0.005 (zm = 0.5904 at v=180, limit 0.5913) | 0.5904 |
| PASS | front_dmdv_min | Sec. 9 Hayward text: dm/dv = 3.7 -> 4.1 (v=100) | 3.7 | 0.05 (3.722) | 3.722 |
| PASS | front_dmdv_max | Sec. 9 Hayward text: ... 4.1 (v=180) | 4.1 | 0.05 (4.073) | 4.073 |
| PASS | front_yphi_min | Sec. 9 Hayward text: y phi_v^2 = 0.13-0.145 (v=100) | 0.13 | 0.005 (0.1325) | 0.1325 |
| PASS | front_yphi_max | Sec. 9 Hayward text: ... 0.145 (v=180) | 0.145 | 0.0005 (0.1452) | 0.1452 |
| PASS | front_sv_100 | Sec. 9 Hayward text: sigma_v rises from -0.094 at v=100 | -0.094 | 0.000505 | -0.09408 |
| PASS | front_sv_180 | Sec. 9 Hayward text: ... to -0.056 at v=180 | -0.056 | 0.000505 | -0.05609 |
| PASS | front_sv_incr_lo | Sec. 9 Hayward text: increment of 6.3-6.5e-4 per unit v over 160 <= v <= 190: smallest of the 10-unit differences / 10 | 6.3e-4 | 5e-06 (quoted to two digits) | 0.000625 |
| PASS | front_sv_incr_hi | Sec. 9 Hayward text: ... largest | 6.5e-4 | 5e-06 (quoted to two digits (6.47e-4)) | 0.000647 |
| PASS | masslaw_B0.003_[80,90] | Sec. 9 Hayward mass increment vs trapezoid integral of 8 pi r^2 y phi_v^2, U~1, B=0.003, v in [80,90] | 1.1e-4 | 1e-05 | 0.00011 |
| PASS | masslaw_B0.003_[90,100] | Sec. 9 Hayward mass increment vs trapezoid integral of 8 pi r^2 y phi_v^2, U~1, B=0.003, v in [90,100] | 2.1e-5 | 1e-06 | 2.1e-05 |
| PASS | masslaw_B0.003_[100,108] | Sec. 9 Hayward mass increment vs trapezoid integral of 8 pi r^2 y phi_v^2, U~1, B=0.003, v in [100,108] | 7.5e-6 | 1e-07 | 7.5e-06 |
| PASS | masslaw_B0.003_[60,70] | Sec. 9 Hayward mass increment vs trapezoid integral of 8 pi r^2 y phi_v^2, U~1, B=0.003, v in [60,70] | 1.3e-2 | 0.001 | 0.013 |
| PASS | masslaw_B0.003_[70,80] | Sec. 9 Hayward mass increment vs trapezoid integral of 8 pi r^2 y phi_v^2, U~1, B=0.003, v in [70,80] | 1.1e-3 | 0.0001 | 0.0011 |
| PASS | masslaw_B0.03_[60,70] | Sec. 9 Hayward mass increment vs trapezoid integral of 8 pi r^2 y phi_v^2, U~1, B=0.03, v in [60,70] | 6.4e-4 | 1e-05 | 0.00064 |
| PASS | masslaw_B0.03_[70,80] | Sec. 9 Hayward mass increment vs trapezoid integral of 8 pi r^2 y phi_v^2, U~1, B=0.03, v in [70,80] | 5.9e-5 | 1e-06 | 5.9e-05 |
| PASS | tab_end_v100_sigma_v | Table tab:end, v=100, sigma_v | -0.094251 | 1e-06 | -0.094251 |
| PASS | tab_end_v100_delta_sigma_v | Table tab:end, v=100, delta sigma_v | 3e-11 | 1e-11 | 3e-11 |
| PASS | tab_end_v100_G | Table tab:end, v=100, G | -0.092186 | 1e-06 | -0.092186 |
| PASS | tab_end_v100_v_sigma_v | Table tab:end, v=100, v sigma_v | -9.425 | 0.001 | -9.425 |
| PASS | tab_end_v100_z | Table tab:end, v=100, z | 5.64e-3 | 5.05e-06 | 0.005636 |
| PASS | tab_end_v100_dmdv | Table tab:end, v=100, dm/dv | 3.730 | 0.001 | 3.73 |
| PASS | tab_end_v100_closed | Table tab:end, v=100, closed | 3.693 | 0.001 | 3.693 |
| PASS | tab_end_v100_K | Table tab:end, v=100, K | 1.1e25 | 5.005e+23 | 1.1238e+25 |
| PASS | tab_end_v120_sigma_v | Table tab:end, v=120, sigma_v | -0.087733 | 1e-06 | -0.087733 |
| PASS | tab_end_v120_delta_sigma_v | Table tab:end, v=120, delta sigma_v | 2e-11 | 1e-11 | 2e-11 |
| PASS | tab_end_v120_G | Table tab:end, v=120, G | -0.087031 | 1e-06 | -0.087031 |
| PASS | tab_end_v120_v_sigma_v | Table tab:end, v=120, v sigma_v | -10.528 | 0.001 | -10.528 |
| PASS | tab_end_v120_z | Table tab:end, v=120, z | 3.27e-3 | 5.05e-06 | 0.0032684 |
| PASS | tab_end_v120_dmdv | Table tab:end, v=120, dm/dv | 3.848 | 0.001 | 3.848 |
| PASS | tab_end_v120_closed | Table tab:end, v=120, closed | 3.816 | 0.001 | 3.816 |
| PASS | tab_end_v120_K | Table tab:end, v=120, K | 1.7e25 | 5.005e+23 | 1.7188e+25 |
| PASS | tab_end_v140_sigma_v | Table tab:end, v=140, sigma_v | -0.079755 | 1e-06 | -0.079755 |
| PASS | tab_end_v140_delta_sigma_v | Table tab:end, v=140, delta sigma_v | 3e-11 | 1e-11 | 3e-11 |
| PASS | tab_end_v140_G | Table tab:end, v=140, G | -0.079363 | 1e-06 | -0.079363 |
| PASS | tab_end_v140_v_sigma_v | Table tab:end, v=140, v sigma_v | -11.166 | 0.001 | -11.166 |
| PASS | tab_end_v140_z | Table tab:end, v=140, z | 2.29e-3 | 5.05e-06 | 0.0022854 |
| PASS | tab_end_v140_dmdv | Table tab:end, v=140, dm/dv | 3.926 | 0.001 | 3.926 |
| PASS | tab_end_v140_closed | Table tab:end, v=140, closed | 3.896 | 0.001 | 3.896 |
| PASS | tab_end_v140_K | Table tab:end, v=140, K | 6.0e25 | 5.005e+23 | 5.9755e+25 |
| PASS | tab_end_v160_sigma_v | Table tab:end, v=160, sigma_v | -0.068968 | 1e-06 | -0.068968 |
| PASS | tab_end_v160_delta_sigma_v | Table tab:end, v=160, delta sigma_v | 6e-11 | 1e-11 | 6e-11 |
| PASS | tab_end_v160_G | Table tab:end, v=160, G | -0.068687 | 1e-06 | -0.068687 |
| PASS | tab_end_v160_v_sigma_v | Table tab:end, v=160, v sigma_v | -11.035 | 0.001 | -11.035 |
| PASS | tab_end_v160_z | Table tab:end, v=160, z | 1.75e-3 | 5.05e-06 | 0.001749 |
| PASS | tab_end_v160_dmdv | Table tab:end, v=160, dm/dv | 4.004 | 0.001 | 4.004 |
| PASS | tab_end_v160_closed | Table tab:end, v=160, closed | 3.976 | 0.001 | 3.976 |
| PASS | tab_end_v160_K | Table tab:end, v=160, K | 2.5e26 | 5.005e+24 | 2.4526e+26 |
| PASS | tab_end_v180_sigma_v | Table tab:end, v=180, sigma_v | -0.056255 | 1e-06 | -0.056255 |
| PASS | tab_end_v180_delta_sigma_v | Table tab:end, v=180, delta sigma_v | 2e-10 | 1e-10 | 2e-10 |
| PASS | tab_end_v180_G | Table tab:end, v=180, G | -0.056017 | 1e-06 | -0.056017 |
| PASS | tab_end_v180_v_sigma_v | Table tab:end, v=180, v sigma_v | -10.126 | 0.001 | -10.126 |
| PASS | tab_end_v180_z | Table tab:end, v=180, z | 1.41e-3 | 5.05e-06 | 0.0014111 |
| PASS | tab_end_v180_dmdv | Table tab:end, v=180, dm/dv | 4.086 | 0.001 | 4.086 |
| PASS | tab_end_v180_closed | Table tab:end, v=180, closed | 4.058 | 0.001 | 4.058 |
| PASS | tab_end_v180_K | Table tab:end, v=180, K | 8.6e26 | 5.005e+24 | 8.5925e+26 |
| PASS | tab_end_v200_sigma_v | Table tab:end, v=200, sigma_v | -0.043998 | 1e-06 | -0.043998 |
| PASS | tab_end_v200_delta_sigma_v | Table tab:end, v=200, delta sigma_v | 4e-10 | 1e-10 | 4e-10 |
| PASS | tab_end_v200_G | Table tab:end, v=200, G | -0.043779 | 1e-06 | -0.043779 |
| PASS | tab_end_v200_v_sigma_v | Table tab:end, v=200, v sigma_v | -8.800 | 0.001 | -8.8 |
| PASS | tab_end_v200_z | Table tab:end, v=200, z | 1.18e-3 | 5.05e-06 | 0.0011788 |
| PASS | tab_end_v200_dmdv | Table tab:end, v=200, dm/dv | 4.162 | 0.001 | 4.162 |
| PASS | tab_end_v200_closed | Table tab:end, v=200, closed | 4.135 | 0.001 | 4.135 |
| PASS | tab_end_v200_K | Table tab:end, v=200, K | 2.2e27 | 5.005e+25 | 2.2239e+27 |
| PASS | tab_end_v220_sigma_v | Table tab:end, v=220, sigma_v | -0.034253 | 1e-06 | -0.034253 |
| PASS | tab_end_v220_delta_sigma_v | Table tab:end, v=220, delta sigma_v | 1e-9 | 1e-09 | 1e-09 |
| PASS | tab_end_v220_G | Table tab:end, v=220, G | -0.034044 | 1e-06 | -0.034044 |
| PASS | tab_end_v220_v_sigma_v | Table tab:end, v=220, v sigma_v | -7.536 | 0.001 | -7.536 |
| PASS | tab_end_v220_z | Table tab:end, v=220, z | 1.01e-3 | 5.05e-06 | 0.0010098 |
| PASS | tab_end_v220_dmdv | Table tab:end, v=220, dm/dv | 4.222 | 0.001 | 4.222 |
| PASS | tab_end_v220_closed | Table tab:end, v=220, closed | 4.195 | 0.001 | 4.195 |
| PASS | tab_end_v220_K | Table tab:end, v=220, K | 4.3e27 | 5.005e+25 | 4.2557e+27 |
| PASS | tab_end_v240_sigma_v | Table tab:end, v=240, sigma_v | -0.027494 | 1e-06 | -0.027494 |
| PASS | tab_end_v240_delta_sigma_v | Table tab:end, v=240, delta sigma_v | 3e-9 | 1e-09 | 3e-09 |
| PASS | tab_end_v240_G | Table tab:end, v=240, G | -0.027293 | 1e-06 | -0.027293 |
| PASS | tab_end_v240_v_sigma_v | Table tab:end, v=240, v sigma_v | -6.599 | 0.001 | -6.599 |
| PASS | tab_end_v240_z | Table tab:end, v=240, z | 8.82e-4 | 5.05e-07 | 0.00088186 |
| PASS | tab_end_v240_dmdv | Table tab:end, v=240, dm/dv | 4.264 | 0.001 | 4.264 |
| PASS | tab_end_v240_closed | Table tab:end, v=240, closed | 4.238 | 0.001 | 4.238 |
| PASS | tab_end_v240_K | Table tab:end, v=240, K | 6.5e27 | 5.005e+25 | 6.5184e+27 |
| PASS | tab_end_v260_sigma_v | Table tab:end, v=260, sigma_v | -0.023090 | 1e-06 | -0.02309 |
| PASS | tab_end_v260_delta_sigma_v | Table tab:end, v=260, delta sigma_v | 5e-9 | 1e-09 | 5e-09 |
| PASS | tab_end_v260_G | Table tab:end, v=260, G | -0.022894 | 1e-06 | -0.022894 |
| PASS | tab_end_v260_v_sigma_v | Table tab:end, v=260, v sigma_v | -6.003 | 0.001 | -6.003 |
| PASS | tab_end_v260_z | Table tab:end, v=260, z | 7.82e-4 | 5.05e-07 | 0.00078197 |
| PASS | tab_end_v260_dmdv | Table tab:end, v=260, dm/dv | 4.292 | 0.001 | 4.292 |
| PASS | tab_end_v260_closed | Table tab:end, v=260, closed | 4.266 | 0.001 | 4.266 |
| PASS | tab_end_v260_K | Table tab:end, v=260, K | 8.7e27 | 5.005e+25 | 8.718e+27 |
| PASS | tab_end_v280_sigma_v | Table tab:end, v=280, sigma_v | -0.020206 | 1e-06 | -0.020206 |
| PASS | tab_end_v280_delta_sigma_v | Table tab:end, v=280, delta sigma_v | 4e-8 | 1e-08 | 4e-08 |
| PASS | tab_end_v280_G | Table tab:end, v=280, G | -0.020014 | 1e-06 | -0.020014 |
| PASS | tab_end_v280_v_sigma_v | Table tab:end, v=280, v sigma_v | -5.658 | 0.001 | -5.658 |
| PASS | tab_end_v280_z | Table tab:end, v=280, z | 7.02e-4 | 5.05e-07 | 0.00070203 |
| PASS | tab_end_v280_dmdv | Table tab:end, v=280, dm/dv | 4.310 | 0.001 | 4.31 |
| PASS | tab_end_v280_closed | Table tab:end, v=280, closed | 4.285 | 0.001 | 4.285 |
| PASS | tab_end_v280_K | Table tab:end, v=280, K | 1.1e28 | 5.005e+26 | 1.0834e+28 |
| PASS | tab_end_v300_sigma_v | Table tab:end, v=300, sigma_v | -0.018223 | 1e-06 | -0.018223 |
| PASS | tab_end_v300_delta_sigma_v | Table tab:end, v=300, delta sigma_v | 9e-6 | 1e-06 | 9e-06 |
| PASS | tab_end_v300_G | Table tab:end, v=300, G | -0.018030 | 1e-06 | -0.01803 |
| PASS | tab_end_v300_v_sigma_v | Table tab:end, v=300, v sigma_v | -5.467 | 0.001 | -5.467 |
| PASS | tab_end_v300_z | Table tab:end, v=300, z | 6.37e-4 | 5.05e-07 | 0.00063653 |
| PASS | tab_end_v300_dmdv | Table tab:end, v=300, dm/dv | 4.372 | 0.001 | 4.372 |
| PASS | tab_end_v300_closed | Table tab:end, v=300, closed | 4.299 | 0.001 | 4.299 |
| PASS | tab_end_v300_K | Table tab:end, v=300, K | 1.3e28 | 5.005e+26 | 1.2943e+28 |
| PASS | end_sv_100 | Sec. 9 The endpoint text: sigma_v rises from -0.094 at v=100 | -0.094 | 0.0005005 | -0.094251 |
| PASS | end_sv_300 | Sec. 9 The endpoint text: ... is -0.0182 at v=300 | -0.0182 | 5.05e-05 | -0.018223 |
| PASS | end_incr_180 | Sec. 9 The endpoint text: d sigma_v/dv = 6.4e-4 at v=180 (central difference over +-5 is not available; 10-unit forward difference 180->190 /10 and backward 170->180 averaged) | 6.4e-4 | 5e-06 (quoted to two digits (6.40e-4 from the 170-190 central difference)) | 0.0006406 |
| PASS | end_incr_230 | Sec. 9 The endpoint text: ... 3.4e-4 at v=230 (central difference 220-240) | 3.4e-4 | 5e-06 (quoted to two digits) | 0.00033795 |
| PASS | end_incr_280 | Sec. 9 The endpoint text: ... 1.2e-4 at v=280 (central difference 270-290) | 1.2e-4 | 5e-06 (quoted to two digits) | 0.0001186 |
| PASS | end_vsig_min | Sec. 9 The endpoint text: v sigma_v has a minimum -11.2 (near v=150) | -11.2 | 0.05 (-11.206 at v=150) | -11.206 |
| PASS | end_vsig_min_v | Sec. 9 The endpoint text: ... near v=150: v of the minimum | 150 | 0 (integer grid) | 150 |
| PASS | end_vsig_300 | Sec. 9 The endpoint text: rises to -5.47 at v=300 | -5.47 | 0.005 (-5.467) | -5.467 |
| PASS | end_vsig_290_B3e-4 | Sec. 9 The endpoint text: -5.58 at v=290 for B=3e-4 (endpoint_B0.0003.log) | -5.58 | 0.005 (-5.58 (rounded)) | -5.578 |
| PASS | end_dmdv_280 | Sec. 9 The endpoint text: dm/dv = 4.30 at v=280 (log 4.310; paper text 4.30 vs Table 4.310) | 4.31 | 0.0055 | 4.31 |
| PASS | end_closed_280 | Sec. 9 The endpoint text: closed form giving 4.29 at v=280 | 4.29 | 0.005 (4.285 rounds to 4.29) | 4.285 |
| PASS | end_zm_240 | Sec. 9 The endpoint text: zm = psi r^3/2 stays at 0.59: m*z at v=240 | 0.59 | 0.005 (m z = 0.5902) | 0.590317 |
| PASS | end_beta_inf | Eq. (dm): 2 r_- beta_inf kappa_- / c1^II -> 4.45 | 4.45 | 0.005 (4.4487 rounds to 4.45) | 4.44868 |
| PASS | tab_k_v100_c0_sigma | Table tab:k, v=100, k=1/2 B=3e-3: sigma_v | -0.04488 | 1e-05 | -0.04488 |
| PASS | tab_k_v100_c0_diff | Table tab:k, v=100, k=1/2 B=3e-3: sigma_v - G in 1e-4 | -16 | 1 | -16 |
| PASS | tab_k_v100_c1_sigma | Table tab:k, v=100, k=3/2 B=3e-4: sigma_v | -0.09908 | 1e-05 | -0.09908 |
| PASS | tab_k_v100_c1_diff | Table tab:k, v=100, k=3/2 B=3e-4: sigma_v - G in 1e-4 | -69 | 1 | -69 |
| PASS | tab_k_v100_c2_sigma | Table tab:k, v=100, k=3/2 B=3e-3: sigma_v | -0.09425 | 1e-05 | -0.09425 |
| PASS | tab_k_v100_c2_diff | Table tab:k, v=100, k=3/2 B=3e-3: sigma_v - G in 1e-4 | -21 | 1 | -21 |
| PASS | tab_k_v100_c3_sigma | Table tab:k, v=100, k=3/2 B=3e-2: sigma_v | -0.09306 | 1e-05 | -0.09306 |
| PASS | tab_k_v100_c3_diff | Table tab:k, v=100, k=3/2 B=3e-2: sigma_v - G in 1e-4 | -8.7 | 0.1 | -8.7 |
| PASS | tab_k_v100_c4_sigma | Table tab:k, v=100, k=3 B=3e-3: sigma_v | -0.10104 | 1e-05 | -0.10104 |
| PASS | tab_k_v100_c4_diff | Table tab:k, v=100, k=3 B=3e-3: sigma_v - G in 1e-4 | -22 | 1 | -22 |
| PASS | tab_k_v150_c0_sigma | Table tab:k, v=150, k=1/2 B=3e-3: sigma_v | -0.02497 | 1e-05 | -0.02497 |
| PASS | tab_k_v150_c0_diff | Table tab:k, v=150, k=1/2 B=3e-3: sigma_v - G in 1e-4 | -3.7 | 0.1 | -3.7 |
| PASS | tab_k_v150_c1_sigma | Table tab:k, v=150, k=3/2 B=3e-4: sigma_v | -0.07482 | 1e-05 | -0.07482 |
| PASS | tab_k_v150_c1_diff | Table tab:k, v=150, k=3/2 B=3e-4: sigma_v - G in 1e-4 | -4.4 | 0.1 | -4.4 |
| PASS | tab_k_v150_c2_sigma | Table tab:k, v=150, k=3/2 B=3e-3: sigma_v | -0.07471 | 1e-05 | -0.07471 |
| PASS | tab_k_v150_c2_diff | Table tab:k, v=150, k=3/2 B=3e-3: sigma_v - G in 1e-4 | -3.2 | 0.1 | -3.2 |
| PASS | tab_k_v150_c3_sigma | Table tab:k, v=150, k=3/2 B=3e-2: sigma_v | -0.07469 | 1e-05 | -0.07469 |
| PASS | tab_k_v150_c3_diff | Table tab:k, v=150, k=3/2 B=3e-2: sigma_v - G in 1e-4 | -3.1 | 0.1 | -3.1 |
| PASS | tab_k_v150_c4_sigma | Table tab:k, v=150, k=3 B=3e-3: sigma_v | -0.09839 | 1e-05 | -0.09839 |
| PASS | tab_k_v150_c4_diff | Table tab:k, v=150, k=3 B=3e-3: sigma_v - G in 1e-4 | -2.7 | 0.1 | -2.7 |
| PASS | tab_k_v200_c0_sigma | Table tab:k, v=200, k=1/2 B=3e-3: sigma_v | -0.01681 | 1e-05 | -0.01681 |
| PASS | tab_k_v200_c0_diff | Table tab:k, v=200, k=1/2 B=3e-3: sigma_v - G in 1e-4 | -2.4 | 0.1 | -2.4 |
| PASS | tab_k_v200_c1_sigma | Table tab:k, v=200, k=3/2 B=3e-4: sigma_v | -0.04402 | 1e-05 | -0.04402 |
| PASS | tab_k_v200_c1_diff | Table tab:k, v=200, k=3/2 B=3e-4: sigma_v - G in 1e-4 | -2.4 | 0.1 | -2.4 |
| PASS | tab_k_v200_c2_sigma | Table tab:k, v=200, k=3/2 B=3e-3: sigma_v | -0.04400 | 1e-05 | -0.044 |
| PASS | tab_k_v200_c2_diff | Table tab:k, v=200, k=3/2 B=3e-3: sigma_v - G in 1e-4 | -2.2 | 0.1 | -2.2 |
| PASS | tab_k_v200_c3_dash | Table tab:k, v=200, k=3/2 B=3e-2: "--" (beyond the accurate range; no value in ktable.log) | 1 | 0 (1 = the entry is "--") | 1 |
| PASS | tab_k_v200_c4_sigma | Table tab:k, v=200, k=3 B=3e-3: sigma_v | -0.09812 | 1e-05 | -0.09812 |
| PASS | tab_k_v200_c4_diff | Table tab:k, v=200, k=3 B=3e-3: sigma_v - G in 1e-4 | -1.9 | 0.1 | -1.9 |
| PASS | tab_k_v250_c0_sigma | Table tab:k, v=250, k=1/2 B=3e-3: sigma_v | -0.01295 | 1e-05 | -0.01295 |
| PASS | tab_k_v250_c0_diff | Table tab:k, v=250, k=1/2 B=3e-3: sigma_v - G in 1e-4 | -2.2 | 0.1 | -2.2 |
| PASS | tab_k_v250_c1_sigma | Table tab:k, v=250, k=3/2 B=3e-4: sigma_v | -0.02507 | 1e-05 | -0.02507 |
| PASS | tab_k_v250_c1_diff | Table tab:k, v=250, k=3/2 B=3e-4: sigma_v - G in 1e-4 | -2.2 | 0.1 | -2.2 |
| PASS | tab_k_v250_c2_sigma | Table tab:k, v=250, k=3/2 B=3e-3: sigma_v | -0.02505 | 1e-05 | -0.02505 |
| PASS | tab_k_v250_c2_diff | Table tab:k, v=250, k=3/2 B=3e-3: sigma_v - G in 1e-4 | -2.0 (manuscript: $-0.02505$ ($-1.9$)) | 0.1 | -2 |
| PASS | tab_k_v250_c3_dash | Table tab:k, v=250, k=3/2 B=3e-2: "--" (beyond the accurate range; no value in ktable.log) | 1 | 0 (1 = the entry is "--") | 1 |
| PASS | tab_k_v250_c4_dash | Table tab:k, v=250, k=3 B=3e-3: "--" (beyond the accurate range; no value in ktable.log) | 1 | 0 (1 = the entry is "--") | 1 |
| PASS | tab_k_v290_c0_sigma | Table tab:k, v=290, k=1/2 B=3e-3: sigma_v | -0.01111 | 1e-05 | -0.01111 |
| PASS | tab_k_v290_c0_diff | Table tab:k, v=290, k=1/2 B=3e-3: sigma_v - G in 1e-4 | -2.8 | 0.1 | -2.8 |
| PASS | tab_k_v290_c1_sigma | Table tab:k, v=290, k=3/2 B=3e-4: sigma_v | -0.01923 | 1e-05 | -0.01923 |
| PASS | tab_k_v290_c1_diff | Table tab:k, v=290, k=3/2 B=3e-4: sigma_v - G in 1e-4 | -3.0 | 0.1 | -3 |
| PASS | tab_k_v290_c2_sigma | Table tab:k, v=290, k=3/2 B=3e-3: sigma_v | -0.01913 | 1e-05 | -0.01913 |
| PASS | tab_k_v290_c2_diff | Table tab:k, v=290, k=3/2 B=3e-3: sigma_v - G in 1e-4 | -1.9 | 0.1 | -1.9 |
| PASS | tab_k_v290_c3_dash | Table tab:k, v=290, k=3/2 B=3e-2: "--" (beyond the accurate range; no value in ktable.log) | 1 | 0 (1 = the entry is "--") | 1 |
| PASS | tab_k_v290_c4_dash | Table tab:k, v=290, k=3 B=3e-3: "--" (beyond the accurate range; no value in ktable.log) | 1 | 0 (1 = the entry is "--") | 1 |
| PASS | k_diff_min | Sec. 9 Other amplitudes and tail exponents text: sigma_v - G = -(1.9-3.0)e-4 for all five cases at v>=200 (Table rows v=200,250,290): smallest /diff/ | 1.9 | 0.05 (quoted to two digits) | 1.9 |
| PASS | k_diff_max | Sec. 9 Other amplitudes and tail exponents text: ... largest /diff/ | 3.0 | 0.05 (quoted to two digits) | 3 |
| PASS | k_diff150_min | Sec. 9 Other amplitudes and tail exponents text: -(2.7-4.4)e-4 at v=150: smallest | 2.7 | 0.05 (quoted to two digits) | 2.7 |
| PASS | k_diff150_max | Sec. 9 Other amplitudes and tail exponents text: ... largest | 4.4 | 0.05 (quoted to two digits) | 4.4 |
| PASS | k_factor_5.8 | Sec. 9 Other amplitudes and tail exponents text: sigma_v differs by a factor 5.8 between k=1/2 and k=3 at v=200 | 5.8 | 0.05 (0.09812/0.01681 = 5.84) | 5.837 |
| PASS | k_limit_k05 | Table tab:k caption: limiting value -(2k+2)/v at v=290, k=1/2 | -0.010 | 0.0005 (-3/290 = -0.01034) | -0.0103448 |
| PASS | k_limit_k15 | Table tab:k caption: ... k=3/2 | -0.017 | 0.0005 (-5/290 = -0.01724) | -0.0172414 |
| PASS | k_limit_k3 | Table tab:k caption: ... k=3 | -0.028 | 0.0005 (-8/290 = -0.02759) | -0.0275862 |
| PASS | k3_plateau_min | Sec. 9 Other amplitudes and tail exponents text: for k=3 sigma_v sits on a plateau -0.098 to -0.099 at 120<=v<=190 (endpoint_k3.log): smallest /sigma_v/ | 0.098 | 0.0005 (quoted to three digits) | 0.098095 |
| PASS | k3_plateau_max | Sec. 9 Other amplitudes and tail exponents text: ... largest /sigma_v/ | 0.099 | 0.0005 (quoted to three digits) | 0.099091 |
| PASS | k3_two_kappa | Sec. 9 Other amplitudes and tail exponents text: ... which is -2 kappa_+ = -0.0979 | 0.0979 | 0.0001 (2 kappa_+ = 0.097937) | 0.0979375 |
| PASS | k05_vsig_100 | Sec. 9 Other amplitudes and tail exponents text: k=1/2: v sigma_v = -4.49 at v=100 | -4.49 | 0.005 (-4.488) | -4.488 |
| PASS | k05_vsig_150 | Sec. 9 Other amplitudes and tail exponents text: ... -3.75 at v=150 | -3.75 | 0.005 (-3.7455) | -3.746 |
| PASS | k05_vsig_200 | Sec. 9 Other amplitudes and tail exponents text: ... -3.36 at v=200 | -3.36 | 0.005 (-3.362) | -3.362 |
| PASS | k05_vsig_290 | Sec. 9 Other amplitudes and tail exponents text: ... -3.22 at v=290 | -3.22 | 0.005 (-3.222) | -3.221 |
| PASS | k05_kernel_200 | Sec. 9 Other amplitudes and tail exponents text: the kernel gives -3.31 at v=200 (k=1/2, G*v) | -3.31 | 0.005 (G*v from the G column) | -3.3136 |
| PASS | slaving_a_phi | Sec. 9 Behind the front (slaving)(a): phi_v varies by 3e-6 across 10<=x<=2e4 (largest of the three times) | 3e-6 | 1e-06 (3.06e-6, 2.89e-6, 2.76e-6) | 3.06e-06 |
| PASS | slaving_d_yrho | Sec. 9 Behind the front (slaving)(d): y rho = beta to 1e-6 (largest /y rho/beta - 1/ over the three times) | 1e-6 | bound: <= paper | 1e-12 |
| PASS | slaving_dm_closed_100 | Sec. 9 Behind the front (slaving) (dm): closed form against direct at v=100 (slaving.log: 3.787 vs 3.793; difference below 0.8%) | 0.8e-2 | bound: <= paper | 0.00282624 |
| PASS | slaving_b_rho_v100 | Sec. 9 Behind the front (slaving)(b): relative variation of rho between x=40 and the largest x printed, v=100 (range over mean of the printed rows) | 1e-4 | 5e-05 | 0.000110939 |
| PASS | slaving_b_rho_v150 | Sec. 9 Behind the front (slaving)(b): relative variation of rho between x=40 and the largest x printed, v=150 (range over mean of the printed rows) | 2e-3 | 0.0005 | 0.00170916 |
| PASS | slaving_b_rho_v200 | Sec. 9 Behind the front (slaving)(b): relative variation of rho between x=40 and the largest x printed, v=200 (range over mean of the printed rows) | 2e-2 | 0.005 | 0.0212751 |
| PASS | slaving_c_mid_v100 | Sec. 9 Behind the front (slaving)(c): rho_v/rho = sigma_v + S/rho, mid-value for 30<=x<=200, v=100 | -0.0922 | 5e-05 (mid-point of the printed rows; the manuscript quotes it with a symmetric error bar) | -0.09225 |
| PASS | slaving_c_halfrange_v100 | Sec. 9 Behind the front (slaving)(c): ... half range (the "+-" of the manuscript) for 30<=x<=200, v=100 | 1e-4 | bound: <= paper | 3e-05 |
| PASS | slaving_c_mid_v150 | Sec. 9 Behind the front (slaving)(c): rho_v/rho = sigma_v + S/rho, mid-value for 40<=x<=2330, v=150 | -0.07438 | 1e-05 (mid-point of the printed rows; the manuscript quotes it with a symmetric error bar) | -0.074375 |
| PASS | slaving_c_halfrange_v150 | Sec. 9 Behind the front (slaving)(c): ... half range (the "+-" of the manuscript) for 40<=x<=2330, v=150 | 2e-5 | bound: <= paper | 1.5e-05 |
| PASS | slaving_c_mid_v200 | Sec. 9 Behind the front (slaving)(c): rho_v/rho = sigma_v + S/rho, mid-value for 60<=x<=10000, v=200 | -0.0432 | 5e-05 (mid-point of the printed rows; the manuscript quotes it with a symmetric error bar) | -0.0432 |
| PASS | slaving_c_halfrange_v200 | Sec. 9 Behind the front (slaving)(c): ... half range (the "+-" of the manuscript) for 60<=x<=10000, v=200 | 1e-4 | bound: <= paper | 8e-05 |
| PASS | slaving_c_Sr_plateau_min | Sec. 9 Behind the front (slaving)(c): in the plateau S/rho = 0.70-0.73 (smallest; rows x=25,30 at v=100, 30,40 at v=150, 40,60 at v=200) | 0.70 | 0.005 (0.7017) | 0.70165 |
| PASS | slaving_c_Sr_plateau_max | Sec. 9 Behind the front (slaving)(c): ... largest | 0.73 | 0.005 (0.7346) | 0.73464 |
| PASS | slaving_c_Sr_behind | Sec. 9 Behind the front (slaving)(c): behind the front (x>=2 x_f) S/rho <~ 5e-3 (largest value in the printed rows with x >= 2 x_f, x_f = 44, 72, 100) | 5e-3 | 0.0005 ("<~": 5.2e-3 at v=150) | 0.00524 |
| PASS | slaving_c_c1_behind | Sec. 9 Behind the front (slaving)(c): behind the front c_1 = z^2 <~ 1e-4 (largest z^2 in the printed rows with x >= 2 x_f) | 1e-4 | bound: <= paper | 8.06045e-05 |
| PASS | slaving_c_sigma_plateau | Sec. 9 Behind the front (slaving)(c): in the plateau sigma_v = -kappa_-(m_f) (x=25, v=100: -0.79502 against -0.79565) | -0.795 | 0.001 (plateau value to 1e-3: -0.79502 (v=100), -0.79372 (v=150) and -0.77779 (v=200) drift with the front passage; only the first is at the plateau value) | -0.79502 |
| PASS | gpred_ratio_100 | Sec. 9 Behind the front (slaving)(a): Phi_PDE/Phi_kernel = 1.0001 at v=100 | 1.0001 | 5.5e-05 | 1.0001 |
| PASS | gpred_ratio_min | Sec. 9 Behind the front (slaving)(a): Phi_PDE/Phi_kernel = 1.0006 for 150<=v<=250 (smallest of the printed values 150, 180, 200, 220, 240, 250) | 1.0006 | 0.0001 (1.00058 ... 1.00062) | 1.00058 |
| PASS | gpred_ratio_max | Sec. 9 Behind the front (slaving)(a): ... largest | 1.0006 | 0.0001 (1.00062) | 1.00062 |
| PASS | gpred_ratio_upper | Sec. 9 Behind the front (slaving)(a): the range of v over which the ratio rounds to 1.0006 ends at v=250 (manuscript: 260; at 260 the ratio is 1.0005) | 250 (manuscript: 1.0006$ for $150\le v\le260$) | 0 (integer grid of the log) | 250 |
| PASS | rhocheck_defect_v200 | Sec. 9 Behind the front (slaving)(d): the last two terms (r_uv/r_u - beta_v/beta) are -9e-5 at v=200 | -9e-5 | 1e-05 (-9.416e-5) | -9.416e-05 |
| PASS | rhocheck_sigma_v200 | Sec. 9 Behind the front (slaving)(d): sigma_v = -0.0438 at v=200 (it is d sg/dv from rho_check.log, third table; the extrapolated sigma_v of Table tab:end is -0.0440, i.e. 1.6e-4 lower: the h_s-systematic) | -0.0438 | 5e-05 (-0.043838) | -0.043838 |
| PASS | rhocheck_decreasing | Sec. 9 Behind the front (slaving)(d): the last two terms decrease faster than 1/v: /v*sum/ decreases monotonically over v = 100, 140, 180, 200, 220, 240, 250 (1 = yes) | 1 | 0 (boolean) | 1 |
| PASS | hsextrap_resid_v180 | Sec. 9 Behind the front (slaving): residual sigma_v - G after the h_s -> 0 extrapolation at v=180 (hs_extrap.log) | -7.5e-5 | 5.5e-07 | -7.49e-05 |
| PASS | hsextrap_resid_v200 | Sec. 9 Behind the front (slaving): residual sigma_v - G after the h_s -> 0 extrapolation at v=200 (hs_extrap.log) | -5.6e-5 | 5.5e-07 | -5.61e-05 |
| PASS | hsextrap_resid_v220 | Sec. 9 Behind the front (slaving): residual sigma_v - G after the h_s -> 0 extrapolation at v=220 (hs_extrap.log) | -4.3e-5 | 5.5e-07 | -4.28e-05 |
| PASS | hsextrap_rel | Sec. 9 Behind the front (slaving): ... 0.13% of G | 0.0013 | 5e-05 (0.0013) | 0.0013 |
| PASS | sigma_minus_G_v100 | Sec. 9 Behind the front (slaving): sigma_v - G at v=100 (Table tab:end) | -2.1e-3 | 5e-05 (difference of two six-digit numbers (-2.065e-3, -3.24e-4, -2.19e-4, -1.98e-4)) | -0.002065 |
| PASS | sigma_minus_G_v150 | Sec. 9 Behind the front (slaving): sigma_v - G at v=150 (Table tab:end) | -3.2e-4 | 5e-06 (difference of two six-digit numbers (-2.065e-3, -3.24e-4, -2.19e-4, -1.98e-4)) | -0.000324 |
| PASS | sigma_minus_G_v200 | Sec. 9 Behind the front (slaving): sigma_v - G at v=200 (Table tab:end) | -2.2e-4 | 5e-06 (difference of two six-digit numbers (-2.065e-3, -3.24e-4, -2.19e-4, -1.98e-4)) | -0.000219 |
| PASS | sigma_minus_G_v250 | Sec. 9 Behind the front (slaving): sigma_v - G at v=250 (Table tab:end) | -2.0e-4 | 5e-06 (difference of two six-digit numbers (-2.065e-3, -3.24e-4, -2.19e-4, -1.98e-4)) | -0.000198 |
| PASS | dm_closed_pct | Sec. 9 Behind the front (slaving): the closed form gives dm/dv to 0.8% (mean of the relative differences of the two quoted cases, v=100: 0.99%, v=200: 0.65%) | 0.008 | 0.0005 (0.82%; the individual differences are 0.99% and 0.65%, the quoted figure is their mean) | 0.00820342 |
| PASS | bounded_aniso_diff_v95 | Sec. 9 Behind the front (slaving): bounded model sigma_v - rho_v/rho at v=95 (bounded_aniso.log) | -3.6e-4 | 5e-06 | -0.000362 |
| PASS | bounded_aniso_diff_v110 | Sec. 9 Behind the front (slaving): bounded model sigma_v - rho_v/rho at v=110 (bounded_aniso.log) | -1.8e-4 | 5e-06 | -0.000185 |
| PASS | bounded_aniso_diff_v125 | Sec. 9 Behind the front (slaving): bounded model sigma_v - rho_v/rho at v=125 (bounded_aniso.log) | -1.0e-4 | 1e-05 (1.05e-4 printed to 3 digits and quoted as 1.0e-4) | -0.000105 |
| PASS | bounded_aniso_sigma_v95 | Sec. 9 Behind the front (slaving): bounded model sigma_v at v=95 | -0.0552 | 5.5e-05 | -0.05518 |
| PASS | bounded_aniso_sigma_v110 | Sec. 9 Behind the front (slaving): bounded model sigma_v at v=110 | -0.0470 | 5.5e-05 | -0.04702 |
| PASS | bounded_aniso_sigma_v125 | Sec. 9 Behind the front (slaving): bounded model sigma_v at v=125 | -0.0411 | 5.5e-05 | -0.04111 |
| PASS | bounded_aniso_Phi_max | Sec. 9 Behind the front (slaving): 2 dln/Phi//dv is within 2-3% of rho_v/rho (an upper bound: largest relative difference over v=95..125 is 1.6%, 1.1% at 125) | 3e-2 | bound: <= paper | 0.0156877 |
| PASS | phi_monotone_ratio | Sec. 9 Asymptotics of the slaved description (i): /Phi(v+1)/Phi(v)/ < 0.9988 on 20<=v<=1200 for k = 1/2, 1, 3/2, 2, 3 (largest ratio; phi_monotone.log) | 0.9988 | bound: <= paper | 0.998741 |
| PASS | phi_monotone_all_decreasing | Sec. 9 Asymptotics of the slaved description (i): strictly decreasing /Phi/ for all five exponents (number of exponents for which it is True) | 5 | 0 (integer count) | 5 |
| PASS | asym_corr_v200 | Sec. 9 Asymptotics of the slaved description (ii): corrections of relative size (k+1)/(kappa_+ v) = 0.26 at v=200 | 0.26 | 0.005 (2.5/(0.04897*200) = 0.2553) | 0.255265 |
| PASS | asym_vG_200 | Sec. 9 Asymptotics of the slaved description (ii): kernel prediction v G (k=3/2) at v=200 (gpred_final.log) | -8.76 | 0.0055 | -8.756 |
| PASS | asym_vG_400 | Sec. 9 Asymptotics of the slaved description (ii): kernel prediction v G (k=3/2) at v=400 (gpred_final.log) | -5.16 | 0.0055 | -5.164 |
| PASS | asym_vG_1000 | Sec. 9 Asymptotics of the slaved description (ii): kernel prediction v G (k=3/2) at v=1000 (gpred_final.log) | -5.05 | 0.0055 | -5.053 |
| PASS | asym_vG_2000 | Sec. 9 Asymptotics of the slaved description (ii): kernel prediction v G (k=3/2) at v=2000 (gpred_final.log) | -5.03 | 0.0055 | -5.028 |
| PASS | asym_vsigma_200 | Sec. 9 Asymptotics of the slaved description (ii): ... against -8.80 at v=200 in Table tab:end | -8.80 | 0.0055 | -8.8 |
| PASS | asym_dlnru | Sec. 9 Asymptotics of the slaved description (iii): d ln/r_u//dv = -1.4e-7 at v=200 (rho_check.log) | -1.4e-7 | 5e-09 (-1.373e-7) | -1.373e-07 |
| PASS | asym_W_index | Sec. 9 Asymptotics of the slaved description (iii): W ~ v^-5.1 (simulated: local power index of W at the end of the trust window, tidal_v600.log; manuscript Sec. curv2: 5.1 to 5.2) | 5.17 | 0.005 (5.17) | 5.17 |
| PASS | k05_K_100 | Sec. 9 Asymptotics of the slaved description (iii): k=1/2: K = 2.1e21 at v=100 (endpoint_k0.5.log) | 2.1e21 | 5e+19 (2.07e21) | 2.0692e+21 |
| PASS | k05_K_290 | Sec. 9 Asymptotics of the slaved description (iii): k=1/2: K = 3.0e19 at v=290 | 3.0e19 | 5e+17 (3.0153e19) | 3.0153e+19 |
| PASS | k3_K_100 | Sec. 9 Asymptotics of the slaved description (iii): k=3: K = 4.9e25 at v=100 (endpoint_k3.log) | 4.9e25 | 5e+23 (4.945e25) | 4.945e+25 |
| PASS | k3_K_190 | Sec. 9 Asymptotics of the slaved description (iii): k=3: K = 3.8e29 at v=190 | 3.8e29 | 5e+27 (quoted to two digits) | 3.7762e+29 |
| PASS | KzPhi_ratio_A | Sec. 9 Asymptotics of the slaved description (iii): K z^-6 Phi^4 changes by a factor 1.7 ... over 100<=v<=280 (B=3e-3: ratio of the values at v=280 and 100, merged file) | 1.8 | 0.05 (7.4459e19/4.1534e19 = 1.79; the manuscript range 1.7-2.2 covers both amplitudes) | 1.79272 |
| PASS | KzPhi_ratio_min | Sec. 9 Asymptotics of the slaved description (iii): ... smallest ratio over the two runs of the unmerged B=3e-3 file to v=240 (curv_hv.log) | 1.7 | 0.05 (7.1219e19/4.1534e19 = 1.715) | 1.71472 |
| PASS | KzPhi_ratio_B3e-4 | Sec. 9 Asymptotics of the slaved description (iii): ... and for B=3e-4 to v=280 (curv_hv_B0.0003.log) | 2.2 | 0.05 (ratio of the first and the last printed value) | 2.17184 |
| PASS | K_changes_1e3 | Sec. 9 Asymptotics of the slaved description (iii): while K changes by 10^3 over 100<=v<=280 (ratio of K(280) and K(100), merged file) | 1e3 | 50 (K(280)/K(100) = 964) | 964.051 |
| PASS | z_exp_280 | Sec. 9 Asymptotics of the slaved description (iii): the local exponent of z is -1.43 at v=280 (curv_hv on the merged file) | -1.43 | 0.01 | -1.43 |
| PASS | z_exp_380 | Sec. 9 Asymptotics of the slaved description (iii): ... and -1.29 at 380 (kstudy_v600.log, code B) | -1.29 | 0.005 (-1.294) | -1.294 |
| PASS | kslope_300 | Sec. 9 Asymptotics of the slaved description: local slope of K, 2.5 at v=300 (code B) | 2.5 | 0.05 (2.52) | 2.52 |
| PASS | curv_static_hay | Sec. 9 Curvature: the Kretschmann formula agrees with f''^2+4f'^2/r^2+4(1-f)^2/r^4 on the static Hayward interior to 3.4e-7 | 3.4e-7 | 1e-08 | 3.4e-07 |
| PASS | curv_static_bnd | Sec. 9 Curvature: ... and bounded interior to 7.2e-8 | 7.2e-8 | 1e-09 | 7.2e-08 |
| PASS | curv_dS | Sec. 9 Curvature: K = 24 l^-4 (de Sitter value) at the pole: 4 psi^2 + 8 Q^2/2 with psi = 1, Q = -2 | 24 | 0 (exact arithmetic: 4 + 8*(4/2) + (4 Sigma)^2 with Sigma = psi/2 - c2 = 1/2 -> (4*0.5)^2 = 4: 4+16+4 = 24) | 24 |
| PASS | curv_maxK_U0.300 | Sec. 9 Curvature: maximum of K on U~0.300 (curv_m1_B0.003.log) -- at v=103 | 2.9e32 | 5.5e+30 | 2.94e+32 |
| PASS | curv_maxK_U0.600 | Sec. 9 Curvature: maximum of K on U~0.600 (curv_m1_B0.003.log) -- at v=85 | 4.7e29 | 5.5e+27 | 4.74e+29 |
| PASS | curv_maxK_U0.999 | Sec. 9 Curvature: maximum of K on U~0.999 (curv_m1_B0.003.log) -- at v=72 | 2.8e27 | 5.5e+25 | 2.77e+27 |
| PASS | curv_K_U1_v80 | Sec. 9 Curvature: K on U~1 at v=80 (late_m1_B0.003_v200.log, ray U=0.999) | 1.4e26 | 5.05e+24 | 1.422e+26 |
| PASS | curv_K_U1_v100 | Sec. 9 Curvature: K on U~1 at v=100 (late_m1_B0.003_v200.log, ray U=0.999) | 1.1e25 | 5.05e+23 | 1.093e+25 |
| PASS | curv_K_U1_v120 | Sec. 9 Curvature: K on U~1 at v=120 (late_m1_B0.003_v200.log, ray U=0.999) | 1.7e25 | 5.05e+23 | 1.676e+25 |
| PASS | curv_K_U1_v140 | Sec. 9 Curvature: K on U~1 at v=140 (late_m1_B0.003_v200.log, ray U=0.999) | 5.8e25 | 5.05e+23 | 5.83e+25 |
| PASS | curv_K_U1_v160 | Sec. 9 Curvature: K on U~1 at v=160 (late_m1_B0.003_v200.log, ray U=0.999) | 2.4e26 | 5.05e+24 | 2.393e+26 |
| PASS | curv_terms_v100_1 | Sec. 9 Curvature: terms of Sigma on U~1 at v=100, column 1 (curv_terms_m1_B0.003.log) | 0.50 | 0.0055 | 0.497 |
| PASS | curv_terms_v100_2 | Sec. 9 Curvature: terms of Sigma on U~1 at v=100, column 2 (curv_terms_m1_B0.003.log) | -0.025 | 0.00055 | -0.0251 |
| PASS | curv_terms_v100_3 | Sec. 9 Curvature: terms of Sigma on U~1 at v=100, column 3 (curv_terms_m1_B0.003.log) | -4.8e4 | 505 | -48310 |
| PASS | curv_terms_v100_4 | Sec. 9 Curvature: terms of Sigma on U~1 at v=100, column 4 (curv_terms_m1_B0.003.log) | 8.3e11 | 5.05e+09 | 8.266e+11 |
| PASS | curv_compat_3e-12 | Sec. 9 Curvature: agrees with the compatibility condition (3e-12) | 3e-12 | 5e-13 (3.4e-12) | 3.41e-12 |
| PASS | curv_later_K_v190 | Sec. 9 Curvature later times: K on U~1 at v=190 (Table tab:end) | 1.4e27 | 5.005e+25 | 1.4396e+27 |
| PASS | curv_later_K_v220 | Sec. 9 Curvature later times: K on U~1 at v=220 (Table tab:end) | 4.3e27 | 5.005e+25 | 4.2557e+27 |
| PASS | curv_later_K_v240 | Sec. 9 Curvature later times: K on U~1 at v=240 (Table tab:end) | 6.5e27 | 5.005e+25 | 6.5184e+27 |
| PASS | curv_later_K_v280 | Sec. 9 Curvature later times: K = 1.3e28 at v=300 (the manuscript writes "at 280"; Table tab:end has 1.1e28 at 280 and 1.3e28 at 300) | 1.3e28 (manuscript: $1.3\times10^{28}$ at $280$ (Table~\ref{tab:end})) | 5e+26 (1.2943e28) | 1.2943e+28 |
| PASS | curv_slope_160 | Sec. 9 Curvature later times: dlnK/dlnv = 10.9 at v=160 (curv_hv.log) | 10.9 | 0.05 (10.94) | 10.94 |
| PASS | curv_slope_240 | Sec. 9 Curvature later times: ... and 4.2 at v=240 | 4.2 | 0.05 (4.23) | 4.23 |
| PASS | curv_B3e-4_K100 | Sec. 9 Curvature: B=3e-4: K = 3.6e34 at v=100 (curv_hv_B0.0003.log) | 3.6e34 | 5e+32 (3.6252e34) | 3.6252e+34 |
| PASS | curv_B3e-4_K120 | Sec. 9 Curvature: ... 1.1e34 at 120 | 1.1e34 | 5e+32 (1.1304e34) | 1.1304e+34 |
| PASS | curv_B3e-4_K290 | Sec. 9 Curvature: ... 1.7e36 at v=290 (endpoint_B0.0003.log) | 1.7e36 | 5e+34 (1.6871e36) | 1.6871e+36 |
| PASS | curv_B3e-4_slope170 | Sec. 9 Curvature: ... slope 9.1 at v=170 | 9.1 | 0.05 (9.06) | 9.06 |
| PASS | curv_B3e-4_slope280 | Sec. 9 Curvature: ... slope 2.1 at v=280 | 2.1 | 0.05 (2.12) | 2.12 |
| PASS | window_dlev_v80 | Sec. 8 What limits the window: inter-level difference of sigma_v on U~0.3 at v=80 (endpoint_m1_B0.003_v200.log) | 3e-10 | 5e-11 (3.3e-10 printed to 2 digits) | 3.3e-10 |
| PASS | window_dlev_v160 | Sec. 8 What limits the window: inter-level difference of sigma_v on U~0.3 at v=160 (endpoint_m1_B0.003_v200.log) | 1.4e-6 | 1e-07 | 1.4e-06 |
| PASS | window_dlev_v180 | Sec. 8 What limits the window: inter-level difference of sigma_v on U~0.3 at v=180 (endpoint_m1_B0.003_v200.log) | 3.4e-5 | 1e-06 | 3.4e-05 |
| PASS | window_dlev_v190 | Sec. 8 What limits the window: inter-level difference of sigma_v on U~0.3 at v=190 (endpoint_m1_B0.003_v200.log) | 2.2e-4 | 1e-05 | 0.00022 |
| PASS | window_B003_Sigma90 | Sec. 8 What limits the window: B=3e-2: inter-level difference of Sigma on U~1 is 1.0e-2 (relative) at v=90 (late_m1_B0.03.log) | 1.0e-2 | 0.001 | 0.01 |
| PASS | window_B003_Sigma100 | Sec. 8 What limits the window: ... and 0.19 at v=100 | 0.19 | 0.01 | 0.19 |
| PASS | window_B003_nonfinite120 | Sec. 8 What limits the window: ... and the run is non-finite at v=120 (late_m1_B0.03_v200.log; 1 = non-finite) | 1 | 0 (boolean) | 1 |
| PASS | window_B0003_end110 | Sec. 8 What limits the window: B=3e-4: the run ends at v=110 inside the window (the last printed row of late_m1_B0.0003.log is v=108, finite; 1 = finite) | 1 | 0 (boolean) | 1 |
| PASS | tab_vb_B0.003_h0.05_measured | Table tab:vb, B=0.003, h_v=0.05: measured first non-finite sample (vb_law.log) | 206 | 0 (integer sampling) | 206 |
| PASS | tab_vb_B0.003_h0.05_law | Table tab:vb, B=0.003, h_v=0.05: Eq. (vb) | 205.2 | 0.1 | 205.2 |
| PASS | tab_vb_B0.003_h0.025_measured | Table tab:vb, B=0.003, h_v=0.025: measured first non-finite sample (vb_law.log) | 234 | 0 (integer sampling) | 234 |
| PASS | tab_vb_B0.003_h0.025_law | Table tab:vb, B=0.003, h_v=0.025: Eq. (vb) | 233.6 | 0.1 | 233.6 |
| PASS | tab_vb_B0.003_h0.0125_measured | Table tab:vb, B=0.003, h_v=0.0125: measured first non-finite sample (vb_law.log) | 262 | 0 (integer sampling) | 262 |
| PASS | tab_vb_B0.003_h0.0125_law | Table tab:vb, B=0.003, h_v=0.0125: Eq. (vb) | 261.9 | 0.1 | 261.9 |
| PASS | tab_vb_B0.003_h0.00625_measured | Table tab:vb, B=0.003, h_v=0.00625: measured first non-finite sample (vb_law.log) | 291 | 0 (integer sampling) | 291 |
| PASS | tab_vb_B0.003_h0.00625_law | Table tab:vb, B=0.003, h_v=0.00625: Eq. (vb) | 290.2 | 0.1 | 290.2 |
| PASS | tab_vb_B0.003_h0.003125_measured | Table tab:vb, B=0.003, h_v=0.003125: measured first non-finite sample (vb_law.log) | 319 | 0 (integer sampling) | 319 |
| PASS | tab_vb_B0.003_h0.003125_law | Table tab:vb, B=0.003, h_v=0.003125: Eq. (vb) | 318.5 | 0.1 | 318.5 |
| PASS | tab_vb_B0.003_h0.0015625_measured | Table tab:vb, B=0.003, h_v=0.0015625: measured first non-finite sample (vb_law.log) | 347 | 0 (integer sampling) | 347 |
| PASS | tab_vb_B0.003_h0.0015625_law | Table tab:vb, B=0.003, h_v=0.0015625: Eq. (vb) | 346.8 | 0.1 | 346.8 |
| PASS | tab_vb_B0.03_h0.0125_measured | Table tab:vb, B=0.03, h_v=0.0125: measured first non-finite sample (vb_law.log) | 169 | 0 (integer sampling) | 169 |
| PASS | tab_vb_B0.03_h0.0125_law | Table tab:vb, B=0.03, h_v=0.0125: Eq. (vb) | 167.8 | 0.1 | 167.8 |
| PASS | tab_vb_B0.03_h0.00625_measured | Table tab:vb, B=0.03, h_v=0.00625: measured first non-finite sample (vb_law.log) | 197 | 0 (integer sampling) | 197 |
| PASS | tab_vb_B0.03_h0.00625_law | Table tab:vb, B=0.03, h_v=0.00625: Eq. (vb) | 196.1 | 0.1 | 196.1 |
| PASS | tab_vb_B0.03_h0.003125_measured | Table tab:vb, B=0.03, h_v=0.003125: measured first non-finite sample (vb_law.log) | 225 | 0 (integer sampling) | 225 |
| PASS | tab_vb_B0.03_h0.003125_law | Table tab:vb, B=0.03, h_v=0.003125: Eq. (vb) | 224.4 | 0.1 | 224.4 |
| PASS | tab_vb_B0.03_h0.0015625_measured | Table tab:vb, B=0.03, h_v=0.0015625: measured first non-finite sample (vb_law.log) | 254 | 0 (integer sampling) | 254 |
| PASS | tab_vb_B0.03_h0.0015625_law | Table tab:vb, B=0.03, h_v=0.0015625: Eq. (vb) | 252.8 | 0.1 | 252.8 |
| PASS | tab_vb_B0.0003_h0.0125_law | Table tab:vb, B=3e-4, h_v=0.0125: Eq. (vb) | 355.9 | 0.1 | 355.9 |
| PASS | tab_vb_B0.0003_h0.00625_law | Table tab:vb, B=3e-4, h_v=0.00625: Eq. (vb) | 384.2 | 0.1 | 384.2 |
| PASS | tab_vb_B0.0003_h0.003125_law | Table tab:vb, B=3e-4, h_v=0.003125: Eq. (vb) | 412.5 | 0.1 | 412.5 |
| PASS | tab_vb_B0.0003_h0.0015625_law | Table tab:vb, B=3e-4, h_v=0.0015625: Eq. (vb) | 440.8 | 0.1 | 440.8 |
| PASS | tab_vb_B0.0003_h0.05_law_formula | Table tab:vb, B=3e-4, h_v=0.05: Eq. (vb) evaluated (205.25 + 2/kappa_+ ln(1.5e-4/(B h_v))) | 299.3 | 0.05 (formula evaluated with kappa_+ = 0.04896874) | 299.293 |
| PASS | tab_vb_B0.0003_h0.025_law_formula | Table tab:vb, B=3e-4, h_v=0.025: Eq. (vb) evaluated (205.25 + 2/kappa_+ ln(1.5e-4/(B h_v))) | 327.6 | 0.05 (formula evaluated with kappa_+ = 0.04896874) | 327.603 |
| PASS | tab_vb_B0.03_h0.05_law_formula | Table tab:vb, B=3e-2, h_v=0.05: Eq. (vb) evaluated | 111.2 | 0.05 (formula evaluated with kappa_+ = 0.04896874) | 111.207 |
| PASS | tab_vb_B0.03_h0.025_law_formula | Table tab:vb, B=3e-2, h_v=0.025: Eq. (vb) evaluated | 139.5 | 0.05 (formula evaluated with kappa_+ = 0.04896874) | 139.517 |
| PASS | vb_shift_halving | Sec. 8 What limits the window: the shift per halving of h_v is ln4/kappa_+ = 28.31 | 28.31 | 0.005 (ln 4/0.04896874 = 28.309) | 28.3098 |
| PASS | vb_amplitude_93 | Sec. 8 What limits the window: B=3e-2 fails earlier than B=3e-3 by 93 (first non-finite 169 vs 262 at h_v=0.0125) and (2/kappa_+) ln10 = 94.0 | 93 | 0 (integer: 262-169) | 93 |
| PASS | vb_amplitude_law | Sec. 8 What limits the window: (2/kappa_+) ln 10 = 94.0 | 94.0 | 0.05 (94.04) | 94.0431 |
| PASS | vb_law_fit_error | Sec. 8 What limits the window: Eq. (vb) describes the data to 1.5 units of v (largest /measured - law/ over the 10 measured entries of Table tab:vb) | 1.5 | bound: <= paper | 1.2 |
| PASS | vb1_hv0.05_v1_250 | Sec. 8 What limits the window: first non-finite v = 205.25 for h_v=0.05, v1=250 (vb1.log) | 205.25 | 0.01 | 205.25 |
| PASS | vb1_hv0.05_v1_400 | Sec. 8 What limits the window: ... v1=400: 205.25 in both | 205.25 | 0.01 | 205.25 |
| PASS | blow1_first_nonfinite | Sec. 8 What limits the window: first non-finite v for isotropic h=0.025 (blow1.log) | 233.575 | 0.0005 | 233.575 |
| PASS | blow2_first_nonfinite | Sec. 8 What limits the window: first non-finite v for isotropic h=0.0125 (blow2.log) | 261.9 | 0.05 | 261.9 |
| PASS | blow3_first_nonfinite | Sec. 8 What limits the window: first non-finite v for isotropic h=0.00625 (blow3.log) | 290.20625 | 1e-05 | 290.206 |
| PASS | blow_shift | Sec. 8 What limits the window: the shift is 28.3 per halving (mean of 261.9 - 233.575 and 290.20625 - 261.9) | 28.3 | 0.05 (28.33 and 28.31) | 28.3156 |
| PASS | errprof_rho_v100 | Sec. 8 What limits the window: relative error of rho between h=0.05 and 0.025 at v=100 on U=1.5 (errprof.log) | 6.6e-3 | 5.5e-05 | 0.00664 |
| PASS | errprof_rho_v150 | Sec. 8 What limits the window: relative error of rho between h=0.05 and 0.025 at v=150 on U=1.5 (errprof.log) | 1.4e-2 | 0.000505 | 0.0142 |
| PASS | errprof_rho_v180 | Sec. 8 What limits the window: relative error of rho between h=0.05 and 0.025 at v=180 on U=1.5 (errprof.log) | 0.12 | 0.005 (0.122 quoted as 0.12) | 0.122 |
| PASS | hs_syst_1.2e-4 | Sec. 8 What limits the window (refining h_v): sigma_v of the h_s=0.05 family is more negative than that of the h_s=0.025 family by 1.2e-4 (150<=v<=220; mean over the printed rows) | 1.2e-4 | 5e-06 (1.2e-4 (1.22-1.26e-4 for 150..220)) | 0.000122625 |
| PASS | hs_syst_1.6e-4 | Sec. 8 What limits the window: ... so by 1.6e-4 than the h_s -> 0 limit (v=150..200) | 1.6e-4 | 1.5e-05 (1.6e-4 at 150, falling to 1.2e-4 at 200 as the front passes) | 0.000163 |
| PASS | hs_syst_025 | Sec. 8 What limits the window: ... and the h_s=0.025 family by 4e-5 | 4e-5 | 5e-06 (4.1e-5) | 4.1e-05 |
| PASS | hs_dsg_v200 | Sec. 8 What limits the window: d sg/dv (finite difference of the stored sigma) at v=200 is -0.043838 (rho_check.log), against the h_s -> 0 value of sigma_v -0.043835 (hs_extrap.log) | -0.043838 | 1e-06 | -0.043838 |
| PASS | hs_limit_v200 | Sec. 8 What limits the window: ... the h_s -> 0 value -0.043835 | -0.043835 | 1e-06 | -0.043835 |
| PASS | hs_floor_v | Sec. 8 What limits the window: the h_s floor 1.6e-4 is reached at v ~ 3e4 if sigma_v = -5/v | 3e4 | 2000 (5/1.6e-4 = 31250) | 31250 |
| PASS | e30kappa | Sec. 8 What limits the window: e^{30 kappa_+} = 4.3 | 4.3 | 0.05 (e^1.469 = 4.34) | 4.34516 |
| PASS | gen_q2_steps | Sec. 8 What limits the window: the finest level (h_v = 0.0015625) has 2.6e5 steps (g2_hs0.05_v400.log: nv = 256001) | 2.6e5 | 5000 (nv = 256001) | 256001 |
| PASS | tidal_err_K_v300 | Sec. 9 The curvature invariant and the tidal integrals to v=380: change of K from the next coarser level at v=300 (tidal_v600.log) | 2.4e-3 | 0.0001 | 0.0024 |
| PASS | tidal_err_K_v340 | Sec. 9 The curvature invariant and the tidal integrals to v=380: change of K from the next coarser level at v=340 (tidal_v600.log) | 1.8e-2 | 0.001 | 0.018 |
| PASS | tidal_err_K_v380 | Sec. 9 The curvature invariant and the tidal integrals to v=380: change of K from the next coarser level at v=380 (tidal_v600.log) | 0.15 | 0.01 | 0.15 |
| PASS | curv2_K_v100 | Sec. 9 The curvature invariant and the tidal integrals to v=380: K (code B) at v=100 (tidal_v600.log) | 1.09e25 | 5.5e+22 | 1.091e+25 |
| PASS | curv2_K_v200 | Sec. 9 The curvature invariant and the tidal integrals to v=380: K (code B) at v=200 (tidal_v600.log) | 2.17e27 | 5.5e+24 | 2.165e+27 |
| PASS | curv2_K_v300 | Sec. 9 The curvature invariant and the tidal integrals to v=380: K (code B) at v=300 (tidal_v600.log) | 1.26e28 | 5.5e+25 | 1.26e+28 |
| PASS | curv2_K_v360 | Sec. 9 The curvature invariant and the tidal integrals to v=380: K (code B) at v=360 (tidal_v600.log) | 1.98e28 | 5.5e+25 | 1.981e+28 |
| PASS | curv2_K_v380 | Sec. 9 The curvature invariant and the tidal integrals to v=380: K (code B) at v=380 (tidal_v600.log) | 2.27e28 | 5.5e+25 | 2.267e+28 |
| PASS | curv2_KA_v100 | Sec. 9 The curvature invariant and the tidal integrals to v=380: K of code A at h_s=0.05 at v=100 (Table tab:end) | 1.12e25 | 5.05e+22 | 1.1238e+25 |
| PASS | curv2_KA_v200 | Sec. 9 The curvature invariant and the tidal integrals to v=380: K of code A at h_s=0.05 at v=200 (Table tab:end) | 2.22e27 | 5.05e+24 | 2.2239e+27 |
| PASS | curv2_KA_v300 | Sec. 9 The curvature invariant and the tidal integrals to v=380: K of code A at h_s=0.05 at v=300 (Table tab:end) | 1.29e28 | 5.05e+25 | 1.2943e+28 |
| PASS | curv2_KA_over_KB | Sec. 9 The curvature invariant and the tidal integrals to v=380: code A gives K higher by 3% (mean of K_A/K_B - 1 at v=100, 200, 300; endpoint_B0.003_merged.log and tidal_v600.log) | 0.03 | 0.005 (1.030, 1.027, 1.027) | 0.028164 |
| PASS | curv2_terms_v340_0 | Sec. 9 The curvature invariant and the tidal integrals to v=380: term of Sigma at v=340: psi/2 (kstudy_v600.log) | 0.4997 | 5.5e-05 | 0.49973 |
| PASS | curv2_terms_v340_1 | Sec. 9 The curvature invariant and the tidal integrals to v=380: term of Sigma at v=340: -c2 (kstudy_v600.log) | -2.4e-3 | 5.5e-05 | -0.00242 |
| PASS | curv2_terms_v340_2 | Sec. 9 The curvature invariant and the tidal integrals to v=380: term of Sigma at v=340: -8 pi c1 g (kstudy_v600.log) | -9.4e4 | 505 | -93840 |
| PASS | curv2_terms_v340_3 | Sec. 9 The curvature invariant and the tidal integrals to v=380: term of Sigma at v=340: 64 pi^2 c3 g^2 (kstudy_v600.log) | 3.3e13 | 5.05e+11 | 3.277e+13 |
| PASS | curv2_c3_share | Sec. 9 The curvature invariant and the tidal integrals to v=380: the c3 term is 1+3e-9 times Sigma at v=340 | 1.000000003 | 1e-09 (1.0000000029) | 1 |
| PASS | curv2_H_share | Sec. 9 The curvature invariant and the tidal integrals to v=380: the other two terms of (kret) are of relative size 1e-17 and smaller (largest H-term share for v>=200) | 1e-16 | bound: <= paper | 5.1e-17 |
| PASS | curv2_c3_exact | Sec. 9 The curvature invariant and the tidal integrals to v=380: K = (512 pi^2)^2 z^6 g^4 to better than 1e-8 (largest c3term/Sigma - 1 for v >= 200) | 1e-8 | bound: <= paper | 7.1e-09 |
| PASS | curv2_Omega | Sec. 9 The curvature invariant and the tidal integrals to v=380: Omega ~ 4 Sigma >= 8e11 behind the front (smallest 4*Sigma at v>=100, curv_hv_merged.log) | 8e11 | bound: >= paper | 3.35224e+12 |
| PASS | curv2_slope_v160 | Sec. 9 The curvature invariant and the tidal integrals to v=380: local slope dlnK/dlnv at v=160 (kstudy_v600.log, +-10 centred differences) | 10.9 | 0.055 | 10.88 |
| PASS | curv2_slope_v200 | Sec. 9 The curvature invariant and the tidal integrals to v=380: local slope dlnK/dlnv at v=200 (kstudy_v600.log, +-10 centred differences) | 7.9 | 0.055 | 7.92 |
| PASS | curv2_slope_v240 | Sec. 9 The curvature invariant and the tidal integrals to v=380: local slope dlnK/dlnv at v=240 (kstudy_v600.log, +-10 centred differences) | 4.2 | 0.055 | 4.18 |
| PASS | curv2_slope_v260 | Sec. 9 The curvature invariant and the tidal integrals to v=380: local slope dlnK/dlnv at v=260 (kstudy_v600.log, +-10 centred differences) | 3.2 | 0.055 | 3.22 |
| PASS | curv2_slope_v280 | Sec. 9 The curvature invariant and the tidal integrals to v=380: local slope dlnK/dlnv at v=280 (kstudy_v600.log, +-10 centred differences) | 2.7 | 0.055 | 2.73 |
| PASS | curv2_slope_v300 | Sec. 9 The curvature invariant and the tidal integrals to v=380: local slope dlnK/dlnv at v=300 (kstudy_v600.log, +-10 centred differences) | 2.5 | 0.055 | 2.52 |
| PASS | curv2_slope_v320 | Sec. 9 The curvature invariant and the tidal integrals to v=380: local slope dlnK/dlnv at v=320 (kstudy_v600.log, +-10 centred differences) | 2.47 | 0.01 | 2.47 |
| PASS | curv2_slope_v340 | Sec. 9 The curvature invariant and the tidal integrals to v=380: local slope dlnK/dlnv at v=340 (kstudy_v600.log, +-10 centred differences) | 2.48 | 0.01 | 2.48 |
| PASS | curv2_slope_v360 | Sec. 9 The curvature invariant and the tidal integrals to v=380: local slope dlnK/dlnv at v=360 (kstudy_v600.log, +-10 centred differences) | 2.50 | 0.01 | 2.5 |
| PASS | curv2_slope_v380 | Sec. 9 The curvature invariant and the tidal integrals to v=380: local slope dlnK/dlnv at v=380 (kstudy_v600.log, +-10 centred differences) | 2.45 | 0.01 | 2.45 |
| PASS | kslope_eq_v300 | Sec. 9 The curvature invariant and the tidal integrals to v=380: Eq. (kslope) with v0 = 86 and the measured /v sigma_v/ = 5.42 at v=300 | 2.42 | 0.01 (formula 4 - 6 v0/(v-v0) + 2(/v sigma_v/ - 5) with v0 = 86; the manuscript rounds /v sigma_v/ to 3 digits first) | 2.41879 |
| PASS | kslope_eq_v340 | Sec. 9 The curvature invariant and the tidal integrals to v=380: Eq. (kslope) with v0 = 86 and the measured /v sigma_v/ = 5.24 at v=340 | 2.45 | 0.01 (formula 4 - 6 v0/(v-v0) + 2(/v sigma_v/ - 5) with v0 = 86; the manuscript rounds /v sigma_v/ to 3 digits first) | 2.4525 |
| PASS | kslope_eq_v380 | Sec. 9 The curvature invariant and the tidal integrals to v=380: Eq. (kslope) with v0 = 86 and the measured /v sigma_v/ = 5.16 at v=380 | 2.56 | 0.01 (formula 4 - 6 v0/(v-v0) + 2(/v sigma_v/ - 5) with v0 = 86; the manuscript rounds /v sigma_v/ to 3 digits first) | 2.5549 |
| PASS | vsigma_code_B_v300 | Sec. 9 The curvature invariant and the tidal integrals to v=380: measured /v sigma_v/ at v=300 (kstudy_v600.log) | 5.42 | 0.006 (-5.415, -5.242, -5.155 rounded to 3 digits) | 5.415 |
| PASS | vsigma_code_B_v340 | Sec. 9 The curvature invariant and the tidal integrals to v=380: measured /v sigma_v/ at v=340 (kstudy_v600.log) | 5.24 | 0.006 (-5.415, -5.242, -5.155 rounded to 3 digits) | 5.242 |
| PASS | vsigma_code_B_v380 | Sec. 9 The curvature invariant and the tidal integrals to v=380: measured /v sigma_v/ at v=380 (kstudy_v600.log) | 5.16 | 0.006 (-5.415, -5.242, -5.155 rounded to 3 digits) | 5.155 |
| PASS | curv2_m_v300 | Sec. 9 The curvature invariant and the tidal integrals to v=380: generalized mass m at v=300 | 926.3 | 0.06 | 926.3 |
| PASS | curv2_m_v340 | Sec. 9 The curvature invariant and the tidal integrals to v=380: generalized mass m at v=340 | 1099.5 | 0.06 | 1099.5 |
| PASS | curv2_m_v380 | Sec. 9 The curvature invariant and the tidal integrals to v=380: generalized mass m at v=380 | 1273 | 0.6 (1273.1 quoted as 1273) | 1273.1 |
| PASS | curv2_dmdv_v300 | Sec. 9 The curvature invariant and the tidal integrals to v=380: dm/dv at v=300 | 4.32 | 0.006 (4.321, 4.338, 4.338) | 4.321 |
| PASS | curv2_dmdv_v340 | Sec. 9 The curvature invariant and the tidal integrals to v=380: dm/dv at v=340 | 4.34 | 0.006 (4.321, 4.338, 4.338) | 4.338 |
| PASS | curv2_dmdv_v380 | Sec. 9 The curvature invariant and the tidal integrals to v=380: dm/dv at v=380 | 4.34 | 0.006 (4.321, 4.338, 4.338) | 4.338 |
| PASS | curv2_v0_v300 | Sec. 9 The curvature invariant and the tidal integrals to v=380: v0 = v - m/(dm/dv) at v=300 | 85.7 | 0.1 | 85.7 |
| PASS | curv2_v0_v340 | Sec. 9 The curvature invariant and the tidal integrals to v=380: v0 = v - m/(dm/dv) at v=340 | 86.6 | 0.1 | 86.6 |
| PASS | curv2_v0_v380 | Sec. 9 The curvature invariant and the tidal integrals to v=380: v0 = v - m/(dm/dv) at v=380 | 86.5 | 0.1 | 86.5 |
| PASS | curv2_v0_v100 | Sec. 9 The curvature invariant and the tidal integrals to v=380: v0 at v=100 (72 and 80) | 72 | 0.25 (72.0, 79.8) | 72 |
| PASS | curv2_v0_v200 | Sec. 9 The curvature invariant and the tidal integrals to v=380: v0 at v=200 (72 and 80) | 80 | 0.25 (72.0, 79.8) | 79.8 |
| PASS | curv2_dlnz_v300 | Sec. 9 The curvature invariant and the tidal integrals to v=380: local exponent of z at v=300 | -1.40 | 0.006 (-1.399, -1.341, -1.294) | -1.399 |
| PASS | curv2_dlnz_v340 | Sec. 9 The curvature invariant and the tidal integrals to v=380: local exponent of z at v=340 | -1.34 | 0.006 (-1.399, -1.341, -1.294) | -1.341 |
| PASS | curv2_dlnz_v380 | Sec. 9 The curvature invariant and the tidal integrals to v=380: local exponent of z at v=380 | -1.29 | 0.006 (-1.399, -1.341, -1.294) | -1.294 |
| PASS | curv2_v0_100_alt | Sec. 9 The curvature invariant and the tidal integrals to v=380: a value v0 = 100 would put Eq. (kslope) at 1.8, 2.0, 2.2 at v=300, 340, 380 (4 - 600/(v-100) + 2(/v sigma_v/ - 5), measured v sigma_v) | 1.8 | 0.05 (1.83 at v=300) | 1.83 |
| PASS | curv2_kslope_1e3 | Sec. 9 The curvature invariant and the tidal integrals to v=380: Eq. (kslope) with v0 = 86 and /v sigma_v/ -> 5 gives 3.4 at v=1e3 | 3.4 | 0.05 (4 - 516/914 = 3.44) | 3.43545 |
| PASS | curv2_kslope_1e4 | Sec. 9 The curvature invariant and the tidal integrals to v=380: ... and 3.95 at v=1e4 | 3.95 | 0.01 (4 - 516/9914 = 3.948) | 3.94795 |
| PASS | curv2_kslope_10pct | Sec. 9 The curvature invariant and the tidal integrals to v=380: 10% of the exponent 4 is reached for v ~ 1.4e3 (4 - 516/(v-86) = 3.6) | 1.4e3 | 100 (v = 86 + 516/0.4 = 1376) | 1376 |
| PASS | tidal_rlDl_v100 | Sec. 9 The curvature invariant and the tidal integrals to v=380: /r_lambda/ Dl at v=100 (tidal_v600.log) | 8e-10 | 5.05e-11 | 8.08e-10 |
| PASS | tidal_TDl2_v100 | Sec. 9 The curvature invariant and the tidal integrals to v=380: T Dl^2 at v=100 | 1.7e-11 | 5.5e-13 | 1.71e-11 |
| PASS | tidal_I2_v100 | Sec. 9 The curvature invariant and the tidal integrals to v=380: double integral at v=100 | 3.2e-11 | 5.5e-13 | 3.17e-11 |
| PASS | tidal_rlDl_v300 | Sec. 9 The curvature invariant and the tidal integrals to v=380: /r_lambda/ Dl at v=300 (tidal_v600.log) | 2.7e-13 | 5.5e-15 | 2.66e-13 |
| PASS | tidal_TDl2_v300 | Sec. 9 The curvature invariant and the tidal integrals to v=380: T Dl^2 at v=300 | 5.0e-16 | 5.5e-18 | 5.04e-16 |
| PASS | tidal_I2_v300 | Sec. 9 The curvature invariant and the tidal integrals to v=380: double integral at v=300 | 9.4e-16 | 5.5e-18 | 9.35e-16 |
| PASS | tidal_rlDl_v350 | Sec. 9 The curvature invariant and the tidal integrals to v=380: /r_lambda/ Dl at v=350 (tidal_v600.log) | 1.4e-13 | 5.5e-15 | 1.39e-13 |
| PASS | tidal_TDl2_v350 | Sec. 9 The curvature invariant and the tidal integrals to v=380: T Dl^2 at v=350 | 2.1e-16 | 5.5e-18 | 2.06e-16 |
| PASS | tidal_I2_v350 | Sec. 9 The curvature invariant and the tidal integrals to v=380: double integral at v=350 | 3.8e-16 | 5.5e-18 | 3.8e-16 |
| PASS | tidal_T_300 | Sec. 9 The curvature invariant and the tidal integrals to v=380: T = 8.1e20 at v=300 | 8.1e20 | 5e+18 (8.058e20) | 8.058e+20 |
| PASS | tidal_T_380 | Sec. 9 The curvature invariant and the tidal integrals to v=380: T = 1.5e21 at v=380 | 1.5e21 | 5e+19 (1.485e21) | 1.485e+21 |
| PASS | tidal_eK_v320 | Sec. 9 The curvature invariant and the tidal integrals to v=380: exponent e_K of K against the remaining affine distance at v=320 | -0.59 | 0.01 | -0.59 |
| PASS | tidal_eK_v340 | Sec. 9 The curvature invariant and the tidal integrals to v=380: exponent e_K of K against the remaining affine distance at v=340 | -0.59 | 0.01 | -0.59 |
| PASS | tidal_eK_v360 | Sec. 9 The curvature invariant and the tidal integrals to v=380: exponent e_K of K against the remaining affine distance at v=360 | -0.60 | 0.01 | -0.6 |
| PASS | tidal_eT_v320 | Sec. 9 The curvature invariant and the tidal integrals to v=380: exponent e_T at v=320 | -0.62 | 0.01 | -0.62 |
| PASS | tidal_eT_v340 | Sec. 9 The curvature invariant and the tidal integrals to v=380: exponent e_T at v=340 | -0.62 | 0.01 | -0.62 |
| PASS | tidal_eT_v360 | Sec. 9 The curvature invariant and the tidal integrals to v=380: exponent e_T at v=360 | -0.62 | 0.01 | -0.62 |
| PASS | tidal_rl_variation | Sec. 9 The curvature invariant and the tidal integrals to v=380: r_lambda = r_v/W varies by 0.6% over v in [200,380] (/e_rl/ small: see tidal_v600.log e_rl <= 0.003) | 0.003 | bound: <= paper | 0.003 |
| PASS | tidal_Dl_tail_diff | Sec. 9 The curvature invariant and the tidal integrals to v=380: the power-law and exponential-tail completions of Delta lambda differ by 20% at v=380 (1 - 2.337e-19/2.937e-19 = 0.20) | 0.20 | 0.01 (0.204) | 0.20429 |
| PASS | tidal_asym_eK | Sec. 9 The curvature invariant and the tidal integrals to v=380: asymptotic e_K = -(4k-2)/(2k+1) = -1 for k = 3/2 | -1 | 0 (exact: -(4*1.5-2)/(2*1.5+1) = -1) | -1 |
| PASS | tidal_asym_eT | Sec. 9 The curvature invariant and the tidal integrals to v=380: asymptotic e_T = -2k/(2k+1) = -3/4 | -0.75 | 0 (exact) | -0.75 |
| PASS | tab_k650_v100_z | Table tab:k650, v=100, z (kstudy2_double_v1500.log) | 5.66e-3 | 5.05e-06 | 0.0056579 |
| PASS | tab_k650_v100_m | Table tab:k650, v=100, m (kstudy2_double_v1500.log) | 104 | 0.51 (integer rounding of m) | 103.9 |
| PASS | tab_k650_v100_dm_dv | Table tab:k650, v=100, dm_dv (kstudy2_double_v1500.log) | 3.722 | 0.00055 | 3.7215 |
| PASS | tab_k650_v100_v0 | Table tab:k650, v=100, v0 (kstudy2_double_v1500.log) | 72.1 | 0.1 | 72.1 |
| PASS | tab_k650_v100_vsigma | Table tab:k650, v=100, vsigma (kstudy2_double_v1500.log) | -9.409 | 0.001 | -9.409 |
| PASS | tab_k650_v100_K | Table tab:k650, v=100, K (kstudy2_double_v1500.log) | 1.12e25 | 5.005e+22 | 1.12011e+25 |
| PASS | tab_k650_v100_slope | Table tab:k650, v=100, slope (kstudy2_double_v1500.log) | -2.80 | 0.0055 | -2.797 |
| PASS | tab_k650_v100_formula | Table tab:k650, v=100, formula (kstudy2_double_v1500.log) | -2.67 | 0.0055 | -2.671 |
| PASS | tab_k650_v100_slope_plus_terms | Table tab:k650, v=100, slope_plus_terms (kstudy2_double_v1500.log) | 3.87 | 0.0055 | 3.873 |
| PASS | tab_k650_v200_z | Table tab:k650, v=200, z (kstudy2_double_v1500.log) | 1.18e-3 | 5.05e-06 | 0.001182 |
| PASS | tab_k650_v200_m | Table tab:k650, v=200, m (kstudy2_double_v1500.log) | 500 | 0.51 (integer rounding of m) | 499.6 |
| PASS | tab_k650_v200_dm_dv | Table tab:k650, v=200, dm_dv (kstudy2_double_v1500.log) | 4.157 | 0.00055 | 4.1572 |
| PASS | tab_k650_v200_v0 | Table tab:k650, v=200, v0 (kstudy2_double_v1500.log) | 79.8 | 0.1 | 79.8 |
| PASS | tab_k650_v200_vsigma | Table tab:k650, v=200, vsigma (kstudy2_double_v1500.log) | -8.767 | 0.001 | -8.767 |
| PASS | tab_k650_v200_K | Table tab:k650, v=200, K (kstudy2_double_v1500.log) | 2.20e27 | 5.005e+24 | 2.20009e+27 |
| PASS | tab_k650_v200_slope | Table tab:k650, v=200, slope (kstudy2_double_v1500.log) | 7.91 | 0.0055 | 7.915 |
| PASS | tab_k650_v200_formula | Table tab:k650, v=200, formula (kstudy2_double_v1500.log) | 7.55 | 0.0055 | 7.55 |
| PASS | tab_k650_v200_slope_plus_terms | Table tab:k650, v=200, slope_plus_terms (kstudy2_double_v1500.log) | 4.36 | 0.0055 | 4.365 |
| PASS | tab_k650_v300_z | Table tab:k650, v=300, z (kstudy2_double_v1500.log) | 6.38e-4 | 5.05e-07 | 0.00063806 |
| PASS | tab_k650_v300_m | Table tab:k650, v=300, m (kstudy2_double_v1500.log) | 926 | 0.51 (integer rounding of m) | 926 |
| PASS | tab_k650_v300_dm_dv | Table tab:k650, v=300, dm_dv (kstudy2_double_v1500.log) | 4.322 | 0.00055 | 4.3219 |
| PASS | tab_k650_v300_v0 | Table tab:k650, v=300, v0 (kstudy2_double_v1500.log) | 85.7 | 0.1 | 85.7 |
| PASS | tab_k650_v300_vsigma | Table tab:k650, v=300, vsigma (kstudy2_double_v1500.log) | -5.416 | 0.001 | -5.416 |
| PASS | tab_k650_v300_K | Table tab:k650, v=300, K (kstudy2_double_v1500.log) | 1.28e28 | 5.005e+25 | 1.27866e+28 |
| PASS | tab_k650_v300_slope | Table tab:k650, v=300, slope (kstudy2_double_v1500.log) | 2.52 | 0.0055 | 2.524 |
| PASS | tab_k650_v300_formula | Table tab:k650, v=300, formula (kstudy2_double_v1500.log) | 2.43 | 0.0055 | 2.431 |
| PASS | tab_k650_v300_slope_plus_terms | Table tab:k650, v=300, slope_plus_terms (kstudy2_double_v1500.log) | 4.09 | 0.0055 | 4.093 |
| PASS | tab_k650_v380_z | Table tab:k650, v=380, z (kstudy2_double_v1500.log) | 4.64e-4 | 5.05e-07 | 0.00046416 |
| PASS | tab_k650_v380_m | Table tab:k650, v=380, m (kstudy2_double_v1500.log) | 1273 | 0.51 (integer rounding of m) | 1273.2 |
| PASS | tab_k650_v380_dm_dv | Table tab:k650, v=380, dm_dv (kstudy2_double_v1500.log) | 4.354 | 0.00055 | 4.3536 |
| PASS | tab_k650_v380_v0 | Table tab:k650, v=380, v0 (kstudy2_double_v1500.log) | 87.5 | 0.1 | 87.5 |
| PASS | tab_k650_v380_vsigma | Table tab:k650, v=380, vsigma (kstudy2_double_v1500.log) | -5.185 | 0.001 | -5.185 |
| PASS | tab_k650_v380_K | Table tab:k650, v=380, K (kstudy2_double_v1500.log) | 2.32e28 | 5.005e+25 | 2.3189e+28 |
| PASS | tab_k650_v380_slope | Table tab:k650, v=380, slope (kstudy2_double_v1500.log) | 2.62 | 0.0051 (2.625 is printed, the manuscript has 2.62 (round-half-down)) | 2.625 |
| PASS | tab_k650_v380_formula | Table tab:k650, v=380, formula (kstudy2_double_v1500.log) | 2.57 | 0.0055 | 2.573 |
| PASS | tab_k650_v380_slope_plus_terms | Table tab:k650, v=380, slope_plus_terms (kstudy2_double_v1500.log) | 4.05 | 0.0055 | 4.052 |
| PASS | tab_k650_v500_z | Table tab:k650, v=500, z (kstudy2_double_v1500.log) | 3.29e-4 | 5.05e-07 | 0.00032886 |
| PASS | tab_k650_v500_m | Table tab:k650, v=500, m (kstudy2_double_v1500.log) | 1797 | 0.51 (integer rounding of m) | 1797.3 |
| PASS | tab_k650_v500_dm_dv | Table tab:k650, v=500, dm_dv (kstudy2_double_v1500.log) | 4.378 | 0.00055 | 4.3781 |
| PASS | tab_k650_v500_v0 | Table tab:k650, v=500, v0 (kstudy2_double_v1500.log) | 89.5 | 0.1 | 89.5 |
| PASS | tab_k650_v500_vsigma | Table tab:k650, v=500, vsigma (kstudy2_double_v1500.log) | -5.122 | 0.001 | -5.122 |
| PASS | tab_k650_v500_K | Table tab:k650, v=500, K (kstudy2_double_v1500.log) | 5.01e28 | 5.005e+25 | 5.00686e+28 |
| PASS | tab_k650_v500_slope | Table tab:k650, v=500, slope (kstudy2_double_v1500.log) | 2.97 | 0.0055 | 2.973 |
| PASS | tab_k650_v500_formula | Table tab:k650, v=500, formula (kstudy2_double_v1500.log) | 2.94 | 0.0055 | 2.937 |
| PASS | tab_k650_v500_slope_plus_terms | Table tab:k650, v=500, slope_plus_terms (kstudy2_double_v1500.log) | 4.04 | 0.0055 | 4.036 |
| PASS | tab_k650_v650_z | Table tab:k650, v=650, z (kstudy2_double_v1500.log) | 2.41e-4 | 5.05e-07 | 0.00024074 |
| PASS | tab_k650_v650_m | Table tab:k650, v=650, m (kstudy2_double_v1500.log) | 2455 | 0.51 (integer rounding of m) | 2455.4 |
| PASS | tab_k650_v650_dm_dv | Table tab:k650, v=650, dm_dv (kstudy2_double_v1500.log) | 4.395 | 0.00055 | 4.3952 |
| PASS | tab_k650_v650_v0 | Table tab:k650, v=650, v0 (kstudy2_double_v1500.log) | 91.3 | 0.1 | 91.3 |
| PASS | tab_k650_v650_vsigma | Table tab:k650, v=650, vsigma (kstudy2_double_v1500.log) | -5.089 | 0.001 | -5.089 |
| PASS | tab_k650_v650_K | Table tab:k650, v=650, K (kstudy2_double_v1500.log) | 1.13e29 | 5.005e+26 | 1.13063e+29 |
| PASS | tab_k650_v650_slope | Table tab:k650, v=650, slope (kstudy2_double_v1500.log) | 3.22 | 0.0055 | 3.223 |
| PASS | tab_k650_v650_formula | Table tab:k650, v=650, formula (kstudy2_double_v1500.log) | 3.20 | 0.0055 | 3.197 |
| PASS | tab_k650_v650_slope_plus_terms | Table tab:k650, v=650, slope_plus_terms (kstudy2_double_v1500.log) | 4.03 | 0.0055 | 4.026 |
| PASS | tab_k650_v800_z | Table tab:k650, v=800, z (kstudy2_double_v1500.log) | 1.90e-4 | 5.05e-07 | 0.00018974 |
| PASS | tab_k650_v800_m | Table tab:k650, v=800, m (kstudy2_double_v1500.log) | 3116 | 0.51 (integer rounding of m) | 3115.5 |
| PASS | tab_k650_v800_dm_dv | Table tab:k650, v=800, dm_dv (kstudy2_double_v1500.log) | 4.406 | 0.00055 | 4.4057 |
| PASS | tab_k650_v800_v0 | Table tab:k650, v=800, v0 (kstudy2_double_v1500.log) | 92.8 | 0.1 | 92.8 |
| PASS | tab_k650_v800_vsigma | Table tab:k650, v=800, vsigma (kstudy2_double_v1500.log) | -5.070 | 0.001 | -5.07 |
| PASS | tab_k650_v800_K | Table tab:k650, v=800, K (kstudy2_double_v1500.log) | 2.24e29 | 5.005e+26 | 2.2439e+29 |
| PASS | tab_k650_v800_slope | Table tab:k650, v=800, slope (kstudy2_double_v1500.log) | 3.37 | 0.0055 | 3.373 |
| PASS | tab_k650_v800_formula | Table tab:k650, v=800, formula (kstudy2_double_v1500.log) | 3.35 | 0.0055 | 3.352 |
| PASS | tab_k650_v800_slope_plus_terms | Table tab:k650, v=800, slope_plus_terms (kstudy2_double_v1500.log) | 4.02 | 0.0055 | 4.021 |
| PASS | tab_k650_v1000_z | Table tab:k650, v=1000, z (kstudy2_double_v1500.log) | 1.48e-4 | 5.05e-07 | 0.00014788 |
| PASS | tab_k650_v1000_m | Table tab:k650, v=1000, m (kstudy2_double_v1500.log) | 3998 | 0.51 (integer rounding of m) | 3997.6 |
| PASS | tab_k650_v1000_dm_dv | Table tab:k650, v=1000, dm_dv (kstudy2_double_v1500.log) | 4.415 | 0.00055 | 4.4145 |
| PASS | tab_k650_v1000_v0 | Table tab:k650, v=1000, v0 (kstudy2_double_v1500.log) | 94.4 | 0.1 | 94.4 |
| PASS | tab_k650_v1000_vsigma | Table tab:k650, v=1000, vsigma (kstudy2_double_v1500.log) | -5.055 | 0.001 | -5.055 |
| PASS | tab_k650_v1000_K | Table tab:k650, v=1000, K (kstudy2_double_v1500.log) | 4.83e29 | 5.005e+26 | 4.83357e+29 |
| PASS | tab_k650_v1000_slope | Table tab:k650, v=1000, slope (kstudy2_double_v1500.log) | 3.50 | 0.0055 | 3.499 |
| PASS | tab_k650_v1000_formula | Table tab:k650, v=1000, formula (kstudy2_double_v1500.log) | 3.48 | 0.0055 | 3.484 |
| PASS | tab_k650_v1000_slope_plus_terms | Table tab:k650, v=1000, slope_plus_terms (kstudy2_double_v1500.log) | 4.02 | 0.0055 | 4.016 |
| PASS | tab_k650_v1200_z | Table tab:k650, v=1200, z (kstudy2_double_v1500.log) | 1.21e-4 | 5.05e-07 | 0.00012111 |
| PASS | tab_k650_v1200_m | Table tab:k650, v=1200, m (kstudy2_double_v1500.log) | 4881 | 0.51 (integer rounding of m) | 4881.1 |
| PASS | tab_k650_v1200_dm_dv | Table tab:k650, v=1200, dm_dv (kstudy2_double_v1500.log) | 4.420 | 0.00055 | 4.4204 |
| PASS | tab_k650_v1200_v0 | Table tab:k650, v=1200, v0 (kstudy2_double_v1500.log) | 95.8 | 0.1 | 95.8 |
| PASS | tab_k650_v1200_vsigma | Table tab:k650, v=1200, vsigma (kstudy2_double_v1500.log) | -5.045 | 0.001 | -5.045 |
| PASS | tab_k650_v1200_K | Table tab:k650, v=1200, K (kstudy2_double_v1500.log) | 9.22e29 | 5.005e+26 | 9.22037e+29 |
| PASS | tab_k650_v1200_slope | Table tab:k650, v=1200, slope (kstudy2_double_v1500.log) | 3.58 | 0.0055 | 3.582 |
| PASS | tab_k650_v1200_formula | Table tab:k650, v=1200, formula (kstudy2_double_v1500.log) | 3.57 | 0.0055 | 3.57 |
| PASS | tab_k650_v1200_slope_plus_terms | Table tab:k650, v=1200, slope_plus_terms (kstudy2_double_v1500.log) | 4.01 | 0.0055 | 4.013 |
| PASS | tab_k650_v1400_z | Table tab:k650, v=1400, z (kstudy2_double_v1500.log) | 1.03e-4 | 5.05e-07 | 0.00010254 |
| PASS | tab_k650_v1400_m | Table tab:k650, v=1400, m (kstudy2_double_v1500.log) | 5766 | 0.51 (integer rounding of m) | 5765.7 |
| PASS | tab_k650_v1400_dm_dv | Table tab:k650, v=1400, dm_dv (kstudy2_double_v1500.log) | 4.425 | 0.00055 | 4.4246 |
| PASS | tab_k650_v1400_v0 | Table tab:k650, v=1400, v0 (kstudy2_double_v1500.log) | 96.9 | 0.1 | 96.9 |
| PASS | tab_k650_v1400_vsigma | Table tab:k650, v=1400, vsigma (kstudy2_double_v1500.log) | -5.038 | 0.001 | -5.038 |
| PASS | tab_k650_v1400_K | Table tab:k650, v=1400, K (kstudy2_double_v1500.log) | 1.61e30 | 5.005e+27 | 1.6091e+30 |
| PASS | tab_k650_v1400_slope | Table tab:k650, v=1400, slope (kstudy2_double_v1500.log) | 3.64 | 0.0055 | 3.641 |
| PASS | tab_k650_v1400_formula | Table tab:k650, v=1400, formula (kstudy2_double_v1500.log) | 3.63 | 0.0055 | 3.63 |
| PASS | tab_k650_v1400_slope_plus_terms | Table tab:k650, v=1400, slope_plus_terms (kstudy2_double_v1500.log) | 4.01 | 0.0055 | 4.01 |
| PASS | k650_K1400 | Sec. 9 Curvature and slaving to kappa_+ v ~ 70: K = 1.61e30 at v=1400 | 1.61e30 | 5.005e+27 | 1.6091e+30 |
| PASS | k650_slope_min | Sec. 9 Curvature and slaving to kappa_+ v ~ 70: minimum of the slope 2.50 at v=340 | 2.50 | 0.005 (2.500) | 2.5 |
| PASS | k650_slope_min_is_340 | Sec. 9 Curvature and slaving to kappa_+ v ~ 70: ... the minimum over the printed rows is at v=340 | 340 | 0 (grid) | 340 |
| PASS | k650_formula_300 | Sec. 9 Curvature and slaving to kappa_+ v ~ 70: Eq. (kslope) reproduces the slope to 0.09 at v=300 | 0.09 | 0.005 (2.524 - 2.431 = 0.093) | 0.093 |
| PASS | k650_formula_650_max | Sec. 9 Curvature and slaving to kappa_+ v ~ 70: ... and 0.02 or less at v>=650 (largest difference for 650<=v<=1400 is 0.026 at v=650) | 0.02 | 0.0065 (0.026 unrounded; 3.22 - 3.20 = 0.02 in the rounded table) | 0.026 |
| PASS | k650_formula_100 | Sec. 9 Curvature and slaving to kappa_+ v ~ 70: ... (0.13 at v=100) | 0.13 | 0.005 (0.126) | 0.126 |
| PASS | k650_formula_200 | Sec. 9 Curvature and slaving to kappa_+ v ~ 70: ... and 0.37 at v=200 | 0.37 | 0.005 (0.365) | 0.365 |
| PASS | k650_v0_drift | Sec. 9 Curvature and slaving to kappa_+ v ~ 70: v0 drifts 85.7 -> 96.9 between v=300 and 1400 | 96.9 | 0.1 | 96.9 |
| PASS | k650_dmdv_closed | Sec. 9 Curvature and slaving to kappa_+ v ~ 70: dm/dv = 4.425 approaches the closed form 4.449 from below (closed form from the static numbers) | 4.449 | 0.0005 (4.4487) | 4.44868 |
| PASS | k650_dlnz | Sec. 9 Curvature and slaving to kappa_+ v ~ 70: dlnz/dlnv = -1.40 -> -1.07 (v=300 -> 1400) | -1.07 | 0.006 (-1.074) | -1.074 |
| PASS | k650_const_1400 | Sec. 9 Curvature and slaving to kappa_+ v ~ 70: the constant of the formula is measured to 0.3% at v=1400 (slope+terms/4 - 1) | 0.003 | 0.0005 (4.010/4 - 1 = 0.0025) | 0.0025 |
| PASS | k650_slope_below | Sec. 9 Curvature and slaving to kappa_+ v ~ 70: ... while the slope itself is still 9% below it | 0.09 | 0.005 (1 - 3.641/4 = 0.090) | 0.08975 |
| PASS | k650_c3share | Sec. 9 Curvature and slaving to kappa_+ v ~ 70: the c3 term of Sigma is 1 + 3e-9 times Sigma or less at v>=300 (manuscript: 1 + 1e-9; the largest value in the log is 1.000000003 at v=300) | 3e-9 (manuscript: $1+10^{-9}$ times $\Sigma$ or less at $v\ge300$) | 5e-10 (printed with 9 decimals) | 3e-09 |
| PASS | k650_zm | Sec. 9 Curvature and slaving to kappa_+ v ~ 70: the product zm stays at 0.5912 (z m at v=1400) | 0.5912 | 5e-05 (0.59124 (z and m printed to 5 and 6 digits)) | 0.591215 |
| PASS | k650_zm_exact | Sec. 9 Curvature and slaving to kappa_+ v ~ 70: ... (1/2 r_-^3 = 0.5913) | 0.5913 | 5e-05 (0.591262) | 0.591262 |
| PASS | tab_scan_k1_2_v | Table tab:scan, k=1/2, v (scans.log) | 1021 | 0.5 (integer v) | 1021 |
| PASS | tab_scan_k1_2_zm | Table tab:scan, k=1/2, zm (scans.log) | 0.59117 | 1e-05 | 0.59117 |
| PASS | tab_scan_k1_2_vsigma | Table tab:scan, k=1/2, vsigma (scans.log) | -3.032 | 0.00055 | -3.0321 |
| PASS | tab_scan_k1_2_dm_dv | Table tab:scan, k=1/2, dm_dv (scans.log) | 4.426 | 0.00055 | 4.4264 |
| PASS | tab_scan_k1_2_v0 | Table tab:scan, k=1/2, v0 (scans.log) | 81.4 | 0.1 | 81.4 |
| PASS | tab_scan_k1_2_slope | Table tab:scan, k=1/2, slope (scans.log) | -0.45 | 0.0055 | -0.446 |
| PASS | tab_scan_k1_2_formula | Table tab:scan, k=1/2, formula (scans.log) | -0.46 | 0.0055 | -0.456 |
| PASS | tab_scan_k1_2_slope_plus_terms | Table tab:scan, k=1/2, slope_plus_terms (scans.log) | 0.010 | 0.001 | 0.01 |
| PASS | tab_scan_k1_v | Table tab:scan, k=1, v (scans.log) | 1021 | 0.5 (integer v) | 1021 |
| PASS | tab_scan_k1_zm | Table tab:scan, k=1, zm (scans.log) | 0.59117 | 1e-05 | 0.59117 |
| PASS | tab_scan_k1_vsigma | Table tab:scan, k=1, vsigma (scans.log) | -4.043 | 0.00055 | -4.0427 |
| PASS | tab_scan_k1_dm_dv | Table tab:scan, k=1, dm_dv (scans.log) | 4.421 | 0.00055 | 4.4208 |
| PASS | tab_scan_k1_v0 | Table tab:scan, k=1, v0 (scans.log) | 87.7 | 0.1 | 87.7 |
| PASS | tab_scan_k1_slope | Table tab:scan, k=1, slope (scans.log) | 1.54 | 0.0055 | 1.535 |
| PASS | tab_scan_k1_formula | Table tab:scan, k=1, formula (scans.log) | 1.52 | 0.0055 | 1.522 |
| PASS | tab_scan_k1_slope_plus_terms | Table tab:scan, k=1, slope_plus_terms (scans.log) | 2.013 | 0.001 | 2.013 |
| PASS | tab_scan_k3_2_v | Table tab:scan, k=3/2, v (scans.log) | 1021 | 0.5 (integer v) | 1021 |
| PASS | tab_scan_k3_2_zm | Table tab:scan, k=3/2, zm (scans.log) | 0.59116 | 1e-05 | 0.59116 |
| PASS | tab_scan_k3_2_vsigma | Table tab:scan, k=3/2, vsigma (scans.log) | -5.054 | 0.00055 | -5.0535 |
| PASS | tab_scan_k3_2_dm_dv | Table tab:scan, k=3/2, dm_dv (scans.log) | 4.415 | 0.00055 | 4.4153 |
| PASS | tab_scan_k3_2_v0 | Table tab:scan, k=3/2, v0 (scans.log) | 94.6 | 0.1 | 94.6 |
| PASS | tab_scan_k3_2_slope | Table tab:scan, k=3/2, slope (scans.log) | 3.51 | 0.0055 | 3.51 |
| PASS | tab_scan_k3_2_formula | Table tab:scan, k=3/2, formula (scans.log) | 3.49 | 0.0055 | 3.494 |
| PASS | tab_scan_k3_2_slope_plus_terms | Table tab:scan, k=3/2, slope_plus_terms (scans.log) | 4.015 | 0.001 | 4.015 |
| PASS | tab_scan_k2_v | Table tab:scan, k=2, v (scans.log) | 1021 | 0.5 (integer v) | 1021 |
| PASS | tab_scan_k2_zm | Table tab:scan, k=2, zm (scans.log) | 0.59116 | 1e-05 | 0.59116 |
| PASS | tab_scan_k2_vsigma | Table tab:scan, k=2, vsigma (scans.log) | -6.065 | 0.00055 | -6.0646 |
| PASS | tab_scan_k2_dm_dv | Table tab:scan, k=2, dm_dv (scans.log) | 4.410 | 0.00055 | 4.4097 |
| PASS | tab_scan_k2_v0 | Table tab:scan, k=2, v0 (scans.log) | 101.6 | 0.1 | 101.6 |
| PASS | tab_scan_k2_slope | Table tab:scan, k=2, slope (scans.log) | 5.48 | 0.0055 | 5.484 |
| PASS | tab_scan_k2_formula | Table tab:scan, k=2, formula (scans.log) | 5.47 | 0.0055 | 5.466 |
| PASS | tab_scan_k2_slope_plus_terms | Table tab:scan, k=2, slope_plus_terms (scans.log) | 6.018 | 0.001 | 6.018 |
| PASS | tab_scan_k3_v | Table tab:scan, k=3, v (scans.log) | 1021 | 0.5 (integer v) | 1021 |
| PASS | tab_scan_k3_zm | Table tab:scan, k=3, zm (scans.log) | 0.59116 | 1e-05 | 0.59116 |
| PASS | tab_scan_k3_vsigma | Table tab:scan, k=3, vsigma (scans.log) | -8.088 | 0.00055 | -8.0876 |
| PASS | tab_scan_k3_dm_dv | Table tab:scan, k=3, dm_dv (scans.log) | 4.399 | 0.00055 | 4.3986 |
| PASS | tab_scan_k3_v0 | Table tab:scan, k=3, v0 (scans.log) | 116.0 | 0.1 | 116 |
| PASS | tab_scan_k3_slope | Table tab:scan, k=3, slope (scans.log) | 9.43 | 0.0055 | 9.43 |
| PASS | tab_scan_k3_formula | Table tab:scan, k=3, formula (scans.log) | 9.41 | 0.0055 | 9.407 |
| PASS | tab_scan_k3_slope_plus_terms | Table tab:scan, k=3, slope_plus_terms (scans.log) | 10.023 | 0.001 | 10.023 |
| PASS | tab_scan_B3e-4_v | Table tab:scan, B=3e-4, v (scans.log) | 1021 | 0.5 (integer v) | 1021 |
| PASS | tab_scan_B3e-4_zm | Table tab:scan, B=3e-4, zm (scans.log) | 0.59117 | 1e-05 | 0.59117 |
| PASS | tab_scan_B3e-4_vsigma | Table tab:scan, B=3e-4, vsigma (scans.log) | -5.054 | 0.00055 | -5.0535 |
| PASS | tab_scan_B3e-4_dm_dv | Table tab:scan, B=3e-4, dm_dv (scans.log) | 4.415 | 0.00055 | 4.4151 |
| PASS | tab_scan_B3e-4_v0 | Table tab:scan, B=3e-4, v0 (scans.log) | 106.2 | 0.1 | 106.2 |
| PASS | tab_scan_B3e-4_slope | Table tab:scan, B=3e-4, slope (scans.log) | 3.43 | 0.0055 | 3.426 |
| PASS | tab_scan_B3e-4_formula | Table tab:scan, B=3e-4, formula (scans.log) | 3.41 | 0.0055 | 3.41 |
| PASS | tab_scan_B3e-4_slope_plus_terms | Table tab:scan, B=3e-4, slope_plus_terms (scans.log) | 4.016 | 0.001 | 4.016 |
| PASS | tab_scan_B3e-2_v | Table tab:scan, B=3e-2, v (scans.log) | 1021 | 0.5 (integer v) | 1021 |
| PASS | tab_scan_B3e-2_zm | Table tab:scan, B=3e-2, zm (scans.log) | 0.59082 | 1e-05 | 0.59082 |
| PASS | tab_scan_B3e-2_vsigma | Table tab:scan, B=3e-2, vsigma (scans.log) | -5.054 | 0.00055 | -5.0536 |
| PASS | tab_scan_B3e-2_dm_dv | Table tab:scan, B=3e-2, dm_dv (scans.log) | 4.426 | 0.00055 | 4.4255 |
| PASS | tab_scan_B3e-2_v0 | Table tab:scan, B=3e-2, v0 (scans.log) | 83.1 | 0.1 | 83.1 |
| PASS | tab_scan_B3e-2_slope | Table tab:scan, B=3e-2, slope (scans.log) | 3.59 | 0.0055 | 3.591 |
| PASS | tab_scan_B3e-2_formula | Table tab:scan, B=3e-2, formula (scans.log) | 3.58 | 0.0055 | 3.576 |
| PASS | tab_scan_B3e-2_slope_plus_terms | Table tab:scan, B=3e-2, slope_plus_terms (scans.log) | 4.015 | 0.001 | 4.015 |
| PASS | tab_scan_m3_v | Table tab:scan, m=3, v (scans.log) | 639 | 0.5 (integer v) | 639 |
| PASS | tab_scan_m3_zm | Table tab:scan, m=3, zm (scans.log) | 0.67867 | 1e-05 | 0.67867 |
| PASS | tab_scan_m3_vsigma | Table tab:scan, m=3, vsigma (scans.log) | -5.058 | 0.00055 | -5.0579 |
| PASS | tab_scan_m3_dm_dv | Table tab:scan, m=3, dm_dv (scans.log) | 2.367 | 0.00055 | 2.3667 |
| PASS | tab_scan_m3_v0 | Table tab:scan, m=3, v0 (scans.log) | 88.3 | 0.1 | 88.3 |
| PASS | tab_scan_m3_slope | Table tab:scan, m=3, slope (scans.log) | 3.19 | 0.0055 | 3.188 |
| PASS | tab_scan_m3_formula | Table tab:scan, m=3, formula (scans.log) | 3.15 | 0.0055 | 3.153 |
| PASS | tab_scan_m3_slope_plus_terms | Table tab:scan, m=3, slope_plus_terms (scans.log) | 4.035 | 0.001 | 4.035 |
| PASS | tab_scan_m10_v | Table tab:scan, m=10, v (scans.log) | 1608 | 0.5 (integer v) | 1608 |
| PASS | tab_scan_m10_zm | Table tab:scan, m=10, zm (scans.log) | 0.54101 | 1e-05 | 0.54101 |
| PASS | tab_scan_m10_vsigma | Table tab:scan, m=10, vsigma (scans.log) | -5.071 | 0.00055 | -5.0708 |
| PASS | tab_scan_m10_dm_dv | Table tab:scan, m=10, dm_dv (scans.log) | 9.452 | 0.00055 | 9.4522 |
| PASS | tab_scan_m10_v0 | Table tab:scan, m=10, v0 (scans.log) | 143.1 | 0.1 | 143.1 |
| PASS | tab_scan_m10_slope | Table tab:scan, m=10, slope (scans.log) | 3.55 | 0.0055 | 3.549 |
| PASS | tab_scan_m10_formula | Table tab:scan, m=10, formula (scans.log) | 3.56 | 0.0055 | 3.555 |
| PASS | tab_scan_m10_slope_plus_terms | Table tab:scan, m=10, slope_plus_terms (scans.log) | 3.994 | 0.001 | 3.994 |
| PASS | tab_scan_zm_closed_m5 | Table tab:scan: 1/2 r_-^3 = 0.5913 (m=5) | 0.5913 | 5e-05 (0.59126) | 0.59126 |
| PASS | tab_scan_zm_closed_m3 | Table tab:scan: 1/2 r_-^3 = 0.6790 (m=3) | 0.6790 | 5e-05 (0.67903) | 0.67903 |
| PASS | tab_scan_zm_closed_m10 | Table tab:scan: 1/2 r_-^3 = 0.5411 (m=10) | 0.5411 | 5e-05 (0.54113) | 0.54113 |
| PASS | tab_scan_closed_dmdv_m3 | Table tab:scan / text: closed form 2 r_- beta_inf kappa_-/c1^II for m=3 | 2.403 | 0.0005 (2.4025) | 2.4025 |
| PASS | tab_scan_closed_dmdv_m5 | Table tab:scan / text: closed form 2 r_- beta_inf kappa_-/c1^II for m=5 | 4.449 | 0.0005 (4.4487) | 4.4487 |
| PASS | tab_scan_closed_dmdv_m10 | Table tab:scan / text: closed form 2 r_- beta_inf kappa_-/c1^II for m=10 | 9.476 | 0.0005 (9.4764) | 9.4764 |
| PASS | scan_formula_maxdiff | Sec. 9 Tail exponents, amplitudes and the inner mass: Eq. (kslopek) predicts the measured slope to <=0.04 for every case (largest /slope - formula/ over the nine rows of the table) | 0.04 | bound: <= paper | 0.035 |
| PASS | scan_formula_maxdiff_m3 | Sec. 9 Tail exponents, amplitudes and the inner mass: ... and to 0.04 for m=3 | 0.04 | 0.005 (0.035) | 0.035 |
| PASS | scan_const_k1_rel | Sec. 9 Tail exponents, amplitudes and the inner mass: the formula constant is within 0.7% of 4k-2 for k>=1 (largest relative deviation over k=1,3/2,2,3) | 0.007 | 0.0005 (0.65%) | 0.0065 |
| PASS | scan_zm_spread | Sec. 9 Tail exponents, amplitudes and the inner mass: zm does not depend on k or B (within 0.06%: spread over the seven m=5 cases) | 6e-4 | 5e-05 ((0.59117-0.59082)/0.59117 = 5.9e-4) | 0.000592046 |
| PASS | scan_dmdv_spread | Sec. 9 Tail exponents, amplitudes and the inner mass: ... nor dm/dv (within 0.6%) | 6e-3 | 0.0005 (4.426/4.399 - 1 = 6.1e-3) | 0.00632019 |
| PASS | scan_dmdv_below_m3 | Sec. 9 Tail exponents, amplitudes and the inner mass: dm/dv approaches the closed form from below: percentage below, m3 (scans.log) | 1.5 | 0.055 (1.49%, 0.75%, 0.255%) | 1.49011 |
| PASS | scan_dmdv_below_m5 | Sec. 9 Tail exponents, amplitudes and the inner mass: dm/dv approaches the closed form from below: percentage below, m5 (scans.log) | 0.8 | 0.06 (1.49%, 0.75%, 0.255%) | 0.750781 |
| PASS | scan_dmdv_below_m10 | Sec. 9 Tail exponents, amplitudes and the inner mass: dm/dv approaches the closed form from below: percentage below, m10 (scans.log) | 0.25 | 0.055 (1.49%, 0.75%, 0.255%) | 0.255371 |
| PASS | m2_static_rm | Sec. 10 Bounded h: r_- of the bounded static solution (m=1.5, alpha=1) | 1.031986 | 1e-06 (6 digits printed) | 1.03199 |
| PASS | m2_static_rp | Sec. 10 Bounded h: r_+ | 2.980943 | 1e-06 (7 digits printed) | 2.98094 |
| PASS | m2_static_km | Sec. 10 Bounded h: kappa_- | 0.797008 | 1e-06 (7 digits printed) | 0.797008 |
| PASS | m2_static_kp | Sec. 10 Bounded h: kappa_+ | 0.161359 | 1e-06 (7 digits printed) | 0.161359 |
| PASS | m2_static_psi | Sec. 10 Bounded h: psi(r_-) | 0.939 | 0.0005 (0.93897) | 0.938971 |
| PASS | m2_static_wall | Sec. 10 Bounded h: distance 0.061 from the wall alpha psi = 1 | 0.061 | 0.0005 (0.06103) | 0.0610286 |
| PASS | m2_plateau_B0.0003 | Sec. 10 Bounded h exponent: sigma_v on U~0.3 differs from -kappa_-(m_f) by (plateau_m2_B0.0003.log) | 1.3e-7 | 1e-08 | 1.3e-07 |
| PASS | m2_plateau_B0.003 | Sec. 10 Bounded h exponent: sigma_v on U~0.3 differs from -kappa_-(m_f) by (plateau_m2_B0.003.log) | 1.8e-6 | 1e-07 | 1.8e-06 |
| PASS | m2_plateau_B0.03 | Sec. 10 Bounded h exponent: sigma_v on U~0.3 differs from -kappa_-(m_f) by (plateau_m2_B0.03.log) | 5.5e-5 | 1e-06 | 5.5e-05 |
| PASS | m2_mf_B0.0003 | Sec. 10 Bounded h exponent: m_f for B=0.0003 (kap_check_m2_M1.5_B0.0003.log) | 1.50000028 | 1e-08 | 1.5 |
| PASS | m2_mf_B0.003 | Sec. 10 Bounded h exponent: m_f for B=0.003 (kap_check_m2_M1.5_B0.003.log) | 1.50002824 | 1e-08 | 1.50003 |
| PASS | m2_mf_B0.03 | Sec. 10 Bounded h exponent: m_f for B=0.03 (kap_check_m2_M1.5_B0.03.log) | 1.50283083 | 1e-08 | 1.50283 |
| PASS | m2_vf_B0.0003 | Sec. 10 Bounded h front: v_f on U~1 for B=0.0003 (front_m2_B0.0003.log) | 59.5 | 0.055 | 59.54 |
| PASS | m2_vf_B0.003 | Sec. 10 Bounded h front: v_f on U~1 for B=0.003 (front_m2_B0.003.log) | 46.1 | 0.055 | 46.08 |
| PASS | m2_vf_B0.03 | Sec. 10 Bounded h front: v_f on U~1 for B=0.03 (front_m2_B0.03.log) | 31.4 | 0.055 | 31.43 |
| PASS | m2_delay_decade | Sec. 10 Bounded h front: delay of 13.5 per decade between the two smaller amplitudes | 13.5 | 0.05 ((59.54 - 46.08) = 13.46) | 13.46 |
| PASS | m2_delay_efold | Sec. 10 Bounded h front: ... 5.85 per e-fold | 5.85 | 0.005 (13.46/ln 10 = 5.846) | 5.8456 |
| PASS | m2_delay_largest | Sec. 10 Bounded h front: ... and 14.7 for the largest | 14.7 | 0.05 (46.08 - 31.43 = 14.65) | 14.65 |
| PASS | m2_wall_gap_v70 | Sec. 10 Bounded h behind the front (B=3e-4, U~1): 1 - alpha psi at v=70 (late_m2_M1.5_B0.0003.log) | 3.1e-3 | 5.05e-05 | 0.003098 |
| PASS | m2_wall_gap_v80 | Sec. 10 Bounded h behind the front (B=3e-4, U~1): 1 - alpha psi at v=80 (late_m2_M1.5_B0.0003.log) | 9.3e-4 | 5.05e-06 | 0.0009258 |
| PASS | m2_wall_gap_v90 | Sec. 10 Bounded h behind the front (B=3e-4, U~1): 1 - alpha psi at v=90 (late_m2_M1.5_B0.0003.log) | 4.3e-4 | 5.05e-06 | 0.0004291 |
| PASS | m2_m_v70 | Sec. 10 Bounded h behind the front: m at v=70 | 6.96 | 0.00505 | 6.9647 |
| PASS | m2_m_v80 | Sec. 10 Bounded h behind the front: m at v=80 | 12.8 | 0.0505 | 12.762 |
| PASS | m2_m_v90 | Sec. 10 Bounded h behind the front: m at v=90 | 18.8 | 0.0505 | 18.752 |
| PASS | m2_dmdv_min | Sec. 10 Bounded h behind the front: dm/dv ~ 0.58 (10-unit difference of m over 70..80, 80..90) | 0.58 | 0.01 (0.58 (70-80), 0.60 (80-90)) | 0.57973 |
| PASS | m2_dmdv_max | Sec. 10 Bounded h behind the front: ... -0.60 | 0.60 | 0.01 (0.600) | 0.599 |
| PASS | m2_r_const | Sec. 10 Bounded h behind the front: r constant at r_- to 1e-6 (/r - 1.031986/ at v=70..90) | 1e-6 | bound: <= paper | 1e-12 |
| PASS | m2_sigma_v70 | Sec. 10 Bounded h behind the front: sigma_v at v=70 | -0.0891 | 5.5e-05 | -0.0891 |
| PASS | m2_sigma_v80 | Sec. 10 Bounded h behind the front: sigma_v at v=80 | -0.0685 | 5.5e-05 | -0.06847 |
| PASS | m2_sigma_v90 | Sec. 10 Bounded h behind the front: sigma_v at v=90 | -0.0587 | 5.5e-05 | -0.05869 |
| PASS | m2_dlev_v70 | Sec. 10 Bounded h behind the front: inter-level difference of Sigma at v=70 (relative) | 6e-9 | 5.5e-10 | 6e-09 |
| PASS | m2_dlev_v80 | Sec. 10 Bounded h behind the front: inter-level difference of Sigma at v=80 (relative) | 1.6e-6 | 1e-07 | 1.6e-06 |
| PASS | m2_dlev_v90 | Sec. 10 Bounded h behind the front: inter-level difference of Sigma at v=90 (relative) | 3e-4 | 5.5e-05 | 0.0003 |
| PASS | m2_dlev_v100 | Sec. 10 Bounded h behind the front: inter-level difference of Sigma at v=100 (relative) | 5e-2 | 0.005 (5.5e-2 quoted as 5e-2) | 0.055 |
| PASS | m2_K_v70 | Sec. 10 Bounded h behind the front: K at v=70 (units alpha=1) | 5.0e37 | 5e+35 (4.961e37) | 4.961e+37 |
| PASS | m2_K_v80 | Sec. 10 Bounded h behind the front: K at v=80 (units alpha=1) | 2.1e36 | 5.05e+34 | 2.077e+36 |
| PASS | m2_K_v90 | Sec. 10 Bounded h behind the front: K at v=90 (units alpha=1) | 3.5e35 | 5.05e+33 | 3.539e+35 |
| PASS | m2_win_B003_60 | Sec. 10 Bounded h windows: B=3e-3: inter-level difference of Sigma 2e-5 at v=60 | 2e-5 | 5.5e-06 | 2.1e-05 |
| PASS | m2_win_B003_70 | Sec. 10 Bounded h windows: ... 8e-3 at v=70 | 8e-3 | 0.0005 (7.7e-3) | 0.0077 |
| PASS | m2_win_B03_nonfinite | Sec. 10 Bounded h windows: B=3e-2: non-finite at v=60 on U~1 (late_m2_M1.5_B0.03.log; 1 = non-finite); the manuscript: beyond v ~ 55 | 1 | 0 (boolean) | 1 |
| PASS | m2_vb_h0.0125 | Sec. 10 Bounded h windows: first non-finite sample at h_v=0.0125 for B=3e-4 (bounded_aniso.log) | 127 | 0 (integer sampling) | 127 |
| PASS | m2_vb_h0.00625 | Sec. 10 Bounded h windows: first non-finite sample at h_v=0.00625 for B=3e-4 (bounded_aniso.log) | 135 | 0 (integer sampling) | 135 |
| PASS | m2_vb_h0.003125 | Sec. 10 Bounded h windows: first non-finite sample at h_v=0.003125 for B=3e-4 (bounded_aniso.log) | 144 | 0 (integer sampling) | 144 |
| PASS | m2_vb_h0.0015625 | Sec. 10 Bounded h windows: first non-finite sample at h_v=0.0015625 for B=3e-4 (bounded_aniso.log) | 153 | 0 (integer sampling) | 153 |
| PASS | m2_vb_shift | Sec. 10 Bounded h windows: 8.6 per halving of h_v (mean of 135-127, 144-135, 153-144) | 8.6 | 0.08 (26/3 = 8.67; integer sampling of v (increments 8, 9, 9)) | 8.66667 |
| PASS | m2_vb_law | Sec. 10 Bounded h windows: ln4/kappa_+ = 8.59 with kappa_+ = 0.1614 | 8.59 | 0.005 (ln 4/0.161359 = 8.592) | 8.59134 |
| PASS | m2_win_dlev_95 | Sec. 10 Bounded h windows: inter-level difference of sigma_v 1e-11 at v=95 | 1e-11 | 1e-11 | 1e-11 |
| PASS | m2_win_dlev_125 | Sec. 10 Bounded h windows: ... 1e-4 at v=125 | 1e-4 | 0.0001 | 0.0001 |
| PASS | m2_sigma_cont_v100 | Sec. 10 Bounded h windows: sigma_v continues to rise, at v=100 (bounded_aniso.log) | -0.0521 | 5.5e-05 | -0.05211 |
| PASS | m2_sigma_cont_v115 | Sec. 10 Bounded h windows: sigma_v continues to rise, at v=115 (bounded_aniso.log) | -0.0449 | 5.5e-05 | -0.04487 |
| PASS | m2_sigma_cont_v125 | Sec. 10 Bounded h windows: sigma_v continues to rise, at v=125 (bounded_aniso.log) | -0.0411 | 5.5e-05 | -0.04111 |
| PASS | m2_rho_rel | Sec. 10 Bounded h windows: sigma_v ~ rho_v/rho holds to 4e-4 for v>=95 (largest /sigma_v - dln rho/dv/ for 95<=v<=125) | 4e-4 | 5e-05 (3.62e-4) | 0.000362 |
| PASS | b4_r_h0.1 | Sec. 7 Code B (i): error in r at v=98 for h=0.1 (t_static_b4.log, maximum over the four rays) | 1.1e-6 | 5.5e-08 | 1.1e-06 |
| PASS | b4_r_h0.05 | Sec. 7 Code B (i): error in r at v=98 for h=0.05 (t_static_b4.log, maximum over the four rays) | 6.9e-8 | 5.5e-10 | 6.86e-08 |
| PASS | b4_r_h0.025 | Sec. 7 Code B (i): error in r at v=98 for h=0.025 (t_static_b4.log, maximum over the four rays) | 4.3e-9 | 5.5e-11 | 4.3e-09 |
| PASS | b4_sigma_v_h0.1 | Sec. 7 Code B (i): error in sigma_v at v=98 for h=0.1 (t_static_b4.log, maximum over the four rays) | 1.5e-5 | 5.5e-07 | 1.49e-05 |
| PASS | b4_sigma_v_h0.05 | Sec. 7 Code B (i): error in sigma_v at v=98 for h=0.05 (t_static_b4.log, maximum over the four rays) | 9.4e-7 | 5.5e-09 | 9.36e-07 |
| PASS | b4_sigma_v_h0.025 | Sec. 7 Code B (i): error in sigma_v at v=98 for h=0.025 (t_static_b4.log, maximum over the four rays) | 5.9e-8 | 5.5e-10 | 5.86e-08 |
| PASS | b4_psi_h0.1 | Sec. 7 Code B (i): error in psi at v=98 for h=0.1 (t_static_b4.log, maximum over the four rays) | 1.9e-6 | 5.5e-08 | 1.85e-06 |
| PASS | b4_psi_h0.05 | Sec. 7 Code B (i): error in psi at v=98 for h=0.05 (t_static_b4.log, maximum over the four rays) | 1.2e-7 | 5.5e-09 | 1.16e-07 |
| PASS | b4_psi_h0.025 | Sec. 7 Code B (i): error in psi at v=98 for h=0.025 (t_static_b4.log, maximum over the four rays) | 7.3e-9 | 5.5e-11 | 7.26e-09 |
| PASS | b4_order | Sec. 7 Code B (i): observed order 4.00 in every quantity at every time (smallest and largest over the 12 rows; smallest) | 4.00 | 0.005 (order(last) printed to 2 decimals) | 4 |
| PASS | b4_order_max | Sec. 7 Code B (i): ... largest | 4.00 | 0.005 (order(last) printed to 2 decimals) | 4 |
| PASS | b4_proj0_order | Sec. 7 Code B (i): the unconstrained version has the same order (smallest of the 12 rows; t_static_b4_proj0.log) | 4.00 | 0.005 (order(last) printed to 2 decimals) | 4 |
| PASS | b4_proj0_order_max | Sec. 7 Code B (i): ... largest | 4.00 | 0.005 (order(last) printed to 2 decimals) | 4 |
| PASS | hs_r60_05_0125 | Sec. 7 Code B (ii): relative difference between h_s=0.05 and 0.0125 in r at v=60 (cmp_hs.log) | 1.6e-8 | 1e-09 | 1.6e-08 |
| PASS | hs_r_05_025 | Sec. 7 Code B (ii): ... and 1.5e-8 between 0.05 and 0.025 | 1.5e-8 | 1e-09 | 1.5e-08 |
| PASS | hs_sV60 | Sec. 7 Code B (ii): ... 5.9e-8 in sigma_v at v=60 (0.05 vs 0.0125) | 5.9e-8 | 1e-09 | 5.9e-08 |
| PASS | hs_ratio_r | Sec. 7 Code B (ii): ratio of the errors of h_s=0.05 and 0.025 against 0.0125 is 17.0 in r (smallest over v=40..200) | 17.0 | 0.05 (fourth-order value 17 (printed to 0.1)) | 17 |
| PASS | hs_ratio_PV | Sec. 7 Code B (ii): ratio of the errors of h_s=0.05 and 0.025 against 0.0125 is 17.0 in phi_v (smallest over v=40..200) | 17.0 | 0.05 (fourth-order value 17 (printed to 0.1)) | 17 |
| PASS | hs_ratio_sV | Sec. 7 Code B (ii): ratio of the errors of h_s=0.05 and 0.025 against 0.0125 is 17.0 in sigma_v (smallest over v=40..200) | 17.0 | 0.05 (fourth-order value 17 (printed to 0.1)) | 17 |
| PASS | hs_ratio_sV250 | Sec. 7 Code B (ii): the clean ratio is lost beyond v=200: 4.5 at v=250 in sigma_v | 4.5 | 0.1 | 4.5 |
| PASS | hs_ratio_sV300 | Sec. 7 Code B (ii): ... 3.2 at v=300 | 3.2 | 0.1 | 3.2 |
| PASS | codeb_vb_hv0.2 | Sec. 7 Code B (iii): first non-finite v of code B at h_v=0.2 (cmp_table.log) | 252 | 0 (integer sampling) | 252 |
| PASS | codeb_vb_hv0.1 | Sec. 7 Code B (iii): first non-finite v of code B at h_v=0.1 (cmp_table.log) | 307 | 0 (integer sampling) | 307 |
| PASS | codeb_vb_hv0.05 | Sec. 7 Code B (iii): first non-finite v of code B at h_v=0.05 (cmp_table.log) | 364 | 0 (integer sampling) | 364 |
| PASS | codeb_vb_hv0.025 | Sec. 7 Code B (iii): first non-finite v of code B at h_v=0.025 (cmp_table.log) | 420 | 0 (integer sampling) | 420 |
| PASS | codeb_vb_hv0.0125 | Sec. 7 Code B (iii): first non-finite v of code B at h_v=0.0125 (cmp_table.log) | 477 | 0 (integer sampling) | 477 |
| PASS | codeb_vb_v360 | Sec. 7 Code B (iii): the blow-up does not depend on the end of the grid: h_v=0.1 gives 307 for v1=360 and 400 | 307 | 0 (integer sampling) | 307 |
| PASS | codeb_vb_shift0 | Sec. 7 Code B (iii): shift per halving of h_v, step 1 | 55 | 0 (integer sampling) | 55 |
| PASS | codeb_vb_shift1 | Sec. 7 Code B (iii): shift per halving of h_v, step 2 | 57 | 0 (integer sampling) | 57 |
| PASS | codeb_vb_shift2 | Sec. 7 Code B (iii): shift per halving of h_v, step 3 | 56 | 0 (integer sampling) | 56 |
| PASS | codeb_vb_shift3 | Sec. 7 Code B (iii): shift per halving of h_v, step 4 | 57 | 0 (integer sampling) | 57 |
| PASS | codeb_shift_theory | Sec. 7 Code B (iii): p ln2/kappa_+ = 56.6 for p=4 | 56.6 | 0.05 (4 ln 2/0.04896874 = 56.62) | 56.6196 |
| PASS | codeb_unconstrained_nf | Sec. 7 Code B (iv): the unconstrained version is non-finite at v = 70, 95, 112 for h_v = 0.1, 0.05, 0.025 (sum of the three) | 277 | 0 (integer sampling) | 277 |
| PASS | codeb_unc_70 | Sec. 7 Code B (iv): ... 70 at h_v=0.1 | 70 | 0 (integer sampling) | 70 |
| PASS | codeb_unc_95 | Sec. 7 Code B (iv): ... 95 at h_v=0.05 | 95 | 0 (integer sampling) | 95 |
| PASS | codeb_unc_112 | Sec. 7 Code B (iv): ... 112 at h_v=0.025 | 112 | 0 (integer sampling) | 112 |
| PASS | codeb_dhv_200 | Sec. 7 Code B (iii): change of sigma_v from the next coarser level at v=200 is 2e-7 (magnitude) | 2e-7 | 7.5e-08 | 2.1e-07 |
| PASS | codeb_dhv_300 | Sec. 7 Code B (iii): ... 2.2e-5 at v=300 (magnitude) | 2.2e-5 | 7.5e-07 | 2.2e-05 |
| PASS | cmpAB_sV_v40 | Sec. 7 Code B comparison with code A: relative difference of the two codes in sigma_v at v=40 (cmp_AB_final.log) | 4.6e-7 | 5.5e-09 | 4.6e-07 |
| PASS | cmpAB_sV_v60 | Sec. 7 Code B comparison with code A: relative difference of the two codes in sigma_v at v=60 (cmp_AB_final.log) | 6.3e-7 | 5.5e-09 | 6.3e-07 |
| PASS | cmpAB_sV_v100 | Sec. 7 Code B comparison with code A: relative difference of the two codes in sigma_v at v=100 (cmp_AB_final.log) | 2.5e-7 | 5.5e-09 | 2.5e-07 |
| PASS | cmpAB_sV_v150 | Sec. 7 Code B comparison with code A: relative difference of the two codes in sigma_v at v=150 (cmp_AB_final.log) | 6.2e-6 | 5.05e-08 | 6.2e-06 |
| PASS | cmpAB_sV_v200 | Sec. 7 Code B comparison with code A: relative difference of the two codes in sigma_v at v=200 (cmp_AB_final.log) | 8.1e-5 | 1e-06 | 8.1e-05 |
| PASS | cmpAB_r | Sec. 7 Code B comparison: relative difference in r is 1.0e-7 at 40<=v<=250 | 1.0e-7 | 1e-08 | 1e-07 |
| PASS | cmpAB_PV_v40 | Sec. 7 Code B comparison: relative difference in phi_v at v=40 | 3.8e-7 | 5.5e-09 | 3.8e-07 |
| PASS | cmpAB_PV_v100 | Sec. 7 Code B comparison: relative difference in phi_v at v=100 | 5.9e-7 | 5.5e-09 | 5.9e-07 |
| PASS | cmpAB_PV_v200 | Sec. 7 Code B comparison: relative difference in phi_v at v=200 | 1.6e-5 | 1e-06 | 1.6e-05 |
| PASS | cmpAB_PV_range_max | Sec. 7 Code B comparison: phi_v 3.8e-7 to 5.9e-7 for v<=100: largest (v=100) | 5.9e-7 | 1e-08 | 5.9e-07 |
| PASS | cmpAB_B_err_v150 | Sec. 7 Code B comparison: (change of B from h_v=0.1)/15 in sigma_v at v=150 | 6e-6 | 5e-06 (9e-5/15 = 6e-6, 1e-3/15 = 6.7e-5 (the log prints one digit)) | 6e-06 |
| PASS | cmpAB_B_err_v200 | Sec. 7 Code B comparison: (change of B from h_v=0.1)/15 in sigma_v at v=200 | 7e-5 | 1e-05 (9e-5/15 = 6e-6, 1e-3/15 = 6.7e-5 (the log prints one digit)) | 6.66667e-05 |
| PASS | tab_codeb_v100_A | Table tab:codeb, v=100, A (cmp_table.log) | -0.094251 | 1e-06 | -0.094251 |
| PASS | tab_codeb_v100_A+1.6e-4 | Table tab:codeb, v=100, A+1.6e-4 (cmp_table.log) | -0.094091 | 1e-06 | -0.094091 |
| PASS | tab_codeb_v100_B | Table tab:codeb, v=100, B (cmp_table.log) | -0.094081 | 1e-06 | -0.094081 |
| PASS | tab_codeb_v100_Delta_AB | Table tab:codeb, v=100, Delta_AB (cmp_table.log) | +1.0e-5 | 1e-06 | 1e-05 |
| PASS | tab_codeb_v100_Delta_h | Table tab:codeb, v=100, Delta_h (cmp_table.log) | 1e-9 | 6e-10 | 1.1e-09 |
| PASS | tab_codeb_v140_A | Table tab:codeb, v=140, A (cmp_table.log) | -0.079755 | 1e-06 | -0.079755 |
| PASS | tab_codeb_v140_A+1.6e-4 | Table tab:codeb, v=140, A+1.6e-4 (cmp_table.log) | -0.079595 | 1e-06 | -0.079595 |
| PASS | tab_codeb_v140_B | Table tab:codeb, v=140, B (cmp_table.log) | -0.079593 | 1e-06 | -0.079593 |
| PASS | tab_codeb_v140_Delta_AB | Table tab:codeb, v=140, Delta_AB (cmp_table.log) | +2.5e-6 | 1e-07 | 2.5e-06 |
| PASS | tab_codeb_v140_Delta_h | Table tab:codeb, v=140, Delta_h (cmp_table.log) | -2e-8 | 5.5e-09 | -1.6e-08 |
| PASS | tab_codeb_v180_A | Table tab:codeb, v=180, A (cmp_table.log) | -0.056255 | 1e-06 | -0.056255 |
| PASS | tab_codeb_v180_A+1.6e-4 | Table tab:codeb, v=180, A+1.6e-4 (cmp_table.log) | -0.056095 | 1e-06 | -0.056095 |
| PASS | tab_codeb_v180_B | Table tab:codeb, v=180, B (cmp_table.log) | -0.056092 | 1e-06 | -0.056092 |
| PASS | tab_codeb_v180_Delta_AB | Table tab:codeb, v=180, Delta_AB (cmp_table.log) | +3.4e-6 | 1e-07 | 3.4e-06 |
| PASS | tab_codeb_v180_Delta_h | Table tab:codeb, v=180, Delta_h (cmp_table.log) | -9e-8 | 5.5e-09 | -9.3e-08 |
| PASS | tab_codeb_v220_A | Table tab:codeb, v=220, A (cmp_table.log) | -0.034253 | 1e-06 | -0.034253 |
| PASS | tab_codeb_v220_A+1.6e-4 | Table tab:codeb, v=220, A+1.6e-4 (cmp_table.log) | -0.034093 | 1e-06 | -0.034093 |
| PASS | tab_codeb_v220_B | Table tab:codeb, v=220, B (cmp_table.log) | -0.034090 | 1e-06 | -0.03409 |
| PASS | tab_codeb_v220_Delta_AB | Table tab:codeb, v=220, Delta_AB (cmp_table.log) | +3.5e-6 | 1e-07 | 3.5e-06 |
| PASS | tab_codeb_v220_Delta_h | Table tab:codeb, v=220, Delta_h (cmp_table.log) | -5e-7 | 5.5e-08 | -4.9e-07 |
| PASS | tab_codeb_v260_A | Table tab:codeb, v=260, A (cmp_table.log) | -0.023090 | 1e-06 | -0.02309 |
| PASS | tab_codeb_v260_A+1.6e-4 | Table tab:codeb, v=260, A+1.6e-4 (cmp_table.log) | -0.022930 | 1e-06 | -0.02293 |
| PASS | tab_codeb_v260_B | Table tab:codeb, v=260, B (cmp_table.log) | -0.022925 | 1e-06 | -0.022925 |
| PASS | tab_codeb_v260_Delta_AB | Table tab:codeb, v=260, Delta_AB (cmp_table.log) | +5.4e-6 | 1e-07 | 5.4e-06 |
| PASS | tab_codeb_v260_Delta_h | Table tab:codeb, v=260, Delta_h (cmp_table.log) | -3e-6 | 5.5e-07 | -3.1e-06 |
| PASS | tab_codeb_v300_A | Table tab:codeb, v=300, A (cmp_table.log) | -0.018223 | 1e-06 | -0.018223 |
| PASS | tab_codeb_v300_A+1.6e-4 | Table tab:codeb, v=300, A+1.6e-4 (cmp_table.log) | -0.018063 | 1e-06 | -0.018063 |
| PASS | tab_codeb_v300_B | Table tab:codeb, v=300, B (cmp_table.log) | -0.018050 | 1e-06 | -0.01805 |
| PASS | tab_codeb_v300_Delta_AB | Table tab:codeb, v=300, Delta_AB (cmp_table.log) | +1.3e-5 | 1e-06 | 1.3e-05 |
| PASS | tab_codeb_v300_Delta_h | Table tab:codeb, v=300, Delta_h (cmp_table.log) | -2e-5 | 5.5e-06 | -2.2e-05 |
| PASS | cmpAB_delta_range | Sec. 7 Code B: A and B agree to 4e-6 (absolute) for 120<=v<=240 (largest /B-(A+1.6e-4)/) | 4e-6 | bound: <= paper | 3.9e-06 |
| PASS | cmpAB_delta_300 | Sec. 7 Code B: ... and 1.3e-5 at v=300 | 1.3e-5 | 1e-06 | 1.3e-05 |
| PASS | cmpAB_delta_100 | Sec. 7 Code B: at v=100 the difference is 1.0e-5 | 1.0e-5 | 1e-06 | 1e-05 |
| PASS | cmpAB_dsig_260 | Sec. 7 Code B: the error estimate of Table tab:end is 5e-9 at v=260 (endpoint_B0.003_merged.log) | 5e-9 | 1e-09 | 5e-09 |
| PASS | cmpAB_dsig_280 | Sec. 7 Code B: ... 4e-8 at v=280 | 4e-8 | 1e-08 | 4e-08 |
| PASS | cmpAB_gap_260 | Sec. 7 Code B: three orders below the gap to code B there: 5e-6 at v=260 | 5e-6 | 5e-07 (5.4e-6) | 5.4e-06 |
| PASS | cmpAB_gap_280 | Sec. 7 Code B: ... 7e-6 at v=280 | 7e-6 | 5e-07 (7.2e-6) | 7.2e-06 |
| PASS | mech1d_p4_hv0.2_v100 | Table tab:mech1d p=4, h_v=0.2, v=100 (mech_vb_B3e-3.log) | 3.63e-5 | 5.5e-08 | 3.63e-05 |
| PASS | mech1d_p4_hv0.2_v250 | Table tab:mech1d p=4, h_v=0.2, v=250 | 5.62e-2 | 5.5e-05 | 0.05621 |
| PASS | mech1d_p4_hv0.1_v100 | Table tab:mech1d p=4, h_v=0.1, v=100 (mech_vb_B3e-3.log) | 2.41e-6 | 5.5e-09 | 2.408e-06 |
| PASS | mech1d_p4_hv0.1_v250 | Table tab:mech1d p=4, h_v=0.1, v=250 | 3.73e-3 | 5.5e-06 | 0.003729 |
| PASS | mech1d_p4_hv0.1_ratio | Table tab:mech1d p=4, h_v=0.1, ratio to the previous step (v=100) | 15.1 | 0.05 (ratio printed to 0.1) | 15.1 |
| PASS | mech1d_p4_hv0.05_v100 | Table tab:mech1d p=4, h_v=0.05, v=100 (mech_vb_B3e-3.log) | 1.53e-7 | 5.5e-10 | 1.529e-07 |
| PASS | mech1d_p4_hv0.05_v250 | Table tab:mech1d p=4, h_v=0.05, v=250 | 2.37e-4 | 5.5e-07 | 0.0002368 |
| PASS | mech1d_p4_hv0.05_ratio | Table tab:mech1d p=4, h_v=0.05, ratio to the previous step (v=100) | 15.7 | 0.05 (ratio printed to 0.1) | 15.7 |
| PASS | mech1d_p4_hv0.025_v100 | Table tab:mech1d p=4, h_v=0.025, v=100 (mech_vb_B3e-3.log) | 9.59e-9 | 5.5e-12 | 9.594e-09 |
| PASS | mech1d_p4_hv0.025_v250 | Table tab:mech1d p=4, h_v=0.025, v=250 | 1.49e-5 | 5.5e-08 | 1.486e-05 |
| PASS | mech1d_p4_hv0.025_ratio | Table tab:mech1d p=4, h_v=0.025, ratio to the previous step (v=100) | 15.9 | 0.05 (ratio printed to 0.1) | 15.9 |
| PASS | mech1d_p4_hv0.0125_v100 | Table tab:mech1d p=4, h_v=0.0125, v=100 (mech_vb_B3e-3.log) | 6.00e-10 | 5.5e-13 | 6.002e-10 |
| PASS | mech1d_p4_hv0.0125_v250 | Table tab:mech1d p=4, h_v=0.0125, v=250 | 9.30e-7 | 5.5e-10 | 9.295e-07 |
| PASS | mech1d_p4_hv0.0125_ratio | Table tab:mech1d p=4, h_v=0.0125, ratio to the previous step (v=100) | 16.0 | 0.05 (ratio printed to 0.1) | 16 |
| PASS | mech1d_p2_hv0.2_v100 | Table tab:mech1d p=2, h_v=0.2, v=100 (mech_vb_B3e-3.log) | 2.46e-3 | 5.5e-06 | 0.002455 |
| PASS | mech1d_p2_hv0.2_v250 | Table tab:mech1d p=2, h_v=0.2, v=250 | 3.80 | 0.0055 | 3.801 |
| PASS | mech1d_p2_hv0.1_v100 | Table tab:mech1d p=2, h_v=0.1, v=100 (mech_vb_B3e-3.log) | 6.42e-4 | 5.5e-07 | 0.0006419 |
| PASS | mech1d_p2_hv0.1_v250 | Table tab:mech1d p=2, h_v=0.1, v=250 | 0.994 | 0.00055 | 0.9941 |
| PASS | mech1d_p2_hv0.1_ratio | Table tab:mech1d p=2, h_v=0.1, ratio to the previous step (v=100) | 3.8 | 0.05 (ratio printed to 0.1) | 3.8 |
| PASS | mech1d_p2_hv0.05_v100 | Table tab:mech1d p=2, h_v=0.05, v=100 (mech_vb_B3e-3.log) | 1.63e-4 | 5.5e-07 | 0.0001627 |
| PASS | mech1d_p2_hv0.05_v250 | Table tab:mech1d p=2, h_v=0.05, v=250 | 0.252 | 0.00055 | 0.2519 |
| PASS | mech1d_p2_hv0.05_ratio | Table tab:mech1d p=2, h_v=0.05, ratio to the previous step (v=100) | 3.9 | 0.05 (ratio printed to 0.1) | 3.9 |
| PASS | mech1d_p2_hv0.025_v100 | Table tab:mech1d p=2, h_v=0.025, v=100 (mech_vb_B3e-3.log) | 4.08e-5 | 5.5e-08 | 4.084e-05 |
| PASS | mech1d_p2_hv0.025_v250 | Table tab:mech1d p=2, h_v=0.025, v=250 | 6.33e-2 | 5.5e-05 | 0.06325 |
| PASS | mech1d_p2_hv0.025_ratio | Table tab:mech1d p=2, h_v=0.025, ratio to the previous step (v=100) | 4.0 | 0.05 (ratio printed to 0.1) | 4 |
| PASS | mech1d_p2_hv0.0125_v100 | Table tab:mech1d p=2, h_v=0.0125, v=100 (mech_vb_B3e-3.log) | 1.02e-5 | 5.5e-08 | 1.023e-05 |
| PASS | mech1d_p2_hv0.0125_v250 | Table tab:mech1d p=2, h_v=0.0125, v=250 | 1.58e-2 | 5.5e-05 | 0.01584 |
| PASS | mech1d_p2_hv0.0125_ratio | Table tab:mech1d p=2, h_v=0.0125, ratio to the previous step (v=100) | 4.0 | 0.05 (ratio printed to 0.1) | 4 |
| PASS | mech1d_ratio4_lo | Sec. 8 Mechanism: ratio per halving for p=4 lies in 15.1--16.0 at all four times (smallest) | 15.1 | 0.05 (printed to 0.1) | 15.1 |
| PASS | mech1d_ratio4_hi | Sec. 8 Mechanism: ... largest | 16.0 | 0.05 (printed to 0.1) | 16 |
| PASS | mech1d_ratio2_lo | Sec. 8 Mechanism: ratio per halving for p=2 lies in 3.8--4.0 (smallest) | 3.8 | 0.05 (printed to 0.1) | 3.8 |
| PASS | mech1d_ratio2_hi | Sec. 8 Mechanism: ... largest | 4.0 | 0.05 (printed to 0.1) | 4 |
| PASS | mech1d_growth | Sec. 8 Mechanism: growth of the p=4 error between v=100 and 250 (finest step) is 1548 | 1548 | 1 (error columns printed to 4 digits (0.05% relative)) | 1548.65 |
| PASS | mech1d_growth_exp | Sec. 8 Mechanism: e^{150 kappa_+} = 1549 | 1549 | 1 (kappa_+ = 0.04896874 to 7 digits) | 1548.92 |
| PASS | mech1d_C4 | Sec. 8 Mechanism: eps_4 = 20.4 B^2 h_v^4 e^{kappa_+ v} (finest step, v=100) | 20.4 | 0.05 (C_4 = 20.43 from 6.002e-10) | 20.4047 |
| PASS | mech1d_C2 | Sec. 8 Mechanism: eps_2 = 54 B^2 h_v^2 e^{kappa_+ v} | 54 | 0.5 (C_2 = 54.4) | 54.3412 |
| PASS | mech1d_shift2 | Sec. 8 Mechanism: 2 ln2/kappa_+ = 28.3 | 28.3 | 0.05 (28.31) | 28.3098 |
| PASS | vbpred_err_hv0.2 | Sec. 8 Mechanism: model error at the measured blow-up, h_v=0.2 (vb_prediction.log) | 0.0620 | 0.0001 | 0.062 |
| PASS | vbpred_err_hv0.1 | Sec. 8 Mechanism: model error at the measured blow-up, h_v=0.1 (vb_prediction.log) | 0.0608 | 0.0001 | 0.0608 |
| PASS | vbpred_err_hv0.05 | Sec. 8 Mechanism: model error at the measured blow-up, h_v=0.05 (vb_prediction.log) | 0.0629 | 0.0001 | 0.0629 |
| PASS | vbpred_err_hv0.025 | Sec. 8 Mechanism: model error at the measured blow-up, h_v=0.025 (vb_prediction.log) | 0.0613 | 0.0001 | 0.0613 |
| PASS | vbpred_err_hv0.0125 | Sec. 8 Mechanism: model error at the measured blow-up, h_v=0.0125 (vb_prediction.log) | 0.0625 | 0.0001 | 0.0625 |
| PASS | vbpred_delta | Sec. 8 Mechanism: delta* = 0.0619 (Table tab:vbmech) | 0.0619 | 0.0001 | 0.0619 |
| PASS | vbpred_delta_text | Sec. 8 Mechanism: delta* = 0.062 +- 0.001 in the text | 0.062 | 0.0005 (rounded to 3 decimals in the text (0.0619)) | 0.0619 |
| PASS | vbpred_delta_err | Sec. 8 Mechanism: ... the scatter 0.0008 is below the quoted +-0.001 | 0.001 | bound: <= paper | 0.0008 |
| PASS | vbpred_0.003_0.2 | Table tab:vbmech model row B=0.003, h_v=0.2 (vb_prediction.log) | 252.0 | 0.1 | 252 |
| PASS | vbpred_0.003_0.1 | Table tab:vbmech model row B=0.003, h_v=0.1 (vb_prediction.log) | 307.4 | 0.1 | 307.4 |
| PASS | vbpred_0.003_0.05 | Table tab:vbmech model row B=0.003, h_v=0.05 (vb_prediction.log) | 363.7 | 0.1 | 363.7 |
| PASS | vbpred_0.003_0.025 | Table tab:vbmech model row B=0.003, h_v=0.025 (vb_prediction.log) | 420.2 | 0.1 | 420.2 |
| PASS | vbpred_0.003_0.0125 | Table tab:vbmech model row B=0.003, h_v=0.0125 (vb_prediction.log) | 476.8 | 0.1 | 476.8 |
| PASS | vbpred_0.03_0.2 | Table tab:vbmech model row B=0.03, h_v=0.2 (vb_prediction.log) | 158.4 | 0.1 | 158.4 |
| PASS | vbpred_0.03_0.1 | Table tab:vbmech model row B=0.03, h_v=0.1 (vb_prediction.log) | 213.9 | 0.1 | 213.9 |
| PASS | vbpred_0.03_0.05 | Table tab:vbmech model row B=0.03, h_v=0.05 (vb_prediction.log) | 270.3 | 0.1 | 270.3 |
| PASS | vbpred_0.03_0.025 | Table tab:vbmech model row B=0.03, h_v=0.025 (vb_prediction.log) | 326.9 | 0.1 | 326.9 |
| PASS | vbpred_0.03_0.0125 | Table tab:vbmech model row B=0.03, h_v=0.0125 (vb_prediction.log) | 383.6 | 0.1 | 383.6 |
| PASS | vbpred_0.0003_0.2 | Table tab:vbmech model row B=0.0003, h_v=0.2 (vb_prediction.log) | 346.2 | 0.1 | 346.2 |
| PASS | vbpred_0.0003_0.1 | Table tab:vbmech model row B=0.0003, h_v=0.1 (vb_prediction.log) | 401.5 | 0.1 | 401.5 |
| PASS | vbpred_0.0003_0.05 | Table tab:vbmech model row B=0.0003, h_v=0.05 (vb_prediction.log) | 457.8 | 0.1 | 457.8 |
| PASS | vbpred_0.0003_0.025 | Table tab:vbmech model row B=0.0003, h_v=0.025 (vb_prediction.log) | 514.2 | 0.1 | 514.2 |
| PASS | vbpred_0.0003_0.0125 | Table tab:vbmech model row B=0.0003, h_v=0.0125 (vb_prediction.log) | 570.8 | 0.1 | 570.8 |
| PASS | vbmeas_0.003_0.2 | Table tab:vbmech measured, B=0.003, h_v=0.2 | 252 | 0 (integer sampling) | 252 |
| PASS | vbmeas_0.003_0.1 | Table tab:vbmech measured, B=0.003, h_v=0.1 | 307 | 0 (integer sampling) | 307 |
| PASS | vbmeas_0.003_0.05 | Table tab:vbmech measured, B=0.003, h_v=0.05 | 364 | 0 (integer sampling) | 364 |
| PASS | vbmeas_0.003_0.025 | Table tab:vbmech measured, B=0.003, h_v=0.025 | 420 | 0 (integer sampling) | 420 |
| PASS | vbmeas_0.003_0.0125 | Table tab:vbmech measured, B=0.003, h_v=0.0125 | 477 | 0 (integer sampling) | 477 |
| PASS | vbmeas_0.03_0.2 | Table tab:vbmech measured, B=0.03, h_v=0.2 | 158 | 0 (integer sampling) | 158 |
| PASS | vbmeas_0.03_0.1 | Table tab:vbmech measured, B=0.03, h_v=0.1 | 214 | 0 (integer sampling) | 214 |
| PASS | vbmeas_0.03_0.05 | Table tab:vbmech measured, B=0.03, h_v=0.05 | 270 | 0 (integer sampling) | 270 |
| PASS | vbmeas_0.0003_0.2 | Table tab:vbmech measured, B=0.0003, h_v=0.2 | 346 | 0 (integer sampling) | 346 |
| PASS | vbshift_B_0.2 | Sec. 8 Mechanism: v_b(B=3e-2) - v_b(B=3e-3) at h_v=0.2 | -94 | 0 (integers) | -94 |
| PASS | vbshift_B_0.1 | Sec. 8 Mechanism: v_b(B=3e-2) - v_b(B=3e-3) at h_v=0.1 | -93 | 0 (integers) | -93 |
| PASS | vbshift_B_0.05 | Sec. 8 Mechanism: v_b(B=3e-2) - v_b(B=3e-3) at h_v=0.05 | -94 | 0 (integers) | -94 |
| PASS | vbshift_theory | Sec. 8 Mechanism: -(2/kappa_+) ln 10 = -94.0 | -94.0 | 0.05 (-94.04) | -94.0431 |
| PASS | vbmodel_C2ratio | Sec. 8 Mechanism: delta*/C_2 for the midpoint model is 1.1e-3 | 1.1e-3 | 0.0001 (0.0619/54.4 = 1.14e-3; the text quotes two digits) | 0.00113787 |
| PASS | vbB_0.03_k1.5_0.2 | Sec. 8 Mechanism: first non-finite advanced time of code B, genb_p1_hs0.05_m1_B0.03_k1.5_v330.json, h_v=0.2 (vb_B3e-2_B3e-4.log) | 158 | 0 (integer sampling) | 158 |
| PASS | vbB_0.03_k1.5_0.1 | Sec. 8 Mechanism: first non-finite advanced time of code B, genb_p1_hs0.05_m1_B0.03_k1.5_v330.json, h_v=0.1 (vb_B3e-2_B3e-4.log) | 214 | 0 (integer sampling) | 214 |
| PASS | vbB_0.03_k1.5_0.05 | Sec. 8 Mechanism: first non-finite advanced time of code B, genb_p1_hs0.05_m1_B0.03_k1.5_v330.json, h_v=0.05 (vb_B3e-2_B3e-4.log) | 270 | 0 (integer sampling) | 270 |
| PASS | vbB_0.0003_k1_0.2 | Sec. 8 Mechanism: first non-finite advanced time of code B, genb_p1_hs0.05_m1_B0.0003_k1.5_v400.json, h_v=0.2 (vb_B3e-2_B3e-4.log) | 346 | 0 (integer sampling) | 346 |
| PASS | te_r_h0.2 | Sec. 8 Code E (i): error in r at v=98 for h=0.2 (t_static_e.log) | 1.2e-5 | 5.5e-07 | 1.24e-05 |
| PASS | te_r_h0.1 | Sec. 8 Code E (i): error in r at v=98 for h=0.1 (t_static_e.log) | 8.0e-7 | 5.5e-09 | 7.96e-07 |
| PASS | te_r_h0.05 | Sec. 8 Code E (i): error in r at v=98 for h=0.05 (t_static_e.log) | 5.0e-8 | 5.5e-10 | 5.04e-08 |
| PASS | te_sigma_v_h0.2 | Sec. 8 Code E (i): error in sigma_v at v=98 for h=0.2 (t_static_e.log) | 2.3e-4 | 5.5e-06 | 0.000225 |
| PASS | te_sigma_v_h0.1 | Sec. 8 Code E (i): error in sigma_v at v=98 for h=0.1 (t_static_e.log) | 1.4e-5 | 6e-07 (1.44e-5 printed as 1.4e-5 in the paper) | 1.44e-05 |
| PASS | te_sigma_v_h0.05 | Sec. 8 Code E (i): error in sigma_v at v=98 for h=0.05 (t_static_e.log) | 9.0e-7 | 5.5e-09 | 9.03e-07 |
| PASS | te_psi_h0.2 | Sec. 8 Code E (i): error in psi at v=98 for h=0.2 (t_static_e.log) | 2.1e-5 | 5.5e-07 | 2.09e-05 |
| PASS | te_psi_h0.1 | Sec. 8 Code E (i): error in psi at v=98 for h=0.1 (t_static_e.log) | 1.4e-6 | 5.5e-08 | 1.35e-06 |
| PASS | te_psi_h0.05 | Sec. 8 Code E (i): error in psi at v=98 for h=0.05 (t_static_e.log) | 8.5e-8 | 5.5e-10 | 8.53e-08 |
| PASS | te_order_lo | Sec. 8 Code E (i): observed order 3.98--3.99 (smallest) | 3.98 | 0.005 (printed to 2 decimals) | 3.98 |
| PASS | te_order_hi | Sec. 8 Code E (i): ... largest | 3.99 | 0.005 (printed to 2 decimals) | 3.99 |
| PASS | ce2_hv_dsv | Sec. 8 Code E (ii): the change of sigma_v on halving h_v is 5e-7 and constant for 100<=v<=1100 (smallest) | 5e-7 | 1e-07 (4.9e-7 ... 5.3e-7) | 4.9e-07 |
| PASS | ce2_hv_dsv_hi | Sec. 8 Code E (ii): ... largest | 5e-7 | 1e-07 (4.9e-7 ... 5.3e-7) | 5.3e-07 |
| PASS | ce2_hs_dsv_100 | Sec. 8 Code E (ii): the change on halving h_s is 1.6e-7 at v=100 | 1.6e-7 | 1e-08 | 1.6e-07 |
| PASS | ce2_hs_dsv_late | Sec. 8 Code E (ii): ... and <=5e-9 for 300<=v<=1000 (largest, v=300) | 5e-9 | bound: <= paper | 4.6e-09 |
| PASS | ce2_hv_dr | Sec. 8 Code E (ii): relative change of r is 3.3e-7 (h_v), constant in v | 3.3e-7 | 1e-08 | 3.3e-07 |
| PASS | ce2_hs_dr | Sec. 8 Code E (ii): ... 3.9e-6 (h_s) | 3.9e-6 | 1e-07 | 3.9e-06 |
| PASS | ce2_v1_K_650 | Sec. 8 Code E range: changing v_1 from 1200 to 1500 changes K by <=6e-9 for v<=650 | 6e-9 | 5e-10 (6.1e-9) | 6.1e-09 |
| PASS | ce2_v1_K_1000 | Sec. 8 Code E range: ... 4e-7 at v=1000 | 4e-7 | 5.5e-08 | 3.8e-07 |
| PASS | ce2_v1_K_1100 | Sec. 8 Code E range: ... 3e-6 at v=1100 | 3e-6 | 5.5e-07 | 2.9e-06 |
| PASS | ce2_hv_K | Sec. 8 Code E range: halving h_v changes K by 2e-5 (v=100..1100; largest) | 2e-5 | 1e-05 (2.1e-5 ... 2.7e-5) | 2.7e-05 |
| PASS | ce2_hs_K | Sec. 8 Code E range: halving h_s changes K by 3e-4 (5e-4 at v=100) | 3e-4 | 5e-05 (3.2e-4 ... 3.5e-4) | 0.00033 |
| PASS | ce2_hs_K100 | Sec. 8 Code E range: ... 5e-4 at v=100 | 5e-4 | 5.5e-05 | 0.0005 |
| PASS | ce2_hv_dr_abs | Sec. 8 Code E range: halving h_v changes r by 3e-7 | 3e-7 | 5e-08 (3.3e-7) | 3.3e-07 |
| PASS | ce2_hs_dr_abs | Sec. 8 Code E range: halving h_s changes r by 4e-6 | 4e-6 | 5e-07 (3.9e-6) | 3.9e-06 |
| PASS | ce2_hv_dsv_abs | Sec. 8 Code E range: halving h_v changes sigma_v by 5e-7 (absolute) | 5e-7 | 1e-07 (4.9e-7 ... 5.3e-7) | 5.2e-07 |
| PASS | ce2_ld_K | Sec. 8 Code E range (c): long double against double, K differs by <=4e-7 at v<=1100 (largest 4.2e-7) | 4e-7 (manuscript: $K$ differs by $\le4\times10^{-7}$ and) | 3e-08 (4.2e-7 in the log, one digit in the paper) | 4.2e-07 |
| PASS | ce2_ld_dsv | Sec. 8 Code E range (c): ... and sigma_v by <=6e-13 | 6e-13 | bound: <= paper (+5e-14: 5.9e-13) (5.9e-13) | 5.9e-13 |
| PASS | ce_sV_v100 | Sec. 8 Code E (iii): relative difference of sigma_v between code E and code B at v=100 (conv_e.log) | 1.0e-4 | 1e-05 | 0.0001 |
| PASS | ce_sV_v140 | Sec. 8 Code E (iii): relative difference of sigma_v between code E and code B at v=140 (conv_e.log) | 8.7e-6 | 1e-07 | 8.7e-06 |
| PASS | ce_sV_v180 | Sec. 8 Code E (iii): relative difference of sigma_v between code E and code B at v=180 (conv_e.log) | 3.6e-6 | 1e-07 | 3.6e-06 |
| PASS | ce_sV_v220 | Sec. 8 Code E (iii): relative difference of sigma_v between code E and code B at v=220 (conv_e.log) | 3.8e-6 | 1e-07 | 3.8e-06 |
| PASS | ce_sV_v260 | Sec. 8 Code E (iii): relative difference of sigma_v between code E and code B at v=260 (conv_e.log) | 1.2e-5 | 1e-06 | 1.2e-05 |
| PASS | ce_sV_v300 | Sec. 8 Code E (iii): relative difference of sigma_v between code E and code B at v=300 (conv_e.log) | 8e-5 | 5e-06 (8.3e-5) | 8.3e-05 |
| PASS | ce_sV_v380 | Sec. 8 Code E (iii): relative difference of sigma_v between code E and code B at v=380 (conv_e.log) | 5.6e-3 | 0.0001 | 0.0056 |
| PASS | ce_r | Sec. 8 Code E (iii): relative difference of r is 2.6e-7 | 2.6e-7 | 1e-08 | 2.6e-07 |
| PASS | ce_PV_lo | Sec. 8 Code E (iii): phi_v differs by (5--7)e-7 for v<=220 (smallest) | 5e-7 | 5e-08 (4.6e-7) | 4.6e-07 |
| PASS | ce_PV_hi | Sec. 8 Code E (iii): ... largest | 7e-7 | 5e-08 (6.8e-7) | 6.8e-07 |
| PASS | ce_codeb_dh_300 | Sec. 8 Code E (iii): Table tab:codeb Delta_h = -2e-5 at v=300 | -2e-5 | 5e-06 (-2.2e-5) | -2.2e-05 |
| PASS | seed_tab_0.05_1e-15 | Table tab:seed, v (>0.05), eps=1e-15 (seed_amplitude.log) | 747 | 0 (integer sampling) | 747 |
| PASS | seed_tab_0.05_3.55e-15 | Table tab:seed, v (>0.05), eps=3.55e-15 (seed_amplitude.log) | 722 | 0 (integer sampling) | 722 |
| PASS | seed_tab_0.05_1e-14 | Table tab:seed, v (>0.05), eps=1e-14 (seed_amplitude.log) | 701 | 0 (integer sampling) | 701 |
| PASS | seed_tab_0.05_1e-13 | Table tab:seed, v (>0.05), eps=1e-13 (seed_amplitude.log) | 656 | 0 (integer sampling) | 656 |
| PASS | seed_tab_0.05_1e-12 | Table tab:seed, v (>0.05), eps=1e-12 (seed_amplitude.log) | 610 | 0 (integer sampling) | 610 |
| PASS | seed_tab_0.5_1e-15 | Table tab:seed, v (>0.5), eps=1e-15 (seed_amplitude.log) | 788 | 0 (integer sampling) | 788 |
| PASS | seed_tab_0.5_3.55e-15 | Table tab:seed, v (>0.5), eps=3.55e-15 (seed_amplitude.log) | 763 | 0 (integer sampling) | 763 |
| PASS | seed_tab_0.5_1e-14 | Table tab:seed, v (>0.5), eps=1e-14 (seed_amplitude.log) | 742 | 0 (integer sampling) | 742 |
| PASS | seed_tab_0.5_1e-13 | Table tab:seed, v (>0.5), eps=1e-13 (seed_amplitude.log) | 696 | 0 (integer sampling) | 696 |
| PASS | seed_tab_0.5_1e-12 | Table tab:seed, v (>0.5), eps=1e-12 (seed_amplitude.log) | 650 | 0 (integer sampling) | 650 |
| PASS | seed_slope | Sec. 9 Seed: shift -19.8 per e-fold of eps (fit 1e-15..1e-12, threshold 0.05) | -19.8 | 0.055 | -19.81 |
| PASS | seed_rms | Sec. 9 Seed: rms residual 0.2 | 0.2 | 0.05 (0.21) | 0.21 |
| PASS | seed_expect | Sec. 9 Seed: -1/kappa_+ = -20.4 | -20.4 | 0.055 | -20.42 |
| PASS | seed_expect2 | Sec. 9 Seed: 1/kappa_+ = 20.4 from the static kappa_+ | 20.4 | 0.05 (20.42) | 20.4212 |
| PASS | seed_s_loose740 | Sec. 9 Seed (iii): v sigma_v at v=740 for loose tolerances is -4.47 | -4.47 | 0.005 (-4.4664 printed with 4 decimals) | -4.4664 |
| PASS | seed_s_default740 | Sec. 9 Seed (iii): ... -4.94 (default) | -4.94 | 0.005 (-4.94032) | -4.94032 |
| PASS | seed_s_tight740 | Sec. 9 Seed (iii): ... -5.23 (tight) | -5.23 | 0.005 (-5.22996) | -5.22996 |
| PASS | seed_s_offset | Sec. 9 Seed (v): r_+ - r_H(0) = 3.55e-15 (two ulps) | 3.55e-15 | 5e-18 (3.553e-15) | 3.553e-15 |
| PASS | seed_s_eps0 | Sec. 9 Seed: corrected row (EPS=0) v sigma_v at v=780 is regular (-5.07205) | -5.07205 | 1e-05 | -5.07205 |
| PASS | seed_s_eps355 | Sec. 9 Seed: EPS=3.55e-15 reproduces the former behaviour (v=780: -3.29) | -3.29 | 0.005 (-3.29359 vs the default -3.29144 (EPS 3.55e-15 vs the actual 3.553e-15)) | -3.29359 |
| PASS | seed_s_chan | Sec. 9 Seed (iv): replacing any column channel changes nothing visible (largest change of v sigma_v at v<=780) | 0 | bound: <= paper (+5e-06: five printed digits) (five printed digits) | 0 |
| PASS | seed_s_rowdoes | Sec. 9 Seed (iv): replacing the initial row does the whole change (tight row + default column equals the tight run at v=740) | -5.23 | 0.005 (-5.22996) | -5.22996 |
| PASS | seed_s_noise | Sec. 9 Seed: perturbing sigma_U^H or phi_U^H by 1e-12 has no effect (largest change) | 0 | bound: <= paper (+1e-13: printed 0.0e+00) (printed 0.0e+00) | 0 |
| PASS | seed_s_colchange | Sec. 9 Seed: the column changes by a few ulps only (largest relative difference of r_H, sigma_H, sigma_v^H <= 5e-14) | 5e-14 | bound: <= paper (+1e-13: the log prints max over the fields (2e-15, 5e-14, 2e-15)) (the log prints max over the fields (2e-15, 5e-14, 2e-15)) | 5e-14 |
| PASS | seed_s_rvH | Sec. 9 Seed: r_v^H of the column differs at 3e-18 only (absolute, v=0) | 3e-18 | 1e-18 | 3e-18 |
| PASS | int_rel_far | Sec. 12 Collapse (ii): psi equals the static Hayward function to <=1e-5 from r=30 down to r~11 (largest /rel/ for r>=11, interior.log) | 1e-5 | bound: <= paper (+2e-07: the largest is 1.0e-5 printed to 2 digits) (the largest is 1.0e-5 printed to 2 digits) | 1e-05 |
| PASS | int_rel_r38 | Sec. 12 Collapse (ii): ... 4e-5 at r=3.8 (log: 4.5e-5) | 4e-5 | 1e-05 (the paper rounds 4.5e-5 down to one digit) | 4.5e-05 |
| PASS | int_rel_r1058 | Sec. 12 Collapse (ii): ... 1.3e-3 at r=1.0579 | 1.3e-3 | 0.0001 | 0.0013 |
| PASS | int_r1058 | Sec. 12 Collapse (ii): the radius of that point is 1.0579 | 1.0579 | 0.0001 | 1.0579 |
| PASS | int_rm_gap | Sec. 12 Collapse (ii): that point is within 1e-3 of r_- = 1.05747 (r - r_-) | 1e-3 | bound: <= paper | 0.00043 |
| PASS | int_rel_tail1 | Sec. 12 Collapse (ii): beyond that the deviation grows to 1.5% (u=35.1) | 1.5e-2 | 0.0005 (1.5e-2 printed with 2 digits) | 0.015 |
| PASS | int_rel_tail2 | Sec. 12 Collapse (ii): ... 6% (u=36.4) | 6e-2 | 0.005 (6.4e-2 rounded to one digit by the paper) | 0.064 |
| PASS | int_rel_tail3 | Sec. 12 Collapse (ii): ... 45% at the last point (u=39) | 45e-2 | 0.0075 | 0.45 |
| PASS | int_nan | Sec. 12 Collapse (ii): no non-finite point on the row (nan count) | 0 | 0 (integer) | 0 |
| PASS | overlap_34.920 | Sec. 12 Collapse test (a): psi on v=150 against stage L at r_*=34.920 (overlap.log) | 5e-5 | 1e-05 | 4.9e-05 |
| PASS | overlap_19.895 | Sec. 12 Collapse test (a): psi on v=150 against stage L at r_*=19.895 (overlap.log) | 2.5e-4 | 3e-05 | 0.000247 |
| PASS | overlap_1.817 | Sec. 12 Collapse test (a): psi on v=150 against stage L at r_*=1.817 (overlap.log) | 1.4e-3 | 0.0001 | 0.00138 |
| PASS | overlap_-10.238 | Sec. 12 Collapse test (a): psi on v=150 against stage L at r_*=-10.238 (overlap.log) | 1.6e-2 | 0.001 | 0.0156 |
| PASS | overlap_np_34.941 | Sec. 12 Collapse test (c): k=2 matching, stage N against stage L at r_*=34.941 (overlap_np.log) | 1e-3 | 0.0001 (9.55e-4 quoted as 1e-3) | 0.000955 |
| PASS | overlap_np_19.971 | Sec. 12 Collapse test (c): k=2 matching, stage N against stage L at r_*=19.971 (overlap_np.log) | 1.3e-4 | 5.5e-06 | 0.000133 |
| PASS | overlap_np_-8.912 | Sec. 12 Collapse test (c): k=2 matching, stage N against stage L at r_*=-8.912 (overlap_np.log) | 1.1e-4 | 5.5e-06 | 0.000114 |
| PASS | tables_v1 | Sec. 12 Collapse test (b): the horizon table is independent of the switching time v_1=60,70,80 to 3e-5 (largest over both models, both comparisons, all windows) | 3e-5 | bound: <= paper (+1e-06: 2.6e-5 printed with 2 digits) (2.6e-5 printed with 2 digits) | 2.6e-05 |
| PASS | tables_h | Sec. 12 Collapse test (b): ... and of the mesh (h_N=h_L=0.1 -> 0.05) to 5e-5 | 5e-5 | bound: <= paper (+1e-06: 5.0e-5) (5.0e-5) | 5e-05 |
| PASS | mscale_E_m3.0 | Sec. 12 Collapse test (c): Einstein limit B/m^3 for m=3.0 (mscale.log) | 0.2017 | 0.0001 | 0.2017 |
| PASS | mscale_E_m5.0 | Sec. 12 Collapse test (c): Einstein limit B/m^3 for m=5.0 (mscale.log) | 0.2017 | 0.0001 | 0.2017 |
| PASS | mscale_E_m10.0 | Sec. 12 Collapse test (c): Einstein limit B/m^3 for m=10.0 (mscale.log) | 0.2017 | 0.0001 | 0.2017 |
| PASS | mscale_H_m3.0 | Sec. 12 Collapse test (d): Hayward B/m^3 for m=3.0 | 0.2052 | 0.0001 | 0.2052 |
| PASS | mscale_H_m5.0 | Sec. 12 Collapse test (d): Hayward B/m^3 for m=5.0 | 0.2033 | 0.0001 | 0.2033 |
| PASS | mscale_H_m10.0 | Sec. 12 Collapse test (d): Hayward B/m^3 for m=10.0 | 0.2015 | 0.0001 | 0.2015 |
| PASS | mscale_ratio_m3.0 | Sec. 12 Collapse test (d): Hayward over Einstein, percent, m=3.0 | +1.7 | 0.06 (ratio of the two printed 4-digit coefficients) | 1.73525 |
| PASS | mscale_ratio_m5.0 | Sec. 12 Collapse test (d): Hayward over Einstein, percent, m=5.0 | +0.8 | 0.06 (ratio of the two printed 4-digit coefficients) | 0.793257 |
| PASS | mscale_ratio_m10.0 | Sec. 12 Collapse test (d): Hayward over Einstein, percent, m=10.0 | -0.1 | 0.06 (ratio of the two printed 4-digit coefficients) | -0.0991572 |
| PASS | mscale_B25 | Sec. 12 Collapse test (d): B = 25.41 for m=5 (Hayward, window [1000,2900] m/5) | 25.41 | 0.006 (25.4112) | 25.4112 |
| PASS | fit_E_k | Sec. 12 Collapse result: free fit exponent for t in [1200,2400], Einstein limit: 3.009 | 3.009 | 0.00055 | 3.0088 |
| PASS | fit_H_k | Sec. 12 Collapse result: ... Hayward: 3.009 | 3.009 | 0.0006 (3.0090 (log) versus 3.0088 for the Einstein limit; both round to 3.009) | 3.009 |
| PASS | fit_E_B | Sec. 12 Collapse result: k=3 fit, Einstein limit, B = 25.26 | 25.26 | 0.00505 | 25.2613 |
| PASS | fit_E_vs | Sec. 12 Collapse result: ... v_s - v_start = 23.8 | 23.8 | 0.055 | 23.79 |
| PASS | fit_H_B | Sec. 12 Collapse result: k=3 fit, Hayward, B = 25.45 | 25.45 | 0.00505 | 25.4474 |
| PASS | fit_H_vs | Sec. 12 Collapse result: ... v_s - v_start = 23.2 | 23.2 | 0.055 | 23.23 |
| PASS | fit_E_k_early | Sec. 12 Collapse result: an early window t in [600,1200] gives k = 3.4 (Einstein) | 3.4 | 0.05 (3.418 / 3.449) | 3.4181 |
| PASS | fit_H_k_early | Sec. 12 Collapse result: ... (Hayward) | 3.4 | 0.06 (3.449) | 3.4493 |
| PASS | fit_early_vs | Sec. 12 Collapse result: ... with v_s < v_start (v_s - v_start < 0, largest of the two) | 0 | bound: <= paper | -105.48 |
| PASS | ascale_B_0.80 | Sec. 12 Collapse result: B(k=3) for A/A0=0.80 (ascale.log) | 16.5 | 0.051 (one decimal place in the paper) | 16.5134 |
| PASS | ascale_B_0.90 | Sec. 12 Collapse result: B(k=3) for A/A0=0.90 (ascale.log) | 21.1 | 0.051 (one decimal place in the paper) | 21.0679 |
| PASS | ascale_B_1.00 | Sec. 12 Collapse result: B(k=3) for A/A0=1.00 (ascale.log) | 25.4 | 0.051 (one decimal place in the paper) | 25.4339 |
| PASS | ascale_B_1.10 | Sec. 12 Collapse result: B(k=3) for A/A0=1.10 (ascale.log) | 28.8 | 0.051 (one decimal place in the paper) | 28.7619 |
| PASS | ascale_B_1.20 | Sec. 12 Collapse result: B(k=3) for A/A0=1.20 (ascale.log) | 30.6 | 0.051 (one decimal place in the paper) | 30.6012 |
| PASS | ascale_m_lo | Sec. 12 Collapse result: generalized masses 3.2 ... (A/A0=0.8) | 3.2 | 0.051 (3.2088) | 3.2088 |
| PASS | ascale_m_hi | Sec. 12 Collapse result: ... 7.2 (A/A0=1.2) | 7.2 | 0.051 (7.1758) | 7.1758 |
| PASS | ascale_slope_small_m | Sec. 12 Collapse result: B ~ m^1.0 at small m (d ln B/d ln m between the two smallest masses) | 1.0 | 0.05 (1.04) | 1.03972 |
| PASS | ascale_saturating | Sec. 12 Collapse result: ... saturating (the last d ln B/d ln m is below 0.5) | 0.5 | bound: <= paper | 0.359835 |
| PASS | ascale_notA3 | Sec. 12 Collapse result: ... not A^3 (the largest d ln B/d ln A is below 3, = 2.07) | 3 | bound: <= paper | 2.06801 |
| PASS | linear_B | Sec. 12 Collapse result: linear test field on the static m=5 Hayward exterior B_lin = 68.8 (linear.log) | 68.8 | 0.05005 | 68.7863 |
| PASS | linear_ratio | Sec. 12 Collapse result: ... so the nonlinear tail is 0.37 of the linear one | 0.37 | 0.0055 | 0.37 |
| PASS | linear_Bnl | Sec. 12 Collapse result: B_nonlinear in the linear.log (= ascale B at A/A0=1) is 25.434 | 25.434 | 0.001 | 25.434 |
| PASS | cE_front_ray0 | Sec. 12 Code E on the collapse tail: front arrival time on ray 0 (collapse_E.log) | 53 | 0 (integer sampling) | 53 |
| PASS | cE_front_ray1 | Sec. 12 Code E on the collapse tail: front arrival time on ray 1 (collapse_E.log) | 78 | 0 (integer sampling) | 78 |
| PASS | cE_front_ray2 | Sec. 12 Code E on the collapse tail: front arrival time on ray 2 (collapse_E.log) | 70 | 0 (integer sampling) | 70 |
| PASS | cE_front_ray3 | Sec. 12 Code E on the collapse tail: front arrival time on ray 3 (collapse_E.log) | 68 | 0 (integer sampling) | 68 |
| PASS | cE_front_range_lo | Sec. 12 Code E on the collapse tail: the front arrives at v = 53--78 on the four rays (smallest) | 53 | 0 (integer) | 53 |
| PASS | cE_front_range_hi | Sec. 12 Code E on the collapse tail: ... (largest) | 78 | 0 (integer) | 78 |
| PASS | cE_front_presc | Sec. 12 Code E on the collapse tail: earlier than the prescribed B=3e-3, k=3 run (73 on U~1) | 73 | 0 (integer) | 73 |
| PASS | cE_zm | Sec. 12 Code E on the collapse tail: zm behind the front (U~1, v=1100) | 0.59117 | 1e-05 | 0.59117 |
| PASS | cE_zm_closed | Sec. 12 Code E on the collapse tail: closed form r_-^3/2 = 0.59126 | 0.59126 | 1e-05 | 0.59126 |
| PASS | cE_zm_presc | Sec. 12 Code E on the collapse tail: ... and 0.59117 for the prescribed k=3 run | 0.59117 | 1e-05 | 0.59117 |
| PASS | cE_dm | Sec. 12 Code E on the collapse tail: dm/dv = 4.403 in both (collapse run, v=1100) | 4.403 | 0.001 (4.4035 (collapse) and 4.4023 (prescribed) differ in the 4th digit; the text quotes both as 4.403) | 4.4035 |
| PASS | cE_dm_presc | Sec. 12 Code E on the collapse tail: ... (prescribed run, v=1100) | 4.403 | 0.001 (4.4023) | 4.4023 |
| PASS | cE_m1400 | Sec. 12 Code E on the collapse tail: m = 5742 at v=1400 (U~1) | 5742 | 1 (5742.4) | 5742.4 |
| PASS | cE_vsV1100 | Sec. 12 Code E on the collapse tail: -v sigma_v = 8.246 at v=1100 | 8.246 | 0.001 | 8.246 |
| PASS | cE_vsV1400 | Sec. 12 Code E on the collapse tail: ... 8.20 at 1400 | 8.20 | 0.006 (8.202) | 8.202 |
| PASS | cE_vsV_presc | Sec. 12 Code E on the collapse tail: ... 8.081 at 1100 for the prescribed run | 8.081 | 0.001 | 8.081 |
| PASS | cE_slope1100 | Sec. 12 Code E on the collapse tail: local slope of K is 9.914 at v=1100 (U~1) | 9.914 (manuscript: $9.914$ at $v=1100$) | 0.001 (9.915 for h_v=0.2 and 9.914 for h_v=0.1) | 9.915 |
| PASS | cE_slope1400_ray0 | Sec. 12 Code E on the collapse tail: ... slope at v=1400 on ray 0 | 9.83 | 0.006 (2-digit quote of 9.830, 9.899, 9.939, 9.947) | 9.83 |
| PASS | cE_slope1400_ray1 | Sec. 12 Code E on the collapse tail: ... slope at v=1400 on ray 1 | 9.90 | 0.006 (2-digit quote of 9.830, 9.899, 9.939, 9.947) | 9.899 |
| PASS | cE_slope1400_ray2 | Sec. 12 Code E on the collapse tail: ... slope at v=1400 on ray 2 | 9.94 | 0.006 (2-digit quote of 9.830, 9.899, 9.939, 9.947) | 9.939 |
| PASS | cE_slope1400_ray3 | Sec. 12 Code E on the collapse tail: ... slope at v=1400 on ray 3 | 9.95 | 0.006 (2-digit quote of 9.830, 9.899, 9.939, 9.947) | 9.947 |
| PASS | cE_slope_presc | Sec. 12 Code E on the collapse tail: ... against 9.47 for the prescribed run at 1100 | 9.47 | 0.005 (9.469) | 9.469 |
| PASS | cE_K1400 | Sec. 12 Code E on the collapse tail: K(1400) = 1.3e33 on U~1 (profile row) | 1.3e33 | 5e+31 (1.300e33) | 1.3e+33 |
| PASS | cE_K1400_zero | Sec. 12 Code E on the collapse tail: ... and 1.3e31 with phi_U = 0 on the starting row | 1.3e31 | 5e+29 (1.321e31) | 1.321e+31 |
| PASS | cE_Kratio_ray0 | Sec. 12 Code E on the collapse tail: K(profile)/K(zero) at v=1100 on ray 0 | 2.6 | 0.05 (two-digit quote) | 2.64235 |
| PASS | cE_Kratio_ray1 | Sec. 12 Code E on the collapse tail: K(profile)/K(zero) at v=1100 on ray 1 | 8.3 | 0.05 (two-digit quote) | 8.34286 |
| PASS | cE_Kratio_ray2 | Sec. 12 Code E on the collapse tail: K(profile)/K(zero) at v=1100 on ray 2 | 99 | 0.6 (two-digit quote) | 98.9167 |
| PASS | cE_Kratio_ray3 | Sec. 12 Code E on the collapse tail: K(profile)/K(zero) at v=1100 on ray 3 | 6e4 | 2500 (two-digit quote) | 62309.6 |
| PASS | cE_Psratio_ray0 | Sec. 12 Code E on the collapse tail: ratio of phi_U (profile/zero) on ray 0 | 0.76 | 0.0051 (3-digit log value rounded to 2) | 0.761 |
| PASS | cE_Psratio_ray1 | Sec. 12 Code E on the collapse tail: ratio of phi_U (profile/zero) on ray 1 | 0.53 | 0.0051 (3-digit log value rounded to 2) | 0.529 |
| PASS | cE_Psratio_ray2 | Sec. 12 Code E on the collapse tail: ratio of phi_U (profile/zero) on ray 2 | 0.13 | 0.0051 (3-digit log value rounded to 2) | 0.13 |
| PASS | cE_Psratio_ray3 | Sec. 12 Code E on the collapse tail: ratio of phi_U (profile/zero) on ray 3 | -0.13 | 0.0051 (3-digit log value rounded to 2) | -0.131 |
| PASS | cE_K_ratio_row | Sec. 12 Code E on the collapse tail: row-profile sensitivity at U=0.9968, v=1200 (K ratio 98.7) | 98.7 | 0.0505 | 98.716 |
| PASS | cE_m_agree | Sec. 12 Code E on the collapse tail: m (and z) agree between the profile and phi_U = 0 runs to 0.3% (largest relative difference over the four rays at v=1100: 0.59%) | 0.6e-2 (manuscript: $m$, $z$ to $0.3\%$) | 0.0005 (5.9e-3) | 0.00588235 |
| PASS | convc_dr | Sec. 12 Code E on the collapse tail mesh: change in r (relative) 4.3e-6 (conv_c.log) | 4.3e-6 | 1e-07 | 4.3e-06 |
| PASS | convc_dsV | Sec. 12 Code E on the collapse tail mesh: change in sigma_v and in phi_v 8e-6 (sigma_v at v=1400) | 8e-6 | 5e-07 (8.3e-6) | 8.3e-06 |
| PASS | convc_dPV | Sec. 12 Code E on the collapse tail mesh: ... phi_v (relative) 8e-6 | 8e-6 | 5.5e-07 | 8e-06 |
| PASS | convc_dlnm | Sec. 12 Code E on the collapse tail mesh: (1-4)e-5 in ln m, largest 3.6e-5 (all four rays, v = 100 ... 1400; the shipped conv_c.log of the first release was stale: the ORIGINAL conv_c.py on the original data gives this log) | 3.6e-5 | 5e-07 | 3.6e-05 |
| PASS | convc_dlnK100 | Sec. 12 Code E on the collapse tail mesh: <=7e-4 in ln K at v=100, all rays (largest 7.1e-4; the manuscript now quotes 7.1e-4) | 7.1e-4 | 5e-06 | 0.00071 |
| PASS | convc_dlnK1400 | Sec. 12 Code E on the collapse tail mesh: ... decreasing to <=1.2e-4 at v=1400 (largest over the rays; 1.1e-4 in the stale first-release log) | 1.2e-4 | 5e-06 | 0.00012 |
| PASS | k2_zm_0 | Sec. 12 k=2 tail, code E: zm behind the front at v=1000, b=1, ray 0 lies in 0.59114--0.59119 (value at v=1000) | 0.59115 | 5e-05 (range 0.59114-0.59119 over rays) | 0.59115 |
| PASS | k2_zm_1 | Sec. 12 k=2 tail, code E: zm behind the front at v=1000, b=1, ray 1 lies in 0.59114--0.59119 (value at v=1000) | 0.59115 | 5e-05 (range 0.59114-0.59119 over rays) | 0.59115 |
| PASS | k2_zm_2 | Sec. 12 k=2 tail, code E: zm behind the front at v=1000, b=1, ray 2 lies in 0.59114--0.59119 (value at v=1000) | 0.59115 | 5e-05 (range 0.59114-0.59119 over rays) | 0.59114 |
| PASS | k2_zm_3 | Sec. 12 k=2 tail, code E: zm behind the front at v=1000, b=1, ray 3 lies in 0.59114--0.59119 (value at v=1000) | 0.59115 | 5e-05 (range 0.59114-0.59119 over rays) | 0.59114 |
| PASS | k2_zm_lo | Sec. 12 k=2 tail, code E: zm = 0.59114 -- 0.59119 (smallest over rays, v=1000..1200, b=1) | 0.59114 | 5e-06 (5-digit log values) | 0.59114 |
| PASS | k2_zm_hi | Sec. 12 k=2 tail, code E: ... (largest) | 0.59119 | 5e-06 (5-digit log values) | 0.59119 |
| PASS | k2_zm_closed | Sec. 12 k=2 tail, code E: 1/2 r_-^3 = 0.59126 | 0.59126 | 1e-05 | 0.59126 |
| PASS | k2_dm_b1 | Sec. 12 k=2 tail, code E: dm/dv = 4.42 at v=1400 for b=1 | 4.42 | 0.006 (4.4234) | 4.4234 |
| PASS | k2_dm_b01 | Sec. 12 k=2 tail, code E: ... and for b=0.1 | 4.42 | 0.006 (4.4246) | 4.4246 |
| PASS | k2_vsV_b1_1000 | Sec. 12 k=2 tail, code E: v sigma_v at v=1000, b=1 | -5.800 | 0.001 | -5.8 |
| PASS | k2_vsV_b1_1200 | Sec. 12 k=2 tail, code E: v sigma_v at v=1200, b=1 | -5.839 | 0.001 | -5.839 |
| PASS | k2_vsV_b1_1400 | Sec. 12 k=2 tail, code E: v sigma_v at v=1400, b=1 | -5.867 | 0.001 | -5.867 |
| PASS | k2_vsV_b01_1000 | Sec. 12 k=2 tail, code E: v sigma_v at v=1000, b=0.1 | -5.507 | 0.001 | -5.507 |
| PASS | k2_vsV_b01_1200 | Sec. 12 k=2 tail, code E: v sigma_v at v=1200, b=0.1 | -5.612 | 0.001 | -5.612 |
| PASS | k2_vsV_b01_1400 | Sec. 12 k=2 tail, code E: v sigma_v at v=1400, b=0.1 | -5.685 | 0.001 | -5.685 |
| PASS | k2_slope_b1_1000 | Sec. 12 k=2 tail, code E: local slope of K at v=1000, b=1 | 5.07 | 0.0055 | 5.069 |
| PASS | k2_slope_b1_1200 | Sec. 12 k=2 tail, code E: local slope of K at v=1200, b=1 | 5.23 | 0.0055 | 5.227 |
| PASS | k2_slope_b1_1400 | Sec. 12 k=2 tail, code E: local slope of K at v=1400, b=1 | 5.34 | 0.0055 | 5.339 |
| PASS | k2_slope_b01_1000 | Sec. 12 k=2 tail, code E: local slope of K at v=1000, b=0.1 | 4.37 | 0.0055 | 4.371 |
| PASS | k2_slope_b01_1200 | Sec. 12 k=2 tail, code E: local slope of K at v=1200, b=0.1 | 4.68 | 0.0055 | 4.684 |
| PASS | k2_slope_b01_1400 | Sec. 12 k=2 tail, code E: local slope of K at v=1400, b=0.1 | 4.90 | 0.0055 | 4.9 |
| PASS | k2_below_b1 | Sec. 12 k=2 tail, code E: slope at v=1400 is still 11% below 4k-2=6 (b=1) | 11 | 0.5 ((6-5.339)/6 = 11.0%) | 11.0167 |
| PASS | k2_below_b01 | Sec. 12 k=2 tail, code E: ... and 18% below (b=0.1) | 18 | 0.5 ((6-4.900)/6 = 18.3%) | 18.3333 |
| PASS | k2_terms_b1_1000 | Sec. 12 k=2 tail, code E: slope + terms at v=1000, b=1 | 5.998 | 0.001 | 5.998 |
| PASS | k2_terms_b1_1200 | Sec. 12 k=2 tail, code E: slope + terms at v=1200, b=1 | 5.993 | 0.001 | 5.993 |
| PASS | k2_terms_b1_1400 | Sec. 12 k=2 tail, code E: slope + terms at v=1400, b=1 | 5.987 | 0.001 | 5.987 |
| PASS | k2_terms_b01_1000 | Sec. 12 k=2 tail, code E: slope + terms at v=1000, b=0.1 | 5.995 | 0.001 | 5.995 |
| PASS | k2_terms_b01_1200 | Sec. 12 k=2 tail, code E: slope + terms at v=1200, b=0.1 | 5.991 | 0.001 | 5.991 |
| PASS | k2_terms_b01_1400 | Sec. 12 k=2 tail, code E: slope + terms at v=1400, b=0.1 | 5.986 | 0.001 | 5.986 |
| PASS | k2_terms_other_lo | Sec. 12 k=2 tail, code E: slope+terms is 5.99--6.00 on the other three rays (smallest, both amplitudes, v=1000..1200) | 5.99 | 0.0051 (5.991 ... 5.998) | 5.991 |
| PASS | k2_terms_other_hi | Sec. 12 k=2 tail, code E: ... (largest) | 6.00 | 0.0051 (5.998) | 5.998 |
| PASS | k2_v0_b1 | Sec. 12 k=2 tail, code E: measured v_0 = 81 (b=1, v=1000, U~1) | 81 | 0.6 (81.1) | 81.1 |
| PASS | k2_v0_b01 | Sec. 12 k=2 tail, code E: ... and 96 (b=0.1) | 96 | 0.6 (96.1) | 96.1 |
| PASS | k2x_front0 | Sec. 12 k=2 tail, code E: front at v = 53 on ray 0 (b=1; k2_extra.log) | 53 | 0 (integer) | 53 |
| PASS | k2x_front1 | Sec. 12 k=2 tail, code E: ... 80 on ray 1 | 80 | 0 (integer) | 80 |
| PASS | k2x_front2 | Sec. 12 k=2 tail, code E: ... 67 on ray 2 | 67 | 0 (integer) | 67 |
| PASS | k2x_front3 | Sec. 12 k=2 tail, code E: ... 61 on ray 3 | 61 | 0 (integer) | 61 |
| PASS | k2x_K_b1 | Sec. 12 k=2 tail, code E: K(1400) = 4.5e21 (b=1, U~1) | 4.5e21 | 5e+19 (4.529e21) | 4.529e+21 |
| PASS | k2x_K_b01 | Sec. 12 k=2 tail, code E: ... and 1.4e32 (b=0.1) | 1.4e32 | 5e+30 (1.376e32) | 1.376e+32 |
| PASS | k2x_fit_a | Sec. 12 k=2 tail, code E: the fit a + c/v to the slope (b=1, 1000<=v<=1450) gives a = 6.01 | 6.01 | 0.006 (6.006) | 6.006 |
| PASS | k2x_fit_c | Sec. 12 k=2 tail, code E: ... c = -937 | -937 | 1.5 (-936) | -936 |
| PASS | k2x_m | Sec. 12 k=2 tail, code E: the interior stays at m = 5.0011 up to the front (v=40, U~1) | 5.0011 | 0.0001 | 5.0011 |
| PASS | k2x_r | Sec. 12 k=2 tail, code E: ... and r = r_- = 1.05746 (ray 4, v=40; ray 3 gives 1.05755) | 1.05746 | 1e-05 | 1.05746 |
| PASS | convk2_lnK100 | Sec. 12 k=2 tail, code E mesh: <= 7.6e-4 in ln K at v=100 (conv_c_k2.log) | 7.6e-4 | 1e-05 | 0.00076 |
| PASS | convk2_lnK200 | Sec. 12 k=2 tail, code E mesh: <= 4e-4 at 200<=v<=400 | 4e-4 | 5e-05 (3.9e-4 printed with 2 digits) | 0.00039 |
| PASS | convk2_lnK800 | Sec. 12 k=2 tail, code E mesh: <= 1.5e-4 at v >= 800 | 1.5e-4 | 1e-05 | 0.00015 |
| PASS | convk2_sV | Sec. 12 k=2 tail, code E mesh: 1.3e-5 in sigma_v (largest, v=100) | 1.3e-5 | 1e-06 | 1.3e-05 |
| PASS | convk2_r | Sec. 12 k=2 tail, code E mesh: 4.3e-6 in r | 4.3e-6 | 1e-07 | 4.3e-06 |
| PASS | convk2_lnm | Sec. 12 k=2 tail, code E mesh: 5e-5 in ln m (largest 4.9e-5) | 5e-5 | 1e-06 (4.9e-5) | 4.9e-05 |
| PASS | convk2_PV | Sec. 12 k=2 tail, code E mesh: 9e-6 in phi_v (largest 8.7e-6) | 9e-6 | 4e-07 (8.7e-6) | 8.7e-06 |
| PASS | nplin_ratio_800 | Sec. 12 k=2 tail, stage N+L (a): phi_H t^2/(-4b) = 0.9295 at t=800 (linear test, Einstein; nplin.log) | 0.9295 | 6e-05 (0.92952) | 0.92952 |
| PASS | nplin_ratio_1600 | Sec. 12 k=2 tail, stage N+L (a): ... 0.9649 at t=1600 | 0.9649 | 6e-05 (0.96485) | 0.96485 |
| PASS | nplin_ratio_3200 | Sec. 12 k=2 tail, stage N+L (a): ... 0.9826 at t=3200 | 0.9826 | 5.5e-05 | 0.98258 |
| PASS | nplin_ratio_6400 | Sec. 12 k=2 tail, stage N+L (a): ... 0.9914 at t=6400 | 0.9914 | 5.5e-05 | 0.99136 |
| PASS | nplin_a0_800 | Sec. 12 k=2 tail, stage N+L (a): a0 = 1.0000 +- 0.0002 (full form, window t>=800, Hayward) (nplin.log) | 1.0000 | 0.0002 (the paper quotes a0 = 1.0000 +- 0.0002 over the windows and forms (largest deviation 1.8e-4 for the c1 form at 800)) | 1.00018 |
| PASS | nplin_a0_1600 | Sec. 12 k=2 tail, stage N+L (a): a0 = 1.0000 +- 0.0002 (full form, window t>=1600, Hayward) (nplin.log) | 1.0000 | 0.0002 (the paper quotes a0 = 1.0000 +- 0.0002 over the windows and forms (largest deviation 1.8e-4 for the c1 form at 800)) | 1.00014 |
| PASS | nplin_a0_3200 | Sec. 12 k=2 tail, stage N+L (a): a0 = 1.0000 +- 0.0002 (full form, window t>=3200, Hayward) (nplin.log) | 1.0000 | 0.0002 (the paper quotes a0 = 1.0000 +- 0.0002 over the windows and forms (largest deviation 1.8e-4 for the c1 form at 800)) | 1.00009 |
| PASS | nplin_a0_full | Sec. 12 k=2 tail, stage N+L (a): a0 = 1 to 4e-5 with the full form (window >= 800..3200, both backgrounds, largest deviation) | 4e-5 | bound: <= paper | 4e-05 |
| PASS | nplin_a0_bkg | Sec. 12 k=2 tail, stage N+L (a): the two backgrounds agree to 1e-4 (largest difference of a0 between nplin_m0 and nplin_m1, all windows and forms) | 1e-4 | bound: <= paper | 1e-05 |
| PASS | nplin_k | Sec. 12 k=2 tail, stage N+L (a): a free fit gives k = 2.0005 | 2.0005 | 0.0001 | 2.0005 |
| PASS | npfit_full_H1 | Sec. 12 k=2 tail, stage N+L (b): a0 = 1.0000 (full form, window >= 1600) for npdata/np_m1_b1.0_h1.npz (np_fit.log) | 1.0000 | 3e-05 (/a0-1/ <= 3e-5 stated in the paper) | 1 |
| PASS | npfit_full_E1 | Sec. 12 k=2 tail, stage N+L (b): a0 = 1.0000 (full form, window >= 1600) for npdata/np_m0_b1.0_h1.npz (np_fit.log) | 1.0000 | 3e-05 (/a0-1/ <= 3e-5 stated in the paper) | 1 |
| PASS | npfit_full_Hm1 | Sec. 12 k=2 tail, stage N+L (b): a0 = 1.0000 (full form, window >= 1600) for npdata/np_m1_b-1.0_h1.npz (np_fit.log) | 1.0000 | 3e-05 (/a0-1/ <= 3e-5 stated in the paper) | 0.99999 |
| PASS | npfit_full_H05 | Sec. 12 k=2 tail, stage N+L (b): a0 = 1.0000 (full form, window >= 1600) for npdata/np_m1_b0.5_h1.npz (np_fit.log) | 1.0000 | 3e-05 (/a0-1/ <= 3e-5 stated in the paper) | 1 |
| PASS | npfit_full_H2 | Sec. 12 k=2 tail, stage N+L (b): a0 = 1.0000 (full form, window >= 1600) for npdata/np_m1_b2.0_h1.npz (np_fit.log) | 1.0000 | 3e-05 (/a0-1/ <= 3e-5 stated in the paper) | 1 |
| PASS | npfit_c1_max | Sec. 12 k=2 tail, stage N+L (b): /a0 - 1/ <= 1.5e-4 with only the c1/t correction, windows >= 1600 (largest of the five cases) | 1.5e-4 | bound: <= paper | 0.00013 |
| PASS | npfit_full_max | Sec. 12 k=2 tail, stage N+L (b): /a0 - 1/ <= 3e-5 with the full form, windows >= 1600 (largest of the five cases; real scipy gives 3.0e-5 at window 3200) | 3e-5 | bound: <= paper (+1e-07: the fit is printed to 5 decimals) (the fit is printed to 5 decimals) | 3e-05 |
| PASS | npfit_k_800 | Sec. 12 k=2 tail, stage N+L (b): free index, window t >= 800, b=1 Hayward | 2.0013 | 0.0001 | 2.0013 |
| PASS | npfit_B_800 | Sec. 12 k=2 tail, stage N+L (b): B/(4/b/), window t >= 800 | 1.013 | 0.0006 (1.0131, 1.0071, 1.0039) | 1.0131 |
| PASS | npfit_k_1600 | Sec. 12 k=2 tail, stage N+L (b): free index, window t >= 1600, b=1 Hayward | 2.0007 | 0.0001 | 2.0007 |
| PASS | npfit_B_1600 | Sec. 12 k=2 tail, stage N+L (b): B/(4/b/), window t >= 1600 | 1.007 | 0.0006 (1.0131, 1.0071, 1.0039) | 1.0071 |
| PASS | npfit_k_3200 | Sec. 12 k=2 tail, stage N+L (b): free index, window t >= 3200, b=1 Hayward | 2.0004 | 0.0001 | 2.0004 |
| PASS | npfit_B_3200 | Sec. 12 k=2 tail, stage N+L (b): B/(4/b/), window t >= 3200 | 1.004 | 0.0006 (1.0131, 1.0071, 1.0039) | 1.0039 |
| PASS | npfit_s | Sec. 12 k=2 tail, stage N+L (b): fitted shift s ~ -44 (window 1600) | -44 | 0.2 (-44.1) | -44.1 |
| PASS | nplinb_rel_50 | Sec. 12 k=2 tail, stage N+L (b): relative spread of [phi_H(b)-phi_H(0)]/b at t=50 (np_lin_b.log) | 8e-3 | 0.0001 (7.9e-3 quoted as 8e-3) | 0.0079 |
| PASS | nplinb_rel_100 | Sec. 12 k=2 tail, stage N+L (b): relative spread of [phi_H(b)-phi_H(0)]/b at t=100 (np_lin_b.log) | 1e-4 | 5.05e-05 | 0.0001 |
| PASS | nplinb_rel_200 | Sec. 12 k=2 tail, stage N+L (b): relative spread of [phi_H(b)-phi_H(0)]/b at t=200 (np_lin_b.log) | 6.5e-4 | 5.5e-06 | 0.00065 |
| PASS | nplinb_rel_400 | Sec. 12 k=2 tail, stage N+L (b): relative spread of [phi_H(b)-phi_H(0)]/b at t=400 (np_lin_b.log) | 6e-5 | 5e-06 (5.8e-5 quoted as 6e-5) | 5.8e-05 |
| PASS | nplinb_rel_late | Sec. 12 k=2 tail, stage N+L (b): ... <= 6e-5 for t >= 400 (largest) | 6e-5 | bound: <= paper | 5.8e-05 |
| PASS | tc_a0_H.02_800 | Sec. 12 k=2, nonzero charge: a0 (full form) for sp/tc_H_m0_5_c0.02.npz, window t >= 800 (tc_fit.log) | 0.99993 | 1e-05 | 0.99993 |
| PASS | tc_a0_E.02_800 | Sec. 12 k=2, nonzero charge: a0 (full form) for sp/tc_E_m0_5_c0.02.npz, window t >= 800 (tc_fit.log) | 0.99993 | 1e-05 | 0.99993 |
| PASS | tc_a0_H.02_1600 | Sec. 12 k=2, nonzero charge: a0 (full form) for sp/tc_H_m0_5_c0.02.npz, window t >= 1600 (tc_fit.log) | 0.99999 | 1e-05 | 0.99999 |
| PASS | tc_a0_E.02_1600 | Sec. 12 k=2, nonzero charge: a0 (full form) for sp/tc_E_m0_5_c0.02.npz, window t >= 1600 (tc_fit.log) | 0.99999 | 1e-05 | 0.99999 |
| PASS | tc_a0_H.02_3200 | Sec. 12 k=2, nonzero charge: a0 (full form) for sp/tc_H_m0_5_c0.02.npz, window t >= 3200 (tc_fit.log) | 1.0000 | 5e-05 (1.0000 quoted to 4 digits) | 1 |
| PASS | tc_a0_E.02_3200 | Sec. 12 k=2, nonzero charge: a0 (full form) for sp/tc_E_m0_5_c0.02.npz, window t >= 3200 (tc_fit.log) | 1.0000 | 5e-05 (1.0000 quoted to 4 digits) | 1 |
| PASS | tc_a0_H.01_800 | Sec. 12 k=2, nonzero charge: a0 (full form) for sp/tc_H_m0_5_c0.01.npz, window t >= 800 (tc_fit.log) | 0.99999 | 1e-05 | 0.99999 |
| PASS | tc_a0_H.04_800 | Sec. 12 k=2, nonzero charge: a0 (full form) for sp/tc_H_m0_5_c0.04.npz, window t >= 800 (tc_fit.log) | 0.99990 | 1e-05 | 0.9999 |
| PASS | tc_a0_H.01_3200 | Sec. 12 k=2, nonzero charge: a0 (full form) for sp/tc_H_m0_5_c0.01.npz, window t >= 3200 (tc_fit.log) | 1.0000 | 5e-05 (1.0000 quoted to 4 digits) | 1 |
| PASS | tc_a0_H.04_3200 | Sec. 12 k=2, nonzero charge: a0 (full form) for sp/tc_H_m0_5_c0.04.npz, window t >= 3200 (tc_fit.log) | 0.99999 | 1e-05 | 0.99999 |
| PASS | tc_a0_H25_800 | Sec. 12 k=2, nonzero charge: a0 (full form) for sp/tc_H_m2.5_5_c0.02.npz, window t >= 800 (tc_fit.log) | 0.99992 | 1e-05 | 0.99992 |
| PASS | tc_a0_H25_1600 | Sec. 12 k=2, nonzero charge: a0 (full form) for sp/tc_H_m2.5_5_c0.02.npz, window t >= 1600 (tc_fit.log) | 0.99999 | 1e-05 | 0.99999 |
| PASS | tc_a0_H10_3200 | Sec. 12 k=2, nonzero charge: a0 (full form) for sp/tc_H_m0_10_c0.02.npz, window t >= 3200 (tc_fit.log) | 1.0000 | 5e-05 (1.0000 quoted to 4 digits) | 1 |
| PASS | tc_a0_H10_800 | Sec. 12 k=2, nonzero charge: a0 (full form) for sp/tc_H_m0_10_c0.02.npz, window t >= 800 (tc_fit.log) | 1.0045 | 5.5e-05 | 1.00449 |
| PASS | tc_k_H.02_800 | Sec. 12 k=2, nonzero charge: free index, c=0.02 Hayward, window >= 800 | 2.0020 | 0.0001 | 2.0021 |
| PASS | tc_k_E.02_800 | Sec. 12 k=2, nonzero charge: free index, c=0.02 Einstein, window >= 800 (alike) | 2.0020 | 0.0001 | 2.002 |
| PASS | tc_k_H.02_1600 | Sec. 12 k=2, nonzero charge: free index, c=0.02 Hayward, window >= 1600 | 2.0010 | 0.0001 | 2.001 |
| PASS | tc_k_E.02_1600 | Sec. 12 k=2, nonzero charge: free index, c=0.02 Einstein, window >= 1600 (alike) | 2.0010 | 0.0001 | 2.001 |
| PASS | tc_k_H.02_3200 | Sec. 12 k=2, nonzero charge: free index, c=0.02 Hayward, window >= 3200 | 2.0005 | 0.0001 | 2.0005 |
| PASS | tc_k_E.02_3200 | Sec. 12 k=2, nonzero charge: free index, c=0.02 Einstein, window >= 3200 (alike) | 2.0005 | 0.0001 | 2.0005 |
| PASS | tc_B_H.02_800 | Sec. 12 k=2, nonzero charge: B/(4/I0/), window >= 800 | 1.020 | 0.0009 (Hayward 1.0208, 1.0102, 1.0053; Einstein 1.0203, 1.0100, 1.0051; the text quotes 1.020, 1.010, 1.005 for both) | 1.0208 |
| PASS | tc_B_H.02_1600 | Sec. 12 k=2, nonzero charge: B/(4/I0/), window >= 1600 | 1.010 | 0.0009 (Hayward 1.0208, 1.0102, 1.0053; Einstein 1.0203, 1.0100, 1.0051; the text quotes 1.020, 1.010, 1.005 for both) | 1.0102 |
| PASS | tc_B_H.02_3200 | Sec. 12 k=2, nonzero charge: B/(4/I0/), window >= 3200 | 1.005 | 0.0009 (Hayward 1.0208, 1.0102, 1.0053; Einstein 1.0203, 1.0100, 1.0051; the text quotes 1.020, 1.010, 1.005 for both) | 1.0053 |
| PASS | tc_k_other_lo | Sec. 12 k=2, nonzero charge: free index 2.0004--2.0010 for the other cases at t >= 3200 (smallest) | 2.0004 | 5e-05 | 2.0004 |
| PASS | tc_k_other_hi | Sec. 12 k=2, nonzero charge: ... (largest) | 2.0010 | 5e-05 | 2.001 |
| PASS | tc_k_m10 | Sec. 12 k=2, nonzero charge: ... 2.0021 for m_t = 10 | 2.0021 | 0.0001 | 2.0021 |
| PASS | tc_deficit_H.01 | Sec. 12 k=2, nonzero charge: mass deficit 5 - m_f (units 1e-4), sp/tc_H_m0_5_c0.01.npz | 3.8 | 0.06 (5 - 4.99962 etc. (m_f printed to 5 decimals)) | 3.8 |
| PASS | tc_deficit_H.02 | Sec. 12 k=2, nonzero charge: mass deficit 5 - m_f (units 1e-4), sp/tc_H_m0_5_c0.02.npz | 15.1 | 0.06 (5 - 4.99962 etc. (m_f printed to 5 decimals)) | 15.1 |
| PASS | tc_deficit_H.04 | Sec. 12 k=2, nonzero charge: mass deficit 5 - m_f (units 1e-4), sp/tc_H_m0_5_c0.04.npz | 60.3 | 0.06 (5 - 4.99962 etc. (m_f printed to 5 decimals)) | 60.3 |
| PASS | tc_mf_H.01 | Sec. 12 k=2, nonzero charge: m_f(stage N), sp/tc_H_m0_5_c0.01.npz | 4.99962 | 1e-05 | 4.99962 |
| PASS | tc_mf_H.02 | Sec. 12 k=2, nonzero charge: m_f(stage N), sp/tc_H_m0_5_c0.02.npz | 4.99849 | 1e-05 | 4.99849 |
| PASS | tc_mf_H.04 | Sec. 12 k=2, nonzero charge: m_f(stage N), sp/tc_H_m0_5_c0.04.npz | 4.99397 | 1e-05 | 4.99397 |
| PASS | tc_I0_mf | Sec. 12 k=2, nonzero charge: I0 = -c m_t is preferred to -c m_f (a0 = 1.0012 with m_f at c=0.04, t >= 3200) | 1.0012 | 6e-05 (a0 * m_t/m_f = 0.99999 * 5/4.99397) | 1.0012 |
| PASS | tc_linear_c | Sec. 12 k=2, nonzero charge: a0 is unchanged to 1e-4 between c = 0.01 and 0.04 (full form, window >= 3200) | 1e-4 | bound: <= paper | 1e-05 |
| PASS | strong_mf_5->5.01 | Table tab:strong m_f for m0=5 -> 5.01 | 5.01 | 0.0005 (table rows are labelled by the target mass) | 5.01 |
| PASS | strong_A_5->5.01 | Table tab:strong A for 5->5.01 | 0.00140 | 1e-05 | 0.0014 |
| PASS | strong_Q_5->5.01 | Table tab:strong /Q/ for 5->5.01 | 0.0464 | 5.5e-05 | 0.04639 |
| PASS | strong_B_5->5.01 | Table tab:strong B for 5->5.01 | 1.87 | 0.0055 | 1.867 |
| PASS | strong_F_5->5.01 | Table tab:strong B/(8 m_f /Q/) for 5->5.01 | 1.004 | 0.00055 | 1.0042 |
| PASS | strong_Bm3_5->5.01 | Table tab:strong B/m_f^3 for 5->5.01 | 0.0148 | 0.0001 | 0.0148 |
| PASS | strong_mf_5->5.5 | Table tab:strong m_f for m0=5 -> 5.5 | 5.5 | 0.0005 (table rows are labelled by the target mass) | 5.5 |
| PASS | strong_A_5->5.5 | Table tab:strong A for 5->5.5 | 0.00939 | 1e-05 | 0.00939 |
| PASS | strong_Q_5->5.5 | Table tab:strong /Q/ for 5->5.5 | 0.398 | 0.000505 | 0.39825 |
| PASS | strong_B_5->5.5 | Table tab:strong B for 5->5.5 | 16.30 | 0.0055 | 16.302 |
| PASS | strong_F_5->5.5 | Table tab:strong B/(8 m_f /Q/) for 5->5.5 | 0.930 | 0.00055 | 0.9303 |
| PASS | strong_Bm3_5->5.5 | Table tab:strong B/m_f^3 for 5->5.5 | 0.0980 | 0.0001 | 0.098 |
| PASS | strong_mf_5->6.5 | Table tab:strong m_f for m0=5 -> 6.5 | 6.5 | 0.0005 (table rows are labelled by the target mass) | 6.5 |
| PASS | strong_A_5->6.5 | Table tab:strong A for 5->6.5 | 0.01487 | 1e-05 | 0.01487 |
| PASS | strong_Q_5->6.5 | Table tab:strong /Q/ for 5->6.5 | 0.960 | 0.000505 | 0.96047 |
| PASS | strong_B_5->6.5 | Table tab:strong B for 5->6.5 | 41.15 | 0.0055 | 41.152 |
| PASS | strong_F_5->6.5 | Table tab:strong B/(8 m_f /Q/) for 5->6.5 | 0.824 | 0.00055 | 0.824 |
| PASS | strong_Bm3_5->6.5 | Table tab:strong B/m_f^3 for 5->6.5 | 0.1498 | 0.0001 | 0.1498 |
| PASS | strong_mf_5->8 | Table tab:strong m_f for m0=5 -> 8 | 8 | 0.0005 (table rows are labelled by the target mass) | 8 |
| PASS | strong_A_5->8 | Table tab:strong A for 5->8 | 0.01885 | 1e-05 | 0.01885 |
| PASS | strong_Q_5->8 | Table tab:strong /Q/ for 5->8 | 2.004 | 0.000505 | 2.00442 |
| PASS | strong_B_5->8 | Table tab:strong B for 5->8 | 92.94 | 0.0055 | 92.944 |
| PASS | strong_F_5->8 | Table tab:strong B/(8 m_f /Q/) for 5->8 | 0.725 | 0.00055 | 0.7245 |
| PASS | strong_Bm3_5->8 | Table tab:strong B/m_f^3 for 5->8 | 0.1815 | 0.0001 | 0.1815 |
| PASS | strong_mf_0->10 | Table tab:strong m_f for m0=0 -> 10 | 10 | 0.0005 (table rows are labelled by the target mass) | 10 |
| PASS | strong_A_0->10 | Table tab:strong A for 0->10 | 0.03003 | 1e-05 | 0.03003 |
| PASS | strong_Q_0->10 | Table tab:strong /Q/ for 0->10 | 6.824 | 0.000505 | 6.82365 |
| PASS | strong_B_0->10 | Table tab:strong B for 0->10 | 202.68 | 0.0055 | 202.682 |
| PASS | strong_F_0->10 | Table tab:strong B/(8 m_f /Q/) for 0->10 | 0.371 | 0.00055 | 0.3713 |
| PASS | strong_Bm3_0->10 | Table tab:strong B/m_f^3 for 0->10 | 0.2027 | 0.0001 | 0.2027 |
| PASS | strong_mf_2.5->10 | Table tab:strong m_f for m0=2.5 -> 10 | 10 | 0.0005 (table rows are labelled by the target mass) | 10 |
| PASS | strong_A_2.5->10 | Table tab:strong A for 2.5->10 | 0.02626 | 1e-05 | 0.02626 |
| PASS | strong_Q_2.5->10 | Table tab:strong /Q/ for 2.5->10 | 5.309 | 0.000505 | 5.30889 |
| PASS | strong_B_2.5->10 | Table tab:strong B for 2.5->10 | 212.96 | 0.0055 | 212.958 |
| PASS | strong_F_2.5->10 | Table tab:strong B/(8 m_f /Q/) for 2.5->10 | 0.501 | 0.00055 | 0.5014 |
| PASS | strong_Bm3_2.5->10 | Table tab:strong B/m_f^3 for 2.5->10 | 0.2130 | 0.0001 | 0.213 |
| PASS | strong_mf_5->10 | Table tab:strong m_f for m0=5 -> 10 | 10 | 0.0005 (table rows are labelled by the target mass) | 10 |
| PASS | strong_A_5->10 | Table tab:strong A for 5->10 | 0.02165 | 1e-05 | 0.02165 |
| PASS | strong_Q_5->10 | Table tab:strong /Q/ for 5->10 | 3.853 | 0.000505 | 3.85335 |
| PASS | strong_B_5->10 | Table tab:strong B for 5->10 | 198.88 | 0.0055 | 198.878 |
| PASS | strong_F_5->10 | Table tab:strong B/(8 m_f /Q/) for 5->10 | 0.645 | 0.00055 | 0.6451 |
| PASS | strong_Bm3_5->10 | Table tab:strong B/m_f^3 for 5->10 | 0.1989 | 0.0001 | 0.1989 |
| PASS | strong_mf_7.5->15 | Table tab:strong m_f for m0=7.5 -> 15 | 15 | 0.0005 (table rows are labelled by the target mass) | 15 |
| PASS | strong_A_7.5->15 | Table tab:strong A for 7.5->15 | 0.02165 | 1e-05 | 0.02165 |
| PASS | strong_Q_7.5->15 | Table tab:strong /Q/ for 7.5->15 | 8.669 | 0.000505 | 8.66948 |
| PASS | strong_B_7.5->15 | Table tab:strong B for 7.5->15 | 670.85 | 0.0055 | 670.85 |
| PASS | strong_F_7.5->15 | Table tab:strong B/(8 m_f /Q/) for 7.5->15 | 0.645 | 0.00055 | 0.6448 |
| PASS | strong_Bm3_7.5->15 | Table tab:strong B/m_f^3 for 7.5->15 | 0.1988 | 0.0001 | 0.1988 |
| PASS | strong_mf_10->20 | Table tab:strong m_f for m0=10 -> 20 | 20 | 0.0005 (table rows are labelled by the target mass) | 20 |
| PASS | strong_A_10->20 | Table tab:strong A for 10->20 | 0.02165 | 1e-05 | 0.02165 |
| PASS | strong_Q_10->20 | Table tab:strong /Q/ for 10->20 | 15.41 | 0.005005 | 15.4121 |
| PASS | strong_B_10->20 | Table tab:strong B for 10->20 | 1589.9 | 0.0505 | 1589.92 |
| PASS | strong_F_10->20 | Table tab:strong B/(8 m_f /Q/) for 10->20 | 0.645 | 0.00055 | 0.6448 |
| PASS | strong_Bm3_10->20 | Table tab:strong B/m_f^3 for 10->20 | 0.1987 | 0.0001 | 0.1987 |
| PASS | strong_mf_5->15 | Table tab:strong m_f for m0=5 -> 15 | 15 | 0.0005 (table rows are labelled by the target mass) | 15 |
| PASS | strong_A_5->15 | Table tab:strong A for 5->15 | 0.02484 | 1e-05 | 0.02484 |
| PASS | strong_Q_5->15 | Table tab:strong /Q/ for 5->15 | 10.84 | 0.005005 | 10.842 |
| PASS | strong_B_5->15 | Table tab:strong B for 5->15 | 711.88 | 0.0055 | 711.88 |
| PASS | strong_F_5->15 | Table tab:strong B/(8 m_f /Q/) for 5->15 | 0.547 | 0.00055 | 0.5472 |
| PASS | strong_Bm3_5->15 | Table tab:strong B/m_f^3 for 5->15 | 0.2109 | 0.0001 | 0.2109 |
| PASS | strong_mf_5->20 | Table tab:strong m_f for m0=5 -> 20 | 20 | 0.0005 (table rows are labelled by the target mass) | 20 |
| PASS | strong_A_5->20 | Table tab:strong A for 5->20 | 0.02626 | 1e-05 | 0.02626 |
| PASS | strong_Q_5->20 | Table tab:strong /Q/ for 5->20 | 21.23 | 0.005005 | 21.2347 |
| PASS | strong_B_5->20 | Table tab:strong B for 5->20 | 1702.0 | 0.0505 | 1701.99 |
| PASS | strong_F_5->20 | Table tab:strong B/(8 m_f /Q/) for 5->20 | 0.501 | 0.00055 | 0.5009 |
| PASS | strong_Bm3_5->20 | Table tab:strong B/m_f^3 for 5->20 | 0.2127 | 0.0001 | 0.2127 |
| PASS | strong_mf_2.5->12.5 | Table tab:strong m_f for m0=2.5 -> 12.5 | 12.5 | 0.0005 (table rows are labelled by the target mass) | 12.5 |
| PASS | strong_A_2.5->12.5 | Table tab:strong A for 2.5->12.5 | 0.02707 | 1e-05 | 0.02707 |
| PASS | strong_Q_2.5->12.5 | Table tab:strong /Q/ for 2.5->12.5 | 8.759 | 0.000505 | 8.75945 |
| PASS | strong_B_2.5->12.5 | Table tab:strong B for 2.5->12.5 | 415.42 | 0.0055 | 415.419 |
| PASS | strong_F_2.5->12.5 | Table tab:strong B/(8 m_f /Q/) for 2.5->12.5 | 0.474 | 0.00055 | 0.4743 |
| PASS | strong_Bm3_2.5->12.5 | Table tab:strong B/m_f^3 for 2.5->12.5 | 0.2127 | 0.0001 | 0.2127 |
| PASS | strong_mf_5->25 | Table tab:strong m_f for m0=5 -> 25 | 25 | 0.0005 (table rows are labelled by the target mass) | 25 |
| PASS | strong_A_5->25 | Table tab:strong A for 5->25 | 0.02707 | 1e-05 | 0.02707 |
| PASS | strong_Q_5->25 | Table tab:strong /Q/ for 5->25 | 35.04 | 0.005005 | 35.037 |
| PASS | strong_B_5->25 | Table tab:strong B for 5->25 | 3321.3 | 0.0505 | 3321.33 |
| PASS | strong_F_5->25 | Table tab:strong B/(8 m_f /Q/) for 5->25 | 0.474 | 0.00055 | 0.474 |
| PASS | strong_Bm3_5->25 | Table tab:strong B/m_f^3 for 5->25 | 0.2126 | 0.0001 | 0.2126 |
| PASS | strong_k_lo | Table tab:strong caption: free index 3.011 -- 3.012 in every row (smallest, Hayward rows) | 3.011 | 0.0005 (3.0114) | 3.0114 |
| PASS | strong_k_hi | Table tab:strong caption: ... (largest) | 3.012 | 0.0005 (3.0120) | 3.012 |
| PASS | strong_k_E | Sec. 12 strong: the flat start of the previous sections has free index 3.009 (Einstein limit) and 3.010 (Einstein rows of the table) | 3.010 | 0.0006 (3.0099-3.0100) | 3.0099 |
| PASS | strong_mu_half | Sec. 12 strong: F = 0.645 for mu=1/2 (mf = 10, 15, 20): largest spread of the three | 0.0005 | bound: <= paper (+0.0001: 0.6451, 0.6448, 0.6448) (0.6451, 0.6448, 0.6448) | 0.0003 |
| PASS | strong_mu_quarter | Sec. 12 strong: F at mu=1/4 and 1/5 agree between the two scales to <=1e-3 (largest difference) | 1e-3 | bound: <= paper | 0.0005 |
| PASS | strongE_Bm3_t0_m5_mt10 | Sec. 12 strong: Einstein B/m_f^3 for t0_m5_mt10.npz | 0.1985 | 0.0001 | 0.1985 |
| PASS | strongE_Bm3_t0_m2.5_mt10 | Sec. 12 strong: Einstein B/m_f^3 for t0_m2.5_mt10.npz | 0.2125 | 0.0001 | 0.2125 |
| PASS | strongE_Bm3_t0_m5_mt25 | Sec. 12 strong: Einstein B/m_f^3 for t0_m5_mt25.npz | 0.2124 | 0.0001 | 0.2124 |
| PASS | strongE_Bm3_t0_m0_mt10 | Sec. 12 strong: Einstein B/m_f^3 for t0_m0_mt10.npz | 0.2022 | 0.0001 | 0.2022 |
| PASS | strongE_diff | Sec. 12 strong: the Einstein table differs by <= 0.25% in B/m_f^3 (largest of the four) | 0.25e-2 | bound: <= paper (+5e-06: 0.25% = 0.2027/0.2022 - 1 = 0.2473%) (0.25% = 0.2027/0.2022 - 1 = 0.2473%) | 0.0024728 |
| PASS | strong_F_mu0 | Sec. 12 strong: F(mu=0) = 0.371 | 0.371 | 0.00055 | 0.3713 |
| PASS | strong_F_mu0_5 | Sec. 12 strong: ... where 0.373 at m_f = 5 (flat start, Table of Sec. collapse: B/(8 m /Q/) = 68.8*0.370/68.24 -> 0.373) | 0.373 | 0.0006 (25.434/(8*5.00000*1.70606) = 0.3727) | 0.372699 |
| PASS | strong_nearfold | Sec. 12 strong: F - mu = 0.29 (1-mu) at mu = 1/2 | 0.29 | 0.005 ((0.6451-0.5)/0.5 = 0.290) | 0.2902 |
| PASS | strong_nearone | Sec. 12 strong: F = mu + 0.23 (1-mu) near mu = 1 (m_f = 5.5) | 0.23 | 0.005 ((0.9303 - 10/11)/(1/11) = 0.2336) | 0.2333 |
| PASS | strong_Bm3_max | Sec. 12 strong: B/m_f^3 has a flat maximum 0.213 at mu ~ 0.2--0.25 | 0.213 | 0.00055 | 0.213 |
| PASS | width_F_sh_narrow_m0_0_10 | Sec. 12 strong: F for pulse width (4s, 8s, 16s) at mu = 0 and 1/2, sh_narrow_m0_0_10.npz (charge_row.log) | 0.363 | 0.0006 (0.3630, 0.3704, 0.3842, 0.6319, 0.6441, 0.6679) | 0.363 |
| PASS | width_F_t0_m0_mt10 | Sec. 12 strong: F for pulse width (4s, 8s, 16s) at mu = 0 and 1/2, t0_m0_mt10.npz (charge_row.log) | 0.370 | 0.0006 (0.3630, 0.3704, 0.3842, 0.6319, 0.6441, 0.6679) | 0.3704 |
| PASS | width_F_sh_wide_m0_0_10 | Sec. 12 strong: F for pulse width (4s, 8s, 16s) at mu = 0 and 1/2, sh_wide_m0_0_10.npz (charge_row.log) | 0.384 | 0.0006 (0.3630, 0.3704, 0.3842, 0.6319, 0.6441, 0.6679) | 0.3842 |
| PASS | width_F_sh_narrow_m0_5_10 | Sec. 12 strong: F for pulse width (4s, 8s, 16s) at mu = 0 and 1/2, sh_narrow_m0_5_10.npz (charge_row.log) | 0.632 | 0.0006 (0.3630, 0.3704, 0.3842, 0.6319, 0.6441, 0.6679) | 0.6319 |
| PASS | width_F_t0_m5_mt10 | Sec. 12 strong: F for pulse width (4s, 8s, 16s) at mu = 0 and 1/2, t0_m5_mt10.npz (charge_row.log) | 0.644 | 0.0006 (0.3630, 0.3704, 0.3842, 0.6319, 0.6441, 0.6679) | 0.6441 |
| PASS | width_F_sh_wide_m0_5_10 | Sec. 12 strong: F for pulse width (4s, 8s, 16s) at mu = 0 and 1/2, sh_wide_m0_5_10.npz (charge_row.log) | 0.668 | 0.0006 (0.3630, 0.3704, 0.3842, 0.6319, 0.6441, 0.6679) | 0.6679 |
| PASS | qabs_Q0_5->5.01 | Table tab:qabs /Q_0/ for 5->5.01 | 0.0464 | 0.0001 | 0.0464 |
| PASS | qabs_Qabs_5->5.01 | Table tab:qabs /Q_abs/ for 5->5.01 | 0.0001 | 5e-05 | 0.0001 |
| PASS | qabs_F1_5->5.01 | Table tab:qabs 1-Qabs/Q0 for 5->5.01 | 0.9983 | 0.0001 | 0.9983 |
| PASS | qabs_Fm_5->5.01 | Table tab:qabs F_meas for 5->5.01 | 1.0042 | 0.0001 | 1.0042 |
| PASS | qabs_ratio_5->5.01 | Table tab:qabs ratio for 5->5.01 | 1.0059 | 0.0001 | 1.0059 |
| PASS | qabs_Q0_5->5.5 | Table tab:qabs /Q_0/ for 5->5.5 | 0.398 | 0.00055 | 0.3983 |
| PASS | qabs_Qabs_5->5.5 | Table tab:qabs /Q_abs/ for 5->5.5 | 0.030 | 0.0005 (the table rounds to the significant digits shown; the log has 4 decimals) | 0.0299 |
| PASS | qabs_F1_5->5.5 | Table tab:qabs 1-Qabs/Q0 for 5->5.5 | 0.9249 | 0.0001 | 0.9249 |
| PASS | qabs_Fm_5->5.5 | Table tab:qabs F_meas for 5->5.5 | 0.9303 | 0.0001 | 0.9303 |
| PASS | qabs_ratio_5->5.5 | Table tab:qabs ratio for 5->5.5 | 1.0059 | 0.0001 | 1.0059 |
| PASS | qabs_Q0_5->8 | Table tab:qabs /Q_0/ for 5->8 | 2.004 | 0.00055 | 2.0044 |
| PASS | qabs_Qabs_5->8 | Table tab:qabs /Q_abs/ for 5->8 | 0.561 | 0.0005 (the table rounds to the significant digits shown; the log has 4 decimals) | 0.5606 |
| PASS | qabs_F1_5->8 | Table tab:qabs 1-Qabs/Q0 for 5->8 | 0.7203 | 0.0001 | 0.7203 |
| PASS | qabs_Fm_5->8 | Table tab:qabs F_meas for 5->8 | 0.7245 | 0.0001 | 0.7245 |
| PASS | qabs_ratio_5->8 | Table tab:qabs ratio for 5->8 | 1.0058 | 0.0001 | 1.0058 |
| PASS | qabs_Q0_5->10 | Table tab:qabs /Q_0/ for 5->10 | 3.853 | 0.00055 | 3.8533 |
| PASS | qabs_Qabs_5->10 | Table tab:qabs /Q_abs/ for 5->10 | 1.382 | 0.0005 (the table rounds to the significant digits shown; the log has 4 decimals) | 1.3818 |
| PASS | qabs_F1_5->10 | Table tab:qabs 1-Qabs/Q0 for 5->10 | 0.6414 | 0.0001 | 0.6414 |
| PASS | qabs_Fm_5->10 | Table tab:qabs F_meas for 5->10 | 0.6451 | 0.0001 | 0.6451 |
| PASS | qabs_ratio_5->10 | Table tab:qabs ratio for 5->10 | 1.0059 | 0.0001 | 1.0059 |
| PASS | qabs_Q0_5->15 | Table tab:qabs /Q_0/ for 5->15 | 10.84 | 0.00505 | 10.8419 |
| PASS | qabs_Qabs_5->15 | Table tab:qabs /Q_abs/ for 5->15 | 4.945 | 0.0005 (the table rounds to the significant digits shown; the log has 4 decimals) | 4.9445 |
| PASS | qabs_F1_5->15 | Table tab:qabs 1-Qabs/Q0 for 5->15 | 0.5439 | 0.0001 | 0.5439 |
| PASS | qabs_Fm_5->15 | Table tab:qabs F_meas for 5->15 | 0.5472 | 0.0001 | 0.5472 |
| PASS | qabs_ratio_5->15 | Table tab:qabs ratio for 5->15 | 1.0059 | 0.0001 | 1.0059 |
| PASS | qabs_Q0_5->25 | Table tab:qabs /Q_0/ for 5->25 | 35.04 | 0.00505 | 35.037 |
| PASS | qabs_Qabs_5->25 | Table tab:qabs /Q_abs/ for 5->25 | 18.53 | 0.005 (the table rounds to the significant digits shown; the log has 4 decimals) | 18.5291 |
| PASS | qabs_F1_5->25 | Table tab:qabs 1-Qabs/Q0 for 5->25 | 0.4712 | 0.0001 | 0.4712 |
| PASS | qabs_Fm_5->25 | Table tab:qabs F_meas for 5->25 | 0.4740 | 0.0001 | 0.474 |
| PASS | qabs_ratio_5->25 | Table tab:qabs ratio for 5->25 | 1.0060 | 0.0001 | 1.006 |
| PASS | qabs_Q0_2.5->10 | Table tab:qabs /Q_0/ for 2.5->10 | 5.309 | 0.00055 | 5.3089 |
| PASS | qabs_Qabs_2.5->10 | Table tab:qabs /Q_abs/ for 2.5->10 | 2.662 | 0.0005 (the table rounds to the significant digits shown; the log has 4 decimals) | 2.6623 |
| PASS | qabs_F1_2.5->10 | Table tab:qabs 1-Qabs/Q0 for 2.5->10 | 0.4985 | 0.0001 | 0.4985 |
| PASS | qabs_Fm_2.5->10 | Table tab:qabs F_meas for 2.5->10 | 0.5014 | 0.0001 | 0.5014 |
| PASS | qabs_ratio_2.5->10 | Table tab:qabs ratio for 2.5->10 | 1.0058 | 0.0001 | 1.0058 |
| PASS | qabs_Q0_0->10 | Table tab:qabs /Q_0/ for 0->10 | 6.824 | 0.00055 | 6.8237 |
| PASS | qabs_Qabs_0->10 | Table tab:qabs /Q_abs/ for 0->10 | 4.305 | 0.0005 (the table rounds to the significant digits shown; the log has 4 decimals) | 4.3047 |
| PASS | qabs_F1_0->10 | Table tab:qabs 1-Qabs/Q0 for 0->10 | 0.3691 | 0.0001 | 0.3691 |
| PASS | qabs_Fm_0->10 | Table tab:qabs F_meas for 0->10 | 0.3713 | 0.0001 | 0.3713 |
| PASS | qabs_ratio_0->10 | Table tab:qabs ratio for 0->10 | 1.0058 | 0.0001 | 1.0058 |
| PASS | qabs_Q0_0->10 Einstein | Table tab:qabs /Q_0/ for 0->10 Einstein | 6.824 | 0.00055 | 6.8235 |
| PASS | qabs_Qabs_0->10 Einstein | Table tab:qabs /Q_abs/ for 0->10 Einstein | 4.309 | 0.0005 (the table rounds to the significant digits shown; the log has 4 decimals) | 4.309 |
| PASS | qabs_F1_0->10 Einstein | Table tab:qabs 1-Qabs/Q0 for 0->10 Einstein | 0.3685 | 0.0001 | 0.3685 |
| PASS | qabs_Fm_0->10 Einstein | Table tab:qabs F_meas for 0->10 Einstein | 0.3704 | 0.0001 | 0.3704 |
| PASS | qabs_ratio_0->10 Einstein | Table tab:qabs ratio for 0->10 Einstein | 1.0052 | 0.0001 | 1.0052 |
| PASS | qabs_Q0_0->10 w4s | Table tab:qabs /Q_0/ for 0->10 w4s | 2.385 | 0.00055 | 2.3851 |
| PASS | qabs_Qabs_0->10 w4s | Table tab:qabs /Q_abs/ for 0->10 w4s | 1.524 | 0.0005 (the table rounds to the significant digits shown; the log has 4 decimals) | 1.5238 |
| PASS | qabs_F1_0->10 w4s | Table tab:qabs 1-Qabs/Q0 for 0->10 w4s | 0.3611 | 0.0001 | 0.3611 |
| PASS | qabs_Fm_0->10 w4s | Table tab:qabs F_meas for 0->10 w4s | 0.3630 | 0.0001 | 0.363 |
| PASS | qabs_ratio_0->10 w4s | Table tab:qabs ratio for 0->10 w4s | 1.0052 | 0.0001 | 1.0052 |
| PASS | qabs_Q0_5->10 w16s | Table tab:qabs /Q_0/ for 5->10 w16s | 10.93 | 0.00505 | 10.9343 |
| PASS | qabs_Qabs_5->10 w16s | Table tab:qabs /Q_abs/ for 5->10 w16s | 3.669 | 0.0005 (the table rounds to the significant digits shown; the log has 4 decimals) | 3.6692 |
| PASS | qabs_F1_5->10 w16s | Table tab:qabs 1-Qabs/Q0 for 5->10 w16s | 0.6644 | 0.0001 | 0.6644 |
| PASS | qabs_Fm_5->10 w16s | Table tab:qabs F_meas for 5->10 w16s | 0.6679 | 0.0001 | 0.6679 |
| PASS | qabs_ratio_5->10 w16s | Table tab:qabs ratio for 5->10 w16s | 1.0052 | 0.0001 | 1.0052 |
| PASS | hr_ncases | Sec. 12 strong, 22 cases: number of cases (valid rows of horizon_ray.log) | 22 | 0 | 22 |
| PASS | hr_ratio_mean | Sec. 12 strong, 22 cases: F_meas/(1-Qabs/Q0) lies 0.56% above the identity on average | 1.0056 | 5e-05 (1.00557) | 1.00562 |
| PASS | hr_ratio_min | Sec. 12 strong, 22 cases: ... smallest ratio 1.0052 | 1.0052 | 7.5e-05 | 1.0052 |
| PASS | hr_ratio_max | Sec. 12 strong, 22 cases: ... largest ratio 1.0060 | 1.0060 | 7.5e-05 | 1.006 |
| PASS | hr_cons_min | Sec. 12 strong, 22 cases: conservation Q0=QS+QH holds to 1.4e-6 (smallest /cons.err/, relative to Q0) | 1.4e-6 | 5e-08 (1.4e-6 and 1.6e-6 for the two Einstein-type rows; min is 1.4e-6) | 1.4e-06 |
| PASS | hr_cons_max | Sec. 12 strong, 22 cases: ... and to 5.3e-5 (largest /cons.err/, the m_f=5.01 row; the manuscript writes 4.4e-5) | 5.3e-5 (manuscript: holds to $1.4\times10^{-6}$--$4.4\times10^{-5}$ of $Q_0$) | 5e-07 (5.3e-5 is the row t_m5_mt5.01 (4.4e-5 is the second largest, sh_wide_m0_5_10)) | 5.3e-05 |
| PASS | hr_cons_h0.2 | Sec. 12 strong, 22 cases: conservation error for h_N=0.2 at m0=5->10 | 1.1e-4 | 5.5e-06 (two digits) | 0.00011 |
| PASS | hr_cons_h0.1 | Sec. 12 strong, 22 cases: conservation error for h_N=0.1 at m0=5->10 | 2.7e-5 | 1.35e-06 (two digits) | 2.7e-05 |
| PASS | hr_cons_h0.05 | Sec. 12 strong, 22 cases: conservation error for h_N=0.05 at m0=5->10 | 6.8e-6 | 3.4e-07 (two digits) | 6.8e-06 |
| PASS | fc_corr_mean | Fig. fig:strong caption: with the first correction the points lie 0.05% below the identity on average | 0.9995 | 5e-05 (0.99946) | 0.999464 |
| PASS | fc_corr_min | Fig. fig:strong caption: ... 0.09% at most | 0.9991 | 7.5e-05 | 0.9991 |
| PASS | fc_corr_n | fit_corr.log covers the same 22 cases | 22 | 0 | 22 |
| PASS | fc_ratio_sd | Sec. 12 strong: ratio k3/abs = 1.0056 +- 0.0003 (standard deviation, log fit_corr) | 0.0003 | 5e-05 (0.00033 (population sd) / 0.00034 (sample sd)) | 0.000333278 |
| PASS | fc_ratio_mean | Sec. 12 strong: ratio k3/abs = 1.0056 | 1.0056 | 5e-05 | 1.00563 |
| PASS | fc_corr_sd | Sec. 12 strong: corr/abs = 0.9995 +- 0.0002 | 0.0002 | 5e-05 (0.00022) | 0.00022063 |
| PASS | weak_1mF_t_m5_mt5.01 | Sec. 12 weak limit: measured 1-F for t_m5_mt5.01.npz | 0.0017 | 0.0001 | 0.0017 |
| PASS | weak_lin_t_m5_mt5.01 | Sec. 12 weak limit: linearized-horizon value for t_m5_mt5.01.npz | 0.0019 | 0.0001 | 0.0019 |
| PASS | weak_eq_t_m5_mt5.01 | Sec. 12 weak limit: Eq. (weak) for t_m5_mt5.01.npz | 0.0020 | 0.0001 | 0.002 |
| PASS | weak_f_t_m5_mt5.01 | Sec. 12 weak limit: <f>_psi for t_m5_mt5.01.npz | 0.501 | 0.001 | 0.501 |
| PASS | weak_pct_t_m5_mt5.01 | Sec. 12 weak limit: (lin - measured)/measured in percent for t_m5_mt5.01.npz | 12 | 0.5 (the percentage is rounded to an integer) | 11.7647 |
| PASS | weak_1mF_t_m5_mt5.5 | Sec. 12 weak limit: measured 1-F for t_m5_mt5.5.npz | 0.0751 | 0.0001 | 0.0751 |
| PASS | weak_lin_t_m5_mt5.5 | Sec. 12 weak limit: linearized-horizon value for t_m5_mt5.5.npz | 0.0823 | 0.0001 | 0.0823 |
| PASS | weak_eq_t_m5_mt5.5 | Sec. 12 weak limit: Eq. (weak) for t_m5_mt5.5.npz | 0.0862 | 0.0001 | 0.0862 |
| PASS | weak_f_t_m5_mt5.5 | Sec. 12 weak limit: <f>_psi for t_m5_mt5.5.npz | 0.527 | 0.001 | 0.527 |
| PASS | weak_pct_t_m5_mt5.5 | Sec. 12 weak limit: (lin - measured)/measured in percent for t_m5_mt5.5.npz | 10 | 0.5 (the percentage is rounded to an integer) | 9.58722 |
| PASS | weak_1mF_t_m5_mt6.5 | Sec. 12 weak limit: measured 1-F for t_m5_mt6.5.npz | 0.1808 | 0.0001 | 0.1808 |
| PASS | weak_lin_t_m5_mt6.5 | Sec. 12 weak limit: linearized-horizon value for t_m5_mt6.5.npz | 0.1940 | 0.0001 | 0.194 |
| PASS | weak_eq_t_m5_mt6.5 | Sec. 12 weak limit: Eq. (weak) for t_m5_mt6.5.npz | 0.2031 | 0.0001 | 0.2031 |
| PASS | weak_f_t_m5_mt6.5 | Sec. 12 weak limit: <f>_psi for t_m5_mt6.5.npz | 0.568 | 0.001 | 0.568 |
| PASS | weak_pct_t_m5_mt6.5 | Sec. 12 weak limit: (lin - measured)/measured in percent for t_m5_mt6.5.npz | 7 | 0.5 (the percentage is rounded to an integer) | 7.30088 |
| PASS | weak_1mF_t_m5_mt8 | Sec. 12 weak limit: measured 1-F for t_m5_mt8.npz | 0.2797 | 0.0001 | 0.2797 |
| PASS | weak_lin_t_m5_mt8 | Sec. 12 weak limit: linearized-horizon value for t_m5_mt8.npz | 0.2935 | 0.0001 | 0.2935 |
| PASS | weak_eq_t_m5_mt8 | Sec. 12 weak limit: Eq. (weak) for t_m5_mt8.npz | 0.3072 | 0.0001 | 0.3072 |
| PASS | weak_f_t_m5_mt8 | Sec. 12 weak limit: <f>_psi for t_m5_mt8.npz | 0.610 | 0.001 | 0.61 |
| PASS | weak_pct_t_m5_mt8 | Sec. 12 weak limit: (lin - measured)/measured in percent for t_m5_mt8.npz | 5 | 0.5 (the percentage is rounded to an integer) | 4.93386 |
| PASS | weak_coef_t_m5_mt5.01 | Sec. 12 weak limit: coefficient 0.8 measured as (1-F)/(Dm/m_f) at Dm/m_f=0.002 | 0.85 | 0.006 (0.85 (0.0017/0.0020), 0.83, 0.746 rounded to two digits) | 0.85 |
| PASS | weak_coef_t_m5_mt5.5 | Sec. 12 weak limit: coefficient 0.8 measured as (1-F)/(Dm/m_f) at Dm/m_f=0.09 | 0.83 | 0.006 (0.85 (0.0017/0.0020), 0.83, 0.746 rounded to two digits) | 0.826183 |
| PASS | weak_coef_t_m5_mt8 | Sec. 12 weak limit: coefficient 0.8 measured as (1-F)/(Dm/m_f) at Dm/m_f=0.375 | 0.75 | 0.006 (0.85 (0.0017/0.0020), 0.83, 0.746 rounded to two digits) | 0.745867 |
| PASS | linbound_max | Sec. 12 strong: after v1 the horizon takes up <= 1.2e-5 m_f in the tables of the pulses (largest dm_H/m_f of the nine tables) | 1.2e-5 | bound: <= paper (+5e-07: 1.209e-5 for t_m2.5_mt10) (1.209e-5 for t_m2.5_mt10) | 1.209e-05 |
| PASS | linbound_c04 | Sec. 12 strong: ... and <= 1.2e-3 m_f in the table with c=0.04 (tc_H_m0_5_c0.04: 1.223e-3) | 1.2e-3 | bound: <= paper (+5e-05: 1.223e-3) (1.223e-3) | 0.001223 |
| PASS | rowflux_min | Sec. 12 strong: E_scri = (0.05 -- 8.7)e-6 m_f in the 9 tables (smallest, 4.667e-8 = 0.05e-6) | 0.05e-6 | 5e-09 (4.667e-8) | 4.667e-08 |
| PASS | rowflux_max | Sec. 12 strong: ... (largest, 8.7e-6 for m_f=15) | 8.7e-6 | 5e-08 (8.664e-6) | 8.736e-06 |
| PASS | rowflux_n | Sec. 12 strong: 9 tables of the pulses in rowflux.log | 9 | 0 | 9 |
| PASS | rowflux_frac_lo | Sec. 12 strong: E_scri/E_row = 42--43% (smallest 0.416 -> 42%) | 0.42 | 0.006 (0.416 rounds to 42%) | 0.416 |
| PASS | rowflux_frac_hi | Sec. 12 strong: ... (largest 0.431 -> 43%) | 0.43 | 0.006 (0.431 rounds to 43%) | 0.431 |
| PASS | rowflux_direct_a | Sec. 12 strong: direct evolution of the row gives the same E_scri to 0.7% (m_f=10: 7.8596e-5 against 7.8606e-5) | 0.7e-2 | bound: <= paper (+0.0005: 0.7% is the larger of the two cases (b: 2.1510e-4 against 2.164e-4 for m_f=25 is 0.65%)) (0.7% is the larger of the two cases (b: 2.1510e-4 against 2.164e-4 for m_f=25 is 0.65%)) | 0.0065124 |
| PASS | ps_rf_0.01 | Table tab:pscan r_f at P=0.01 | 9.946 | 0.0005 (table rounds the log value 9.9456, 10.3542, 11.3570, 13.7233, 16.5965 to 3 decimals; half-ulp rule with the log value at 4 decimals) | 9.9456 |
| PASS | ps_mf_0.01 | Table tab:pscan m_f at P=0.01 | 5.024 | 0.0006 (log has 4 decimals (5.0236, 5.2258, 5.7229, 6.8983, 8.3285)) | 5.0236 |
| PASS | ps_rinf_0.01 | Table tab:pscan r_inf at P=0.01 | 1.05711 | 1e-05 | 1.05711 |
| PASS | ps_ms_0.01 | Table tab:pscan m* at P=0.01 | 5.028 | 0.0006 (log has 4 decimals) | 5.0277 |
| PASS | ps_mray_0.01 | Table tab:pscan m_ray at P=0.01 | 5.029 | 0.0006 (log has 4 decimals) | 5.0294 |
| PASS | ps_rm_0.01 | Table tab:pscan r_-(m_f) at P=0.01 | 1.05716 | 1e-05 | 1.05716 |
| PASS | ps_dmdv_0.01 | Table tab:pscan dm/dv at P=0.01 | 4.41 | 0.006 (log has 3 decimals; the table has 2) | 4.411 |
| PASS | ps_asy_0.01 | Table tab:pscan closed form (asympt.) at P=0.01 | 4.48 | 0.006 (log has 3 decimals; the table has 2) | 4.477 |
| PASS | ps_rf_0.03 | Table tab:pscan r_f at P=0.03 | 10.354 | 0.0005 (table rounds the log value 9.9456, 10.3542, 11.3570, 13.7233, 16.5965 to 3 decimals; half-ulp rule with the log value at 4 decimals) | 10.3542 |
| PASS | ps_mf_0.03 | Table tab:pscan m_f at P=0.03 | 5.226 | 0.0006 (log has 4 decimals (5.0236, 5.2258, 5.7229, 6.8983, 8.3285)) | 5.2258 |
| PASS | ps_rinf_0.03 | Table tab:pscan r_inf at P=0.03 | 1.05436 | 1e-05 | 1.05436 |
| PASS | ps_ms_0.03 | Table tab:pscan m* at P=0.03 | 5.248 | 0.0006 (log has 4 decimals) | 5.2481 |
| PASS | ps_mray_0.03 | Table tab:pscan m_ray at P=0.03 | 5.260 | 0.0006 (log has 4 decimals) | 5.2597 |
| PASS | ps_rm_0.03 | Table tab:pscan r_-(m_f) at P=0.03 | 1.05462 | 1e-05 | 1.05462 |
| PASS | ps_dmdv_0.03 | Table tab:pscan dm/dv at P=0.03 | 4.61 | 0.006 (log has 3 decimals; the table has 2) | 4.614 |
| PASS | ps_asy_0.03 | Table tab:pscan closed form (asympt.) at P=0.03 | 4.70 | 0.006 (log has 3 decimals; the table has 2) | 4.7 |
| PASS | ps_rf_0.05 | Table tab:pscan r_f at P=0.05 | 11.357 | 0.0005 (table rounds the log value 9.9456, 10.3542, 11.3570, 13.7233, 16.5965 to 3 decimals; half-ulp rule with the log value at 4 decimals) | 11.357 |
| PASS | ps_mf_0.05 | Table tab:pscan m_f at P=0.05 | 5.723 | 0.0006 (log has 4 decimals (5.0236, 5.2258, 5.7229, 6.8983, 8.3285)) | 5.7229 |
| PASS | ps_rinf_0.05 | Table tab:pscan r_inf at P=0.05 | 1.04903 | 1e-05 | 1.04903 |
| PASS | ps_ms_0.05 | Table tab:pscan m* at P=0.05 | 5.746 | 0.0006 (log has 4 decimals) | 5.7455 |
| PASS | ps_mray_0.05 | Table tab:pscan m_ray at P=0.05 | 5.752 | 0.0006 (log has 4 decimals) | 5.7524 |
| PASS | ps_rm_0.05 | Table tab:pscan r_-(m_f) at P=0.05 | 1.04925 | 1e-05 | 1.04925 |
| PASS | ps_dmdv_0.05 | Table tab:pscan dm/dv at P=0.05 | 5.11 | 0.006 (log has 3 decimals; the table has 2) | 5.114 |
| PASS | ps_asy_0.05 | Table tab:pscan closed form (asympt.) at P=0.05 | 5.20 | 0.006 (log has 3 decimals; the table has 2) | 5.202 |
| PASS | ps_rf_0.07 | Table tab:pscan r_f at P=0.07 | 13.723 | 0.0005 (table rounds the log value 9.9456, 10.3542, 11.3570, 13.7233, 16.5965 to 3 decimals; half-ulp rule with the log value at 4 decimals) | 13.7233 |
| PASS | ps_mf_0.07 | Table tab:pscan m_f at P=0.07 | 6.898 | 0.0006 (log has 4 decimals (5.0236, 5.2258, 5.7229, 6.8983, 8.3285)) | 6.8983 |
| PASS | ps_rinf_0.07 | Table tab:pscan r_inf at P=0.07 | 1.03985 | 1e-05 | 1.03985 |
| PASS | ps_ms_0.07 | Table tab:pscan m* at P=0.07 | 6.915 | 0.0006 (log has 4 decimals) | 6.9153 |
| PASS | ps_mray_0.07 | Table tab:pscan m_ray at P=0.07 | 6.916 | 0.0006 (log has 4 decimals) | 6.9155 |
| PASS | ps_rm_0.07 | Table tab:pscan r_-(m_f) at P=0.07 | 1.03996 | 1e-05 | 1.03996 |
| PASS | ps_dmdv_0.07 | Table tab:pscan dm/dv at P=0.07 | 6.33 | 0.006 (log has 3 decimals; the table has 2) | 6.334 |
| PASS | ps_asy_0.07 | Table tab:pscan closed form (asympt.) at P=0.07 | 6.38 | 0.006 (log has 3 decimals; the table has 2) | 6.38 |
| PASS | ps_rf_0.08 | Table tab:pscan r_f at P=0.08 | 16.597 | 0.0006 (table rounds the log value 9.9456, 10.3542, 11.3570, 13.7233, 16.5965 to 3 decimals; half-ulp rule with the log value at 4 decimals) | 16.5965 |
| PASS | ps_mf_0.08 | Table tab:pscan m_f at P=0.08 | 8.329 | 0.0006 (log has 4 decimals (5.0236, 5.2258, 5.7229, 6.8983, 8.3285)) | 8.3285 |
| PASS | ps_rinf_0.08 | Table tab:pscan r_inf at P=0.08 | 1.03223 | 1e-05 | 1.03223 |
| PASS | ps_ms_0.08 | Table tab:pscan m* at P=0.08 | 8.396 | 0.0006 (log has 4 decimals) | 8.396 |
| PASS | ps_mray_0.08 | Table tab:pscan m_ray at P=0.08 | 8.396 | 0.0006 (log has 4 decimals) | 8.396 |
| PASS | ps_rm_0.08 | Table tab:pscan r_-(m_f) at P=0.08 | 1.03251 | 1e-05 | 1.03251 |
| PASS | ps_dmdv_0.08 | Table tab:pscan dm/dv at P=0.08 | 7.82 | 0.006 (log has 3 decimals; the table has 2) | 7.816 |
| PASS | ps_asy_0.08 | Table tab:pscan closed form (asympt.) at P=0.08 | 7.87 | 0.006 (log has 3 decimals; the table has 2) | 7.868 |
| PASS | ps_vfreeze_0.01 | Table tab:pscan caption: freezing time v for P=0.01 | 42 | 0 | 42 |
| PASS | ps_vfreeze_0.03 | Table tab:pscan caption: freezing time v for P=0.03 | 45 | 0 | 45 |
| PASS | ps_vfreeze_0.05 | Table tab:pscan caption: freezing time v for P=0.05 | 50 | 0 | 50 |
| PASS | ps_vfreeze_0.07 | Table tab:pscan caption: freezing time v for P=0.07 | 64 | 0 | 64 |
| PASS | ps_vfreeze_0.08 | Table tab:pscan caption: freezing time v for P=0.08 | 84 | 0 | 84 |
| PASS | ps_rinf_rm_001 | Result of the scan: /r_inf - r_-(m_f)/ = 5e-5 at P=0.01 | 5e-5 | bound: <= paper (+1e-09: 5e-5 (1.05716-1.05711); floating-point slack) (5e-5 (1.05716-1.05711); floating-point slack) | 5e-05 |
| PASS | ps_rinf_rm_low | Result of the scan: /r_inf - r_-(m_f)/ >= 1e-4 for P=0.03..0.08 (smallest is P=0.07: 1.1e-4) | 1e-4 | bound: >= paper (-0: 1.1e-4) (1.1e-4) | 0.00011 |
| PASS | ps_rinf_rm_hi | Result of the scan: /r_inf - r_-(m_f)/ <= 3e-4 for P=0.03..0.08 | 3e-4 | bound: <= paper (+0: 2.8e-4) (2.8e-4) | 0.00028 |
| PASS | ps_mstar_lo | Result of the scan: m* differs from m_f by 0.1--0.8% (smallest, P=0.07: 0.25%; P=0.01: 0.08%) | 0.1 | 0.05 (percent: 0.08, 0.44, 0.40, 0.25, 0.81; smallest is 0.08 which the paper rounds to 0.1) | 0.0816148 |
| PASS | ps_mstar_hi | Result of the scan: ... 0.8% (largest, P=0.08) | 0.8 | 0.05 (0.81%) | 0.81047 |
| PASS | ps_mstar_ray_0.01 | Result of the scan: m* vs ray mass just before inflation, P=0.01 (percent) | 0.03 | 0.005 (percent differences 0.0276, 0.2169(0.22), 0.1215, 0.0030, <1e-4 (the logs have 4 decimals, hence the last digit)) | 0.0338012 |
| PASS | ps_mstar_ray_0.03 | Result of the scan: m* vs ray mass just before inflation, P=0.03 (percent) | 0.22 | 0.005 (percent differences 0.0276, 0.2169(0.22), 0.1215, 0.0030, <1e-4 (the logs have 4 decimals, hence the last digit)) | 0.220545 |
| PASS | ps_mstar_ray_0.05 | Result of the scan: m* vs ray mass just before inflation, P=0.05 (percent) | 0.12 | 0.005 (percent differences 0.0276, 0.2169(0.22), 0.1215, 0.0030, <1e-4 (the logs have 4 decimals, hence the last digit)) | 0.11995 |
| PASS | ps_mstar_ray_0.07 | Result of the scan: m* vs ray mass just before inflation, P=0.07 (percent) | 0.003 | 0.0006 (percent differences 0.0276, 0.2169(0.22), 0.1215, 0.0030, <1e-4 (the logs have 4 decimals, hence the last digit)) | 0.00289205 |
| PASS | ps_mstar_ray_0.08 | Result of the scan: m* vs ray mass just before inflation, P=0.08 (percent) | 1e-4 | bound: <= paper (+0: percent differences 0.0276, 0.2169(0.22), 0.1215, 0.0030, <1e-4 (the logs have 4 decimals, hence the last digit)) (percent differences 0.0276, 0.2169(0.22), 0.1215, 0.0030, <1e-4 (the logs have 4 decimals, hence the last digit)) | 0 |
| PASS | ps_r_fall_a | Result of the scan: the radius falls from 1.0571 ... | 1.0571 | 5e-05 | 1.05711 |
| PASS | ps_r_fall_b | Result of the scan: ... to 1.0322 | 1.0322 | 5e-05 | 1.03223 |
| PASS | ps_mass_gain | Result of the scan: the scan ends at P=0.08 (a horizon mass gain of 3.3 on m=5) | 3.3 | 0.05 (8.3285-5 = 3.33) | 3.3285 |
| PASS | ps_zm_0.01 | Result of the scan: zm(900) at P=0.01 | 0.59055 | 1e-05 | 0.59055 |
| PASS | ps_zmh_0.01 | Result of the scan: r^3/2 at P=0.01 | 0.59065 | 1e-05 | 0.59065 |
| PASS | ps_zm_0.03 | Result of the scan: zm(900) at P=0.03 | 0.58596 | 1e-05 | 0.58596 |
| PASS | ps_zmh_0.03 | Result of the scan: r^3/2 at P=0.03 | 0.58605 | 1e-05 | 0.58605 |
| PASS | ps_zm_0.05 | Result of the scan: zm(900) at P=0.05 | 0.57713 | 1e-05 | 0.57713 |
| PASS | ps_zmh_0.05 | Result of the scan: r^3/2 at P=0.05 | 0.57721 | 1e-05 | 0.57721 |
| PASS | ps_zm_0.07 | Result of the scan: zm(900) at P=0.07 | 0.56213 | 1e-05 | 0.56213 |
| PASS | ps_zmh_0.07 | Result of the scan: r^3/2 at P=0.07 | 0.56219 | 6e-05 (0.56220 (log, sample r_inf) vs 0.56219 printed: one unit of rounding) | 0.5622 |
| PASS | ps_zm_0.08 | Result of the scan: zm(900) at P=0.08 | 0.54987 | 1e-05 | 0.54987 |
| PASS | ps_zmh_0.08 | Result of the scan: r^3/2 at P=0.08 | 0.54992 | 1e-05 | 0.54992 |
| PASS | ps_ratio_lo | Result of the scan: the measured dm/dv is 0.7--1.8% below the closed form (largest deficit 1.8%, P=0.03) | 1.8 | 0.05 (1-0.982 = 1.8%) | 1.8 |
| PASS | ps_ratio_hi | Result of the scan: ... (smallest deficit 0.7%, P=0.07/0.08) | 0.7 | 0.05 (1-0.993 = 0.7%) | 0.7 |
| PASS | ps_vsv_0.01 | Result of the scan: v*sigma_v at v=900, P=0.01 | -8.30 | 0.0051 (log has 3 decimals (-8.304, -8.312, -8.333, -8.383, -8.446)) | -8.304 |
| PASS | ps_slope_0.01 | Result of the scan: dlnK/dlnv at v=900, P=0.01 | 10.02 | 0.0051 (log has 3 decimals) | 10.017 |
| PASS | ps_vsv_0.03 | Result of the scan: v*sigma_v at v=900, P=0.03 | -8.31 | 0.0051 (log has 3 decimals (-8.304, -8.312, -8.333, -8.383, -8.446)) | -8.312 |
| PASS | ps_slope_0.03 | Result of the scan: dlnK/dlnv at v=900, P=0.03 | 10.03 | 0.0051 (log has 3 decimals) | 10.033 |
| PASS | ps_vsv_0.05 | Result of the scan: v*sigma_v at v=900, P=0.05 | -8.33 | 0.0051 (log has 3 decimals (-8.304, -8.312, -8.333, -8.383, -8.446)) | -8.333 |
| PASS | ps_slope_0.05 | Result of the scan: dlnK/dlnv at v=900, P=0.05 | 10.02 | 0.0051 (log has 3 decimals) | 10.024 |
| PASS | ps_vsv_0.07 | Result of the scan: v*sigma_v at v=900, P=0.07 | -8.38 | 0.0051 (log has 3 decimals (-8.304, -8.312, -8.333, -8.383, -8.446)) | -8.383 |
| PASS | ps_slope_0.07 | Result of the scan: dlnK/dlnv at v=900, P=0.07 | 9.94 | 0.0051 (log has 3 decimals) | 9.94 |
| PASS | ps_vsv_0.08 | Result of the scan: v*sigma_v at v=900, P=0.08 | -8.45 | 0.0051 (log has 3 decimals (-8.304, -8.312, -8.333, -8.383, -8.446)) | -8.446 |
| PASS | ps_slope_0.08 | Result of the scan: dlnK/dlnv at v=900, P=0.08 | 9.83 | 0.0051 (log has 3 decimals) | 9.825 |
| PASS | hm_max_P09 | Sec. scan: for P=0.09 the map r_f -> r(0) has a maximum of 9.19 near r_f=30 | 9.19 | 0.01 | 9.19 |
| PASS | hm_rp5 | Sec. scan: ... below r_+(5)=9.90 | 9.90 | 0.005 (r_+(5) = 9.8995..., computed in the check below) | 9.89793 |
| PASS | hm_P1_max | Sec. scan: at P=0.1 the local maximum is 5.1 | 5.1 | 0.05 (5.08 at r_f=12) | 5.08 |
| PASS | hm_P09_r145 | Sec. scan: for P=0.09 the map returns to r_+(5) only at r_f ~ 145 (linear interpolation of r(0) between r_f=110 and 200) | 145 | 6 (the crossing is read off a coarse table (r_f=110: 8.20, 200: 12.56) by linear interpolation: 145 +- 6) | 145.049 |
| PASS | hm_m70 | Sec. scan: r_f ~ 145 corresponds to m_f ~ 70 | 70 | 3 (m(r_+=145) = r^3/(2(r^2-1)) = 72.5; the manuscript says ~70) | 72.5034 |
| PASS | vest_P01 | Sec. scan: the Vaidya-like estimate has m_f=21.6 at P=0.10 | 21.6 | 0.05 (21.594) | 21.594 |
| PASS | vest_over_001 | Sec. scan: the Vaidya estimate overestimates m_f by 0.3% at P=0.01 | 0.3 | 0.05 (5.038/5.0236 = 1.00287) | 0.286647 |
| PASS | vest_over_008 | Sec. scan: ... and by 18% at P=0.08 | 18 | 0.5 (9.808/8.3285 = 1.1777) | 17.7643 |
| PASS | vest_pole_between | Sec. scan: pole between P=0.10 (m_f=21.6) and 0.12 | 0.12 | bound: <= paper (+1e-09: the estimate is infinite at 0.12 and finite at 0.1) (the estimate is infinite at 0.12 and finite at 0.1) | 0.12 |
| PASS | cv8_dr | Sec. 12 scan, mesh (P=0.08, h_v halved): r changes by 4.4e-5 | 4.4e-5 | 5e-07 (4.40e-5 -- 4.41e-5) | 4.41e-05 |
| PASS | cv8_sv | Sec. 12 scan, mesh (P=0.08, h_v halved): sigma_v by 4e-5 for v >= 200 (largest, 4.23e-5) | 4e-5 | bound: <= paper (+3e-06: 4.23e-5 rounded to one digit) (4.23e-5 rounded to one digit) | 4.23e-05 |
| PASS | cv8_sv100 | Sec. 12 scan, mesh (P=0.08, h_v halved): ... 7e-4 at v=100 | 7e-4 | 2.5e-05 (7.20e-4) | 0.00072 |
| PASS | cv8_lnm | Sec. 12 scan, mesh (P=0.08, h_v halved): ln m by 9e-4 (largest over v = 200..800: 9.36e-4; 9.03e-4 at v=200) | 9e-4 | bound: <= paper (+4e-05: 9.36e-4 rounds to 9e-4 at the first digit; the paper quotes 9e-4) (9.36e-4 rounds to 9e-4 at the first digit; the paper quotes 9e-4) | 0.000936 |
| PASS | cv8_lnK | Sec. 12 scan, mesh (P=0.08, h_v halved): ln K by 7e-3 for v >= 400 (largest 7.12e-3); the manuscript writes v >= 200 (8.41e-3 at v=200) | 7e-3 (manuscript: $\ln K$ by $7\times10^{-3}$ for $v\ge200$ ($2.2\times10^{-2}$ at $v=100$;) | bound: <= paper (+0.0002: 7.12e-3 for v >= 400) (7.12e-3 for v >= 400) | 0.00712 |
| PASS | cv8_lnK100 | Sec. 12 scan, mesh (P=0.08, h_v halved): ln K 2.2e-2 at v=100 | 2.2e-2 | 0.00055 | 0.0222 |
| PASS | cv8_dmdv | Sec. 12 scan, mesh (P=0.08, h_v halved): dm/dv = 7.809 (h_v halved) against 7.816 (h_v=0.2) | 7.809 | 0.001 | 7.809 |
| PASS | cv8_dmdv0 | Sec. 12 scan, mesh (P=0.08, h_v halved): ... against 7.816 | 7.816 | 0.001 | 7.816 |
| PASS | cv8_slope | Sec. 12 scan, mesh (P=0.08, h_v halved): the slope of K at v=900 is 9.825 in both | 9.825 | 0.001 | 9.825 |
| PASS | cv8_slope0 | Sec. 12 scan, mesh (P=0.08, h_v halved): ... (h_v = 0.2) | 9.825 | 0.001 | 9.825 |
| PASS | cv7_rinf | Sec. 12 scan, mesh (P=0.07, h_s halved): r_inf moves to 1.03991 | 1.03991 | 1e-05 | 1.03991 |
| PASS | cv7_dr | Sec. 12 scan, mesh (P=0.07, h_s halved): ... by +5.3e-5 | 5.3e-5 | 5e-07 (5.31e-5) | 5.31e-05 |
| PASS | cv7_rinf_rm | Sec. 12 scan, mesh (P=0.07, h_s halved): ... 5e-5 from r_-(m_f)=1.03996 | 5e-5 | 5e-07 (1.03996-1.03991 = 5e-5) | 5e-05 |
| PASS | cv7_sv | Sec. 12 scan, mesh (P=0.07, h_s halved): sigma_v by <= 2.6e-4 | 2.6e-4 | bound: <= paper (+5e-06: 2.62e-4) (2.62e-4) | 0.000262 |
| PASS | cv7_sv200 | Sec. 12 scan, mesh (P=0.07, h_s halved): ... (<= 1.2e-6 for v >= 200) | 1.2e-6 | bound: <= paper (+5e-08: 1.15e-6) (1.15e-6) | 1.15e-06 |
| PASS | cv7_lnm_lo | Sec. 12 scan, mesh (P=0.07, h_s halved): ln m by 1e-3 (smallest, 9.76e-4) | 1e-3 | 3e-05 (9.76e-4 and 1.08e-3) | 0.000976 |
| PASS | cv7_lnm_hi | Sec. 12 scan, mesh (P=0.07, h_s halved): ... to 4e-3 (largest, 4.06e-3) | 4e-3 | 0.0001 (4.06e-3) | 0.00406 |
| PASS | cv7_lnK_lo | Sec. 12 scan, mesh (P=0.07, h_s halved): ln K by 6e-4 (smallest for v >= 200, 6.13e-4) | 6e-4 | 2e-05 (6.13e-4) | 0.000613 |
| PASS | cv7_lnK_hi | Sec. 12 scan, mesh (P=0.07, h_s halved): ... to 1.4e-2 (largest for v >= 200, 1.38e-2) | 1.4e-2 | 0.0005 (1.38e-2) | 0.0138 |
| PASS | cv7_dmdv_a | Sec. 12 scan, mesh (P=0.07, h_s halved): dm/dv from 6.334 ... | 6.334 | 0.001 | 6.334 |
| PASS | cv7_dmdv_b | Sec. 12 scan, mesh (P=0.07, h_s halved): ... to 6.279 | 6.279 | 0.001 | 6.279 |
| PASS | cv7_dmdv_pct | Sec. 12 scan, mesh (P=0.07, h_s halved): 0.9% change in dm/dv | 0.9 | 0.05 (6.334/6.279-1 = 0.88%) | 0.875936 |
| PASS | cv7_slope_a | Sec. 12 scan, mesh (P=0.07, h_s halved): the slope of K at v=900 from 9.940 ... | 9.940 | 0.001 | 9.94 |
| PASS | cv7_slope_b | Sec. 12 scan, mesh (P=0.07, h_s halved): ... to 9.973 | 9.973 | 0.001 | 9.973 |
| PASS | eik_psi_lo | Sec. 12 strong, a priori estimate of Q_abs: max/psi_H//max/psi_u0/ = 0.96 (smallest, 0.957) ... | 0.96 | 0.0035 (0.9571 and 0.9646 both round to 0.96) | 0.957072 |
| PASS | eik_psi_hi | Sec. 12 strong, a priori estimate of Q_abs: ... to 0.99 (largest, 0.9943) | 0.99 | 0.0045 (0.9943 rounds to 0.99) | 0.99437 |
| PASS | eik_psi_n | Sec. 12 strong, a priori estimate of Q_abs: number of tables in eik_test.log is 22 | 22 | 0 | 22 |
| PASS | eik_psi_wide | Sec. 12 strong, a priori estimate of Q_abs: the two lowest values belong to the wide pulses (number of wide pulses among the two lowest) | 2 | 0 | 2 |
| PASS | eik_psi_low2 | Sec. 12 strong, a priori estimate of Q_abs: ... (the second lowest value is also 0.96) | 0.96 | 0.005 (0.9646 rounds to 0.96) | 0.964633 |
| PASS | eik_mean_eik | Sec. 12 strong, a priori estimate of Q_abs: with the true horizon radius the estimate is low by 1.5% on average | 1.5 | 0.05 (0.0147 -> 1.47%) | 1.47 |
| PASS | eik_max_eik | Sec. 12 strong, a priori estimate of Q_abs: ... at most 3.6% | 3.6 | 0.05 (0.0363) | 3.63 |
| PASS | eik_mean_V | Sec. 12 strong, a priori estimate of Q_abs: the complete estimate is low by 2.3% on average | 2.3 | 0.05 (0.0229) | 2.29 |
| PASS | eik_max_V | Sec. 12 strong, a priori estimate of Q_abs: ... at most 4.1% | 4.1 | 0.05 (0.0411) | 4.11 |
| PASS | eik_rms_V | Sec. 12 strong, a priori estimate of Q_abs: ... rms 2.6% | 2.6 | 0.06 (0.0255 (2.55 rounds to 2.6)) | 2.55 |
| PASS | eik_rH_V | Sec. 12 strong, a priori estimate of Q_abs: r_H(v0) of the estimate for m0=5->10: 16.37 | 16.37 | 0.0051 (16.370 (3 decimals in the log)) | 16.37 |
| PASS | eik_rH_true | Sec. 12 strong, a priori estimate of Q_abs: ... against 16.44 (true) | 16.44 | 0.0051 (16.435 in eik_test.log, 16.4346 in horizon_ray.log) | 16.435 |
| PASS | eik_rH_ratio | Sec. 12 strong, a priori estimate of Q_abs: ... i.e. 1.64 r_+(m_0): r_H(v0)/r_+(5) with r_+(5)=9.898 is 1.66 (the manuscript writes 1.64, which is the ratio to 2 m_0) | 1.66 (manuscript: i.e.\ $1.64\,r_+(m_0)$)) | 0.005 (16.435/9.8979 = 1.6604) | 1.66045 |
| PASS | eik_rH_max | Sec. 12 strong, a priori estimate of Q_abs: r_H(v0) estimate is accurate to 0.7% (largest over the 22 cases) | 0.7 | 0.05 (0.704%) | 0.703805 |
| PASS | eik_weak | Sec. 12 strong, a priori estimate of Q_abs: the weak-pulse value is reproduced to 2e-4 (0.9981 against 0.9983) | 2e-4 | 5e-06 (0.9983-0.9981) | 0.0002 |
| PASS | eik_weak_a | Sec. 12 strong, a priori estimate of Q_abs: ... 0.9981 | 0.9981 | 7.5e-05 | 0.9981 |
| PASS | eik2_lin_t_m5_mt5.5 | Sec. 12 strong, a priori estimate of Q_abs (linear transfer, eik2.py): F_lin/F_abs-1 in percent for t_m5_mt5.5.npz | -0.4 | 0.06 (-0.43, -0.68, -0.28, +0.75, +0.75, +0.75 percent) | -0.432479 |
| PASS | eik2_lin_t_m5_mt6.5 | Sec. 12 strong, a priori estimate of Q_abs (linear transfer, eik2.py): F_lin/F_abs-1 in percent for t_m5_mt6.5.npz | -0.7 | 0.06 (-0.43, -0.68, -0.28, +0.75, +0.75, +0.75 percent) | -0.683594 |
| PASS | eik2_lin_t_m5_mt8 | Sec. 12 strong, a priori estimate of Q_abs (linear transfer, eik2.py): F_lin/F_abs-1 in percent for t_m5_mt8.npz | -0.3 | 0.06 (-0.43, -0.68, -0.28, +0.75, +0.75, +0.75 percent) | -0.277662 |
| PASS | eik2_lin_t_m5_mt10 | Sec. 12 strong, a priori estimate of Q_abs (linear transfer, eik2.py): F_lin/F_abs-1 in percent for t_m5_mt10.npz | 0.7 | 0.06 (-0.43, -0.68, -0.28, +0.75, +0.75, +0.75 percent) | 0.748363 |
| PASS | eik2_lin_t1_m7.5_mt15 | Sec. 12 strong, a priori estimate of Q_abs (linear transfer, eik2.py): F_lin/F_abs-1 in percent for t1_m7.5_mt15.npz | 0.7 | 0.06 (-0.43, -0.68, -0.28, +0.75, +0.75, +0.75 percent) | 0.74883 |
| PASS | eik2_lin_t1_m10_mt20 | Sec. 12 strong, a priori estimate of Q_abs (linear transfer, eik2.py): F_lin/F_abs-1 in percent for t1_m10_mt20.npz | 0.7 | 0.06 (-0.43, -0.68, -0.28, +0.75, +0.75, +0.75 percent) | 0.748947 |
| PASS | eik2_lin_max | Sec. 12 strong, a priori estimate of Q_abs: the linear transfer is accurate to 0.8% for m_f <= 2 m_0 (largest /error/ over those 6 cases) | 0.8 | 0.06 (0.75%) | 0.748947 |
| PASS | eik2_psi_lo | Sec. 12 strong, a priori estimate of Q_abs: ... against 0.8--3.1% for the eikonal field (smallest, m0=5 -> 5.5) | 0.8 | 0.06 (0.76%) | 0.756839 |
| PASS | eik2_psi_hi | Sec. 12 strong, a priori estimate of Q_abs: ... (largest, m0=5 -> 15: 3.05%) | 3.1 | 0.06 (3.05% (two-digit rounding)) | 3.05203 |
| PASS | eik2_big_t_m5_mt15 | Sec. 12 strong, a priori estimate of Q_abs (linear transfer, larger ratios): F_lin/F_abs-1 in percent for t_m5_mt15.npz | 3.4 | 0.06 (+3.40, +6.94, +5.44, +16.1) | 3.40136 |
| PASS | eik2_big_t_m5_mt25 | Sec. 12 strong, a priori estimate of Q_abs (linear transfer, larger ratios): F_lin/F_abs-1 in percent for t_m5_mt25.npz | 6.9 | 0.06 (+3.40, +6.94, +5.44, +16.1) | 6.93973 |
| PASS | eik2_big_t_m2.5_mt10 | Sec. 12 strong, a priori estimate of Q_abs (linear transfer, larger ratios): F_lin/F_abs-1 in percent for t_m2.5_mt10.npz | 5.4 | 0.06 (+3.40, +6.94, +5.44, +16.1) | 5.43631 |
| PASS | eik2_big_t_m0_mt10 | Sec. 12 strong, a priori estimate of Q_abs (linear transfer, larger ratios): F_lin/F_abs-1 in percent for t_m0_mt10.npz | 16 | 0.5 (+3.40, +6.94, +5.44, +16.1) | 16.1203 |
| PASS | eik2_flat_eik | Sec. 12 strong, a priori estimate of Q_abs: ... where the eikonal estimate is -0.5% (m0 = 0 -> 10) | -0.5 | 0.06 (-0.54%) | -0.541859 |
| PASS | bcr_c3_sym_5 | Sec. 12 BCR benchmark: symmetric pulse, three-parameter fit c at r=5 | -118.2 | 0.055 | -118.17 |
| PASS | bcr_c2_sym_5 | Sec. 12 BCR benchmark: symmetric pulse, two-parameter fit c at r=5 | -116.5 | 0.055 | -116.46 |
| PASS | bcr_c3_sym_10 | Sec. 12 BCR benchmark: symmetric pulse, three-parameter fit c at r=10 | -118.3 | 0.055 | -118.29 |
| PASS | bcr_c2_sym_10 | Sec. 12 BCR benchmark: symmetric pulse, two-parameter fit c at r=10 | -115.6 | 0.055 | -115.64 |
| PASS | bcr_c3_sym_20 | Sec. 12 BCR benchmark: symmetric pulse, three-parameter fit c at r=20 | -119.1 | 0.055 | -119.08 |
| PASS | bcr_c2_sym_20 | Sec. 12 BCR benchmark: symmetric pulse, two-parameter fit c at r=20 | -112.1 | 0.055 | -112.12 |
| PASS | bcr_c3_asym_5 | Sec. 12 BCR benchmark: asymmetric pulse, three-parameter fit c at r=5 | -131.6 | 0.055 | -131.59 |
| PASS | bcr_c2_asym_5 | Sec. 12 BCR benchmark: asymmetric pulse, two-parameter fit c at r=5 | -129.2 | 0.055 | -129.24 |
| PASS | bcr_c3_asym_10 | Sec. 12 BCR benchmark: asymmetric pulse, three-parameter fit c at r=10 | -131.7 | 0.055 | -131.74 |
| PASS | bcr_c2_asym_10 | Sec. 12 BCR benchmark: asymmetric pulse, two-parameter fit c at r=10 | -128.3 | 0.055 | -128.33 |
| PASS | bcr_c3_asym_20 | Sec. 12 BCR benchmark: asymmetric pulse, three-parameter fit c at r=20 | -132.6 | 0.055 | -132.64 |
| PASS | bcr_c2_asym_20 | Sec. 12 BCR benchmark: asymmetric pulse, two-parameter fit c at r=20 | -124.4 | 0.055 | -124.39 |
| PASS | bcr_X1_sym | Sec. 12 BCR benchmark: Gamma_0 = -8 int M_B a du (symmetric) | -116.0 | 0.0505 | -116.009 |
| PASS | bcr_X2_sym | Sec. 12 BCR benchmark: -8 M_ADM Q (symmetric) | -232.0 | 0.0505 | -232.018 |
| PASS | bcr_X1_asym | Sec. 12 BCR benchmark: Gamma_0 (asymmetric) | -128.2 | 0.0505 | -128.223 |
| PASS | bcr_X2_asym | Sec. 12 BCR benchmark: -8 M_ADM Q (asymmetric) | -247.7 | 0.0505 | -247.679 |
| PASS | bcr_X4_asym | Sec. 12 BCR benchmark: weighting by the mass that passed (asymmetric) | -119.5 | 0.0505 | -119.456 |
| PASS | bcr_Madm | Sec. 12 BCR benchmark: ADM mass of the data 14.17 eps^2 (symmetric) | 14.17 | 0.006 (14.1754: the manuscript truncates (14.18 when rounded)) | 14.1754 |
| PASS | bcr_hold_all | Sec. 12 BCR benchmark: the formula holds to 3.5% in all twelve fits (largest deviation, percent) | 3.5 | bound: <= paper (+0: 3.4% (three-parameter) and 3.4% (two-parameter)) (3.4% (three-parameter) and 3.4% (two-parameter)) | 3.44478 |
| PASS | bcr_hold_3lo | Sec. 12 BCR benchmark: three-parameter fits lie 1.9% above ... (smallest) | 1.9 | 0.05 (1.9%) | 1.86279 |
| PASS | bcr_hold_3hi | Sec. 12 BCR benchmark: ... to 3.4% above (largest) | 3.4 | 0.05 (3.4%) | 3.44478 |
| PASS | bcr_hold_2lo | Sec. 12 BCR benchmark: two-parameter fits are off by 0.1% (smallest /dev/, 0.08%) | 0.1 | 0.05 (0.08%) | 0.0834484 |
| PASS | bcr_hold_2hi | Sec. 12 BCR benchmark: ... to 3.4% (largest /dev/, 3.35%) | 3.4 | 0.06 (3.35%) | 3.35233 |
| PASS | bcr_forms_5 | Sec. 12 BCR benchmark: the two forms differ by 1.5% at r=5 (symmetric) | 1.5 | 0.05 (1.47%) | 1.46832 |
| PASS | bcr_forms_20 | Sec. 12 BCR benchmark: ... and by 6% at r=20 (symmetric) | 6 | 0.5 (5.8%) | 6.20763 |
| PASS | bcr_drift_a | Sec. 12 BCR benchmark: t^3 phi_3 at r=5 drifts from -133.4 (t=100) ... | -133.4 | 0.1 | -133.4 |
| PASS | bcr_drift_b | Sec. 12 BCR benchmark: ... to -122.2 (t=300) | -122.2 | 0.1 | -122.2 |
| PASS | bcr_X2_off | Sec. 12 BCR benchmark: -232.0 and -247.7 are "100% off" (mean of /X2/c-1/ over the twelve fits, percent; range 87--107%) | 100 | 10 (the manuscript rounds a range of 87--107% to 100%) | 95.0704 |
| PASS | bcr_conv_100 | Sec. 12 BCR benchmark: ratio of differences at t=100 | 3.96 | 0.01 | 3.96 |
| PASS | bcr_conv_150 | Sec. 12 BCR benchmark: ratio of differences at t=150 | 3.94 | 0.01 | 3.94 |
| PASS | bcr_conv_200 | Sec. 12 BCR benchmark: ratio of differences at t=200 | 3.91 | 0.01 | 3.91 |
| PASS | bcr_conv_250 | Sec. 12 BCR benchmark: ratio of differences at t=250 | 3.87 | 0.01 | 3.87 |
| PASS | bcr_conv_mean | Sec. 12 BCR benchmark: second-order convergence, ratio of differences 3.9 (mean over t=100..250) | 3.9 | 0.05 (3.87--3.96, mean 3.92) | 3.92 |
| PASS | s2a_M_0.04 | Sec. 12 BCR benchmark stage 2a: M_ADM at eps=0.04 | 0.023 | 0.00055 | 0.0228 |
| PASS | s2a_meas_0.04 | Sec. 12 BCR benchmark stage 2a: t^3 phi_NL at r=5, eps=0.04 | -0.0080 | 0.0001 | -0.008 |
| PASS | s2a_pred_0.04 | Sec. 12 BCR benchmark stage 2a: -8 int M_B a du (R_obs -> inf), eps=0.04 | -0.0080 | 0.0001 | -0.008 |
| PASS | s2a_ratio_0.04 | Sec. 12 BCR benchmark stage 2a: measured/predicted at eps=0.04 | 1.0003 | 0.0001 | 1.0003 |
| PASS | s2a_naive_0.04 | Sec. 12 BCR benchmark stage 2a: -8 M_ADM int a du at eps=0.04 | -0.015 | 0.00055 | -0.015 |
| PASS | s2a_e3_0.04 | Sec. 12 BCR benchmark stage 2a: -116 eps^3 at eps=0.04 | -0.0074 | 0.0001 | -0.0074 |
| PASS | s2a_M_0.06 | Sec. 12 BCR benchmark stage 2a: M_ADM at eps=0.06 | 0.051 | 0.00055 | 0.0515 |
| PASS | s2a_meas_0.06 | Sec. 12 BCR benchmark stage 2a: t^3 phi_NL at r=5, eps=0.06 | -0.0296 | 0.0001 | -0.0296 |
| PASS | s2a_pred_0.06 | Sec. 12 BCR benchmark stage 2a: -8 int M_B a du (R_obs -> inf), eps=0.06 | -0.0296 | 0.0001 | -0.0296 |
| PASS | s2a_ratio_0.06 | Sec. 12 BCR benchmark stage 2a: measured/predicted at eps=0.06 | 1.0013 | 0.0001 | 1.0013 |
| PASS | s2a_naive_0.06 | Sec. 12 BCR benchmark stage 2a: -8 M_ADM int a du at eps=0.06 | -0.051 | 0.0006 (-0.0512 printed to 4 decimals; the manuscript has 3) | -0.0512 |
| PASS | s2a_e3_0.06 | Sec. 12 BCR benchmark stage 2a: -116 eps^3 at eps=0.06 | -0.025 | 0.00011 (-0.0251 printed to 4 decimals; the manuscript has 3) | -0.0251 |
| PASS | s2a_M_0.08 | Sec. 12 BCR benchmark stage 2a: M_ADM at eps=0.08 | 0.092 | 0.00055 | 0.0923 |
| PASS | s2a_meas_0.08 | Sec. 12 BCR benchmark stage 2a: t^3 phi_NL at r=5, eps=0.08 | -0.0801 | 0.0001 | -0.0801 |
| PASS | s2a_pred_0.08 | Sec. 12 BCR benchmark stage 2a: -8 int M_B a du (R_obs -> inf), eps=0.08 | -0.0799 | 0.0001 | -0.0799 |
| PASS | s2a_ratio_0.08 | Sec. 12 BCR benchmark stage 2a: measured/predicted at eps=0.08 | 1.0027 | 0.0001 | 1.0027 |
| PASS | s2a_naive_0.08 | Sec. 12 BCR benchmark stage 2a: -8 M_ADM int a du at eps=0.08 | -0.123 | 0.00055 | -0.1233 |
| PASS | s2a_e3_0.08 | Sec. 12 BCR benchmark stage 2a: -116 eps^3 at eps=0.08 | -0.059 | 0.00055 | -0.0594 |
| PASS | s2a_M_0.10 | Sec. 12 BCR benchmark stage 2a: M_ADM at eps=0.10 | 0.146 | 0.00055 | 0.1458 |
| PASS | s2a_meas_0.10 | Sec. 12 BCR benchmark stage 2a: t^3 phi_NL at r=5, eps=0.10 | -0.1892 | 0.0001 | -0.1892 |
| PASS | s2a_pred_0.10 | Sec. 12 BCR benchmark stage 2a: -8 int M_B a du (R_obs -> inf), eps=0.10 | -0.1883 | 0.0001 | -0.1883 |
| PASS | s2a_ratio_0.10 | Sec. 12 BCR benchmark stage 2a: measured/predicted at eps=0.10 | 1.0051 | 0.0001 | 1.0051 |
| PASS | s2a_naive_0.10 | Sec. 12 BCR benchmark stage 2a: -8 M_ADM int a du at eps=0.10 | -0.246 | 0.00055 | -0.2464 |
| PASS | s2a_e3_0.10 | Sec. 12 BCR benchmark stage 2a: -116 eps^3 at eps=0.10 | -0.116 | 0.00055 | -0.116 |
| PASS | s2a_ratio_range | Sec. 12 BCR benchmark stage 2a: ratio 1.0003--1.0051 (largest) | 1.0051 | 7.5e-05 | 1.0051 |
| PASS | tsh_0.2 | Sec. 12 strong collapse test (i): A=0, m0=5, max/m-m0/ at h=0.2 | 7.1e-4 | 3.55e-05 (two digits) | 0.000712 |
| PASS | tsh_0.1 | Sec. 12 strong collapse test (i): A=0, m0=5, max/m-m0/ at h=0.1 | 1.8e-4 | 9e-06 (two digits) | 0.000178 |
| PASS | tsh_0.05 | Sec. 12 strong collapse test (i): A=0, m0=5, max/m-m0/ at h=0.05 | 4.5e-5 | 2.25e-06 (two digits) | 4.45e-05 |
| PASS | tsh_ratio | Sec. 12 strong collapse test (i): ratio of successive errors 4.0 | 4.0 | 0.05 (7.12e-4/1.78e-4 = 4.00, 1.78e-4/4.45e-5 = 4.00) | 4 |
| PASS | spi_m10_far | Sec. 12 strong collapse test (iii): max/psi/psi_s-1/ = 3e-6 for r > 1.5 r_+ (m_f=10; the two outermost bins: 3.16e-6, 3.90e-6) | 3e-6 | 5e-07 (3.16e-6 (r>30) and 3.9e-6 (21.9<r<29.9)) | 3.16e-06 |
| PASS | spi_m10_in | Sec. 12 strong collapse test (iii): ... and <= 4e-5 down to 0.9 r_+ (m_f=10: 3.74e-5) | 4e-5 | bound: <= paper (+0: ) | 3.74e-05 |
| PASS | spi_m25 | Sec. 12 strong collapse test (iii): 2.5e-5 for m_f=25 (largest bin, 2.48e-5) | 2.5e-5 | 5e-07 (2.48e-5) | 2.48e-05 |
| PASS | ovh_0 | Sec. 12 strong collapse (overlap_h.py): stage N to v1+80s against stage L, relative difference at r*=69.354 (m_f=10) | 4e-5 | 5e-06 (4.18e-5, 3.21e-5, 9.28e-5 rounded to one digit) | 4.18e-05 |
| PASS | ovh_1 | Sec. 12 strong collapse (overlap_h.py): stage N to v1+80s against stage L, relative difference at r*=41.028 (m_f=10) | 3e-5 | 5e-06 (4.18e-5, 3.21e-5, 9.28e-5 rounded to one digit) | 3.21e-05 |
| PASS | ovh_2 | Sec. 12 strong collapse (overlap_h.py): stage N to v1+80s against stage L, relative difference at r*=11.960 (m_f=10) | 9e-5 | 5e-06 (4.18e-5, 3.21e-5, 9.28e-5 rounded to one digit) | 9.28e-05 |
| PASS | scv_hN | Sec. 12 strong collapse: halving h_N changes phi_H by <= 3.5e-5 of its maximum (largest entry of the h_N rows) | 3.5e-5 | bound: <= paper (+0: 3.5e-5 (0.05 -> 0.025)) (3.5e-5 (0.05 -> 0.025)) | 3.5e-05 |
| PASS | scv_hN_eq | Sec. 12 strong collapse: ... attained (largest 3.5e-5) | 3.5e-5 | 5e-07 (3.5e-5) | 3.5e-05 |
| PASS | scv_hL | Sec. 12 strong collapse: halving h_L changes phi_H by <= 1.5e-6 of its maximum | 1.5e-6 | 5e-08 (1.5e-6) | 1.5e-06 |
| PASS | sce_rinf | Sec. 12 strong collapse, code E: m_f=10, r_inf = 1.02653 | 1.02653 | 1e-05 | 1.02653 |
| PASS | sce_rm | Sec. 12 strong collapse, code E: ... against r_-(10) = 1.02670 | 1.02670 | 1e-05 | 1.0267 |
| PASS | sce_mstar | Sec. 12 strong collapse, code E: m* = 10.059 | 10.059 | 0.001 | 10.059 |
| PASS | sce_mray | Sec. 12 strong collapse, code E: ray mass 10.055 at the freezing time v=94 | 10.055 | 0.001 | 10.055 |
| PASS | sce_vfr | Sec. 12 strong collapse, code E: freezing time v=94 | 94 | 0 | 94 |
| PASS | sce_zm | Sec. 12 strong collapse, code E: zm -> 0.54085 | 0.54085 | 1e-05 | 0.54085 |
| PASS | sce_zmh | Sec. 12 strong collapse, code E: ... (r_inf^3/2 = 0.54086) | 0.54086 | 1e-05 | 0.54086 |
| PASS | sce_dm | Sec. 12 strong collapse, code E: dm/dv = 9.466 over 1600 <= v <= 1800 | 9.466 | 0.001 | 9.466 |
| PASS | sce_closed | Sec. 12 strong collapse, code E: ... against 9.535 from Eq. (dm) at r_inf | 9.535 | 0.001 | 9.535 |
| PASS | sce_below | Sec. 12 strong collapse, code E: ... (0.7% below) | 0.7 | 0.05 (1-0.993 = 0.7%) | 0.7 |
| PASS | sce_vsv_5 | Sec. 12 strong collapse, code E: v*sigma_v at v=1800, history 5->10: -8.44 | -8.44 | 0.006 (-8.437) | -8.437 |
| PASS | sce_vsv_0 | Sec. 12 strong collapse, code E: ... and -8.43 (history 0->10) | -8.43 | 0.006 (-8.425) | -8.425 |
| PASS | sce_slope_5 | Sec. 12 strong collapse, code E: dlnK/dlnv at v=1800: 10.13 | 10.13 | 0.006 (10.129) | 10.129 |
| PASS | sce_slope_0 | Sec. 12 strong collapse, code E: ... and 10.10 | 10.10 | 0.006 (10.104) | 10.104 |
| PASS | sce_K5 | Sec. 12 strong collapse, code E: K(v=1500) = 8.98e25 (history 5->10) | 8.98e25 | 5e+22 (8.977e25) | 8.977e+25 |
| PASS | sce_K0 | Sec. 12 strong collapse, code E: ... against 8.37e25 (history 0->10) | 8.37e25 | 5e+22 (8.372e25) | 8.372e+25 |
| PASS | sce_Kratio | Sec. 12 strong collapse, code E: ratio 1.072 | 1.072 | 0.001 | 1.072 |
| PASS | sce_B4 | Sec. 12 strong collapse, code E: (B_0/B_5)^4 = 1.079 | 1.079 | 0.001 | 1.079 |
| PASS | sce_B5 | Sec. 12 strong collapse, code E: B = 198.9 (history 5->10) | 198.9 | 0.1 | 198.9 |
| PASS | sce_B0 | Sec. 12 strong collapse, code E: ... and 202.7 (history 0->10) | 202.7 | 0.1 | 202.7 |
| PASS | sce15_rinf | Sec. 12 strong collapse, code E: m_f=15, r_inf = 1.01665 | 1.01665 | 1e-05 | 1.01665 |
| PASS | sce15_rm | Sec. 12 strong collapse, code E: ... against r_-(15) = 1.01740 | 1.01740 | 1e-05 | 1.0174 |
| PASS | sce15_mstar | Sec. 12 strong collapse, code E: implied front mass 15.65 | 15.65 | 0.006 (15.646) | 15.646 |
| PASS | sce15_pct | Sec. 12 strong collapse, code E: ... 4.3% above m_f | 4.3 | 0.05 (4.30) | 4.3 |
| PASS | sce15_zm | Sec. 12 strong collapse, code E: zm = r_inf^3/2 to 1e-5 (m_f=15) | 1e-5 | bound: <= paper (+1e-09: /0.52539-0.52540/ = 1e-5) (/0.52539-0.52540/ = 1e-5) | 1e-05 |
| PASS | sce15_ratio | Sec. 12 strong collapse, code E: dm/dv is 0.992 of Eq. (dm) (m_f=15) | 0.992 | 0.001 | 0.992 |
| PASS | sce25_rinf_0 | Sec. 12 strong collapse, code E: m_f=25 mesh 0, r_inf | 1.00527 | 1e-05 | 1.00527 |
| PASS | sce25_dist_0 | Sec. 12 strong collapse, code E: ... distance from r_-(25) | 5.0e-3 | 0.00025 (two digits) | 0.005 |
| PASS | sce25_mstar_0 | Sec. 12 strong collapse, code E: ... implied front mass | 48.1 | 0.06 (48.057, 40.150, 28.775, 25.799 rounded to 3 digits) | 48.057 |
| PASS | sce25_pct_0 | Sec. 12 strong collapse, code E: ... percent above m_f | 92 | 0.5 (92.23, 60.60, 15.10, 3.19) | 92.23 |
| PASS | sce25_rinf_1 | Sec. 12 strong collapse, code E: m_f=25 mesh 1, r_inf | 1.00633 | 1e-05 | 1.00633 |
| PASS | sce25_dist_1 | Sec. 12 strong collapse, code E: ... distance from r_-(25) | 3.9e-3 | 0.000195 (two digits) | 0.0039 |
| PASS | sce25_mstar_1 | Sec. 12 strong collapse, code E: ... implied front mass | 40.2 | 0.06 (48.057, 40.150, 28.775, 25.799 rounded to 3 digits) | 40.15 |
| PASS | sce25_pct_1 | Sec. 12 strong collapse, code E: ... percent above m_f | 61 | 0.5 (92.23, 60.60, 15.10, 3.19) | 60.6 |
| PASS | sce25_rinf_2 | Sec. 12 strong collapse, code E: m_f=25 mesh 2, r_inf | 1.00888 | 1e-05 | 1.00888 |
| PASS | sce25_dist_2 | Sec. 12 strong collapse, code E: ... distance from r_-(25) | 1.4e-3 | 7e-05 (two digits) | 0.0014 |
| PASS | sce25_mstar_2 | Sec. 12 strong collapse, code E: ... implied front mass | 28.8 | 0.06 (48.057, 40.150, 28.775, 25.799 rounded to 3 digits) | 28.775 |
| PASS | sce25_pct_2 | Sec. 12 strong collapse, code E: ... percent above m_f | 15 | 0.5 (92.23, 60.60, 15.10, 3.19) | 15.1 |
| PASS | sce25_rinf_3 | Sec. 12 strong collapse, code E: m_f=25 mesh 3, r_inf | 1.00993 | 1e-05 | 1.00993 |
| PASS | sce25_dist_3 | Sec. 12 strong collapse, code E: ... distance from r_-(25) | 3.3e-4 | 1.65e-05 (two digits) | 0.00033 |
| PASS | sce25_mstar_3 | Sec. 12 strong collapse, code E: ... implied front mass | 25.8 | 0.06 (48.057, 40.150, 28.775, 25.799 rounded to 3 digits) | 25.799 |
| PASS | sce25_pct_3 | Sec. 12 strong collapse, code E: ... percent above m_f | 3.2 | 0.05 (92.23, 60.60, 15.10, 3.19) | 3.19 |
| PASS | sce25_rm | Sec. 12 strong collapse, code E: r_-(25) = 1.01026 | 1.01026 | 1e-05 | 1.01026 |
| PASS | sce25_ratio_fine | Sec. 12 strong collapse, code E: with both meshes at 0.1 dm/dv = 25.21 is 0.997 of Eq. (dm) | 0.997 | 0.001 | 0.997 |
| PASS | sce25_dm_fine | Sec. 12 strong collapse, code E: ... dm/dv = 25.21 | 25.21 | 0.006 (25.214) | 25.214 |
| PASS | sce25_ratio_0 | Sec. 12 strong collapse, code E: the ratios were 1.20, 0.97, 1.09 on the other meshes | 1.20 | 0.006 (1.196, 0.967, 1.086) | 1.196 |
| PASS | sce25_ratio_1 | Sec. 12 strong collapse, code E: the ratios were 1.20, 0.97, 1.09 on the other meshes | 0.97 | 0.006 (1.196, 0.967, 1.086) | 0.967 |
| PASS | sce25_ratio_2 | Sec. 12 strong collapse, code E: the ratios were 1.20, 0.97, 1.09 on the other meshes | 1.09 | 0.006 (1.196, 0.967, 1.086) | 1.086 |
| PASS | sce25_zm | Sec. 12 strong collapse, code E: zm = r_inf^3/2 to 1e-5 in each of the four m_f=25 meshes (largest difference) | 1e-5 | bound: <= paper (+1e-09: ) | 1e-05 |
| PASS | sce25_vsv | Sec. 12 strong collapse, code E: m_f=25, v*sigma_v = -19.8 at v=2666 (finest mesh) | -19.8 | 0.06 (-19.760) | -19.76 |
| PASS | sce25_sl | Sec. 12 strong collapse, code E: ... dlnK/dlnv = 32.4 | 32.4 | 0.06 (32.404) | 32.404 |
| PASS | sce25_vsv10 | Sec. 12 strong collapse, code E: m_f=10 curve at the same kappa_+ v: -16.6 and 26.6 at v=1200 | -16.6 | 0.06 (-16.562) | -16.562 |
| PASS | sce25_sl10 | Sec. 12 strong collapse, code E: ... 26.6 | 26.6 | 0.06 (26.579) | 26.579 |
| PASS | sce_kpv | Sec. 12 strong collapse, code E: kappa_+ v ~ 26 at v=2666 for m_f=25 (kappa_+ = (r_+ - r_-)... : 1/(2 r_+^2) f'; value from kappa_+(25) = 0.0097) | 26 | 1 (kappa_+(25) = 0.00999 for the Hayward hole, times 2666 = 26.6; the manuscript writes the truncated 26) | 26.6386 |
| PASS | sce_front_mfrac | Sec. 12 strong collapse, code E: implied front mass is 0.6%, 4.3% and 92% above m_f for m_f=10, 15, 25 (0.6% for 10) | 0.6 | 0.05 (0.59) | 0.59 |
| PASS | nearext_repro | nearext.py (not quoted in main.tex): the quick run (t<=1600, h=0.25) reproduces t^2 phi_H at t = 200, 400, 800 of the original runs (sp/nearext.log, sp/nearext2.log, to t = 25600), largest relative difference | 0.02 | bound: <= paper (+0: printed with 3 digits; the transient at t=100 depends on the mesh of the original runs (up to 4%), so t = 100 is not compared) (printed with 3 digits; the transient at t=100 depends on the mesh of the original runs (up to 4%), so t = 100 is not compared) | 0.003367 |
| PASS | rb_v_2e-2 | App. A (ray tests): v_* at B=2e-2 | 46.5 | 0.0505 | 46.525 |
| PASS | rb_dr_2e-2 | App. A (ray tests): r - r_- at v_*, B=2e-2 | -0.56 | 0.00505 | -0.5629 |
| PASS | rb_psi | App. A (ray tests): psi(v_*) = -1e6 (the event) | -1e6 | 1 (-999999.43 (event located by interpolation)) | -1e+06 |
| PASS | rb_v_2e-3 | App. A (ray tests): v_* at B=2e-3 | 57.3 | 0.0505 | 57.295 |
| PASS | rb_dr_2e-3 | App. A (ray tests): r - r_- at v_*, B=2e-3 | -5.6e-3 | 5.05e-05 | -0.005637 |
| PASS | rb_v_2e-4 | App. A (ray tests): v_* at B=2e-4 | 70.1 | 0.0505 | 70.138 |
| PASS | rb_dr_2e-4 | App. A (ray tests): r - r_- at v_*, B=2e-4 | -5.6e-5 | 5.05e-07 | -5.637e-05 |
| PASS | rb_v_2e-5 | App. A (ray tests): v_* at B=2e-5 | 82.8 | 0.0505 | 82.759 |
| PASS | rb_dr_2e-5 | App. A (ray tests): r - r_- at v_*, B=2e-5 | -5.6e-7 | 5.05e-09 | -5.637e-07 |
| PASS | rb_v_2e-6 | App. A (ray tests): v_* at B=2e-6 | 95.2 | 0.0505 | 95.22 |
| PASS | rb_dr_2e-6 | App. A (ray tests): r - r_- at v_*, B=2e-6 | -5.6e-9 | 5.05e-11 | -5.637e-09 |
| PASS | rb_v_2e-7 | App. A (ray tests): v_* at B=2e-7 | 107.6 | 0.0505 | 107.562 |
| PASS | rb_dr_2e-7 | App. A (ray tests): r - r_- at v_*, B=2e-7 | -5.6e-11 | 5.05e-13 | -5.649e-11 |
| PASS | ray_sub_lines | App. A (ray tests): the 11 solves of ray_blowup.py sub (B = 2e-2 ... 2e-7, k = 0.5 ... 3 at B = 2e-3) reproduce the corresponding lines of ray_blowup.log exactly | 11 | 0 (integer count of identical lines (regenerated sub run against the shipped, or in --full the regenerated, full log)) | 11 |
| PASS | rb_fit | App. A (ray tests): v_* increases by 12.3 per decade of B in a linear fit over the six values | 12.3 | 0.05 (12.3 (least-squares slope over log10(1/B))) | 12.3309 |
| PASS | rb_slope_0 | App. A (ray tests): local slope 1 per decade | 12.8 | 0.06 (12.84, 12.62, 12.46, 12.34) | 12.843 |
| PASS | rb_slope_1 | App. A (ray tests): local slope 2 per decade | 12.6 | 0.06 (12.84, 12.62, 12.46, 12.34) | 12.621 |
| PASS | rb_slope_2 | App. A (ray tests): local slope 3 per decade | 12.5 | 0.06 (12.84, 12.62, 12.46, 12.34) | 12.461 |
| PASS | rb_slope_3 | App. A (ray tests): local slope 4 per decade | 12.3 | 0.06 (12.84, 12.62, 12.46, 12.34) | 12.342 |
| PASS | rb_efold_a | App. A (ray tests): 5.58 per e-fold of 1/B (first local slope) | 5.58 | 0.006 (12.843/ln 10 = 5.578) | 5.57764 |
| PASS | rb_efold_b | App. A (ray tests): ... to 5.36 (last local slope) | 5.36 | 0.006 (12.342/ln 10 = 5.360) | 5.36006 |
| PASS | rb_lambda | App. A (ray tests): a rate lambda ~ 1/5.4 would fit (value 1/5.4 = 0.185; slope per e-fold 5.4 between the first and last) | 5.4 | 0.2 (mean local slope per e-fold: 5.46) | 5.45767 |
| PASS | rb_k_0.5 | App. A (ray tests): v_* at B=2e-3 for k=0.5 | 51.5 | 0.0505 | 51.472 |
| PASS | rb_k_1.0 | App. A (ray tests): v_* at B=2e-3 for k=1.0 | 53.6 | 0.0505 | 53.577 |
| PASS | rb_k_1.5 | App. A (ray tests): v_* at B=2e-3 for k=1.5 | 57.3 | 0.0505 | 57.295 |
| PASS | rb_k_2.0 | App. A (ray tests): v_* at B=2e-3 for k=2.0 | 61.8 | 0.0505 | 61.769 |
| PASS | rb_k_3.0 | App. A (ray tests): v_* at B=2e-3 for k=3.0 | 72.1 | 0.0505 | 72.056 |
| PASS | scanu_psi_u-5_v40 | App. A (ray tests) table: psi(40) on u=-5 | 0.8943 | 0.0001 | 0.8943 |
| PASS | scanu_psi_u-5_v56 | App. A (ray tests) table: psi(56) on u=-5 | 0.8943 | 0.0001 | 0.8943 |
| PASS | scanu_psi_u-5_v60 | App. A (ray tests) table: psi(60) on u=-5 | 0.8942 | 0.0001 | 0.8942 |
| PASS | scanu_psi_u-5_v64 | App. A (ray tests) table: psi(64) on u=-5 | 0.8930 | 0.0001 | 0.893 |
| PASS | scanu_sv60_u-5 | App. A (ray tests) table: sigma_v(60) on u=-5 | -0.796 | 0.001 | -0.796 |
| PASS | scanu_sv64_u-5 | App. A (ray tests) table: sigma_v(64) on u=-5 | -0.796 | 0.001 | -0.796 |
| PASS | scanu_sign_u-5 | App. A (ray tests) table: sign of y on u=-5 (negative for u <= -2, positive for u >= -1; value +1 or -1) | -1 | 0 | -1 |
| PASS | scanu_psi_u-4_v40 | App. A (ray tests) table: psi(40) on u=-4 | 0.8943 | 0.0001 | 0.8943 |
| PASS | scanu_psi_u-4_v56 | App. A (ray tests) table: psi(56) on u=-4 | 0.8943 | 0.0001 | 0.8943 |
| PASS | scanu_psi_u-4_v60 | App. A (ray tests) table: psi(60) on u=-4 | 0.8942 | 0.0001 | 0.8942 |
| PASS | scanu_psi_u-4_v64 | App. A (ray tests) table: psi(64) on u=-4 | 0.8929 | 0.0001 | 0.8929 |
| PASS | scanu_sv60_u-4 | App. A (ray tests) table: sigma_v(60) on u=-4 | -0.796 | 0.001 | -0.796 |
| PASS | scanu_sv64_u-4 | App. A (ray tests) table: sigma_v(64) on u=-4 | -0.796 | 0.001 | -0.796 |
| PASS | scanu_sign_u-4 | App. A (ray tests) table: sign of y on u=-4 (negative for u <= -2, positive for u >= -1; value +1 or -1) | -1 | 0 | -1 |
| PASS | scanu_psi_u-3_v40 | App. A (ray tests) table: psi(40) on u=-3 | 0.8943 | 0.0001 | 0.8943 |
| PASS | scanu_psi_u-3_v56 | App. A (ray tests) table: psi(56) on u=-3 | 0.8942 | 0.0001 | 0.8942 |
| PASS | scanu_psi_u-3_v60 | App. A (ray tests) table: psi(60) on u=-3 | 0.8942 | 0.0001 | 0.8942 |
| PASS | scanu_psi_u-3_v64 | App. A (ray tests) table: psi(64) on u=-3 | 0.8928 | 0.0001 | 0.8928 |
| PASS | scanu_sv60_u-3 | App. A (ray tests) table: sigma_v(60) on u=-3 | -0.796 | 0.001 | -0.796 |
| PASS | scanu_sv64_u-3 | App. A (ray tests) table: sigma_v(64) on u=-3 | -0.796 | 0.001 | -0.796 |
| PASS | scanu_sign_u-3 | App. A (ray tests) table: sign of y on u=-3 (negative for u <= -2, positive for u >= -1; value +1 or -1) | -1 | 0 | -1 |
| PASS | scanu_psi_u-2_v40 | App. A (ray tests) table: psi(40) on u=-2 | 0.8943 | 0.0001 | 0.8943 |
| PASS | scanu_psi_u-2_v56 | App. A (ray tests) table: psi(56) on u=-2 | 0.8943 | 0.0001 | 0.8943 |
| PASS | scanu_psi_u-2_v60 | App. A (ray tests) table: psi(60) on u=-2 | 0.8942 | 0.0001 | 0.8942 |
| PASS | scanu_psi_u-2_v64 | App. A (ray tests) table: psi(64) on u=-2 | 0.8936 | 0.0001 | 0.8936 |
| PASS | scanu_sv60_u-2 | App. A (ray tests) table: sigma_v(60) on u=-2 | -0.795 | 0.001 | -0.795 |
| PASS | scanu_sv64_u-2 | App. A (ray tests) table: sigma_v(64) on u=-2 | -0.782 | 0.001 | -0.782 |
| PASS | scanu_sign_u-2 | App. A (ray tests) table: sign of y on u=-2 (negative for u <= -2, positive for u >= -1; value +1 or -1) | -1 | 0 | -1 |
| PASS | scanu_psi_u-1_v40 | App. A (ray tests) table: psi(40) on u=-1 | 0.8950 | 0.0001 | 0.895 |
| PASS | scanu_psi_u-1_v56 | App. A (ray tests) table: psi(56) on u=-1 | 0.8966 | 0.0001 | 0.8966 |
| PASS | scanu_psi_u-1_v60 | App. A (ray tests) table: psi(60) on u=-1 | 0.9136 | 0.0001 | 0.9136 |
| PASS | scanu_psi_u-1_v64 | App. A (ray tests) table: psi(64) on u=-1 | 0.9532 | 0.0001 | 0.9532 |
| PASS | scanu_sv60_u-1 | App. A (ray tests) table: sigma_v(60) on u=-1 | -0.564 | 0.001 | -0.564 |
| PASS | scanu_sv64_u-1 | App. A (ray tests) table: sigma_v(64) on u=-1 | -0.197 | 0.001 | -0.197 |
| PASS | scanu_sign_u-1 | App. A (ray tests) table: sign of y on u=-1 (negative for u <= -2, positive for u >= -1; value +1 or -1) | 1 | 0 | 1 |
| PASS | scanu_psi_u0_v40 | App. A (ray tests) table: psi(40) on u=0 | 0.8977 | 0.0001 | 0.8977 |
| PASS | scanu_psi_u0_v56 | App. A (ray tests) table: psi(56) on u=0 | 0.9069 | 0.0001 | 0.9069 |
| PASS | scanu_psi_u0_v60 | App. A (ray tests) table: psi(60) on u=0 | 0.9435 | 0.0001 | 0.9435 |
| PASS | scanu_psi_u0_v64 | App. A (ray tests) table: psi(64) on u=0 | 0.9694 | 0.0001 | 0.9694 |
| PASS | scanu_sv60_u0 | App. A (ray tests) table: sigma_v(60) on u=0 | -0.294 | 0.001 | -0.294 |
| PASS | scanu_sv64_u0 | App. A (ray tests) table: sigma_v(64) on u=0 | -0.111 | 0.001 | -0.111 |
| PASS | scanu_sign_u0 | App. A (ray tests) table: sign of y on u=0 (negative for u <= -2, positive for u >= -1; value +1 or -1) | 1 | 0 | 1 |
| PASS | scanu_psi_u1_v40 | App. A (ray tests) table: psi(40) on u=1 | 0.8984 | 0.0001 | 0.8984 |
| PASS | scanu_psi_u1_v56 | App. A (ray tests) table: psi(56) on u=1 | 0.9107 | 0.0001 | 0.9107 |
| PASS | scanu_psi_u1_v60 | App. A (ray tests) table: psi(60) on u=1 | 0.9488 | 0.0001 | 0.9488 |
| PASS | scanu_psi_u1_v64 | App. A (ray tests) table: psi(64) on u=1 | 0.9714 | 0.0001 | 0.9714 |
| PASS | scanu_sv60_u1 | App. A (ray tests) table: sigma_v(60) on u=1 | -0.258 | 0.001 | -0.258 |
| PASS | scanu_sv64_u1 | App. A (ray tests) table: sigma_v(64) on u=1 | -0.102 | 0.001 | -0.102 |
| PASS | scanu_sign_u1 | App. A (ray tests) table: sign of y on u=1 (negative for u <= -2, positive for u >= -1; value +1 or -1) | 1 | 0 | 1 |
| PASS | scanu_psi_u2_v40 | App. A (ray tests) table: psi(40) on u=2 | 0.8988 | 0.0001 | 0.8988 |
| PASS | scanu_psi_u2_v56 | App. A (ray tests) table: psi(56) on u=2 | 0.9131 | 0.0001 | 0.9131 |
| PASS | scanu_psi_u2_v60 | App. A (ray tests) table: psi(60) on u=2 | 0.9515 | 0.0001 | 0.9515 |
| PASS | scanu_psi_u2_v64 | App. A (ray tests) table: psi(64) on u=2 | 0.9724 | 0.0001 | 0.9724 |
| PASS | scanu_sv60_u2 | App. A (ray tests) table: sigma_v(60) on u=2 | -0.240 | 0.001 | -0.24 |
| PASS | scanu_sv64_u2 | App. A (ray tests) table: sigma_v(64) on u=2 | -0.098 | 0.001 | -0.098 |
| PASS | scanu_sign_u2 | App. A (ray tests) table: sign of y on u=2 (negative for u <= -2, positive for u >= -1; value +1 or -1) | 1 | 0 | 1 |
| PASS | scanu_psi_u4_v40 | App. A (ray tests) table: psi(40) on u=4 | 0.8989 | 0.0001 | 0.8989 |
| PASS | scanu_psi_u4_v56 | App. A (ray tests) table: psi(56) on u=4 | 0.9135 | 0.0001 | 0.9135 |
| PASS | scanu_psi_u4_v60 | App. A (ray tests) table: psi(60) on u=4 | 0.9517 | 0.0001 | 0.9517 |
| PASS | scanu_psi_u4_v64 | App. A (ray tests) table: psi(64) on u=4 | 0.9722 | 0.0001 | 0.9722 |
| PASS | scanu_sv60_u4 | App. A (ray tests) table: sigma_v(60) on u=4 | -0.237 | 0.001 | -0.237 |
| PASS | scanu_sv64_u4 | App. A (ray tests) table: sigma_v(64) on u=4 | -0.097 | 0.001 | -0.097 |
| PASS | scanu_sign_u4 | App. A (ray tests) table: sign of y on u=4 (negative for u <= -2, positive for u >= -1; value +1 or -1) | 1 | 0 | 1 |
| PASS | scanu_psi_u6_v40 | App. A (ray tests) table: psi(40) on u=6 | 0.8989 | 0.0001 | 0.8989 |
| PASS | scanu_psi_u6_v56 | App. A (ray tests) table: psi(56) on u=6 | 0.9147 | 0.0001 | 0.9147 |
| PASS | scanu_psi_u6_v60 | App. A (ray tests) table: psi(60) on u=6 | 0.9524 | 0.0001 | 0.9524 |
| PASS | scanu_psi_u6_v64 | App. A (ray tests) table: psi(64) on u=6 | 0.9716 | 0.0001 | 0.9716 |
| PASS | scanu_sv60_u6 | App. A (ray tests) table: sigma_v(60) on u=6 | -0.227 | 0.001 | -0.227 |
| PASS | scanu_sv64_u6 | App. A (ray tests) table: sigma_v(64) on u=6 | -0.094 | 0.001 | -0.094 |
| PASS | scanu_sign_u6 | App. A (ray tests) table: sign of y on u=6 (negative for u <= -2, positive for u >= -1; value +1 or -1) | 1 | 0 | 1 |
| PASS | scanu_psi_static | App. A (ray tests): psi stays at the static value 1/r_-^2 = 0.8943 (y<0 rays, v=40) | 0.8943 | 0.0001 | 0.8943 |
| PASS | scanu_rm | App. A (ray tests): 1/r_-(5)^2 = 0.8943 for the Hayward hole m=5 | 0.8943 | 5e-05 (r_-(5) = 1.0575, 1/r^2 = 0.8943 (computed)) | 0.894253 |
| PASS | rm5 | App. A (ray tests): r_-(5) = 1.0575 (Hayward, m=5) | 1.0575 | 5e-05 (1.05746) | 1.05747 |
| PASS | pde_psi_u6 | App. A (ray tests) y<0 side: psi(55.5) on u=-6 is 0.855 (pde_blowup_h0.02.log: psi(vmax-1)) | 0.855 | 0.00055 | 0.855 |
| PASS | pde_psi_u5 | App. A (ray tests) y<0 side: psi(55.5) on u=-5 | 0.853 | 0.0006 (0.8534, 0.8520, 0.8498, 0.8457) | 0.8534 |
| PASS | pde_psi_u4 | App. A (ray tests) y<0 side: psi(55.5) on u=-4 | 0.852 | 0.0006 (0.8534, 0.8520, 0.8498, 0.8457) | 0.852 |
| PASS | pde_psi_u3 | App. A (ray tests) y<0 side: psi(55.5) on u=-3 | 0.850 | 0.0006 (0.8534, 0.8520, 0.8498, 0.8457) | 0.8498 |
| PASS | pde_psi_u2 | App. A (ray tests) y<0 side: psi(55.5) on u=-2 | 0.846 | 0.0006 (0.8534, 0.8520, 0.8498, 0.8457) | 0.8457 |
| PASS | pde_max_lo | App. A (ray tests): psi passes a maximum of 0.894--0.896 at v ~ 32 (smallest) | 0.894 | 0.0006 (0.8943) | 0.8943 |
| PASS | pde_max_hi | App. A (ray tests): ... (largest) | 0.896 | 0.0006 (0.8958) | 0.8958 |
| PASS | pde_vmax_a | App. A (ray tests): maximum at v ~ 32 (u=-3: 32.1) | 32 | 2 (31.5 -- 33.8) | 32.1 |
| PASS | pde_yplus_lo | App. A (ray tests): the y>0 rays rise to 0.905--0.945 (smallest of u=-1..6 maxima: 0.9080) | 0.905 | 0.004 (0.9080 (u=6) -- the manuscript says 0.905) | 0.9051 |
| PASS | pde_yplus_hi | App. A (ray tests): ... to 0.945 (largest psi(vmax-1): 0.9424) | 0.945 | 0.004 (0.9424) | 0.9424 |
| PASS | m2_rm | App. A (ray tests) bounded h: r_- = 1.0927 | 1.0927 | 5.5e-05 | 1.09267 |
| PASS | m2_km | App. A (ray tests) bounded h: kappa_- = 0.5054 | 0.5054 | 5.5e-05 | 0.50543 |
| PASS | m2_psirm | App. A (ray tests) bounded h: psi(r_-) = 0.8376 (psi on u=-6 at v=20) | 0.8376 | 6e-05 (0.83757) | 0.83757 |
| PASS | m2_rangelo | App. A (ray tests) bounded h: the range of psi over the grid is [0.326, ... | 0.326 | 0.0006 (0.32610) | 0.3261 |
| PASS | m2_rangehi | App. A (ray tests) bounded h: ... 0.9727] | 0.9727 | 6e-05 (0.97266) | 0.97266 |
| PASS | m2_vmax | App. A (ray tests) bounded h: the run reaches v = 76 without failure (finite True) | 76 | 0 | 76 |
| PASS | m2_psi_u6 | App. A (ray tests) bounded h: psi at v=76 on u=-6 falls to 0.771 | 0.771 | 0.0006 (0.77077, 0.76961) | 0.77077 |
| PASS | m2_psi_u3 | App. A (ray tests) bounded h: psi at v=76 on u=-3 falls to 0.770 | 0.770 | 0.0006 (0.77077, 0.76961) | 0.76961 |
| PASS | m2_psih_u0 | App. A (ray tests) bounded h: psi at v=76 on u=0 | 0.959 | 0.0006 (0.95916, 0.97261, 0.97262, 0.97243) | 0.95916 |
| PASS | m2_psih_u2 | App. A (ray tests) bounded h: psi at v=76 on u=2 | 0.9726 | 6e-05 (0.95916, 0.97261, 0.97262, 0.97243) | 0.97261 |
| PASS | m2_psih_u4 | App. A (ray tests) bounded h: psi at v=76 on u=4 | 0.9726 | 6e-05 (0.95916, 0.97261, 0.97262, 0.97243) | 0.97262 |
| PASS | m2_psih_u6 | App. A (ray tests) bounded h: psi at v=76 on u=6 | 0.9724 | 6e-05 (0.95916, 0.97261, 0.97262, 0.97243) | 0.97243 |
| PASS | m2_sv_u0 | App. A (ray tests) bounded h: sigma_v at v=76 on u=0 | 0.003 | 0.001 | 0.003 |
| PASS | m2_sv_u2 | App. A (ray tests) bounded h: sigma_v at v=76 on u=2 | 0.026 | 0.001 | 0.026 |
| PASS | m2_sv_u4 | App. A (ray tests) bounded h: sigma_v at v=76 on u=4 | 0.026 | 0.001 | 0.026 |
| PASS | m2_sv_u6 | App. A (ray tests) bounded h: sigma_v at v=76 on u=6 | 0.026 | 0.001 | 0.026 |
| PASS | m2_sv0 | App. A (ray tests) bounded h: sigma_v rises from -kappa_- = -0.505 | -0.505 | 0.001 | -0.505 |
| PASS | m2_y_lo | App. A (ray tests) bounded h: y ~ -9e11 on u=-6, -3 at v=76 | -9e11 | 5e+10 (-9.389e11 and -9.454e11) | -9.389e+11 |
| PASS | m2_y_hi_lo | App. A (ray tests) bounded h: y ~ 1.7e12 (u=0) | 1.7e12 | 5e+10 (1.680e12) | 1.68e+12 |
| PASS | m2_y_hi_hi | App. A (ray tests) bounded h: ... to 1.9e12 (u=2) | 1.9e12 | 5e+10 (1.865e12) | 1.865e+12 |
| PASS | conv_psi_h0.01_v56 | Table tab:conv: psi(56) at h=0.01 | 0.90684 | 1e-05 | 0.90684 |
| PASS | conv_psi_h0.01_v60 | Table tab:conv: psi(60) at h=0.01 | 0.94268 | 1e-05 | 0.94268 |
| PASS | conv_psi_h0.01_v64 | Table tab:conv: psi(64) at h=0.01 | 0.95176 | 1e-05 | 0.95176 |
| PASS | conv_psi_h0.01_v66 | Table tab:conv: psi(66) at h=0.01 | 0.91842 | 1e-05 | 0.91842 |
| PASS | conv_psi_h0.01_v68 | Table tab:conv: psi(68) at h=0.01 | 0.89799 | 1e-05 | 0.89799 |
| PASS | conv_sv64_h0.01 | Table tab:conv: sigma_v(64) at h=0.01 | 0.0939 | 0.0001 | 0.0939 |
| PASS | conv_sv68_h0.01 | Table tab:conv: sigma_v(68) at h=0.01 | 1.1879 | 0.0001 | 1.1879 |
| PASS | conv_psi_h0.005_v56 | Table tab:conv: psi(56) at h=0.005 | 0.90691 | 1e-05 | 0.90691 |
| PASS | conv_psi_h0.005_v60 | Table tab:conv: psi(60) at h=0.005 | 0.94337 | 1e-05 | 0.94337 |
| PASS | conv_psi_h0.005_v64 | Table tab:conv: psi(64) at h=0.005 | 0.96550 | 1e-05 | 0.9655 |
| PASS | conv_psi_h0.005_v66 | Table tab:conv: psi(66) at h=0.005 | 0.95392 | 1e-05 | 0.95392 |
| PASS | conv_psi_h0.005_v68 | Table tab:conv: psi(68) at h=0.005 | 0.91531 | 1e-05 | 0.91531 |
| PASS | conv_sv64_h0.005 | Table tab:conv: sigma_v(64) at h=0.005 | -0.0705 | 0.0001 | -0.0705 |
| PASS | conv_sv68_h0.005 | Table tab:conv: sigma_v(68) at h=0.005 | 0.9805 | 0.0001 | 0.9805 |
| PASS | conv_psi_h0.0025_v56 | Table tab:conv: psi(56) at h=0.0025 | 0.90693 | 1e-05 | 0.90693 |
| PASS | conv_psi_h0.0025_v60 | Table tab:conv: psi(60) at h=0.0025 | 0.94355 | 1e-05 | 0.94355 |
| PASS | conv_psi_h0.0025_v64 | Table tab:conv: psi(64) at h=0.0025 | 0.96942 | 1e-05 | 0.96942 |
| PASS | conv_psi_h0.0025_v66 | Table tab:conv: psi(66) at h=0.0025 | 0.97093 | 1e-05 | 0.97093 |
| PASS | conv_psi_h0.0025_v68 | Table tab:conv: psi(68) at h=0.0025 | 0.95445 | 1e-05 | 0.95445 |
| PASS | conv_sv64_h0.0025 | Table tab:conv: sigma_v(64) at h=0.0025 | -0.1114 | 0.0001 | -0.1114 |
| PASS | conv_sv68_h0.0025 | Table tab:conv: sigma_v(68) at h=0.0025 | 0.3855 | 0.0001 | 0.3855 |
| PASS | conv_psi_h0.00125_v56 | Table tab:conv: psi(56) at h=0.00125 | 0.90693 | 1e-05 | 0.90693 |
| PASS | conv_psi_h0.00125_v60 | Table tab:conv: psi(60) at h=0.00125 | 0.94359 | 1e-05 | 0.94359 |
| PASS | conv_psi_h0.00125_v64 | Table tab:conv: psi(64) at h=0.00125 | 0.97042 | 1e-05 | 0.97042 |
| PASS | conv_psi_h0.00125_v66 | Table tab:conv: psi(66) at h=0.00125 | 0.97575 | 1e-05 | 0.97575 |
| PASS | conv_psi_h0.00125_v68 | Table tab:conv: psi(68) at h=0.00125 | 0.97413 | 1e-05 | 0.97413 |
| PASS | conv_sv64_h0.00125 | Table tab:conv: sigma_v(64) at h=0.00125 | -0.1215 | 0.0001 | -0.1215 |
| PASS | conv_sv68_h0.00125 | Table tab:conv: sigma_v(68) at h=0.00125 | 0.1687 | 0.0001 | 0.1687 |
| PASS | conv_psi_h0.000625_v56 | Table tab:conv: psi(56) at h=0.000625 | 0.90693 | 1e-05 | 0.90693 |
| PASS | conv_psi_h0.000625_v60 | Table tab:conv: psi(60) at h=0.000625 | 0.94360 | 1e-05 | 0.9436 |
| PASS | conv_psi_h0.000625_v64 | Table tab:conv: psi(64) at h=0.000625 | 0.97068 | 1e-05 | 0.97068 |
| PASS | conv_psi_h0.000625_v66 | Table tab:conv: psi(66) at h=0.000625 | 0.97698 | 1e-05 | 0.97698 |
| PASS | conv_psi_h0.000625_v68 | Table tab:conv: psi(68) at h=0.000625 | 0.97962 | 1e-05 | 0.97962 |
| PASS | conv_sv64_h0.000625 | Table tab:conv: sigma_v(64) at h=0.000625 | -0.1241 | 0.0001 | -0.1241 |
| PASS | conv_sv68_h0.000625 | Table tab:conv: sigma_v(68) at h=0.000625 | 0.1197 | 0.0001 | 0.1197 |
| PASS | conv_diff64_0 | App. A (ray tests) resolution: successive difference of psi(64) (1-th) | 1.37e-2 | 0.000685 (two digits) | 0.01374 |
| PASS | conv_diff64_1 | App. A (ray tests) resolution: successive difference of psi(64) (2-th) | 3.9e-3 | 0.000195 (two digits) | 0.00392 |
| PASS | conv_diff64_2 | App. A (ray tests) resolution: successive difference of psi(64) (3-th) | 1.0e-3 | 6e-05 (two digits) | 0.001 |
| PASS | conv_diff64_3 | App. A (ray tests) resolution: successive difference of psi(64) (4-th) | 2.6e-4 | 1.3e-05 (two digits) | 0.00026 |
| PASS | conv_ratio64_0 | App. A (ray tests) resolution: ratio of successive differences (1-th) of psi(64) | 3.5 | 0.06 (3.51, 3.92, 3.85 (from the printed 5-digit values)) | 3.5051 |
| PASS | conv_ratio64_1 | App. A (ray tests) resolution: ratio of successive differences (2-th) of psi(64) | 3.9 | 0.06 (3.51, 3.92, 3.85 (from the printed 5-digit values)) | 3.92 |
| PASS | conv_ratio64_2 | App. A (ray tests) resolution: ratio of successive differences (3-th) of psi(64) | 3.9 | 0.06 (3.51, 3.92, 3.85 (from the printed 5-digit values)) | 3.84615 |
| PASS | conv_fine_sv64 | App. A (ray tests) resolution: the two finest meshes differ by 2.6e-3 in sigma_v(64) | 2.6e-3 | 5e-05 (0.1241-0.1215) | 0.0026 |
| PASS | conv_fine_psi68 | App. A (ray tests) resolution: the two finest meshes differ by 5.5e-3 in psi(68) | 5.5e-3 | 5e-05 (0.97962-0.97413) | 0.00549 |
| PASS | conv_fine_sv68a | App. A (ray tests) resolution: sigma_v(68) = +0.169 ... | 0.169 | 0.0006 (0.1687) | 0.1687 |
| PASS | conv_fine_sv68b | App. A (ray tests) resolution: ... against +0.120 | 0.120 | 0.0006 (0.1197) | 0.1197 |
| PASS | conv_psi64_fin | App. A (ray tests): converged psi = 0.971 and sigma_v = -0.12 at v=64 | 0.971 | 0.0006 (0.97068) | 0.97068 |
| PASS | conv_sv64_fin | App. A (ray tests): ... sigma_v = -0.12 | -0.12 | 0.005 (-0.1241 (two digits)) | -0.1241 |
| PASS | conv_psi68_fin | App. A (ray tests): the finest mesh gives psi = 0.980 at v=68 | 0.980 | 0.0006 (0.97962) | 0.97962 |
| PASS | conv_psi_lt60 | App. A (ray tests): at v <= 60 the solution is converged to 5e-5 in psi already at h=0.0025 (/psi(h=0.0025) - psi(h=0.000625)/, v=56 and 60) | 5e-5 | bound: <= paper (+0: 0.00005 at v=60) (0.00005 at v=60) | 5e-05 |
| PASS | conv_sv_lt60 | App. A (ray tests): ... and 6e-4 in sigma_v (v=56, 60, h=0.0025 against the finest; the sigma_v column of the log gives -0.6728 and -0.2944 / -0.2950) | 6e-4 | bound: <= paper (+0: 0.0006 at v=60) (0.0006 at v=60) | 0.0006 |
| PASS | psiid_0.01_0 | App. A (ray tests) check_psi_identity: defect at h=0.01 in window 1 | 2.1e-3 | 0.0001 | 0.0021 |
| PASS | psiid_0.01_1 | App. A (ray tests) check_psi_identity: defect at h=0.01 in window 2 | 0.39 | 0.01 | 0.39 |
| PASS | psiid_0.01_2 | App. A (ray tests) check_psi_identity: defect at h=0.01 in window 3 | 2.8 | 0.1 | 2.8 |
| PASS | psiid_0.000625_0 | App. A (ray tests) check_psi_identity: defect at h=0.000625 in window 1 | 5.9e-5 | 1e-06 | 5.9e-05 |
| PASS | psiid_0.000625_1 | App. A (ray tests) check_psi_identity: defect at h=0.000625 in window 2 | 1.6e-3 | 0.0001 | 0.0016 |
| PASS | psiid_0.000625_2 | App. A (ray tests) check_psi_identity: defect at h=0.000625 in window 3 | 6.1e-2 | 0.001 | 0.061 |
| PASS | psiid_halving | App. A (ray tests): the defect in the middle window falls by about 4 per halving (mean ratio over the four halvings) | 4 | 0.3 (3.9, 3.8, 4.0, 4.1) | 3.95126 |
| PASS | psiid_62 | App. A (ray tests): the psi-equation is satisfied to 2e-3 for v <= 62 at the finest mesh (windows 1 and 2: 5.9e-5, 1.6e-3) | 2e-3 | bound: <= paper (+0: ) | 0.0016 |
| PASS | psiid_66 | App. A (ray tests): ... and to 6% in [62,66] | 6e-2 | bound: <= paper (+0.001: 6.1e-2: the manuscript rounds 6.1% down to 6%) (6.1e-2: the manuscript rounds 6.1% down to 6%) | 0.061 |
| PASS | mc_sv_max | Sec. 4 (checks) item (v), two discretizations (modecmp.log): extrapolated solutions differ by <= 7.3e-9 in sigma_v at v = 30, 40, ..., 105 | 7.3e-9 | bound: <= paper (+5e-11: 7.32e-9 at v=70) (7.32e-9 at v=70) | 7.32e-09 |
| PASS | mc_sv_105 | Sec. 4 (checks) item (v), two discretizations (modecmp.log): ... 3.3e-9 at v = 105 | 3.3e-9 | 6e-11 (3.25e-9 rounds to 3.3e-9 (half-up)) | 3.25e-09 |
| PASS | mc_z_105 | Sec. 4 (checks) item (v), two discretizations (modecmp.log): 1.6e-6 (relative) in z at v = 105 | 1.6e-6 | 6e-08 (1.61e-6) | 1.61e-06 |
| PASS | mc_z | Sec. 4 (checks) item (v), two discretizations (modecmp.log): ... z = 4.8e-3 at v = 105 | 4.8e-3 | 6e-05 (4.7848e-3) | 0.0047848 |
| PASS | mc_r | Sec. 4 (checks) item (v), two discretizations (modecmp.log): ... and by 9e-10 in r | 9e-10 | 5e-11 (8.69e-10 (largest, v=105)) | 8.69e-10 |
| PASS | mc_front | Sec. 4 (checks) item (v), two discretizations (modecmp.log): through the front (v ~ 70): sigma_v changes from -0.795 to -0.435 between v = 60 and 70 (mode 3) | -0.435 | 0.0006 (-0.4350) | -0.435045 |
| PASS | c3_v70_1 | Sec. 4 (checks) item (vi), sensitivity to c_3 (c3_sensitivity.log): sigma_v on U ~ 1 at v = 70: -0.437 (c_3) | -0.437 | 0.0006 (-0.4373) | -0.4373 |
| PASS | c3_v70_09 | Sec. 4 (checks) item (vi), sensitivity to c_3 (c3_sensitivity.log): ... -0.463 (0.9 c_3) | -0.463 | 0.0006 (-0.4629) | -0.4629 |
| PASS | c3_v70_11 | Sec. 4 (checks) item (vi), sensitivity to c_3 (c3_sensitivity.log): ... -0.413 (1.1 c_3) | -0.413 | 0.0006 (-0.4132) | -0.4132 |
| PASS | c3_v90_0 | Sec. 4 (checks) item (vi), sensitivity to c_3 (c3_sensitivity.log): with c_3 = 0 there is no front: sigma_v = -0.795 at v = 90 | -0.795 | 0.0006 (-0.7951) | -0.7951 |
| PASS | c3_dz_lo | Sec. 4 (checks) item (vi), sensitivity to c_3 (c3_sensitivity.log): the modes differ by the same mesh error for all values: /dz/z/ = 0.8e-2 ... (smallest, FAC = 1, 1.1, 0.9) | 0.8e-2 | 0.0005 (7.6e-3) | 0.0076 |
| PASS | c3_dz_hi | Sec. 4 (checks) item (vi), sensitivity to c_3 (c3_sensitivity.log): ... to 2.6e-2 (largest) | 2.6e-2 | 0.0005 (2.6e-2) | 0.026 |
| PASS | spi_fine_far | Sec. 12 strong collapse test (iii) at h_N = 0.05 s: max/psi/psi_s-1/ for r > 1.5 r_+ (m_f=10); the manuscript states 3e-6 for both meshes, the finer mesh gives 7.0e-6 | 7e-6 (manuscript: $\max/\psi/\psi_s-1/=3\times10^{-6}$ for $r>1.5r_+$ and $\le4\times10^{-5}$ down to $0.9r_+$ for $m_f=10$ ($2.5\times10^{-5}$ for $m_f=25$), at $h_N=0.1s$ and $0.05s$) | 5e-08 (6.96e-6) | 6.96e-06 |
| PASS | spi_fine_in10 | Sec. 12 strong collapse test (iii) at h_N = 0.05 s: ... <= 4e-5 down to 0.9 r_+ (m_f=10) | 4e-5 | bound: <= paper (+0: ) | 1.23e-05 |
| PASS | spi_fine_25 | Sec. 12 strong collapse test (iii) at h_N = 0.05 s: ... <= 2.5e-5 for m_f=25 | 2.5e-5 | bound: <= paper (+0: ) | 1.5e-05 |
| PASS | compat_pole_max | Sec. 4 (checks) item (vi): relative defect of sigma_uv <= 7.1e-50 in 80-digit arithmetic (largest of the five decades of z = 1 - psi) | 7.1e-50 | bound: <= paper (+5e-52: 7.11e-50) (7.11e-50) | 7.11e-50 |
| PASS | compat_pole_n | Sec. 4 (checks): five decades of z = 1 - psi, from 1e-6 to 1e-1 (rows in the log) | 5 | 0 | 5 |
| PASS | compat_pole_states | Sec. 4 (checks): 2000 states per decade (header of the log) | 2000 | 0 | 2000 |
| PASS | compat_pole_digits | Sec. 4 (checks): 80-digit arithmetic | 80 | 0 | 80 |
| PASS | fig_qtg_regenerated | Fig. qtg (App. A): figure regenerated from the shipped data/logs; same pixel dimensions as the figure in the paper (image content depends on the matplotlib version) | 1 | 0 (count of the dimension comparison line (1 = identical size)) | 1 |
| PASS | fig_eh_regenerated | Fig. eh (Sec. 9-10): figure regenerated from the shipped data/logs; same pixel dimensions as the figure in the paper (image content depends on the matplotlib version) | 1 | 0 (count of the dimension comparison line (1 = identical size)) | 1 |
| PASS | fig_collapse_regenerated | Fig. collapse (Sec. 13): figure regenerated from the shipped data/logs; same pixel dimensions as the figure in the paper (image content depends on the matplotlib version) | 1 | 0 (count of the dimension comparison line (1 = identical size)) | 1 |
| PASS | fig_collapse_k2_regenerated | Fig. k2 (Sec. 13): figure regenerated from the shipped data/logs; same pixel dimensions as the figure in the paper (image content depends on the matplotlib version) | 1 | 0 (count of the dimension comparison line (1 = identical size)) | 1 |
| PASS | fig_strong_regenerated | Fig. strong (Sec. 14): figure regenerated from the shipped data/logs; same pixel dimensions as the figure in the paper (image content depends on the matplotlib version) | 1 | 0 (count of the dimension comparison line (1 = identical size)) | 1 |
| PASS | fig_qtg_slope | Fig. qtg a / App. A: slope of the linear fit of v_* against log10(1/B) for B <= 2e-2: 12.3 per decade | 12.3 | 0.05 (12.3 rounded (fit of make_figs.py)) | 12.331 |
| PASS | fig_qtg_model2_finite | Fig. qtg c: the bounded-h run is finite everywhere (printed flag) | 1 | 0 (flag of make_figs.py) | 1 |
| PASS | repro:rowflux | code/eh_qtg/codec/sp/rowflux.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:action_check2 | code/eh_qtg/logs/action_check2.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:tables | code/eh_qtg/codec/logs/tables.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:mscale | code/eh_qtg/codec/logs/mscale.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:free_vs_con | code/eh_qtg/logs/free_vs_con.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:t_static_b_a1_M1.5 | code/eh_qtg/logs/t_static_b_a1_M1.5.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:sp_interior | code/eh_qtg/codec/logs/sp_interior.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:endpoint_k0.5 | code/eh_qtg/logs/endpoint_k0.5.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:endpoint_k3 | code/eh_qtg/logs/endpoint_k3.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:t_static_b_a1 | code/eh_qtg/logs/t_static_b_a1.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:phi_monotone | code/eh_qtg/logs/phi_monotone.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:endpoint_B0.0003 | code/eh_qtg/logs/endpoint_B0.0003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:hs_extrap | code/eh_qtg/logs/hs_extrap.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:endpoint_B0.003_merged | code/eh_qtg/logs/endpoint_B0.003_merged.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:endpoint_B0.03 | code/eh_qtg/logs/endpoint_B0.03.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:check_ruv_B0.003 | code/eh_qtg/logs/check_ruv_B0.003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:endpoint_B0.003 | code/eh_qtg/logs/endpoint_B0.003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:vb1 | code/vb1.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:t_static_cy_mode3 | code/eh_qtg/logs/t_static_cy_mode3.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:t_static_cy_mode2 | code/eh_qtg/logs/t_static_cy_mode2.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:t_static_cy_mode1 | code/eh_qtg/logs/t_static_cy_mode1.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:action_check3 | code/eh_qtg/logs/action_check3.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:fit_tables | code/eh_qtg/codec/logs/fit_tables.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:gpred_final | code/eh_qtg/logs/gpred_final.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:scan_u_h0.0025 | code/scan_u_h0.0025.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:conv_B2e-4_coarse | code/conv_B2e-4_coarse.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:t_static_b4_proj0 | code/eh_qtg/codeb/logs/t_static_b4_proj0.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:t_static_b4 | code/eh_qtg/codeb/logs/t_static_b4.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:mech_vb_B3e-2 | code/eh_qtg/codee/logs/mech_vb_B3e-2.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:scan_summary | code/eh_qtg/codec/sc/scan_summary.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:mech_vb_B3e-3 | code/eh_qtg/codee/logs/mech_vb_B3e-3.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:t_static_free_U3 | code/eh_qtg/logs/t_static_free_U3.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:linear | code/eh_qtg/codec/logs/linear.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:mech_vb_B3e-4 | code/eh_qtg/codee/logs/mech_vb_B3e-4.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:overlap_h | code/eh_qtg/codec/logs/overlap_h.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:overlap_np | code/eh_qtg/codec/logs/overlap_np.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:tc_fit | code/eh_qtg/codec/sp/tc_fit.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:ascale | code/eh_qtg/codec/logs/ascale.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:interior | code/eh_qtg/codec/logs/interior.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:overlap | code/eh_qtg/codec/logs/overlap.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:sym_checks | code/sym_checks.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:validate_model1 | code/validate_model1.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:validate_model2 | code/validate_model2.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:scan_u_h0.005 | code/scan_u_h0.005.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:scans | code/eh_qtg/codee/logs/scans.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:t_static_e | code/eh_qtg/codee/logs/t_static_e.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:strong_codeE | code/eh_qtg/codec/sp/strong_codeE.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:collapse_E_k2 | code/eh_qtg/codec/logs/collapse_E_k2.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:horizon_ray | code/eh_qtg/codec/sp/horizon_ray.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:horizon_map | code/eh_qtg/codec/sc/horizon_map.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:eik_test | code/eh_qtg/codec/sp/eik_test.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:nearext | code/eh_qtg/codec/sp/nearext_quick.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:run_growth | code/run_growth.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:t_static_free | code/eh_qtg/logs/t_static_free.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:check_compat_pole | code/eh_qtg/logs/check_compat_pole.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:strong_fit | code/eh_qtg/codec/sp/strong_fit.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:charge_row | code/eh_qtg/codec/sp/charge_row.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:horizon_ray_conv | code/eh_qtg/codec/sp/horizon_ray_conv.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:model2_h0.02 | code/model2_h0.02.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:eik2 | code/eh_qtg/codec/sp/eik2.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:pde_blowup_h0.02 | code/pde_blowup_h0.02.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:conv_P0.07_hs | code/eh_qtg/codec/sc/conv_P0.07_hs.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:np_fit | code/eh_qtg/codec/logs/np_fit.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:t_static_h | code/eh_qtg/codec/logs/t_static_h.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:check_gr_limit | code/check_gr_limit.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:check_static_identity | code/check_static_identity.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:check_compat | code/check_compat.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:check_psi_identity | code/check_psi_identity.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:check_mass_law | code/check_mass_law.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:lift_check_4d | code/eh_qtg/logs/lift_check_4d.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:static_gen | code/eh_qtg/logs/static_gen.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:check_curv_static | code/eh_qtg/logs/check_curv_static.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:vb_law | code/eh_qtg/logs/vb_law.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:slaving_pde_m1 | code/eh_qtg/logs/slaving_pde_m1.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:slaving_pde_M3 | code/eh_qtg/logs/slaving_pde_M3.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:rho_check | code/eh_qtg/logs/rho_check.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:balance_check | code/eh_qtg/logs/balance_check.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:bounded_aniso | code/eh_qtg/logs/bounded_aniso.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:bounded_slaving | code/eh_qtg/logs/bounded_slaving.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:curv_hv | code/eh_qtg/logs/curv_hv.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:curv_hv_merged | code/eh_qtg/logs/curv_hv_merged.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:curv_hv_B0.0003 | code/eh_qtg/logs/curv_hv_B0.0003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:late_m1_B0.0003 | code/eh_qtg/logs/late_m1_B0.0003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:kernel_ratio_B0.0003 | code/eh_qtg/logs/kernel_ratio_B0.0003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:masslaw_m1_B0.0003 | code/eh_qtg/logs/masslaw_m1_B0.0003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:kap_check_m1_B0.0003 | code/eh_qtg/logs/kap_check_m1_B0.0003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:curv_m1_B0.0003 | code/eh_qtg/logs/curv_m1_B0.0003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:front_m1_B0.0003 | code/eh_qtg/logs/front_m1_B0.0003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:plateau_m1_B0.0003 | code/eh_qtg/logs/plateau_m1_B0.0003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:late_m1_B0.003 | code/eh_qtg/logs/late_m1_B0.003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:kernel_ratio_B0.003 | code/eh_qtg/logs/kernel_ratio_B0.003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:masslaw_m1_B0.003 | code/eh_qtg/logs/masslaw_m1_B0.003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:kap_check_m1_B0.003 | code/eh_qtg/logs/kap_check_m1_B0.003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:curv_m1_B0.003 | code/eh_qtg/logs/curv_m1_B0.003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:front_m1_B0.003 | code/eh_qtg/logs/front_m1_B0.003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:plateau_m1_B0.003 | code/eh_qtg/logs/plateau_m1_B0.003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:late_m1_B0.03 | code/eh_qtg/logs/late_m1_B0.03.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:kernel_ratio_B0.03 | code/eh_qtg/logs/kernel_ratio_B0.03.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:masslaw_m1_B0.03 | code/eh_qtg/logs/masslaw_m1_B0.03.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:kap_check_m1_B0.03 | code/eh_qtg/logs/kap_check_m1_B0.03.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:curv_m1_B0.03 | code/eh_qtg/logs/curv_m1_B0.03.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:front_m1_B0.03 | code/eh_qtg/logs/front_m1_B0.03.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:plateau_m1_B0.03 | code/eh_qtg/logs/plateau_m1_B0.03.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:late_m2_M1.5_B0.0003 | code/eh_qtg/logs/late_m2_M1.5_B0.0003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:kap_check_m2_M1.5_B0.0003 | code/eh_qtg/logs/kap_check_m2_M1.5_B0.0003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:masslaw_m2_M1.5_B0.0003 | code/eh_qtg/logs/masslaw_m2_M1.5_B0.0003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:plateau_m2_B0.0003 | code/eh_qtg/logs/plateau_m2_B0.0003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:front_m2_B0.0003 | code/eh_qtg/logs/front_m2_B0.0003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:late_m2_M1.5_B0.003 | code/eh_qtg/logs/late_m2_M1.5_B0.003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:kap_check_m2_M1.5_B0.003 | code/eh_qtg/logs/kap_check_m2_M1.5_B0.003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:masslaw_m2_M1.5_B0.003 | code/eh_qtg/logs/masslaw_m2_M1.5_B0.003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:plateau_m2_B0.003 | code/eh_qtg/logs/plateau_m2_B0.003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:front_m2_B0.003 | code/eh_qtg/logs/front_m2_B0.003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:late_m2_M1.5_B0.03 | code/eh_qtg/logs/late_m2_M1.5_B0.03.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:kap_check_m2_M1.5_B0.03 | code/eh_qtg/logs/kap_check_m2_M1.5_B0.03.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:masslaw_m2_M1.5_B0.03 | code/eh_qtg/logs/masslaw_m2_M1.5_B0.03.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:plateau_m2_B0.03 | code/eh_qtg/logs/plateau_m2_B0.03.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:front_m2_B0.03 | code/eh_qtg/logs/front_m2_B0.03.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:late_m1_B0.003_v200 | code/eh_qtg/logs/late_m1_B0.003_v200.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:late_m1_B0.03_v200 | code/eh_qtg/logs/late_m1_B0.03_v200.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:endpoint_m1_B0.003_v200 | code/eh_qtg/logs/endpoint_m1_B0.003_v200.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:curv_terms_m1_B0.003 | code/eh_qtg/logs/curv_terms_m1_B0.003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:cmp_add_B0.003 | code/eh_qtg/logs/cmp_add_B0.003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:cmp_add_B0.0003 | code/eh_qtg/logs/cmp_add_B0.0003.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:width_m1 | code/eh_qtg/logs/width_m1.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:cmp_AB_final | code/eh_qtg/codeb/logs/cmp_AB_final.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:cmp_hs | code/eh_qtg/codeb/logs/cmp_hs.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:cmp_table | code/eh_qtg/codeb/logs/cmp_table.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:kstudy2_longdouble_v1200 | code/eh_qtg/codee/logs/kstudy2_longdouble_v1200.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:linbound | code/eh_qtg/codec/sp/linbound.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:weak_limit | code/eh_qtg/codec/sp/weak_limit.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:fit_corr | code/eh_qtg/codec/sp/fit_corr.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:strong_conv | code/eh_qtg/codec/sp/strong_conv.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:scan_zm | code/eh_qtg/codec/sc/scan_zm.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:scan_an | code/eh_qtg/codec/sc/scan_an.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:vaidya_estimate | code/eh_qtg/codec/sc/vaidya_estimate.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:collapse_E | code/eh_qtg/codec/logs/collapse_E.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:conv_c | code/eh_qtg/codec/conv_c.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:conv_c_k2 | code/eh_qtg/codec/logs/conv_c_k2.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:tailfit_results | code/eh_qtg/codec/bcr/tailfit_results.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:s2a_results | code/eh_qtg/codec/bcr/s2a/s2a_results.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:convergence_h | code/eh_qtg/codec/bcr/convergence_h.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:conv_P0.08_hv | code/eh_qtg/codec/sc/conv_P0.08_hv.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:vb_B3e-2_B3e-4 | code/eh_qtg/codee/logs/vb_B3e-2_B3e-4.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:conv_e | code/eh_qtg/codee/logs/conv_e.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:conv_e2 | code/eh_qtg/codee/logs/conv_e2.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:seed_amplitude | code/eh_qtg/codee/logs/seed_amplitude.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:kstudy2_double_v1500 | code/eh_qtg/codee/logs/kstudy2_double_v1500.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:kstudy_v600 | code/eh_qtg/codeb/logs/kstudy_v600.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:tidal_v600 | code/eh_qtg/codeb/logs/tidal_v600.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:nplin | code/eh_qtg/codec/logs/nplin.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:np_lin_b | code/eh_qtg/codec/logs/np_lin_b.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:k2_extra | code/eh_qtg/codec/logs/k2_extra.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:ktable | code/eh_qtg/logs/ktable.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:vb_prediction | code/eh_qtg/codee/logs/vb_prediction.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | repro:eik_summary | code/eh_qtg/codec/sp/eik_summary.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |
| PASS | convc_dlnm_min | Sec. 12 Code E on the collapse tail mesh: ... smallest 1.1e-5 (all four rays, v = 100 ... 1400) | 1.1e-5 | 5e-07 | 1.1e-05 |
| PASS | convc_dsV100 | Sec. 12 Code E on the collapse tail mesh: change in sigma_v 1.1e-5 at v=100 on the first ray (8e-6 elsewhere) | 1.1e-5 | 1e-06 | 1.1e-05 |
| PASS | aq_ratio_0.80 | Sec. 12 Collapse result: B/(8m/Q/) for A/A0 = 0.80 (B of ascale.log, m and Q of the data as in linear_q.py; ascale_q.log) | 0.430 | 0.0006 (0.4302, 0.4026, 0.3727, 0.3358, 0.2944 printed to 3 digits) | 0.4302 |
| PASS | aq_ratio_0.90 | Sec. 12 Collapse result: B/(8m/Q/) for A/A0 = 0.90 (B of ascale.log, m and Q of the data as in linear_q.py; ascale_q.log) | 0.403 | 0.0006 (0.4302, 0.4026, 0.3727, 0.3358, 0.2944 printed to 3 digits) | 0.4026 |
| PASS | aq_ratio_1.00 | Sec. 12 Collapse result: B/(8m/Q/) for A/A0 = 1.00 (B of ascale.log, m and Q of the data as in linear_q.py; ascale_q.log) | 0.373 | 0.0006 (0.4302, 0.4026, 0.3727, 0.3358, 0.2944 printed to 3 digits) | 0.3727 |
| PASS | aq_ratio_1.10 | Sec. 12 Collapse result: B/(8m/Q/) for A/A0 = 1.10 (B of ascale.log, m and Q of the data as in linear_q.py; ascale_q.log) | 0.336 | 0.0006 (0.4302, 0.4026, 0.3727, 0.3358, 0.2944 printed to 3 digits) | 0.3358 |
| PASS | aq_ratio_1.20 | Sec. 12 Collapse result: B/(8m/Q/) for A/A0 = 1.20 (B of ascale.log, m and Q of the data as in linear_q.py; ascale_q.log) | 0.294 | 0.0006 (0.4302, 0.4026, 0.3727, 0.3358, 0.2944 printed to 3 digits) | 0.2944 |
| PASS | aq_Q_0.80 | Sec. 12 Collapse result: Q of the data at A/A0 = 0.80 equals the value of linear_q.log | -1.49525 | 1e-05 | -1.49525 |
| PASS | aq_Q_1.00 | Sec. 12 Collapse result: Q of the data at A/A0 = 1.00 equals the value of linear_q.log | -1.70606 | 1e-05 | -1.70606 |
| PASS | aq_Q_1.20 | Sec. 12 Collapse result: Q of the data at A/A0 = 1.20 equals the value of linear_q.log | -1.81036 | 1e-05 | -1.81036 |
| PASS | aq_Qrow_0.80 | Sec. 12 Collapse result: charge of the exterior part of the row v=60, A/A0 = 0.80 | -0.27 | 0.0051 (-0.2671, -0.3690, -0.4347, -0.3881, -0.3250 rounded to 2 digits) | -0.2671 |
| PASS | aq_Qrow_0.90 | Sec. 12 Collapse result: charge of the exterior part of the row v=60, A/A0 = 0.90 | -0.37 | 0.0051 (-0.2671, -0.3690, -0.4347, -0.3881, -0.3250 rounded to 2 digits) | -0.369 |
| PASS | aq_Qrow_1.00 | Sec. 12 Collapse result: charge of the exterior part of the row v=60, A/A0 = 1.00 | -0.43 | 0.0051 (-0.2671, -0.3690, -0.4347, -0.3881, -0.3250 rounded to 2 digits) | -0.4347 |
| PASS | aq_Qrow_1.10 | Sec. 12 Collapse result: charge of the exterior part of the row v=60, A/A0 = 1.10 | -0.39 | 0.0051 (-0.2671, -0.3690, -0.4347, -0.3881, -0.3250 rounded to 2 digits) | -0.3881 |
| PASS | aq_Qrow_1.20 | Sec. 12 Collapse result: charge of the exterior part of the row v=60, A/A0 = 1.20 | -0.33 | 0.0051 (-0.2671, -0.3690, -0.4347, -0.3881, -0.3250 rounded to 2 digits) | -0.325 |
| PASS | aq_rowratio_0.80 | Sec. 12 Collapse result: B/(8m/Q_row/), A/A0 = 0.80 | 2.4 | 0.05 (2.408, 1.760, 1.463, 1.534, 1.640 rounded to 1 digit) | 2.408 |
| PASS | aq_rowratio_0.90 | Sec. 12 Collapse result: B/(8m/Q_row/), A/A0 = 0.90 | 1.8 | 0.05 (2.408, 1.760, 1.463, 1.534, 1.640 rounded to 1 digit) | 1.76 |
| PASS | aq_rowratio_1.00 | Sec. 12 Collapse result: B/(8m/Q_row/), A/A0 = 1.00 | 1.5 | 0.05 (2.408, 1.760, 1.463, 1.534, 1.640 rounded to 1 digit) | 1.463 |
| PASS | aq_rowratio_1.10 | Sec. 12 Collapse result: B/(8m/Q_row/), A/A0 = 1.10 | 1.5 | 0.05 (2.408, 1.760, 1.463, 1.534, 1.640 rounded to 1 digit) | 1.534 |
| PASS | aq_rowratio_1.20 | Sec. 12 Collapse result: B/(8m/Q_row/), A/A0 = 1.20 | 1.6 | 0.05 (2.408, 1.760, 1.463, 1.534, 1.640 rounded to 1 digit) | 1.64 |
| PASS | repro:ascale_q | code/eh_qtg/codec/logs/ascale_q.log | shipped log | last printed digit x 1.5 (deterministic scripts; the shipped log is the evidence the manuscript cites) | identical |

## Proposed corrections of the manuscript (the script reproduces the corrected value; `main.tex` itself was not edited)

- `val1_w2.7` (Sec. 4 Checks(d) table row "1, v in [20,55.2]"): `$4.2\!\times\!10^{-5}$ & $2.1$; $2.0$` -> `$4.2\!\times\!10^{-5}$ & $2.0$; $2.0$`
- `tab_k_v250_c2_diff` (Table tab:k, v=250, k=3/2 B=3e-3: sigma_v - G in 1e-4): `$-0.02505$ ($-1.9$)` -> `$-0.02505$ ($-2.0$)`
- `gpred_ratio_upper` (Sec. 9 Behind the front (slaving)(a): the range of v over which the ratio rounds to 1.0006 ends at v=250 (manuscript: 260; at 260 the ratio is 1.0005)): `1.0006$ for $150\le v\le260$` -> `1.0006$ for $150\le v\le250$`
- `curv_later_K_v280` (Sec. 9 Curvature later times: K = 1.3e28 at v=300 (the manuscript writes "at 280"; Table tab:end has 1.1e28 at 280 and 1.3e28 at 300)): `$1.3\times10^{28}$ at $280$ (Table~\ref{tab:end})` -> `$1.3\times10^{28}$ at $300$ (Table~\ref{tab:end})`
- `k650_c3share` (Sec. 9 Curvature and slaving to kappa_+ v ~ 70: the c3 term of Sigma is 1 + 3e-9 times Sigma or less at v>=300 (manuscript: 1 + 1e-9; the largest value in the log is 1.000000003 at v=300)): `$1+10^{-9}$ times $\Sigma$ or less at $v\ge300$` -> `$1+3\times10^{-9}$ times $\Sigma$ or less at $v\ge300$`
- `ce2_ld_K` (Sec. 8 Code E range (c): long double against double, K differs by <=4e-7 at v<=1100 (largest 4.2e-7)): `$K$ differs by $\le4\times10^{-7}$ and` -> `$K$ differs by $\le5\times10^{-7}$ and`
- `cE_slope1100` (Sec. 12 Code E on the collapse tail: local slope of K is 9.914 at v=1100 (U~1)): `$9.914$ at $v=1100$` -> `$9.915$ at $v=1100$`
- `cE_m_agree` (Sec. 12 Code E on the collapse tail: m (and z) agree between the profile and phi_U = 0 runs to 0.3% (largest relative difference over the four rays at v=1100: 0.59%)): `$m$, $z$ to $0.3\%$` -> `$m$, $z$ to $0.6\%$`
- `hr_cons_max` (Sec. 12 strong, 22 cases: ... and to 5.3e-5 (largest /cons.err/, the m_f=5.01 row; the manuscript writes 4.4e-5)): `holds to $1.4\times10^{-6}$--$4.4\times10^{-5}$ of $Q_0$` -> `holds to $1.4\times10^{-6}$--$5.3\times10^{-5}$ of $Q_0$`
- `cv8_lnK` (Sec. 12 scan, mesh (P=0.08, h_v halved): ln K by 7e-3 for v >= 400 (largest 7.12e-3); the manuscript writes v >= 200 (8.41e-3 at v=200)): `$\ln K$ by $7\times10^{-3}$ for $v\ge200$ ($2.2\times10^{-2}$ at $v=100$;` -> `$\ln K$ by $7\times10^{-3}$ for $v\ge400$ ($8.4\times10^{-3}$ at $v=200$, $2.2\times10^{-2}$ at $v=100$;`
- `eik_rH_ratio` (Sec. 12 strong, a priori estimate of Q_abs: ... i.e. 1.64 r_+(m_0): r_H(v0)/r_+(5) with r_+(5)=9.898 is 1.66 (the manuscript writes 1.64, which is the ratio to 2 m_0)): `i.e.\ $1.64\,r_+(m_0)$)` -> `i.e.\ $1.66\,r_+(m_0)$)`
- `spi_fine_far` (Sec. 12 strong collapse test (iii) at h_N = 0.05 s: max/psi/psi_s-1/ for r > 1.5 r_+ (m_f=10); the manuscript states 3e-6 for both meshes, the finer mesh gives 7.0e-6): `$\max|\psi/\psi_s-1|=3\times10^{-6}$ for $r>1.5r_+$ and $\le4\times10^{-5}$ down to $0.9r_+$ for $m_f=10$ ($2.5\times10^{-5}$ for $m_f=25$), at $h_N=0.1s$ and $0.05s$` -> `$\max|\psi/\psi_s-1|=3\times10^{-6}$ ($7\times10^{-6}$ at $0.05s$) for $r>1.5r_+$ and $\le4\times10^{-5}$ down to $0.9r_+$ for $m_f=10$ ($2.5\times10^{-5}$ for $m_f=25$), at $h_N=0.1s$ (the bounds $4\times10^{-5}$ and $2.5\times10^{-5}$ hold at $0.05s$ as well)`

## Scripts run

| job | status | wall s | cpu s | log comparison with the shipped log | log |
|---|---|---|---|---|---|
| action_check2 | OK | 1100.3 | 260.6 | identical  | verification/logs/action_check2.log |
| action_check3 | OK | 223.0 | 70.4 | identical  | verification/logs/action_check3.log |
| ascale | OK | 61.5 | 19.8 | identical  | verification/logs/ascale.log |
| ascale_q | OK | 25.5 | 15.9 | identical  | verification/logs/ascale_q.log |
| balance_check | OK | 2.6 | 0.9 | identical  | verification/logs/balance_check.log |
| bounded_aniso | OK | 0.8 | 0.3 | identical  | verification/logs/bounded_aniso.log |
| bounded_slaving | OK | 0.6 | 0.2 | identical  | verification/logs/bounded_slaving.log |
| charge_row | OK | 9.2 | 5.6 | identical  | verification/logs/charge_row.log |
| check_compat | OK | 2.8 | 1.0 | identical  | verification/logs/check_compat.log |
| check_compat_pole | OK | 11.1 | 4.0 | identical  | verification/logs/check_compat_pole.log |
| check_curv_static | OK | 2.6 | 0.9 | identical  | verification/logs/check_curv_static.log |
| check_gr_limit | OK | 2.4 | 0.9 | identical  | verification/logs/check_gr_limit.log |
| check_mass_law | OK | 2.6 | 0.9 | identical  | verification/logs/check_mass_law.log |
| check_psi_identity | OK | 2.2 | 0.8 | identical  | verification/logs/check_psi_identity.log |
| check_ruv_B0.003 | OK | 388.9 | 91.6 | identical  | verification/logs/check_ruv_B0.003.log |
| check_static_identity | OK | 2.8 | 1.1 | identical  | verification/logs/check_static_identity.log |
| cmp_AB_final | OK | 1.8 | 0.7 | identical  | verification/logs/cmp_AB_final.log |
| cmp_add_B0.0003 | OK | 0.6 | 0.2 | identical  | verification/logs/cmp_add_B0.0003.log |
| cmp_add_B0.003 | OK | 0.6 | 0.2 | identical  | verification/logs/cmp_add_B0.003.log |
| cmp_hs | OK | 0.6 | 0.2 | identical  | verification/logs/cmp_hs.log |
| cmp_table | OK | 0.6 | 0.2 | identical  | verification/logs/cmp_table.log |
| collapse_E | OK | 3.2 | 1.2 | identical  | verification/logs/collapse_E.log |
| collapse_E_k2 | OK | 19.3 | 7.5 | identical  | verification/logs/collapse_E_k2.log |
| conv_B2e-4_coarse | OK | 151.2 | 48.1 | identical trailing blanks only | verification/logs/conv_B2e-4_coarse.log |
| conv_P0.07_hs | OK | 5.8 | 2.2 | identical  | verification/logs/conv_P0.07_hs.log |
| conv_P0.08_hv | OK | 4.6 | 1.9 | identical  | verification/logs/conv_P0.08_hv.log |
| conv_c | OK | 2.6 | 1.0 | identical  | verification/logs/conv_c.log |
| conv_c_k2 | OK | 3.3 | 1.2 | identical  | verification/logs/conv_c_k2.log |
| conv_e | OK | 0.6 | 0.2 | identical  | verification/logs/conv_e.log |
| conv_e2 | OK | 2.2 | 0.8 | identical  | verification/logs/conv_e2.log |
| convergence_h | OK | 0.6 | 0.2 | identical  | verification/logs/convergence_h.log |
| curv_hv | OK | 2.2 | 0.8 | identical  | verification/logs/curv_hv.log |
| curv_hv_B0.0003 | OK | 2.2 | 0.8 | identical  | verification/logs/curv_hv_B0.0003.log |
| curv_hv_merged | OK | 2.2 | 0.9 | identical  | verification/logs/curv_hv_merged.log |
| curv_m1_B0.0003 | OK | 2.0 | 0.8 | identical  | verification/logs/curv_m1_B0.0003.log |
| curv_m1_B0.003 | OK | 2.4 | 0.9 | identical  | verification/logs/curv_m1_B0.003.log |
| curv_m1_B0.03 | OK | 2.4 | 0.9 | identical  | verification/logs/curv_m1_B0.03.log |
| curv_terms_m1_B0.003 | OK | 1.8 | 0.7 | identical  | verification/logs/curv_terms_m1_B0.003.log |
| eik2 | OK | 10.3 | 3.9 | identical  | verification/logs/eik2.log |
| eik_summary | OK | 0.4 | 0.2 | identical  | verification/logs/eik_summary.log |
| eik_test | OK | 18.1 | 6.9 | identical  | verification/logs/eik_test.log |
| endpoint_B0.0003 | OK | 362.1 | 86.3 | identical  | verification/logs/endpoint_B0.0003.log |
| endpoint_B0.003 | OK | 350.2 | 87.8 | identical  | verification/logs/endpoint_B0.003.log |
| endpoint_B0.003_merged | OK | 369.2 | 89.3 | identical  | verification/logs/endpoint_B0.003_merged.log |
| endpoint_B0.03 | OK | 365.5 | 86.6 | identical  | verification/logs/endpoint_B0.03.log |
| endpoint_k0.5 | OK | 395.5 | 87.4 | identical  | verification/logs/endpoint_k0.5.log |
| endpoint_k3 | OK | 354.4 | 83.7 | identical  | verification/logs/endpoint_k3.log |
| endpoint_m1_B0.003_v200 | OK | 0.6 | 0.2 | identical  | verification/logs/endpoint_m1_B0.003_v200.log |
| fig_collapse | OK | 10.7 | 4.1 |   | verification/logs/fig_collapse.log |
| fig_collapse_k2 | OK | 9.7 | 3.6 |   | verification/logs/fig_collapse_k2.log |
| fig_eh | OK | 15.7 | 5.8 |   | verification/logs/fig_eh.log |
| fig_qtg | OK | 16.0 | 6.1 |   | verification/logs/fig_qtg.log |
| fig_strong | OK | 11.7 | 4.1 |   | verification/logs/fig_strong.log |
| fit_corr | OK | 4.4 | 1.7 | identical  | verification/logs/fit_corr.log |
| fit_tables | OK | 199.6 | 63.3 | identical  | verification/logs/fit_tables.log |
| free_vs_con | OK | 556.4 | 118.7 | identical  | verification/logs/free_vs_con.log |
| front_m1_B0.0003 | OK | 0.6 | 0.2 | identical  | verification/logs/front_m1_B0.0003.log |
| front_m1_B0.003 | OK | 0.6 | 0.2 | identical  | verification/logs/front_m1_B0.003.log |
| front_m1_B0.03 | OK | 0.8 | 0.2 | identical  | verification/logs/front_m1_B0.03.log |
| front_m2_B0.0003 | OK | 0.6 | 0.2 | identical  | verification/logs/front_m2_B0.0003.log |
| front_m2_B0.003 | OK | 0.6 | 0.2 | identical  | verification/logs/front_m2_B0.003.log |
| front_m2_B0.03 | OK | 0.6 | 0.2 | identical  | verification/logs/front_m2_B0.03.log |
| gpred_final | OK | 169.7 | 55.1 | identical  | verification/logs/gpred_final.log |
| horizon_map | OK | 18.9 | 7.3 | identical  | verification/logs/horizon_map.log |
| horizon_ray | OK | 16.6 | 6.2 | identical  | verification/logs/horizon_ray.log |
| horizon_ray_conv | OK | 14.7 | 5.2 | identical  | verification/logs/horizon_ray_conv.log |
| hs_extrap | OK | 378.3 | 89.5 | identical  | verification/logs/hs_extrap.log |
| interior | OK | 59.1 | 18.7 | identical  | verification/logs/interior.log |
| k2_extra | OK | 2.8 | 1.2 | identical  | verification/logs/k2_extra.log |
| kap_check_m1_B0.0003 | OK | 2.2 | 0.8 | identical  | verification/logs/kap_check_m1_B0.0003.log |
| kap_check_m1_B0.003 | OK | 2.4 | 0.8 | identical  | verification/logs/kap_check_m1_B0.003.log |
| kap_check_m1_B0.03 | OK | 2.2 | 0.8 | identical  | verification/logs/kap_check_m1_B0.03.log |
| kap_check_m2_M1.5_B0.0003 | OK | 3.0 | 1.1 | identical  | verification/logs/kap_check_m2_M1.5_B0.0003.log |
| kap_check_m2_M1.5_B0.003 | OK | 3.0 | 1.2 | identical  | verification/logs/kap_check_m2_M1.5_B0.003.log |
| kap_check_m2_M1.5_B0.03 | OK | 2.8 | 1.1 | identical  | verification/logs/kap_check_m2_M1.5_B0.03.log |
| kernel_ratio_B0.0003 | OK | 2.6 | 1.0 | identical  | verification/logs/kernel_ratio_B0.0003.log |
| kernel_ratio_B0.003 | OK | 2.8 | 1.1 | identical  | verification/logs/kernel_ratio_B0.003.log |
| kernel_ratio_B0.03 | OK | 2.4 | 0.9 | identical  | verification/logs/kernel_ratio_B0.03.log |
| kstudy2_double_v1500 | OK | 2.2 | 0.8 | identical  | verification/logs/kstudy2_double_v1500.log |
| kstudy2_longdouble_v1200 | OK | 2.0 | 0.8 | identical  | verification/logs/kstudy2_longdouble_v1200.log |
| kstudy_v600 | OK | 2.2 | 0.8 | identical  | verification/logs/kstudy_v600.log |
| ktable | OK | 0.2 | 0.0 | identical  | verification/logs/ktable.log |
| late_m1_B0.0003 | OK | 2.2 | 0.8 | identical  | verification/logs/late_m1_B0.0003.log |
| late_m1_B0.003 | OK | 2.4 | 0.9 | identical  | verification/logs/late_m1_B0.003.log |
| late_m1_B0.003_v200 | OK | 2.4 | 0.9 | identical  | verification/logs/late_m1_B0.003_v200.log |
| late_m1_B0.03 | OK | 2.2 | 0.8 | identical  | verification/logs/late_m1_B0.03.log |
| late_m1_B0.03_v200 | OK | 2.4 | 0.9 | identical  | verification/logs/late_m1_B0.03_v200.log |
| late_m2_M1.5_B0.0003 | OK | 2.2 | 0.8 | identical  | verification/logs/late_m2_M1.5_B0.0003.log |
| late_m2_M1.5_B0.003 | OK | 2.6 | 1.0 | identical  | verification/logs/late_m2_M1.5_B0.003.log |
| late_m2_M1.5_B0.03 | OK | 2.2 | 0.8 | identical  | verification/logs/late_m2_M1.5_B0.03.log |
| lift_check_4d | OK | 3.0 | 1.1 | identical  | verification/logs/lift_check_4d.log |
| linbound | OK | 1.6 | 0.5 | identical  | verification/logs/linbound.log |
| linear | OK | 86.4 | 27.2 | identical  | verification/logs/linear.log |
| masslaw_m1_B0.0003 | OK | 2.2 | 0.8 | identical  | verification/logs/masslaw_m1_B0.0003.log |
| masslaw_m1_B0.003 | OK | 2.4 | 0.8 | identical  | verification/logs/masslaw_m1_B0.003.log |
| masslaw_m1_B0.03 | OK | 2.4 | 0.9 | identical  | verification/logs/masslaw_m1_B0.03.log |
| masslaw_m2_M1.5_B0.0003 | OK | 2.4 | 0.9 | identical  | verification/logs/masslaw_m2_M1.5_B0.0003.log |
| masslaw_m2_M1.5_B0.003 | OK | 2.2 | 0.8 | identical  | verification/logs/masslaw_m2_M1.5_B0.003.log |
| masslaw_m2_M1.5_B0.03 | OK | 2.2 | 0.8 | identical  | verification/logs/masslaw_m2_M1.5_B0.03.log |
| mech_vb_B3e-2 | OK | 117.9 | 37.0 | identical  | verification/logs/mech_vb_B3e-2.log |
| mech_vb_B3e-3 | OK | 110.5 | 35.5 | identical  | verification/logs/mech_vb_B3e-3.log |
| mech_vb_B3e-4 | OK | 98.5 | 30.9 | identical  | verification/logs/mech_vb_B3e-4.log |
| model2_h0.02 | OK | 8.2 | 3.1 | identical  | verification/logs/model2_h0.02.log |
| mscale | OK | 692.2 | 147.7 | identical trailing blanks only | verification/logs/mscale.log |
| nearext | OK | 17.7 | 6.9 | identical  | verification/logs/nearext.log |
| np_fit | OK | 6.5 | 2.4 | identical  | verification/logs/np_fit.log |
| np_lin_b | OK | 0.8 | 0.2 | identical  | verification/logs/np_lin_b.log |
| nplin | OK | 4.0 | 1.5 | identical  | verification/logs/nplin.log |
| overlap | OK | 58.3 | 18.4 | identical  | verification/logs/overlap.log |
| overlap_h | OK | 91.8 | 29.6 | identical  | verification/logs/overlap_h.log |
| overlap_np | OK | 75.6 | 24.5 | identical  | verification/logs/overlap_np.log |
| pde_blowup_h0.02 | OK | 7.4 | 2.8 | identical  | verification/logs/pde_blowup_h0.02.log |
| phi_monotone | OK | 361.1 | 85.6 | identical  | verification/logs/phi_monotone.log |
| plateau_m1_B0.0003 | OK | 0.6 | 0.2 | identical  | verification/logs/plateau_m1_B0.0003.log |
| plateau_m1_B0.003 | OK | 0.6 | 0.2 | identical  | verification/logs/plateau_m1_B0.003.log |
| plateau_m1_B0.03 | OK | 0.8 | 0.2 | identical  | verification/logs/plateau_m1_B0.03.log |
| plateau_m2_B0.0003 | OK | 0.8 | 0.2 | identical  | verification/logs/plateau_m2_B0.0003.log |
| plateau_m2_B0.003 | OK | 0.6 | 0.2 | identical  | verification/logs/plateau_m2_B0.003.log |
| plateau_m2_B0.03 | OK | 0.6 | 0.2 | identical  | verification/logs/plateau_m2_B0.03.log |
| ray_blowup_sub | OK | 55.5 | 17.2 |   | verification/logs/ray_blowup_sub.log |
| rho_check | OK | 0.8 | 0.2 | identical  | verification/logs/rho_check.log |
| rowflux | OK | 1242.0 | 292.1 | identical  | verification/logs/rowflux.log |
| run_growth | OK | 12.5 | 4.8 | identical  | verification/logs/run_growth.log |
| s2a_results | OK | 0.6 | 0.2 | identical  | verification/logs/s2a_results.log |
| scan_an | OK | 2.8 | 1.0 | identical  | verification/logs/scan_an.log |
| scan_summary | OK | 105.1 | 33.3 | identical  | verification/logs/scan_summary.log |
| scan_u_h0.0025 | OK | 148.6 | 48.1 | identical trailing blanks only | verification/logs/scan_u_h0.0025.log |
| scan_u_h0.005 | OK | 43.6 | 13.5 | identical trailing blanks only | verification/logs/scan_u_h0.005.log |
| scan_zm | OK | 0.8 | 0.3 | identical  | verification/logs/scan_zm.log |
| scans | OK | 44.5 | 13.9 | identical  | verification/logs/scans.log |
| seed_amplitude | OK | 0.6 | 0.2 | identical  | verification/logs/seed_amplitude.log |
| slaving_pde_M3 | OK | 0.6 | 0.2 | identical  | verification/logs/slaving_pde_M3.log |
| slaving_pde_m1 | OK | 0.8 | 0.3 | identical  | verification/logs/slaving_pde_m1.log |
| sp_interior | OK | 441.4 | 96.1 | identical  | verification/logs/sp_interior.log |
| static_gen | OK | 3.8 | 1.4 | identical  | verification/logs/static_gen.log |
| strong_codeE | OK | 25.1 | 8.8 | identical  | verification/logs/strong_codeE.log |
| strong_conv | OK | 2.4 | 0.9 | identical  | verification/logs/strong_conv.log |
| strong_fit | OK | 10.8 | 4.1 | identical  | verification/logs/strong_fit.log |
| sym_checks | IMPORTED | 0.0 | 0.0 | identical log imported from verification/imported (missing here: sympy, mpmath); | verification/logs/sym_checks.log |
| t_static_b4 | OK | 120.0 | 38.2 | identical trailing blanks only | verification/logs/t_static_b4.log |
| t_static_b4_proj0 | OK | 116.8 | 38.0 | identical trailing blanks only | verification/logs/t_static_b4_proj0.log |
| t_static_b_a1 | OK | 363.5 | 85.4 | identical  | verification/logs/t_static_b_a1.log |
| t_static_b_a1_M1.5 | OK | 478.5 | 100.4 | identical  | verification/logs/t_static_b_a1_M1.5.log |
| t_static_cy_mode1 | OK | 220.9 | 72.3 | identical trailing blanks only | verification/logs/t_static_cy_mode1.log |
| t_static_cy_mode2 | OK | 244.8 | 76.2 | identical trailing blanks only | verification/logs/t_static_cy_mode2.log |
| t_static_cy_mode3 | OK | 261.1 | 78.1 | identical trailing blanks only | verification/logs/t_static_cy_mode3.log |
| t_static_e | OK | 37.0 | 13.1 | identical trailing blanks only | verification/logs/t_static_e.log |
| t_static_free | OK | 14.5 | 5.4 | identical trailing blanks only | verification/logs/t_static_free.log |
| t_static_free_U3 | OK | 96.8 | 30.7 | identical trailing blanks only | verification/logs/t_static_free_U3.log |
| t_static_h | OK | 7.3 | 2.7 | identical  | verification/logs/t_static_h.log |
| tables | OK | 771.7 | 163.0 | identical  | verification/logs/tables.log |
| tailfit_results | OK | 2.6 | 0.9 | identical  | verification/logs/tailfit_results.log |
| tc_fit | OK | 62.7 | 19.7 | identical trailing blanks only | verification/logs/tc_fit.log |
| tidal_v600 | OK | 2.4 | 0.9 | identical  | verification/logs/tidal_v600.log |
| vaidya_estimate | OK | 4.4 | 1.6 | identical  | verification/logs/vaidya_estimate.log |
| validate_model1 | OK | 47.2 | 14.1 | identical  | verification/logs/validate_model1.log |
| validate_model2 | OK | 47.4 | 14.1 | identical  | verification/logs/validate_model2.log |
| vb1 | OK | 325.4 | 83.7 | identical  | verification/logs/vb1.log |
| vb_B3e-2_B3e-4 | OK | 0.6 | 0.2 | identical  | verification/logs/vb_B3e-2_B3e-4.log |
| vb_law | OK | 0.8 | 0.3 | identical  | verification/logs/vb_law.log |
| vb_prediction | OK | 0.6 | 0.2 | identical  | verification/logs/vb_prediction.log |
| weak_limit | OK | 3.0 | 1.1 | identical  | verification/logs/weak_limit.log |
| width_m1 | OK | 1.6 | 0.6 | identical  | verification/logs/width_m1.log |
