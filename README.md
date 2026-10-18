# Paper F — The mass-tracking closure in four-dimensional quasi-topological gravity

Drafted 2026-10-10, revised 2026-10-11 (event-horizon-regular data, constrained evolution, Hayward and bounded results). `main.tex` / `main.pdf` (37 pp); `references.bib`; `fig_qtg.pdf|png` (interior-data figure), `fig_eh.pdf|png` (event-horizon-regular runs).
`code/` — interior-data runs and checks (Sections 3-8): `bash code/run_all.sh` (about 30 min on 2 cores; needs gcc, numpy, scipy, matplotlib; imports the static Hayward interior `Bg` from `../paperE_inner_horizon/code/nonlinear`, so build that library first, see its README); then `python3 make_figs.py`.
`code/eh_qtg/` — event-horizon-regular data and the constrained evolution (Sections 9-12): `bash code/eh_qtg/setup.sh && bash code/eh_qtg/run_eh.sh` (about 90 min on one core); README there lists the modules, data and logs and the status of each claim.
Logs shipped: check_*.log, validate_model{1,2}.log, ray_blowup.log (+json), scan_u_h*.log, conv_B2e-4.log (+ npz), model2_h0.02.log, pde_blowup_h0.02.log (interior-data runs); `code/eh_qtg/logs/*.log` (event-horizon-regular runs).
Sources of the equations: arXiv:2509.19016 Eqs. (36)-(38), (51) (Bueno-Cano-Hennigar-Murcia); static Hayward identification arXiv:2602.16773 (Borissova-Carballo-Rubio).
Main results: Proposition 1 (y >= 1/2 for data regular on the event horizon => generalized mass non-decreasing; the interior-data singularity is a data artefact); constrained evolution (free evolution fails by v~60 on exact static data); flux = Paper G kernel + O(B^2); metric exponent -kappa_-(m_f); front, then psi -> 1/l^2 with m growing linearly; curvature >> l^-4 behind the front. Not decided: the endpoint beyond v~170.

Update 2026-10-12 (later): mechanism of the numerical window law, code E (`code/eh_qtg/codee/`), K to v=650, scans over k, B and m (Sec. 'Why the window closes ...').
