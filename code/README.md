# Code of Paper F

Code, logs and data behind "The Mass-Tracking Closure in Four-Dimensional Quasi-Topological Gravity: Double-Null Equations, an Exact Generalized-Mass Law and Evolution from Event-Horizon-Regular Data" (doi 10.5281/zenodo.23455595). This directory is self-contained: the modules of the Paper E archive that are needed are copied in `vendor_E/` (copied from the Paper E archive, doi 10.5281/zenodo.23455587) and, for the data construction, in `eh_qtg/` (see "Vendored Paper E modules"); no sibling folder is required.

## Requirements

Python >= 3.10, numpy >= 2, scipy >= 1.11, sympy, mpmath, matplotlib (`../requirements.txt`), gcc, and xz (only for `eh_qtg/codec/restore_archive.sh`). `bash ../verify.sh` (see the top-level `README.md`, "Verify") runs everything below, compares the output with the shipped logs and checks every number quoted in `main.tex`. Reference environment of the logs in `../verification/` (all scripts run with real scipy): Python 3.13.16, numpy 2.5.3, scipy 1.18.1, matplotlib 3.11.2, gcc 13.3.0, Linux x86_64, 2 shared cores. `sym_checks.py` needs sympy and mpmath, which that machine did not have and could not install (no network): its log was produced on a second machine (Python 3.10.12, sympy 1.14.0, mpmath 1.3.0) and is shipped as `../verification/imported/sym_checks.log`, marked IMPORTED in the report (`../verification/imported/PROVENANCE.txt`). Earlier versions of the logs of this directory were made with a numpy stand-in for scipy; they have been replaced by logs made with scipy wherever they differed (see "Status of the re-runs").

## Quick start (clean checkout, nothing else needed)

All of it, with comparison and checks: `bash ../verify.sh --quick` (about one CPU-hour, see "Measured run times"), `--full` for the hours-long runs. The individual steps:

```
cd code
bash build.sh                                  # libqtg.so, vendor_E/libdouble_null.so
python3 check_gr_limit.py                      # the checks of Section 4, a fraction of a second each
python3 check_static_identity.py
python3 check_mass_law.py
python3 check_psi_identity.py
python3 check_compat.py
bash run_all.sh                                # all interior-data logs of Sections 3-8 (see "Measured run times"); then: python3 make_figs.py

cd eh_qtg
bash setup.sh                                  # builds every library (also codeb/, codee/, codec/)
bash codec/restore_archive.sh                  # copies the pulse-scan tables and run files of ../../archive into codec/sc, codec/sp
bash run_eh.sh                                 # event-horizon-regular runs of Sections 9-12 (long; the runs are independent)
bash run_analysis.sh                           # analysis logs: re-runs each script and compares with the shipped log
ONLY=endpoint bash run_analysis.sh             # only the entries whose log name contains "endpoint"
RUN_LONG=1 bash run_analysis.sh                # additionally starts the long PDE and collapse runs (output in rerun_logs/long)
```

`run_analysis.sh` writes into `rerun_logs/` (set `OUT=` to change) and never touches the shipped logs; each line reports "same" (identical text) or "differs" (see "Status of the re-runs").

## Dependency graph

```
vendor_E/dn2lib.py, double_null.c ──build.sh──> vendor_E/libdouble_null.so ─┐
qtg_dn.c ───────────────────────────build.sh──> libqtg.so ──────────────────┼──> qtg_lib.py ──> check_*.py, run_qtg_validate.py, ray_blowup.py,
                                                                            │                   run_scan_u.py, run_conv.py, run_model2.py, run_pde_blowup2.py,
                                                                            │                   make_figs.py            (Sections 3-8; run_all.sh)
eh_qtg/setup.sh builds: libdouble_null.so, libstream.so, libstream2.so (Paper E modules in eh_qtg/), codeb/libqtgb.so, codee/libqtge.so, libqtgel.so,
                        codec/libqtgcol.so (includes ../../qtg_dn.c), codec/libqtgL.so
static_gen.py ──> dnU_qtg.py ──> gen_q.py, gen_q2.py ──> data/*.json ──> analyze_q.py ──> late_q, endpoint_q, front_q, kernel_ratio_q, masslaw_q, curv_q, ...
                                      └─ endpoint_table.py, ktable.py, hs_extrap.py, vb_law.py, slaving_pde.py, gpred_q.py, ... (run_analysis.sh, section 1)
codeb/qtg_b.c ──> libqtgb.so ──> gen_b.py ──> codeb/data ──> cmp_AB_final.py, cmp_hs.py, kstudy.py, tidal.py
codee/qtg_e.c, qtg_el.c ──> libqtge.so, libqtgel.so ──> gen_e.py, gen_el.py ──> codee/data ──> kstudy2.py, conv_e*.py, dm_limit.py, seed_amplitude.py, mech_vb.py ──> vb_prediction.py
codec/qtg_col.c (stage N), qtg_L.c (stage L) ──> collapse_lib.py ──> pipeline.py ──> collapse_tail.py ──> data/tail_*.npz (phi_H(v) tables)
        tail tables ──> gen_c.py (needs codee/libqtge.so) ──> runs in ce/, sc/, sp/ ──> collapse_E.py, conv_c.py, pscan_*.py, strong_fit.py, horizon_ray.py, ...
../archive/paperF_pulse_scan_data ──restore_archive.sh──> codec/sc, codec/sp (tables pt_P*.npz, strong tables, genc_*.json runs)
codec/bcr (independent regular-centre code bcr.py) ──> tailfit.py, s2a_an.py, convergence_h.py
eh_qtg/blowup_probe.py, phi_monotone.py: stand-alone generators of vb1.log and of Phi_kernel.npy / logs/phi_monotone.log
```

## Vendored Paper E modules

`vendor_E/` holds `dn2lib.py` and `double_null.c` (the static Hayward interior class `Bg` and its C library), copied from the Paper E archive (G. Ownby, doi 10.5281/zenodo.23455587; MIT licence). The other Paper E modules used by the event-horizon-regular runs (`dnU.py`, `kernel_lib.py`, `transfer*.py`, `stream.c`, `stream2.c`, `raylib.py`, ...) are copies from the same archive and sit in `eh_qtg/`. Nothing outside this repository is needed. The file `eh_qtg/shell_kernel.py` (an inherited exploratory script that imports `ori_model.py`, which is not in this repository) is not used by any result of the paper or by `verify.sh`; it is listed for removal (see the notes of the release).

## Measured run times

Measured by `verify.py` (CPU seconds of each job, user + system, from `os.wait4`; the CPU time does not depend on the load of the machine, the wall time does). Machine: 2 cores shared with other jobs (load average 11-14), Python 3.13, numpy 2.5.3, scipy 1.18.1, `--jobs 2`.

| tier | what | jobs | CPU time | wall time here |
|---|---|---|---|---|
| `--quick` (default) | builds the C libraries (3-5 s), re-runs 162 scripts, evaluates 2170 checks (all PASS) | 162 | 55 min | 108 min (2 workers, shared machine) |
| `--quick` | the same on 4 free cores (default is `min(4, cpus)` workers; estimate, not measured) | | 55 min | about 15 min |
| `--full` | in addition: the jobs below (tier `full` in `verify.py`) | +40 | +about 6.5 CPU-hours for the jobs that were run (marked *), +about 12 hours for the others | |

`--full` jobs (CPU time of the measured ones; the wall times of the others are those printed in the shipped logs):
- re-run during the verification (*): `ray_blowup` (all 12 solves; the solve at B = 0.2 ends with status -1 after 14 min) 14.5 min; `blow1`, `blow2`, `blow3` (`blow_trace.py`) 2.0, 7.6, 31 min; `slaving` 3.4 min; `errprof` 10.3 min; `modecmp` 11 min; `c3_sensitivity` 1.9 min; `linear_q` 1.9 min; `prof2` + `slaving_prof` 1.9 min; `rowflux_direct` 1.5 min; `sp_interior_fine` 1.4 min; `gen_b_B0.03_v330` 1.6 min and `gen_b_B0.0003_v400` 0.4 min (the run files are byte-identical to the shipped ones); `gen_b_v480` (byte-identical to `codeb/data/genb_hs0.05_v480.json`); `gen_b_v600` (12.5 CPU-min, byte-identical to `codeb/data/genb_hs0.05_v600.json`); `seed_search` 15 min; `conv_B2e-4` (five meshes, 13 min wall on the shared machine, the five `.npz` files byte-identical to the shipped ones); `action_check` (6.7 min wall on the shared machine, identical).
- run by `--full`, not re-run here except where stated (expected duration from the wall times in the shipped logs, one core): `g2_hs0.05_v400` (six levels, about 45 min to 80 min per level at the finest), `g2_hs0.025_v400`, `g2_A_v360` (7600 s), `g2_B0.0003_v300`, `g2_B0.03_v300`, `g2_k0.5_v300`, `g2_k3_v300` (re-run completely: 916 CPU-s, run file byte-identical to `data/genq2_hs0.05_m1_B0.003_k3_v300.json`), `g2_M3_v250`, `g2_b_B0.0003_v200` (each 0.7-1 hour), `collapse_P0.01` ... `collapse_P0.08` (about 20 min each, 40 min for the finer meshes), `strong_S5to10`, `strong_S0to10`, `strong_S5to15` (8-11 min), `strong_S5to25` (four meshes, about 1.7 hours).

## Status of the re-runs

A complete `bash ../verify.sh --quick` on the machine above: every regenerated log is identical to the shipped log (155 of 155 comparisons; "identical" means equal up to timing figures, trailing blanks and the last printed digit), 2149 of 2149 checks PASS. Logs that were replaced by regenerated ones during the verification, with the reason:
- scipy instead of the numpy stand-in (last digits): `codec/logs/np_fit.log` (a0 of the window 3200: 1.00000 -> 0.99997), `codec/logs/fit_tables.log` (early window B = 887.891 -> 887.896; the free fit in that window is ill conditioned), `codec/logs/interior.log`, `ascale.log`, `codec/sp/rowflux.log`.
- extension or format only (the numbers of the original log are unchanged; the regenerated log has more rows/columns/lines or different file prefixes): `logs/endpoint_B0.003_merged.log` (header line), `endpoint_B0.03.log` (column dm/dv(closed)), `rho_check.log` (second table), `slaving_pde_m1.log`, `gpred_final.log` (more rows), `codec/sp/rowflux_direct.log` and `runsh_narrow.log` (clean lines without file prefix), `vb1.log` (label of the mesh), `logs/late_m2_*.log` (a stray source line), `codeb/logs/kstudy_v600.log` (one more row, v = 380), `codec/logs/collapse_E_k2.log` (the original file is two scripts concatenated; the ray-2 numbers are identical), `codec/sc/conv_P0.08_hv.log` and `codec/sp/strong_codeE.log` (added lines).
- numerically different from the log of the first release; the ORIGINAL script, run on the ORIGINAL data, reproduces the regenerated log and not the old one (the old log was a stale output of an earlier version of the script or data; PROVENANCE.md has the evidence): `codec/conv_c.log` (largest change of ln m 3.6e-5 and of ln K at v = 1400 1.2e-4, against 2.1e-5 and 1.1e-4 in the old log; the manuscript was corrected), `codeb/logs/t_static_b4_proj0.log` (errors 25-88 % different, the order 4.00 is the same; not round-off), `codec/sp/charge_row.log` (the first row, the weak pulse m_f = 5.01, differs because the old log was run with the default STRONG_DR = 0.1, the others with -0.3; the 17 + 6 rows of the regenerated log are now run with STRONG_DR = -0.3 and the pulse arguments of each table family, 4 12 20 / 4 8 20 / 4 20 28), `logs/ktable.log` (three entries, because `ktable.py` now reads `endpoint_B0.003_merged.log`), `codee/logs/seed_search.log` (the script `seed_search.py` is a re-creation; the entry for EPS = 3.55e-15 at v = 780 differs in the fourth digit).
- last digits only (scipy against numpy): `codec/logs/interior.log`, `codec/sp/rowflux.log`, `logs/t_static_b_a1.log` (round-off column).
- `codec/bcr/tailfit_results.log` is unchanged, but `tailfit.py base` used the asymmetric pulse when B_ASYM = 1.5 was exported for the second run; `tailfit.py` now sets the asymmetry from its argument (`base`: symmetric; `asym1`: B_ASYM, default 1.5). `codeb/logs/tidal_v600.log` is unchanged; the command is `tidal.py ... 0.0125 380 ...` (trust window v <= 380).
- new generator, built from functions of the original modules: `codec/ascale_q.py` with `codec/logs/ascale_q.log` (B/(8m|Q|) for A/A0 = 0.8 ... 1.2 and the charge of the exterior part of the row v = 60, quoted in Sec. 'Collapse-generated horizon tails'; reproduces `linear_q.log` at A/A0 = 0.8, 1.0, 1.2).
- logs that did not exist: `run_growth.log`, `conv_B2e-4_coarse.log`, `codec/sp/nearext_quick.log`, `codec/logs/{k2_extra,overlap_h,sp_interior,sp_interior_fine,t_static_h}.log`, `logs/curv_hv_merged.log`, and `verification/logs/` (one log per script).
Quantities that depend on the library (scipy 1.18 against the stand-in) and were reported with more digits than they are stable: the free-fit amplitude B in the window [600, 1200] of `fit_tables.log` (887.891 / 887.896, ill-conditioned; the manuscript quotes it to 3 digits), `np_fit.log` a0.

## Logs without a shipped generator

Re-created generators: the scripts `eh_qtg/blow_trace.py`, `blowup_probe.py`, `err_prof.py`, `prof2.py`, `phi_monotone.py`, `codee/seed_search.py`, `codec/eik_summary.py`, `codec/nplin_rows.py`, `codec/k2_extra.py`, `codec/strong_k1500.py`, `codec/bcr/convergence_h.py` and `sym_checks.py` are not in the original archive (it has the logs, not these scripts); the logs that they replace are the logs of the first release (`blow1-3.log`, `vb1.log`, `errprof.log`, `slaving_prof.log`, `seed_search.log`, `eik_summary.log`, `nplin.log`, `convergence_h.log`). Of these, `blow_trace.py` was run again for `blow1.log` and reproduces it line by line; `phi_monotone.log`, `k2_extra.log` and the K(1500) block of `strong_codeE.log` have no log in the first release. `verification/imported/sym_checks.log` was produced on another machine (sympy, mpmath) and is imported, not re-run, here. See `../PROVENANCE.md`.

Every number, table and "verified" statement of `main.tex` has a generator script, an input (shipped or produced by a shipped `--full` job) and a saved output; `../verification/REPORT.md` lists them. The generators that were scratch scripts before the verification pass are now shipped: `eh_qtg/err_prof.py` (`errprof.log`), `eh_qtg/prof2.py` (writes `prof2_U.npy`, `prof2_snap.npy`, read by `slaving_prof.py`), `eh_qtg/blow_trace.py` (`blow1.log`-`blow3.log`), `eh_qtg/codee/seed_search.py`, `eh_qtg/slaving_q.py`, `modecmp.py`, `c3_sensitivity.py`, `eh_qtg/codec/linear_q.py`, `eh_qtg/codec/nearext.py`, `phi_monotone.py` (writes `Phi_kernel.npy`), `codee/first_nonfinite.py`, and the code-B inputs `codeb/data/genb_p1_hs0.05_m1_B0.03_k1.5_v330.json`, `genb_p1_hs0.05_m1_B0.0003_k1.5_v400.json` (regenerated by the `--full` jobs `gen_b_B0.03_v330`, `gen_b_B0.0003_v400`) and the table `tc_E_m0_5.npz` (now in `../archive/paperF_pulse_scan_data/strong/`, restored by `codec/restore_archive.sh`). Remaining exceptions:
- `eh_qtg/codee/logs/noise_tests.log` is a hand-written summary of runs of `eh_qtg/codee/noise_tests.py` (usage `PROW/PCOL/PERT python3 noise_tests.py v1 hs hv stride out.npz`); nothing in it is quoted numerically in the paper.
- `run_growth.log` (the growth of the difference of two runs, `run_growth.py 0.02 56 2e-3`) is reproduced by `verify.sh` but not quoted in the paper.
- `eh_qtg/codec/logs/collapse_E_k2.log` is the concatenation of `an_k.py` runs (job `collapse_E_k2` of `verify.py` has the exact loop).

## Fitted and heuristic quantities

The threshold delta* = 0.062 of the error law is fitted to the five failure times of code B at B = 3e-3 (`eh_qtg/codee/mech_vb.py`, `vb_prediction.py`); the constant 205.25 and the coefficient of the earlier fit in `vb_law.py` are fits; the bounds "2-4 %" for the a priori estimates of the absorbed charge (`eik_test.py`, `eik2.py`) are the observed errors in 22 cases, not bounds; the ranges quoted from `codec/bcr/tailfit.py` are fit results over the window 100 <= t <= 300.
