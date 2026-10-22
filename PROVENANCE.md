# PROVENANCE: bh-paperF-qtg-dynamics

## 0 Baselines used in this file

Three states are compared: (1) the author's tree `old_archive/1_sources/sources/<paper>`; (2) the first Zenodo release (the initial git commit of this repository); (3) the current repository. On 2026-10-21 (1) and (2) were compared byte for byte: they are identical except for the repository metadata (`.gitignore`, `.zenodo.json`, `CITATION.cff`), the compiled PDF and `archive/` (the Paper F scan data, `3_archive_paperF_scan_data` in the old archive). The rest of the old archive (`old_archive/2_docs_and_archive_1/archive/`: earlier manuscript versions, session logs, audit directories) was searched for code and data behind this paper's results; files found there that are not in the Zenodo release are listed below where they matter. Wherever this file says "original" or "v1.0.1" it means (1) = (2).

## 1. Lineage

This repository is a reorganization of the author's archive of Paper F ("QTG dynamics, Hayward double-null"; Zenodo v1.0.1, 577 files). It adds `verify.sh`, `verify.py`, `verification/`, README files, `LICENSE.md`, `requirements.txt`, regenerated logs, `code/vendor_E/` (byte-identical copies of the Paper E modules `dn2lib.py` and `double_null.c`), the archived tables (`archive/paperF_pulse_scan_data/`, 59 files) and a number of scripts that were not in the archive (section 3).

Audit (2026-10, by Claude, read-only on both trees, comparison by md5 and by running the ORIGINAL scripts on a scratch copy): of the 577 original files 503 are byte-identical here, 66 differ (37 source files, 29 logs), 4 are LaTeX build products that were dropped (`main.aux`, `main.blg`, `main.log`, `main.out`). 94 files are new outside the infrastructure. No C file (`qtg_dn.c`, `qtg_b.c`, `qtg_e.c`, `qtg_el.c`, `qtg_col.c`, `qtg_L.c`, `stream*.c`) differs. `shell_kernel.py` is the author's file; it imports `ori_model.py`, which is not in the archive, and nothing uses it.

## 2. Files that differ from the original

Class (a): paths, environment variables, comments, arguments. (b): bug fix. (c): output can differ (here only additive).

| path (under `code/`) | class | what changed | evidence |
|---|---|---|---|
| `qtg_lib.py` | a | `sys.path` line: `../../paperE_inner_horizon/code/nonlinear` -> `vendor_E` | RAN old and new `build()`+`run()`, models 0 and 1, h = 0.08 and 0.04: result arrays bitwise equal (md5 and `np.array_equal`); `libqtg.so` binary-identical |
| `check_gr_limit.py`, `run_all.sh`, `make_figs.py` (`FIG_OUT`) | a | docstring, paths, comments | read |
| `ray_blowup.py` | a | additive mode `sub` (the 11 solves without B = 2e-1, which takes about an hour); `__main__` unchanged | `verification/logs/ray_blowup_sub.log` = the 11 corresponding lines of the original `ray_blowup.log` (read) |
| `eh_qtg/c3_sens_m1.py`, `c3_sensitivity.py`, `curv_hv.py`, `fig_eh.py`, `setup.sh`, `run_eh.sh` | a | tempfile directory; a hard-coded `/mnt/user-data/...` path; `FIG_OUT`; build lines | read |
| `eh_qtg/codeb/gen_b.py`, `codee/gen_e.py`, `codee/gen_el.py`, `codec/gen_c.py` | a | ctypes library path relative to the script (`gen_c.py`: `../codee/libqtge.so`, the original expected `codec/libqtge.so`, which nothing builds) | read; the C sources are identical |
| `eh_qtg/codec/fig_collapse.py`, `fig_collapse_k2.py`, `fig_strong.py`, `codec/run_all.sh`, `codec/sc/runh.sh`, `runq.sh`, `runs.sh`, `codec/sp/runconv.sh`, `rune.sh`, `rune_b.sh`, `rune_c.sh`, `runeik.sh`, `runeik2.sh`, `runhr.sh`, `runsh.sh`, `runst.sh`, `runst2.sh`, `runtc.sh` | a | absolute scratch paths (`/mnt/user-data/...`, `/tmp/claude-0/.../scratchpad/...`) replaced by relative ones; logs to `${LOGDIR:-.}`; `FIG_OUT` | read |
| `eh_qtg/codec/bcr/tailfit.py` | b | sets `B_ASYM` ('0' for tag `base`, else 1.5) before `import bcr`; the original depended on an exported variable (without it `asym1` prints the wrong X1: c/X1 = 1.134 instead of 1.026) | RAN old and new `tailfit.py base` / `asym1` (old with the variable exported as in the run that made the log): stdout identical; equals `bcr/tailfit_results.log` (8 lines) |
| `eh_qtg/codeb/kstudy.py` | c (additive) | `range(100,361,20)` -> `range(100,381,20)`: one more row, v = 380 (slope 2.45, K = 2.2665e28) | RAN original on `codeb/data/genb_hs0.05_v600.json 0.0125` reproduces the original `kstudy_v600.log` exactly; the new log differs only by the v = 380 row |
| `eh_qtg/ktable.py` | c | input `endpoint_B0.003.log` -> `endpoint_B0.003_merged.log` (identical except its header, and it has the rows v = 250 and 290 that the original manuscript Table k already quoted) | RAN: old script on old logs = old `ktable.log`; new script on merged log = new `ktable.log` (3 entries differ) |
| `eh_qtg/README.md`, `README.md` | docs | see section 4 for wording corrected in this release | |

No file was restored: every difference above either is needed to run outside the author's scratch machine or is additive.

## 3. Files without an original

| path | generates | basis | quoted numbers that depend on it |
|---|---|---|---|
| `archive/paperF_pulse_scan_data/**` (59 files) | archived tables of the pulse scan, strong tables, code-E runs | no original in the archive | everything in Tables strong, qabs, pscan; basis: the ORIGINAL `strong_table.py` regenerates `t_m5_mt5.5.npz` and `t_m0_mt10.npz` bit-identically (sec. 5); the other tables were not regenerated individually but reproduce `horizon_ray.log` |
| `eh_qtg/blow_trace.py` | `blow1-3.log` | re-created (not in the archive) | singular times of code B; `blow1.log` re-run: equal to the original line by line; blow2, blow3 not re-run |
| `eh_qtg/blowup_probe.py`, `err_prof.py`, `prof2.py` | `vb1.log`, `errprof.log`, `slaving_prof.log` | re-created; job `vb1` identical to the original; `errprof`, `slaving_prof` not re-run by the audit | error law, slaving profile |
| `eh_qtg/phi_monotone.py` | `phi_monotone.log`, `Phi_kernel.npy` | re-created, no earlier log | monotonicity statement of the kernel |
| `eh_qtg/codee/seed_search.py` | `seed_search.log` | re-created; primary entries identical, one line differs in the 4th digit | seed of the late-time departure |
| `eh_qtg/codec/eik_summary.py`, `nplin_rows.py`, `bcr/convergence_h.py` | `eik_summary.log`, `nplin.log`, `convergence_h.log` | re-created; regenerated output identical to the original logs | a priori error statistics of Q_abs; h-convergence of the BCR code |
| `eh_qtg/codec/k2_extra.py`, `strong_k1500.py` | `k2_extra.log`; the K(1500) block of `strong_codeE.log` | re-created, the K(1500) numbers (8.977e25, 8.372e25, ratio 1.072) were quoted in the original manuscript but not in the original log | k = 2 extra rows; K(1500) ratio |
| `eh_qtg/codec/ascale_q.py` | `logs/ascale_q.log` | NEW in this release, built from functions of the original `pipeline.py`, `collapse_lib.py`, `runL.py` and the conventions of `linear_q.py`; reproduces `linear_q.log` (Q = -1.49525, -1.70606, -1.81036) | B/(8m\|Q\|) = 0.430, 0.403, 0.373, 0.336, 0.294; row charges -0.27, -0.37, -0.43, -0.39, -0.33 and ratios 2.4, 1.8, 1.5, 1.5, 1.6 (none of these was in a log before) |
| `sym_checks.py`, `verification/imported/sym_checks.log` | exact/multi-precision checks of the algebra of Secs. 2, 4, 5, 7 | the log was produced on another machine (sympy 1.14, mpmath 1.3, Python 3.10) and is imported, not re-run here (sympy, mpmath absent in the audit environment) | r_-, r_+, kappa, Q(1/r_-^2) = -1.5048, mass-law identities |
| `run_analysis.sh`, `restore_archive.sh`, `build.sh` | infrastructure | | |

## 4. Results that changed relative to the original

Logs for which the regenerated number differs from the original log (details: `code/README.md`, "Status of the re-runs"). In each case the ORIGINAL script on the ORIGINAL data reproduces the regenerated log, so the original log was a stale output.

| log | difference | manuscript |
|---|---|---|
| `codec/conv_c.log` | ln m change up to 3.6e-5 (rays 0 and 3, v = 1400), ln K(1400) up to 1.2e-4 (ray 1); original log 2.1e-5 and 1.1e-4 | the sentence "2e-5 in ln m ... <= 1.1e-4 on all four rays" was wrong; now "(1-4)e-5 in ln m (at most 3.6e-5) ... <= 1.2e-4"; checks `convc_dlnm`, `convc_dlnK1400` now test all rays and v with the exact values |
| `codeb/logs/t_static_b4_proj0.log` | errors 25-88 % different, order 4.00 unchanged | only "order 4.00" is quoted. The earlier README called this "round-off level"; that was wrong |
| `codec/sp/charge_row.log` | row 1 (`t_m5_mt5.01`): Q_S -0.0306 -> -0.0314, F_pred 0.9796 -> 0.9969: the original ran with the default STRONG_DR = 0.1, which does not cover the horizon of a weak pulse; `horizon_ray` uses -0.3. The previous regeneration additionally gave the six `sh_*` rows the pulse arguments `4 12 20` (they need `4 8 20` / `4 20 28`), which changed them by up to 62 %; the original log had them right | not quoted numerically (F_meas column unaffected, used by checks `width_F_*`). `verify.py` now runs the three table families with their own arguments; the regenerated log equals the original in 22 of 23 rows and differs in row 1 by STRONG_DR only (RAN both) |
| `logs/ktable.log` | 3 entries (v = 250, 270, 290, k = 3/2, B = 3e-3) | `ktable.py` input changed (section 2) |
| `codec/logs/np_fit.log`, `fit_tables.log` | a0 1.00000 -> 0.99997; early-window B 887.891 -> 887.896 (ill-conditioned) | quoted values (25.2613, 25.4474, k = 3.009) unchanged |
| `codee/logs/seed_search.log` | EPS = 3.55e-15 entry at v = 780: -3.29359 vs -3.29144 | not quoted at that digit |

Manuscript numbers changed in this release (each backed by a check): conv_c sentence (above); Table qabs rows "width 4s/16s" are labeled Einstein (they are model 0 tables, the caption says "Hayward unless stated"); the width sentence says Einstein and gives the Hayward 8s values (0.3713, 0.6451) next to the Einstein ones (0.3704, 0.6441); the row charge for A/A0 = 1 is -0.43 (was -0.44; the script gives -0.4347). The twelve earlier numerical corrections of the collapse section (9.914 -> 9.915, 0.3% -> 0.6%, 4.4e-5 -> 5.3e-5, ...) are the "proposed correction" entries of `verification/checks.py`.

## 5. What reproduces from the ORIGINAL code

All run on a scratch copy of the original tree, `nice -n 10`, scipy 1.18.1, numpy 2.5.3.

| run | time | result |
|---|---|---|
| `horizon_ray.py` (STRONG_DR = -0.3; `4 12 20` for the 17 `t*/t0*` tables, `4 8 20` narrow, `4 20 28` wide) on the archived tables | 22.6 s | `horizon_ray.log` reproduced exactly: Table qabs and the 22 cases (ratio 1.0052-1.0060) |
| `strong_fit.py` on 17 tables; `fit_corr.py` | seconds | `strong_fit.log` (Table strong, F = 0.645, 0.501, 0.474, 0.371) and `fit_corr.log` (F_corr/F_abs = 0.9995 +- 0.0002) reproduced |
| `strong_table.py 1 5 5.5 0.1 0.1 2900`; `strong_table.py 1 0 10 0.1 0.1 2900` | 46 s; 55 s | `t_m5_mt5.5.npz`, `t_m0_mt10.npz` identical in every array to the archived tables; Q = -6.823651832540591, A = 0.030030032254932823, B = 202.682, F = 0.3713 |
| `fit_tables.py` | about 2 min | B = 25.2613, 25.4474, k = 3.009, 23.79, 23.23 = manuscript; equals the regenerated log |
| `np_fit.py` | 11.7 s | a0 = 0.99997 (regenerated log) |
| `conv_c.py` on the original data | 2 s | equals the regenerated `conv_c.log` |
| `t_static_b4.py` with PROJ=0 | 84 s | equals the regenerated `t_static_b4_proj0.log` |
| `kstudy.py`, `ktable.py`, `tailfit.py base/asym1`, `charge_row.py` | seconds | sections 2 and 4 |
| `blow_trace.py 0.003 300 0.025` (re-created script) | about 4 min | equals the original `blow1.log` line by line (first non-finite v = 233.575 at h = 0.025) |
| `qtg_lib` old vs new | seconds | bitwise equal |
| `verify.py --only charge_row,ascale_q,conv_c,conv_c_k2,ascale`, then `--checks-only` | about 2 min | all jobs identical to the shipped logs; 2170 of 2170 checks PASS |

## 6. Known limits

- `verify.py` compares a regenerated log with the shipped one to 1.5 units of the last printed digit (timings and warnings masked); only `interior` (atol 1e-13), `fit_tables` (rtol 1e-5), `ascale` (rtol 1e-6) have an explicit extra tolerance. The figure checks compare the pixel size of the PNG files, not their content.
- 99 of the first 2149 checks (and a few of the 21 added in this release) have a tolerance wider than the rounding of the quoted number (see `verification/expected.json`, field `tol`). The widest: `bcr_X2_off` (paper "100 %", computed 95.07, tol 10), `scan_dmdv_below_m10` (22 %), `overlap_19.895` (12 %), `cmp_add_range_min/max` (4-6 %), `hm_P09_r145`, `hm_m70`, `rb_lambda`, `bcr_hold_all` (3.5-4 %).
- Quick mode does not regenerate the hours-long jobs. The README says several of them (`ray_blowup` with B = 2e-1, `blow1-3`, `errprof`, `modecmp`, `c3_sensitivity`, `seed_search`, `conv_B2e-4`, `g2_*`, `linear_q`) were re-run on the author's machine; their checks read the shipped logs. The audit did not re-run them (except `blow1`).
- Not re-run by the audit: the pulse-scan jobs `codec/sc/*` (Table pscan), the Table pscan logs themselves, the 15 other archived strong tables individually, the BCR runs (the log is identical to the original and was checked against the manuscript by reading), `sym_checks`.
- The values of Table qabs "(Einstein, width ...)" and of the width sentence come from `sh_narrow`/`sh_wide` tables with model 0; the width-16s table at mu = 0 (`sh_wide_m0_0_10`) does not contain the event horizon at v_1 (r = 25 > r_+ = 20), so Eq. (Fabs) cannot be evaluated there; its F_meas = 0.3842 is the fixed-index fit printed in `charge_row.log`.
- `ascale_q.log` is a regeneration with a new script; its row-charge values agree with the manuscript to the rounding printed (the third differs by 0.005 and was corrected).
