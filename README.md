# The Mass-Tracking Closure in Four-Dimensional Quasi-Topological Gravity

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23455595.svg)](https://doi.org/10.5281/zenodo.23455595)

Gracen Ownby, *The Mass-Tracking Closure in Four-Dimensional Quasi-Topological Gravity: Double-Null Equations, an Exact Generalized-Mass Law and Evolution from Event-Horizon-Regular Data* (Paper F of a seven-paper series on the Hayward regular black hole). 54 pages. License: code MIT, text and data CC-BY-4.0 (`LICENSE.md`). How to cite: `CITATION.cff`.

## Contents

| path | what |
|---|---|
| `main.tex`, `references.bib`, `main.bbl` | LaTeX source (pdflatex, bibtex, pdflatex, pdflatex) |
| `paperF_qtg_dynamics.pdf` | the compiled paper (54 pp) |
| `fig_*.pdf`, `fig_*.png` | figures of the paper |
| `code/` | all code, logs and data; `code/README.md` has the dependency graph, one measured run time per script, the status of the re-runs and the list of logs that have no generator |
| `code/vendor_E/` | `dn2lib.py` and `double_null.c`, copied from the Paper E archive, doi 10.5281/zenodo.23455587 |
| `code/eh_qtg/` | event-horizon-regular data and the constrained evolution (Sections 9-14); `codeb/` (second code), `codee/` (code E), `codec/` (collapse-generated tails), its README lists the modules, data and the status of each claim |
| `archive/paperF_pulse_scan_data/` | tables and run files of the pulse scan and of the strong-pulse study (restored into `code/eh_qtg/codec/` by `restore_archive.sh`) |
| `verify.sh`, `verify.py`, `verification/` | self-verification: re-runs the scripts, re-derives every number quoted in `main.tex`, writes `verification/REPORT.md` (PASS/FAIL table, environment), `expected.json` (quantity, location in the paper, paper value, tolerance and reason, computed value, status), `logs/<script>.log`, `figures/` |
| `requirements.txt` | Python packages (numpy>=2, scipy>=1.11, sympy, mpmath, matplotlib); also needed: gcc, xz |

## Verify

```
bash verify.sh            # = --quick: builds the C libraries, re-runs the affordable computations, re-derives every quoted number from the shipped data (55 CPU-minutes: about 15 min on four free cores; 108 min measured on two shared cores)
bash verify.sh --full     # additionally re-runs the hours-long jobs that make the data (40 more jobs, about 7 CPU-hours that were re-run here plus about 12 hours of data-making runs; `python3 verify.py --list --full` lists each job with its duration, `code/README.md` the measured ones)
```

Needs Python >= 3.10, numpy >= 2, scipy >= 1.11, sympy, mpmath, matplotlib and gcc (`requirements.txt`); no network, no absolute paths, nothing outside this folder (the Paper E modules are vendored in `code/vendor_E/`, doi 10.5281/zenodo.23455587). The script is idempotent; the last line is `RESULT bh-paperF-qtg-dynamics: PASSED n/n checks (quick)` and the exit code is non-zero if any check fails. `PYTHON=python3.12 bash verify.sh` selects the interpreter, `VERIFY_JOBS=4` the number of parallel processes, `python3 verify.py --only <substring>` re-runs single jobs, `--list` shows all jobs. Without scipy the scipy jobs print SKIPPED (and the result is INCOMPLETE, not PASSED); without sympy/mpmath the log of `code/sym_checks.py` imported from `verification/imported/` is used and marked IMPORTED. Results: `verification/REPORT.md`, `verification/expected.json`, one log per script in `verification/logs/`, regenerated figures in `verification/figures/`.

| result in the paper | script (job) | shipped log |
|---|---|---|
| exact identities of Sections 3-8 (compatibility, sigma_uv, static identity, mass law, Hayward pole, action): symbolic, rational and 80-digit checks | `code/sym_checks.py` (sympy), `check_gr_limit.py`, `check_static_identity.py`, `check_compat.py`, `check_psi_identity.py`, `check_mass_law.py`, `eh_qtg/check_compat_pole.py` (mpmath), `eh_qtg/action_check*.py` | `code/*.log`, `code/sym_checks.log` |
| interior characteristic data, singular time v_*(B), bounded h, convergence (Appendix A, Fig. qtg) | `ray_blowup.py`, `run_scan_u.py`, `run_conv.py`, `run_model2.py`, `run_pde_blowup2.py`, `run_growth.py`, `make_figs.py` | `code/ray_blowup.log`, `scan_u_*.log`, `conv_B2e-4*.log`, `model2_h0.02.log`, `pde_blowup_h0.02.log` |
| event-horizon-regular evolution: exponent -kappa_-(m_f), front, delay per decade of B, endpoint tables, mass law, Kretschmann (Sections 9-12, Fig. eh) | `eh_qtg/endpoint_table.py`, `ktable.py`, `hs_extrap.py`, `vb_law.py`, `gpred_q.py`, `curv_hv.py`, `fig_eh.py`, ... (analyses of `data/genq*_*.json`) | `eh_qtg/logs/` |
| error law h_v^p exp(kappa_+ v), delta* = 0.062, blow-up times, slaving, mode comparison, c_3 sensitivity | `eh_qtg/blowup_probe.py`, `err_prof.py`, `blow_trace.py`, `codee/mech_vb.py`, `vb_prediction.py`, `seed_search.py`, `slaving_q.py`, `modecmp.py`, `c3_sensitivity.py` | `code/errprof.log`, `code/blow*.log`, `eh_qtg/codee/logs/`, `eh_qtg/logs/` |
| independent fourth-order code B and code E: comparison, static tests, tidal forces | `eh_qtg/codeb/cmp_*.py`, `t_static_b4.py`, `kstudy.py`, `tidal.py`; `codee/kstudy2.py`, `t_static_e.py` | `eh_qtg/codeb/logs/`, `codee/logs/` |
| collapse tails v^-3 (and v^-2): Table of tails, BCR benchmark and stage-2a tables | `eh_qtg/codec/bcr/tailfit.py` (B_ASYM = 1.5 is the default of `asym1` in `verify.sh`), `s2a_an.py`, `convergence_h.py`, `fit_tables.py`, `np_fit.py`, `nplin_*.py`, `collapse_E.py`, `conv_c.py` | `codec/bcr/*.log`, `codec/logs/` |
| strong pulses: F = B/(8 m_f\|Q_0\|) = 1 - Q_abs/Q_0 in 22 cases (mean 0.05 %, max 0.09 %; ratio 1.0056 +- 0.0003 without the 1/(v-v_s) correction), linearity bound (<= 1.2e-5), row flux (E_scri/m_f <= 8.7e-6), weak limit, fixed-index fits, near-extremal tables | `codec/sp/horizon_ray.py`, `fit_corr.py`, `linbound.py`, `rowflux.py`, `weak_limit.py`, `strong_fit.py`, `charge_row.py`, `eik*.py`, `nearext.py` | `codec/sp/*.log` |
| pulse scan P = 0.01-0.08, horizon map, Vaidya estimate, resolution tests | `codec/pscan_*.py`, `horizon_map.py`, `vaidya_estimate.py`, `sc/` | `codec/sc/*.log` |
| every figure (fig_qtg, fig_eh, fig_collapse, fig_collapse_k2, fig_strong) | `make_figs.py`, `fig_eh.py`, `codec/fig_*.py` | `verification/figures/` |

`code/README.md` lists, for each script, the inputs, the dependency graph, measured run times and what each job reproduces; `verification/REPORT.md` is the authoritative list of checks.

## Provenance

`PROVENANCE.md` states what this repository is (a reorganization of the author's archive, Zenodo v1.0.1), which files differ from the original and why, which files have no original (re-created generators), which logs changed numerically and why, and what was reproduced from the ORIGINAL code.

## Reproduce

```
cd code && bash build.sh && python3 check_gr_limit.py        # interior-data checks (Sections 3-8); bash run_all.sh for all of them
cd eh_qtg && bash setup.sh                                    # builds every library; no other folder is needed
bash codec/restore_archive.sh                                 # unpacks the archived tables and runs
bash run_analysis.sh                                          # re-runs the analysis scripts and compares with the shipped logs (ONLY=<substring> selects)
bash run_eh.sh                                                # the long runs of Sections 9-12
```

## What the paper shows and what it does not

The generalized mass of the quasi-topological theory with the Hayward function obeys d_v m = 8 pi r^2 y phi_v^2 along ingoing rays; for a real scalar and data regular on the event horizon y >= 1/2, so m cannot decrease (the finite-time singularity of interior characteristic data belongs to the branch y < 0). A constrained evolution from event-horizon-regular data, confirmed by an independent fourth-order code, gives a metric exponent -kappa_-(m_f) and a front behind which psi tends to 1/l^2, m grows linearly and the Kretschmann invariant is far above l^-4. The accuracy window of a scheme of order p is limited by an error growing as h_v^p exp(kappa_+ v); its mechanism is derived (the forward integration of the horizon Raychaudhuri equation) with one fitted constant, the threshold delta* = 0.062, and evolving the difference from the exact horizon solution removes it. Collapse-generated horizon tails give v^-3, and v^-2 for data with a nonzero Newman-Penrose constant; for strong pulses the v^-3 coefficient is F 8 m_f |Q| with F = 1 - Q_abs/Q_0, which holds to 0.05% on average in 22 cases. The identification of Q_abs with the horizon term of the time-inverted Newman-Penrose constant of Gajic and Kehrberger is conditional: the hypotheses of their theorem (a metric settling to Schwarzschild at a polynomial rate up to the horizon, Assumption 3.1) were not verified for the collapse data and do not hold for the Hayward exterior, so for Hayward the coefficient 8 m |Q| is a numerical result (1e-4), while for a Schwarzschild exterior it follows from their Theorem 4.1; only the statements of that paper (Sections 1-4), not its proofs, were read. Not established: extendibility at v = infinity, timelike tidal forces, the Hawking back-reaction.

Sources of the equations: arXiv:2509.19016 (Bueno, Cano, Hennigar, Murcia) and arXiv:2602.16773 (Borissova, Carballo-Rubio); see the paper for the level at which each source was read.
