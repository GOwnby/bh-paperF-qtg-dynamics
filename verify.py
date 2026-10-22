#!/usr/bin/env python3
"""Self-verification of the repository of Paper F (bh-paperF-qtg-dynamics).

usage:  python3 verify.py [--quick|--full] [--jobs N] [--only SUBSTR] [--checks-only] [--list]
        (normally started through  bash verify.sh [--quick|--full])

What it does
  1. builds the C libraries (code/build.sh, code/eh_qtg/setup.sh) and unpacks the archived tables (codec/restore_archive.sh);
  2. runs every generator script listed in JOBS below (stdout -> verification/logs/<job>.log, stderr -> <job>.err when not empty);
     --quick: everything that re-derives the numbers of the paper from the shipped data and the short PDE runs;
     --full : additionally the hours-long runs that produce that data (see the list at the end of JOBS for the expected durations);
  3. compares each regenerated log with the log shipped in the repository (numbers: agreement to 1.5 units of the last printed digit);
  4. evaluates every entry of verification/checks.py: a number of the manuscript, its location, the tolerance and the reason for it,
     the value recomputed from the regenerated logs, and PASS/FAIL;
  5. writes verification/REPORT.md, verification/expected.json (all checks) and verification/jobs.json (timings), prints the final line

        RESULT bh-paperF-qtg-dynamics: PASSED n/n checks (quick)

Exit code: 0 if every check passed, 1 if a check or a job failed, 3 if checks were skipped because a Python package is missing.
Needs Python >= 3.10, numpy >= 2, scipy >= 1.11, sympy, mpmath, matplotlib, gcc.  No network, no absolute paths, no git.
"""
import os, sys, re, json, time, shutil, argparse, platform, subprocess, datetime, importlib, math, threading
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = 'bh-paperF-qtg-dynamics'
CODE = os.path.join(ROOT, 'code')
EH = os.path.join(CODE, 'eh_qtg')
VER = os.path.join(ROOT, 'verification')
LOGS = os.path.join(VER, 'logs')
PY = os.environ.get('PYTHON') or sys.executable or 'python3'


# --------------------------------------------------------------------------------------------------------------------------------------
# JOBS.  J(id, cwd, command, ref=<shipped log to compare with>, tier='quick'|'full', needs=(packages), stage=<0 first ... 9 last>, est=<seconds, one core>)
#   cwd and ref are relative to the repository root; the command is run by bash with  $PY  = the Python interpreter; stdout is the log.
# --------------------------------------------------------------------------------------------------------------------------------------
JOBS = []
try:                                   # CPU seconds measured in the reference run (real scipy, Linux); used for the estimates and the scheduling order only
    MEASURED = json.load(open(os.path.join(VER, 'cpu_times.json')))
except Exception:
    MEASURED = {}


def J(id, cwd, cmd, ref=None, tier='quick', needs=(), stage=1, est=10, cmp='num', note='', work=False, atol=0.0, rtol=0.0, why=''):
    """work=True: run in verification/work/<id> (scripts that write side files); PYTHONPATH still contains code/ and code/eh_qtg/"""
    est = max(2, int(round(MEASURED[id] * 1.15))) if id in MEASURED else est
    JOBS.append(dict(id=id, cwd=('verification/work/' + id) if work else cwd, cmd=cmd, ref=ref, tier=tier, needs=tuple(needs), stage=stage, est=est, cmp=cmp, note=note, work=work, atol=atol, rtol=rtol, why=why))


C = 'code'
E = 'code/eh_qtg'
B_ = 'code/eh_qtg/codeb'
EE = 'code/eh_qtg/codee'
CC = 'code/eh_qtg/codec'
SP = 'code/eh_qtg/codec/sp'
SC = 'code/eh_qtg/codec/sc'
BCR = 'code/eh_qtg/codec/bcr'
G = 'genq2_hs0.05_m1'

# ---- stage 0: build (done by build_step(), not a job) ------------------------------------------------------------------------------------

# ---- A. Sections 3-8: equations, checks, interior data (code/) ------------------------------------------------------------------------
for s in ('check_gr_limit', 'check_static_identity', 'check_compat', 'check_psi_identity', 'check_mass_law'):
    J(s, C, f'$PY {s}.py', ref=f'{C}/{s}.log', needs=('scipy',), est=2)
J('validate_model1', C, 'MODEL=1 L2=1.0 VMAX2=55.2 $PY ../../../code/run_qtg_validate.py', ref=f'{C}/validate_model1.log', needs=('scipy',), est=15, work=True)   # writes validate_model1.json into its work directory
J('validate_model2', C, 'MODEL=2 L2=1.0 MASS=1.0 VMAX2=60 $PY ../../../code/run_qtg_validate.py', ref=f'{C}/validate_model2.log', needs=('scipy',), est=15, work=True)
J('ray_blowup', C, '$PY ../../../code/ray_blowup.py', ref=f'{C}/ray_blowup.log', tier='full', needs=('scipy',), est=3600, work=True,
  note='all 12 solves; the one at B = 0.2 (status -1: DOP853 gives up at the singularity with atol = 1e-300) takes about 14 CPU-minutes; writes ray_blowup.json into its work directory')
J('ray_blowup_sub', C, '$PY ../../../code/ray_blowup.py sub', needs=('scipy',), est=40, work=True,
  note='the 11 solves of ray_blowup.py other than B = 0.2 (about 17 CPU-s); compared with the shipped ray_blowup.log by the check ray_sub_lines')
J('scan_u_h0.005', C, '$PY run_scan_u.py 0.005 66 2e-4', ref=f'{C}/scan_u_h0.005.log', needs=('numpy', 'scipy'), est=10)
J('scan_u_h0.0025', C, '$PY run_scan_u.py 0.0025 66 2e-4', ref=f'{C}/scan_u_h0.0025.log', needs=('numpy', 'scipy'), est=40)
J('conv_B2e-4_coarse', C, 'for h in 0.01 0.005 0.0025; do $PY ../../../code/run_conv.py $h 70 2e-4 B2e-4; done; for f in conv_B2e-4_h*.npz; do if cmp -s $f ../../../code/$f; then echo "$f: byte-identical to the shipped copy" >&2; else echo "$f: DIFFERS from the shipped copy" >&2; fi; done', ref=f'{C}/conv_B2e-4_coarse.log', needs=('numpy', 'scipy'), est=40, work=True)   # the three coarse meshes of Table conv; writes conv_*.npz into its work directory
J('conv_B2e-4', C, 'for h in 0.01 0.005 0.0025 0.00125 0.000625; do $PY ../../../code/run_conv.py $h 70 2e-4 B2e-4; done', ref=f'{C}/conv_B2e-4.log', tier='full', needs=('numpy', 'scipy'), est=600, work=True)   # all five meshes (the two finest take 73 s and 288 s on a free core)
J('model2_h0.02', C, '$PY run_model2.py 0.02 76 2e-3 0.02 1.0', ref=f'{C}/model2_h0.02.log', needs=('numpy', 'scipy'), est=60)
J('pde_blowup_h0.02', C, '$PY run_pde_blowup2.py 0.02 56.5 0.02 0.002', ref=f'{C}/pde_blowup_h0.02.log', needs=('numpy', 'scipy'), est=60)
J('run_growth', C, '$PY run_growth.py 0.02 56 2e-3', ref=f'{C}/run_growth.log', needs=('numpy', 'scipy'), est=10, note='growth of the difference between the runs with B = 0.002 and B = 0 (model 1, h = 0.02); not quoted numerically in the manuscript, shipped as a record of the calculation behind the discussion of Appendix A')

# ---- B. exact arithmetic (sympy / mpmath / rational): the claims "verified symbolically / exactly" ----------------------------------------
J('sym_checks', C, '$PY sym_checks.py', ref=f'{C}/sym_checks.log', needs=('sympy', 'mpmath'), est=20, cmp='text')
J('check_compat_pole', E, '$PY check_compat_pole.py', ref=f'{E}/logs/check_compat_pole.log', est=5)
J('lift_check_4d', E, 'for s in 0 1 2 3 4; do echo "seed $s"; $PY lift_check_4d.py $s; done', ref=f'{E}/logs/lift_check_4d.log', est=10)
J('static_gen', E, '$PY static_gen.py', ref=f'{E}/logs/static_gen.log', needs=('scipy',), est=2)
J('check_curv_static', E, '$PY check_curv_static.py', ref=f'{E}/logs/check_curv_static.log', needs=('scipy',), est=2)
J('action_check2', E, '$PY action_check2.py 6', ref=f'{E}/logs/action_check2.log', est=120, cmp='num')
J('action_check3', E, '$PY action_check3.py 4', ref=f'{E}/logs/action_check3.log', est=120, cmp='num')
J('action_check', E, '$PY action_check.py 10', ref=f'{E}/logs/action_check.log', tier='full', est=600, cmp='num')

# ---- C. anisotropic constrained runs, Sections 10-11 (inputs: data/genq2_*.json; the command is that of the shipped log) ----------------
EP = ('scipy',)
J('endpoint_B0.0003', E + '/data', f'VB_LAW=1 $PY ../endpoint_table.py {G}_B0.0003_k1.5_v300.json 0.0003 1.5 0.795649', ref=f'{E}/logs/endpoint_B0.0003.log', needs=EP, est=60)
J('endpoint_B0.003', E + '/data', f'VB_LAW=1 $PY ../endpoint_table.py {G}_B0.003_k1.5_v400.json 0.003 1.5 0.795653', ref=f'{E}/logs/endpoint_B0.003.log', needs=EP, est=60)
J('endpoint_B0.003_merged', E + '/data', f'VB_LAW=1 $PY ../endpoint_table.py {G}_B0.003_k1.5_merged.json 0.003 1.5 0.795653', ref=f'{E}/logs/endpoint_B0.003_merged.log', needs=EP, est=60)
J('endpoint_B0.03', E + '/data', f'VB_LAW=1 $PY ../endpoint_table.py {G}_B0.03_k1.5_v300.json 0.03 1.5 0.796066', ref=f'{E}/logs/endpoint_B0.03.log', needs=EP, est=60)
J('endpoint_k0.5', E + '/data', f'$PY ../endpoint_table.py {G}_B0.003_k0.5_v300.json 0.003 0.5 0.7957', ref=f'{E}/logs/endpoint_k0.5.log', needs=EP, est=40)
J('endpoint_k3', E + '/data', f'VB_LAW=1 $PY ../endpoint_table.py {G}_B0.003_k3_v300.json 0.003 3 0.79565', ref=f'{E}/logs/endpoint_k3.log', needs=EP, est=40)
J('ktable', 'verification/logs', '$PY ../../code/eh_qtg/ktable.py', ref=f'{E}/logs/ktable.log', est=2, stage=2)   # reads the regenerated endpoint_*.log
J('hs_extrap', E + '/data', f'$PY ../hs_extrap.py {G}_B0.003_k1.5_v400.json genq2_hs0.025_m1_B0.003_k1.5_v400.json 0.003 1.5 0.795653', ref=f'{E}/logs/hs_extrap.log', needs=EP, est=60)
J('vb_law', E + '/data', f'$PY ../vb_law.py {G}_B0.003_k1.5_v400.json {G}_B0.03_k1.5_v300.json {G}_B0.0003_k1.5_v300.json', ref=f'{E}/logs/vb_law.log', est=3)
J('slaving_pde_m1', E + '/data', f'$PY ../slaving_pde.py {G}_B0.003_k1.5_merged.json', ref=f'{E}/logs/slaving_pde_m1.log', needs=EP, est=20)
J('slaving_pde_M3', E + '/data', f'$PY ../slaving_pde.py {G}_M3_B0.003_k1.5_v250.json', ref=f'{E}/logs/slaving_pde_M3.log', needs=EP, est=20)
J('gpred_final', E + '/data', f'$PY ../gpred_q.py 0.003 1.5 0.7957 {G}_B0.003_k1.5_v400.json', ref=f'{E}/logs/gpred_final.log', needs=EP, est=30)
J('rho_check', E + '/data', f'$PY ../rho_check.py {G}_B0.003_k1.5_v400.json', ref=f'{E}/logs/rho_check.log', needs=EP, est=5)
J('balance_check', E + '/data', f'$PY ../balance_check.py {G}_B0.003_k1.5_v400.json 0.7956534', ref=f'{E}/logs/balance_check.log', needs=EP, est=5)
J('bounded_aniso', E + '/data', '$PY ../bounded_aniso.py genq2_hs0.05_m2_a1_M1.5_B0.0003_k1.5_v200.json', ref=f'{E}/logs/bounded_aniso.log', needs=('numpy', 'scipy'), est=10)
J('bounded_slaving', E + '/data', '$PY ../bounded_slaving.py genq_m2_a1_M1.5_B0.0003_k1.5_v110.json genq_m2_a1_M1.5_B0.003_k1.5_v110.json', ref=f'{E}/logs/bounded_slaving.log', needs=('numpy', 'scipy'), est=10)
J('curv_hv', E + '/data', f'$PY ../curv_hv.py {G}_B0.003_k1.5_v400.json 4 2 241', ref=f'{E}/logs/curv_hv.log', needs=('numpy', 'scipy'), est=10)
J('curv_hv_merged', E + '/data', f'$PY ../curv_hv.py {G}_B0.003_k1.5_merged.json 4 2 281', ref=f'{E}/logs/curv_hv_merged.log', needs=EP, est=10)   # same script as curv_hv on the eight-level merged file (reaches v=300)
J('curv_hv_B0.0003', E + '/data', f'$PY ../curv_hv.py {G}_B0.0003_k1.5_v300.json 4 2 281', ref=f'{E}/logs/curv_hv_B0.0003.log', needs=('numpy', 'scipy'), est=10)

# ---- D. analyses of the isotropic four-mesh runs (data/genq_*.json): Sections 9-12 --------------------------------------------------------
KM = {'0.0003': '0.7956493155', '0.003': '0.7956534352', '0.03': '0.7960655916'}
for Bv in ('0.0003', '0.003', '0.03'):
    F = f'data/genq_m1_B{Bv}_k1.5_v110.json'
    L = f'{E}/logs'
    J(f'late_m1_B{Bv}', E, f'$PY late_q.py {F} 1 1.0 60 70 80 90 100 108', ref=f'{L}/late_m1_B{Bv}.log', needs=EP, est=5)
    J(f'kernel_ratio_B{Bv}', E, f'$PY kernel_ratio_q.py {F}', ref=f'{L}/kernel_ratio_B{Bv}.log', needs=EP, est=5)
    J(f'masslaw_m1_B{Bv}', E, f'$PY masslaw_q.py {F} 1 1.0', ref=f'{L}/masslaw_m1_B{Bv}.log', needs=EP, est=5)
    J(f'kap_check_m1_B{Bv}', E, f'$PY kap_check.py {F}', ref=f'{L}/kap_check_m1_B{Bv}.log', needs=EP, est=5)
    J(f'curv_m1_B{Bv}', E, f'$PY curv_q.py {F}', ref=f'{L}/curv_m1_B{Bv}.log', needs=EP, est=5)
    J(f'front_m1_B{Bv}', E, f'$PY front_q.py {F} 0.048968742118989196', ref=f'{L}/front_m1_B{Bv}.log', needs=EP, est=5)
    J(f'plateau_m1_B{Bv}', E, f'$PY plateau_q.py {F} {KM[Bv]}', ref=f'{L}/plateau_m1_B{Bv}.log', needs=EP, est=5)
KB = {'0.0003': '0.79700775', '0.003': '0.79701569', '0.03': '0.79780932'}
for Bv in ('0.0003', '0.003', '0.03'):
    F = f'data/genq_m2_a1_M1.5_B{Bv}_k1.5_v110.json'
    L = f'{E}/logs'
    J(f'late_m2_M1.5_B{Bv}', E, f'$PY late_q.py {F} 2 1.0 40 50 60 70 80 90 100 108', ref=f'{L}/late_m2_M1.5_B{Bv}.log', needs=EP, est=5)
    J(f'kap_check_m2_M1.5_B{Bv}', E, f'$PY kap_check_b.py {F} 1.5 1.0', ref=f'{L}/kap_check_m2_M1.5_B{Bv}.log', needs=EP, est=5)
    J(f'masslaw_m2_M1.5_B{Bv}', E, f'$PY masslaw_q.py {F} 2 1.0', ref=f'{L}/masslaw_m2_M1.5_B{Bv}.log', needs=EP, est=5)
    J(f'plateau_m2_B{Bv}', E, f'$PY plateau_q.py {F} {KB[Bv]} 20', ref=f'{L}/plateau_m2_B{Bv}.log', needs=EP, est=5)
    J(f'front_m2_B{Bv}', E, f'$PY front_q.py {F} 0.16135947', ref=f'{L}/front_m2_B{Bv}.log', needs=EP, est=5)
for Bv in ('0.003', '0.03'):
    J(f'late_m1_B{Bv}_v200', E, f'$PY late_q.py data/genq_m1_B{Bv}_k1.5_v200.json 1 1.0 60 80 100 120 140 160 180 198', ref=f'{E}/logs/late_m1_B{Bv}_v200.log', needs=EP, est=5)
J('endpoint_m1_B0.003_v200', E, '$PY endpoint_q.py data/genq_m1_B0.003_k1.5_v200.json', ref=f'{E}/logs/endpoint_m1_B0.003_v200.log', needs=EP, est=20)
J('curv_terms_m1_B0.003', E, '$PY curv_terms_q.py data/genq_m1_B0.003_k1.5_v200.json 80 100 120 140 160', ref=f'{E}/logs/curv_terms_m1_B0.003.log', needs=('numpy', 'scipy'), est=10)
J('cmp_add_B0.003', E, '$PY cmp_add.py data/genq_m1_B0.003_k1.5_v110.json 0.003', ref=f'{E}/logs/cmp_add_B0.003.log', needs=EP, est=5)
J('cmp_add_B0.0003', E, '$PY cmp_add.py data/genq_m1_B0.0003_k1.5_v110.json 0.0003', ref=f'{E}/logs/cmp_add_B0.0003.log', needs=EP, est=5)

J('width_m1', E, 'for B in 0.0003 0.003 0.03; do $PY width_q.py data/genq_m1_B${B}_k1.5_v110.json; done', ref=f'{E}/logs/width_m1.log', needs=EP, est=15)

# ---- E. validation of the constrained evolution against exact static data (short PDE runs) -------------------------------------------------
J('t_static_free', E, '$PY t_static_q.py', ref=f'{E}/logs/t_static_free.log', needs=EP, est=40)
J('t_static_free_U3', E, '$PY t_static_free.py', ref=f'{E}/logs/t_static_free_U3.log', needs=EP, est=60)
for M in (1, 2, 3):
    J(f't_static_cy_mode{M}', E, f'MODE={M} $PY t_static_cy.py', ref=f'{E}/logs/t_static_cy_mode{M}.log', needs=EP, est=60)
J('t_static_b_a1_M1.5', E, 'MASS=1.5 $PY t_static_b.py 1.0', ref=f'{E}/logs/t_static_b_a1_M1.5.log', needs=EP, est=60)
J('t_static_b_a1', E, '$PY t_static_b.py 1.0', ref=f'{E}/logs/t_static_b_a1.log', needs=EP, est=60)
J('free_vs_con', E, '$PY free_vs_con.py', ref=f'{E}/logs/free_vs_con.log', needs=EP, est=60)
J('check_ruv_B0.003', E, '$PY check_ruv_q.py 0.003 110 0.05 0.025 0.0125 -- 40 60 80 100', ref=f'{E}/logs/check_ruv_B0.003.log', needs=EP, est=90)

# ---- F. blow-up law (Section 'What limits the window') ---------------------------------------------------------------------------------------
J('vb1', E, '$PY blowup_probe.py 0.003 0.05 0.05 250; $PY blowup_probe.py 0.003 0.05 0.05 400', ref=f'{C}/vb1.log', needs=EP, est=190)
# jobs whose generators were scratch scripts before this verification was added (now code/eh_qtg/{err_prof,blow_trace,slaving_q,modecmp,c3_sensitivity,prof2}.py, codee/seed_search.py):
J('errprof', E, '$PY err_prof.py', ref=f'{C}/errprof.log', tier='full', needs=EP, est=620, note='three meshes of code A to v1=300 (about 10 CPU-minutes)')
J('blow1', E, '$PY ../../../code/eh_qtg/blow_trace.py 0.003 300 0.025', ref=f'{C}/blow1.log', tier='full', needs=EP, est=130, work=True)     # first non-finite v = 233.575 (isotropic h = 0.025); writes blow_h*.npy into its work directory
J('blow2', E, '$PY ../../../code/eh_qtg/blow_trace.py 0.003 300 0.0125', ref=f'{C}/blow2.log', tier='full', needs=EP, est=500, work=True)  # first non-finite v = 261.9
J('blow3', E, '$PY ../../../code/eh_qtg/blow_trace.py 0.003 300 0.00625', ref=f'{C}/blow3.log', tier='full', needs=EP, est=2000, work=True) # first non-finite v = 290.20625
J('slaving', E, '$PY slaving_q.py 0.003 0.05 0.003125 200 100 150 190', ref=f'{E}/logs/slaving.log', tier='full', needs=EP, est=210)
J('modecmp', E, '$PY modecmp.py 0.003 110 0.05 0.025 0.0125 0.00625', ref=f'{E}/logs/modecmp.log', tier='full', needs=EP, est=1800)
J('c3_sensitivity', E, '$PY c3_sensitivity.py 0.003 110 0.025 1 0 1.1 0.9', ref=f'{E}/logs/c3_sensitivity.log', tier='full', needs=EP, est=130)
CMPG = ' ; for f in genq2_*.json; do if [ -e ../../../code/eh_qtg/data/$f ]; then if cmp -s $f ../../../code/eh_qtg/data/$f; then echo "$f: byte-identical to the shipped copy" >&2; else echo "$f: DIFFERS from the shipped copy" >&2; fi; else echo "$f: no shipped file of that name" >&2; fi; done'
J('g2_hs0.05_v400', E, '$PY ../../../code/eh_qtg/gen_q2.py 1 1.0 0.003 1.5 400 0.05:0.05 0.05:0.025 0.05:0.0125 0.05:0.00625 0.05:0.003125 0.05:0.0015625' + CMPG, ref=f'{E}/logs/g2_hs0.05_v400.log', tier='full', needs=EP, est=2700, work=True,
  note='anisotropic constrained run, six levels h_v = 0.05 ... 0.0015625; writes genq2_hs0.05_m1_B0.003_k1.5_v400.json into its work directory (shipped as data/genq2_hs0.05_m1_B0.003_k1.5_v400.json)')
# ---- F2. figures (regenerated into verification/figures/; compared with the shipped figures by pixel dimensions) -------------------------------
FIGCP = 'mkdir -p ../../figures && cp fig_*.png ../../figures/'
CD_ = '../../../code/eh_qtg/codec'
J('fig_qtg', C, 'cp ../../../code/ray_blowup.json ../../../code/conv_B2e-4_h*.npz . && FIG_OUT=. $PY ../../../code/make_figs.py && $PY ../../figcmp.py fig_qtg.png ../../../fig_qtg.png && ' + FIGCP,
  needs=('numpy', 'scipy', 'matplotlib'), est=30, work=True, note='Figure qtg: a from ray_blowup.json, b from the five meshes conv_B2e-4_h*.npz (shipped), c recomputed (model 2, h = 0.02)')
J('fig_eh', E, 'FIG_OUT=. $PY ../../../code/eh_qtg/fig_eh.py && $PY ../../figcmp.py fig_eh.png ../../../fig_eh.png && ' + FIGCP,
  needs=('numpy', 'matplotlib'), est=10, work=True, note='Figure eh from data/genq_*.json and logs/kernel_ratio_B*.log')
J('fig_collapse', CC, f'ln -sf {CD_}/data/tail_m1_v60_h05.npz . && ln -sf {CD_}/data/tail_m0_v60_h05.npz . && ln -sf {CD_}/data/collapseE_profile_hv0.2.json genc_prof_hs0.2_hv0.2_v1500.json && FIG_OUT=. $PY {CD_}/fig_collapse.py && $PY ../../figcmp.py fig_collapse.png ../../../fig_collapse.png && ' + FIGCP,
  needs=('numpy', 'matplotlib'), est=10, work=True, note='Figure collapse: horizon field and local index from tail_m*_v60_h05.npz, panel c from the code-E run on the collapse tail (collapseE_profile_hv0.2.json)')
J('fig_collapse_k2', CC, f'for x in npdata ce data nplin_m0_M5_h0.2.npz nplin_m1_M5_h0.2.npz; do ln -sf {CD_}/$x .; done; FIG_OUT=. $PY {CD_}/fig_collapse_k2.py && $PY ../../figcmp.py fig_collapse_k2.png ../../../fig_collapse_k2.png && ' + FIGCP,
  needs=('numpy', 'scipy', 'matplotlib'), est=15, work=True, note='Figure k2: npdata/*.npz, nplin_*.npz, ce/*.json')
J('fig_strong', SP, f'ln -sf {CD_}/sp . && FIG_OUT=. $PY {CD_}/fig_strong.py && $PY ../../figcmp.py fig_strong.png ../../../fig_strong.png && ' + FIGCP,
  needs=('numpy', 'scipy', 'matplotlib'), est=20, work=True, note='Figure strong: fixed-index fits of the 17 tables sp/t*_m*_mt*.npz and the Q_abs column of sp/horizon_ray.log (shipped)')
# ---- G. code B and code E ---------------------------------------------------------------------------------------------------------------------
J('cmp_AB_final', B_, '$PY cmp_AB_final.py', ref=f'{B_}/logs/cmp_AB_final.log', est=5)
J('cmp_hs', B_, '$PY cmp_hs.py', ref=f'{B_}/logs/cmp_hs.log', est=5)
J('cmp_table', B_, '$PY cmp_table.py', ref=f'{B_}/logs/cmp_table.log', est=5)
J('kstudy2_longdouble_v1200', EE, '$PY kstudy2.py data/genel_p1_hs0.2_m1_B0.003_k1.5_v1200_ray2.json 0.1 1100 0', ref=f'{EE}/logs/kstudy2_longdouble_v1200.log', needs=('numpy', 'scipy'), est=10)
J('mech_vb_B3e-3', EE, '$PY mech_vb.py 600 3e-3 1.5', ref=f'{EE}/logs/mech_vb_B3e-3.log', needs=EP, est=60)
J('mech_vb_B3e-2', EE, '$PY mech_vb.py 600 3e-2 1.5', ref=f'{EE}/logs/mech_vb_B3e-2.log', needs=EP, est=60)
J('mech_vb_B3e-4', EE, '$PY mech_vb.py 600 3e-4 1.5', ref=f'{EE}/logs/mech_vb_B3e-4.log', needs=EP, est=60)
J('vb_prediction', EE, '$PY vb_prediction.py', ref=f'{EE}/logs/vb_prediction.log', needs=EP, stage=2, est=10)

# ---- H. collapse-generated tails (codec/): analyses of shipped tables and runs ---------------------------------------------------------------
T17 = "t_m5_mt5.01.npz t_m5_mt5.5.npz t_m5_mt6.5.npz t_m5_mt8.npz t_m5_mt10.npz t_m5_mt15.npz t_m5_mt25.npz t_m0_mt10.npz t_m2.5_mt10.npz t1_m2.5_mt12.5.npz t1_m5_mt20.npz t1_m7.5_mt15.npz t1_m10_mt20.npz t0_m0_mt10.npz t0_m2.5_mt10.npz t0_m5_mt10.npz t0_m5_mt25.npz"
TSH = "sh_narrow_m0_0_10.npz sh_narrow_m0_2.5_10.npz sh_narrow_m0_5_10.npz sh_wide_m0_0_10.npz sh_wide_m0_2.5_10.npz sh_wide_m0_5_10.npz"
TLB = ("t_m0_mt10.npz t_m2.5_mt10.npz t_m5_mt10.npz t_m5_mt15.npz t_m5_mt25.npz t_m5_mt5.01.npz t_m5_mt5.5.npz t_m5_mt6.5.npz t_m5_mt8.npz t0_m0_mt10.npz t0_m2.5_mt10.npz t0_m5_mt10.npz t0_m5_mt25.npz "
       "t1_m10_mt20.npz t1_m2.5_mt12.5.npz t1_m5_mt20.npz t1_m7.5_mt15.npz tc_E_m0_5.npz tc_E_m0_5_c0.02.npz tc_H_m0_10_c0.02.npz tc_H_m0_5_c0.01.npz tc_H_m0_5_c0.02.npz tc_H_m0_5_c0.04.npz tc_H_m2.5_5_c0.02.npz " + TSH + " w_dr-0.3_5.01.npz w_dr-0.3_5.5.npz")
SD = ''     # STRONG_DR=-0.3 is exported for all jobs by job_env()
J('linbound', SP, SD + f'$PY ../linbound.py {TLB}', ref=f'{SP}/linbound.log', needs=EP, est=15)
J('weak_limit', SP, SD + '$PY ../weak_limit.py 4 12 20 t_m5_mt5.01.npz t_m5_mt5.5.npz t_m5_mt6.5.npz t_m5_mt8.npz', ref=f'{SP}/weak_limit.log', needs=EP, est=5)
J('fit_corr', SP, SD + f'$PY ../fit_corr.py 1000 2900 {T17} sh_narrow_m0_0_10.npz sh_narrow_m0_2.5_10.npz sh_narrow_m0_5_10.npz sh_wide_m0_2.5_10.npz sh_wide_m0_5_10.npz', ref=f'{SP}/fit_corr.log', needs=('numpy', 'scipy'), est=10)
J('strong_fit', SP, SD + '$PY ../strong_fit.py t_m5_mt5.01.npz t_m5_mt5.5.npz t_m5_mt6.5.npz t_m5_mt8.npz t_m5_mt10.npz t_m5_mt15.npz t_m5_mt25.npz t_m0_mt10.npz t_m2.5_mt10.npz t1_m2.5_mt12.5.npz t1_m5_mt20.npz t1_m7.5_mt15.npz t1_m10_mt20.npz t0_m5_mt10.npz t0_m2.5_mt10.npz t0_m5_mt25.npz t0_m0_mt10.npz', ref=f'{SP}/strong_fit.log', needs=('numpy', 'scipy'), est=10)
J('charge_row', SP, SD + f'$PY ../charge_row.py 4 12 20 {T17}; $PY ../charge_row.py 4 8 20 sh_narrow_m0_0_10.npz sh_narrow_m0_2.5_10.npz sh_narrow_m0_5_10.npz | tail -n +2; $PY ../charge_row.py 4 20 28 sh_wide_m0_0_10.npz sh_wide_m0_2.5_10.npz sh_wide_m0_5_10.npz | tail -n +2', ref=f'{SP}/charge_row.log', needs=EP, est=15)   # pulse arguments per table family, as for horizon_ray (the first release used 4 12 20 for the narrow and wide tables)
J('strong_conv', SP, SD + '$PY ../strong_conv.py c_h0.1_L0.1.npz c_h0.05_L0.1.npz c_h0.025_L0.1.npz c_h0.1_L0.05.npz', ref=f'{SP}/strong_conv.log', needs=('numpy', 'scipy'), est=10)
J('tc_fit', CC, SD + '$PY tc_fit.py sp/tc_*_c*.npz 2>/dev/null', ref=f'{SP}/tc_fit.log', needs=('numpy', 'scipy'), est=10)
J('rowflux', CC, SD + 'for a in 5:5.01 5:5.5 5:6.5 5:8 5:10 0:10 2.5:10 5:15 5:25; do m0=${a%%:*}; mt=${a##*:}; $PY rowflux.py 1 $m0 $mt 0.1 0.1 sp/t_m${m0}_mt${mt}.npz | grep -v direct; done', ref=f'{SP}/rowflux.log', needs=EP, est=330)
J('rowflux_direct', CC, SD + 'for a in 10 25; do $PY rowflux.py 1 5 $a 0.1 0.1 sp/t_m5_mt${a}.npz | grep direct; done', ref=f'{SP}/rowflux_direct.log', tier='full', needs=EP, est=70)
J('horizon_ray', SP, SD + "$PY ../horizon_ray.py 4 12 20 " + T17 + "; $PY ../horizon_ray.py 4 8 20 sh_narrow_m0_0_10.npz sh_narrow_m0_2.5_10.npz sh_narrow_m0_5_10.npz | tail -3; $PY ../horizon_ray.py 4 20 28 sh_wide_m0_0_10.npz sh_wide_m0_2.5_10.npz sh_wide_m0_5_10.npz | tail -3", ref=f'{SP}/horizon_ray.log', needs=('numpy', 'scipy'), est=10)
J('eik2', SP, SD + '$PY ../eik2.py 4 12 20 t_m5_mt5.01.npz t_m5_mt5.5.npz t_m5_mt6.5.npz t_m5_mt8.npz t_m5_mt10.npz t_m5_mt15.npz t_m5_mt25.npz t_m0_mt10.npz t_m2.5_mt10.npz t1_m2.5_mt12.5.npz t1_m5_mt20.npz t1_m7.5_mt15.npz t1_m10_mt20.npz', ref=f'{SP}/eik2.log', needs=EP, est=5)
SCF = "genc_P0.01_hs0.2_hv0.2_v1000.json genc_P0.03_hs0.2_hv0.2_v1000.json genc_P0.05_hs0.2_hv0.2_v1000.json genc_P0.07_hs0.2_hv0.2_v1000.json genc_P0.08_hs0.2_hv0.2_v1000.json"
J('scan_zm', SC, SD + f'$PY ../pscan_zm.py {SCF}', ref=f'{SC}/scan_zm.log', needs=('numpy', 'scipy'), est=10)
J('scan_an', SC, SD + f'$PY ../pscan_an.py {SCF}', ref=f'{SC}/scan_an.log', needs=('numpy', 'scipy'), est=10)
J('scan_summary', SC, SD + '$PY ../pscan_summary.py 0.01 0.03 0.05 0.07 0.08', ref=f'{SC}/scan_summary.log', needs=EP, est=30)
J('horizon_map', SC, SD + '$PY ../horizon_map.py', ref=f'{SC}/horizon_map.log', needs=EP, est=30)
J('vaidya_estimate', SC, SD + '$PY ../vaidya_estimate.py', ref=f'{SC}/vaidya_estimate.log', needs=EP, est=30)
STRONG = (
    'echo "== m_f=25 resolution (hs,hv)=(0.2,0.2),(0.1,0.2),(0.2,0.1),(0.1,0.1)"; '
    'F25="genc_S5to25_hs0.2_hv0.2_v4000.json genc_S5to25_hs0.1_hv0.2_v4000.json genc_S5to25_hs0.2_hv0.1_v4000.json genc_S5to25_hs0.1_hv0.1_v4000.json"; '
    '$PY ../pscan_freeze.py 25 $F25; VS=4.4444 $PY ../pscan_zm.py $F25; VS=4.4444 $PY ../pscan_an.py $F25; '
    'echo "== m_f=15"; $PY ../pscan_freeze.py 15 genc_S5to15_hs0.2_hv0.2_v2800.json; VS=3.1111 $PY ../pscan_zm.py genc_S5to15_hs0.2_hv0.2_v2800.json; VS=3.1111 $PY ../pscan_an.py genc_S5to15_hs0.2_hv0.2_v2800.json; '
    'echo "== m_f=10 (S5to10, S0to10)"; F10="genc_S5to10_hs0.2_hv0.2_v2000.json genc_S0to10_hs0.2_hv0.2_v2000.json"; '
    '$PY ../pscan_freeze.py 10 $F10; VS=2 $PY ../pscan_zm.py $F10; VS=2 $PY ../pscan_an.py $F10; '
    'echo "== K(1500) of the two histories"; $PY ../strong_k1500.py $F10 $(awk \'$1=="t_m5_mt10.npz"{print $6}\' strong_fit.log) $(awk \'$1=="t_m0_mt10.npz"{print $6}\' strong_fit.log)')
J('strong_codeE', SP, SD + STRONG, ref=f'{SP}/strong_codeE.log', needs=EP, est=15)
J('collapse_E', CC, SD + '$PY collapse_E.py', ref=f'{CC}/logs/collapse_E.log', needs=('numpy', 'scipy'), est=10)
J('conv_c', CC, SD + '$PY conv_c.py data/collapseE_profile_hv0.2.json data/collapseE_profile_hv0.1.json', ref=f'{CC}/conv_c.log', needs=EP, est=5)
J('conv_c_k2', CC, SD + '$PY conv_c.py ce/genc_np1_hs0.2_hv0.2_v1500.json ce/genc_np1_hs0.2_hv0.1_v1500.json', ref=f'{CC}/logs/conv_c_k2.log', needs=EP, est=5)
J('tailfit_results', BCR, SD + '$PY tailfit.py base; B_ASYM=1.5 $PY tailfit.py asym1', ref=f'{BCR}/tailfit_results.log', needs=EP, est=60)
J('s2a_results', BCR, SD + '$PY s2a_an.py', ref=f'{BCR}/s2a/s2a_results.log', needs=('numpy', 'scipy'), est=10)
J('convergence_h', BCR, SD + '$PY convergence_h.py', ref=f'{BCR}/convergence_h.log', needs=('numpy', 'scipy'), est=10)
J('eik_test', SP, '(' + ' '.join(['$PY ../eik_test.py 4 12 20 ' + T17 + ';', '$PY ../eik_test.py 4 8 20 sh_narrow_m0_0_10.npz sh_narrow_m0_2.5_10.npz sh_narrow_m0_5_10.npz;', '$PY ../eik_test.py 4 20 28 sh_wide_m0_2.5_10.npz sh_wide_m0_5_10.npz']) + ') 2>&1', ref=f'{SP}/eik_test.log', needs=EP, est=60)
J('nearext', SP, '$PY ../nearext.py 1600 0.25 5 2 1.5 1.32 1.31 1.302 1.3005 1.2990401 1.2990581 1.2991380', ref=f'{SP}/nearext_quick.log', needs=EP, est=25, note='linear l=0 horizon field of an ingoing pulse on near-extremal Hayward holes; not quoted in main.tex; sp/nearext.log and sp/nearext2.log are the original runs to t=25600')
J('eik_summary', SP, '$PY ../eik_summary.py ../../../../verification/logs/eik_test.log', ref=f'{SP}/eik_summary.log', needs=('numpy',), est=2, stage=2)
J('horizon_ray_conv', SP, 'for hf in 0.2 0.1 0.05; do echo h=$hf; HNF=$hf $PY ../horizon_ray.py 4 12 20 t_m5_mt10.npz t_m0_mt10.npz t_m5_mt25.npz | tail -3; done', ref=f'{SP}/horizon_ray_conv.log', needs=EP, est=60)
J('conv_P0.08_hv', SC, '$PY ../pscan_conv.py genc_P0.08_hs0.2_hv0.2_v1000.json genc_P0.08_hs0.2_hv0.1_v1000.json; $PY ../pscan_zm.py genc_P0.08_hs0.2_hv0.1_v1000.json; $PY ../pscan_an.py genc_P0.08_hs0.2_hv0.1_v1000.json', ref=f'{SC}/conv_P0.08_hv.log', needs=EP, est=5)
J('conv_P0.07_hs', SC, '$PY ../pscan_conv.py genc_P0.07_hs0.2_hv0.2_v1000.json genc_P0.07_hs0.1_hv0.2_v1000.json; $PY ../pscan_zm.py genc_P0.07_hs0.1_hv0.2_v1000.json; $PY ../pscan_an.py genc_P0.07_hs0.1_hv0.2_v1000.json', ref=f'{SC}/conv_P0.07_hs.log', needs=EP, est=5)
J('overlap_h', CC, '$PY overlap_h.py 1 5 10 0.05 0.05', ref=f'{CC}/logs/overlap_h.log', needs=EP, est=110)

# ---- G2. more code B / code E analyses of shipped data and short runs -------------------------------------------------------------------------
J('vb_B3e-2_B3e-4', EE, '$PY first_nonfinite.py ../codeb/data/genb_p1_hs0.05_m1_B0.03_k1.5_v330.json ../codeb/data/genb_p1_hs0.05_m1_B0.0003_k1.5_v400.json', ref=f'{EE}/logs/vb_B3e-2_B3e-4.log', est=2)
J('seed_search', EE, '$PY seed_search.py', ref=f'{EE}/logs/seed_search.log', tier='full', needs=EP, est=3600, note='about 20 runs of code E, 1-5 minutes each')
J('conv_e', EE, '$PY conv_e.py', ref=f'{EE}/logs/conv_e.log', est=5)
J('conv_e2', EE, '$PY conv_e2.py', ref=f'{EE}/logs/conv_e2.log', est=10)
J('seed_amplitude', EE, '$PY seed_amplitude.py', ref=f'{EE}/logs/seed_amplitude.log', est=5)
J('scans', EE, 'bash scans.sh', ref=f'{EE}/logs/scans.log', needs=EP, est=30)
J('kstudy2_double_v1500', EE, '$PY kstudy2.py data/gene_p1_hs0.2_m1_B0.003_k1.5_v1500_ray2.json 0.1 1400', ref=f'{EE}/logs/kstudy2_double_v1500.log', needs=('numpy', 'scipy'), est=10)
J('t_static_e', EE, '$PY t_static_e.py', ref=f'{EE}/logs/t_static_e.log', needs=EP, est=90)
J('t_static_b4', B_, '$PY t_static_b4.py', ref=f'{B_}/logs/t_static_b4.log', needs=EP, est=90)
J('t_static_b4_proj0', B_, 'PROJ=0 $PY t_static_b4.py', ref=f'{B_}/logs/t_static_b4_proj0.log', needs=EP, est=90)
J('kstudy_v600', B_, '$PY ../../../code/eh_qtg/codeb/kstudy.py ../../../code/eh_qtg/codeb/data/genb_hs0.05_v600.json 0.0125', ref=f'{B_}/logs/kstudy_v600.log', needs=EP, est=5, work=True)   # writes kst_*.npy into its work directory
J('tidal_v600', B_, '$PY tidal.py data/genb_hs0.05_v600.json 0.0125 380 data/genb_hs0.05_v480.json 0.025', ref=f'{B_}/logs/tidal_v600.log', needs=('numpy', 'scipy'), est=10)
J('phi_monotone', E, '$PY ../../../code/eh_qtg/phi_monotone.py', ref=f'{E}/logs/phi_monotone.log', needs=EP, est=40, work=True)

# ---- I. generators added in the verification pass (they were scratch scripts before; see code/README.md) ----------------------------------------------
J('prof2', E, '$PY ../../../code/eh_qtg/prof2.py; $PY -c "import numpy as n; print({a: n.load(\'prof2_%s.npy\' % a).shape for a in (\'U\', \'gp\', \'snap\')})"', ref=None, tier='full', needs=EP, est=190, work=True)      # code A streamed snapshots, writes prof2_*.npy into its work directory
J('slaving_prof', E, 'cd ../prof2 && $PY ../../../code/eh_qtg/slaving_prof.py', ref=f'{E}/logs/slaving_prof.log', tier='full', needs=EP, est=5, stage=2, work=True)   # reads the snapshots prof2_*.npy of job prof2
J('nplin', CC, '$PY nplin_rows.py nplin_m0_M5_h0.2.npz nplin_m1_M5_h0.2.npz; $PY nplin_fit.py nplin_m0_M5_h0.2.npz nplin_m1_M5_h0.2.npz', ref=f'{CC}/logs/nplin.log', needs=EP, est=20)
# ---- K. collapse stages N and L (codec/): the tests and fits of Sec. 'Collapse-generated horizon tails' ----------------------------------------------------------
J('interior', CC, '$PY interior.py 0.05 39.0 70', ref=f'{CC}/logs/interior.log', needs=EP, est=20, atol=1e-13, why='the column rel= at u=0 is a rounding residual (5e-15 or 7e-15 depending on the libm)')
J('overlap', CC, '$PY overlap.py', ref=f'{CC}/logs/overlap.log', needs=EP, est=20)
J('tables', CC, '$PY tables.py', ref=f'{CC}/logs/tables.log', needs=EP, est=150)
J('fit_tables', CC, 'mkdir -p data && $PY ../../../code/eh_qtg/codec/fit_tables.py && $PY ../../tabcmp.py data ../../../code/eh_qtg/codec/data >&2', ref=f'{CC}/logs/fit_tables.log', needs=EP, est=70, rtol=1e-5, work=True, why='the free fit in the early window [600,1200] is ill conditioned (B = 688.22 or 887.89..896); the tolerance of scipy least_squares sets its 6th digit')
J('mscale', CC, '$PY mscale.py 2>&1', ref=f'{CC}/logs/mscale.log', needs=EP, est=140)
J('ascale', CC, '$PY ascale.py 2>&1', ref=f'{CC}/logs/ascale.log', needs=EP, est=25, rtol=1e-6, why='logarithmic derivatives of fitted amplitudes differ in the 7th digit between scipy versions')
J('ascale_q', CC, '$PY ascale_q.py', ref=f'{CC}/logs/ascale_q.log', needs=EP, est=40, note='NEW generator (not in the original archive), built from the original functions; see PROVENANCE.md')
J('linear', CC, '$PY linear.py 2>&1', ref=f'{CC}/logs/linear.log', needs=EP, est=25)
J('linear_q', CC, 'for a in "1 1.0" "1 0.8" "1 1.2" "0 1.0"; do $PY linear_q.py ${a% *} ${a#* } 0.2 12800; done', ref=f'{CC}/logs/linear_q.log', tier='full', needs=EP, est=130)
J('np_fit', CC, '$PY np_fit.py npdata/np_m1_b1.0_h1.npz npdata/np_m0_b1.0_h1.npz npdata/np_m1_b-1.0_h1.npz npdata/np_m1_b0.5_h1.npz npdata/np_m1_b2.0_h1.npz', ref=f'{CC}/logs/np_fit.log', needs=EP, est=30)
J('np_lin_b', CC, '$PY np_lin_b.py', ref=f'{CC}/logs/np_lin_b.log', needs=EP, est=5)
J('overlap_np', CC, '$PY overlap_np.py 2>&1', ref=f'{CC}/logs/overlap_np.log', needs=EP, est=30)
J('collapse_E_k2', CC, 'for f in ce/genc_np1_hs0.2_hv0.2_v1500.json ce/genc_np01_hs0.2_hv0.2_v1500.json; do for r in 0 1 2 3; do $PY an_k.py $f 2 $r; done; done', ref=f'{CC}/logs/collapse_E_k2.log', needs=('numpy', 'scipy'), est=10)
J('k2_extra', CC, '$PY k2_extra.py ce/genc_np1_hs0.2_hv0.2_v1500.json ce/genc_np01_hs0.2_hv0.2_v1500.json', ref=f'{CC}/logs/k2_extra.log', needs=('numpy', 'scipy'), est=10)
J('t_static_h', CC, 'for h in 0.2 0.1 0.05; do $PY t_static_h.py $h 1 5 20; done', ref=f'{CC}/logs/t_static_h.log', needs=EP, est=15)
J('sp_interior', CC, 'for a in "10 0.1" "25 0.1"; do $PY sp_interior.py 1 5 $a; done', ref=f'{CC}/logs/sp_interior.log', needs=EP, est=90)
J('sp_interior_fine', CC, 'for a in "10 0.05" "25 0.05"; do $PY sp_interior.py 1 5 $a; done', ref=f'{CC}/logs/sp_interior_fine.log', tier='full', needs=EP, est=90)   # the h_N = 0.05 s runs of test (iii)
# ---- J. long runs that produce the data (--full only) ---------------------------------------------------------------------------------------
# (see the full-tier entries at the end of the job list)
GQ2 = '$PY ../../../code/eh_qtg/gen_q2.py'
for (jid, args_, ref, est, extra) in [
    ('g2_hs0.025_v400', '1 1.0 0.003 1.5 400 0.025:0.05 0.025:0.025 0.025:0.0125 0.025:0.00625 0.025:0.003125', 'g2_hs0.025_v400.log', 9000, ''),
    ('g2_A_v360', '1 1.0 0.003 1.5 360 0.05:0.00078125 0.05:0.000390625', 'g2_A_v360.log', 7600, ''),
    ('g2_B0.0003_v300', '1 1.0 0.0003 1.5 300 0.05:0.0125 0.05:0.00625 0.05:0.003125 0.05:0.0015625', 'g2_B0.0003_v300.log', 3000, ''),
    ('g2_B0.03_v300', '1 1.0 0.03 1.5 300 0.05:0.0125 0.05:0.00625 0.05:0.003125 0.05:0.0015625', 'g2_B0.03_v300.log', 3000, ''),
    ('g2_k0.5_v300', '1 1.0 0.003 0.5 300 0.05:0.025 0.05:0.0125 0.05:0.00625 0.05:0.003125', 'g2_k0.5_v300.log', 3000, ''),
    ('g2_k3_v300', '1 1.0 0.003 3 300 0.05:0.025 0.05:0.0125 0.05:0.00625 0.05:0.003125', 'g2_k3_v300.log', 3000, ''),
    ('g2_M3_v250', '1 1.0 0.003 1.5 250 0.05:0.0125 0.05:0.00625 0.05:0.003125 0.05:0.0015625', 'g2_M3_v250.log', 2500, 'MASS=3 '),
    ('g2_b_B0.0003_v200', '2 1.0 0.0003 1.5 200 0.05:0.0125 0.05:0.00625 0.05:0.003125 0.05:0.0015625', 'g2_b_B0.0003_v200.log', 2500, 'MASS=1.5 '),
]:
    J(jid, E, extra + GQ2 + ' ' + args_ + CMPG, ref=f'{E}/logs/{ref}', tier='full', needs=EP, est=est, work=True,
      note='anisotropic constrained run (levels as in the shipped log); writes the genq2_*.json run file into its work directory (the shipped copy is in data/); the shipped g2_M3_v250.log lists three levels, the fourth was added later' if jid == 'g2_M3_v250' else
           'anisotropic constrained run (levels as in the shipped log); writes the genq2_*.json run file into its work directory (the shipped copy is in data/)')
J('gen_b_v480', B_, '$PY ../../../code/eh_qtg/codeb/gen_b.py 1 1.0 0.003 1.5 480 0.05:0.025 && cmp genb_p1_hs0.05_m1_B0.003_k1.5_v480.json ../../../code/eh_qtg/codeb/data/genb_hs0.05_v480.json && echo "run file byte-identical to the shipped copy" >&2', ref=f'{B_}/logs/gen_b_v480.log', tier='full', needs=EP, est=230, work=True,
  note='code B (C library) on the isotropic-in-practice mesh h_s = 0.05, h_v = 0.025 to v = 480; writes genb_*_v480.json (shipped as codeb/data/genb_hs0.05_v480.json)')
J('gen_b_v600', B_, '$PY ../../../code/eh_qtg/codeb/gen_b.py 1 1.0 0.003 1.5 600 0.05:0.0125 && cmp genb_p1_hs0.05_m1_B0.003_k1.5_v600.json ../../../code/eh_qtg/codeb/data/genb_hs0.05_v600.json && echo "run file byte-identical to the shipped copy" >&2', ref=f'{B_}/logs/gen_b_v600.log', tier='full', needs=EP, est=860, work=True,
  note='code B, h_v = 0.0125 to v = 600; writes genb_*_v600.json (shipped as codeb/data/genb_hs0.05_v600.json)')
J('gen_b_B0.03_v330', B_, '$PY ../../../code/eh_qtg/codeb/gen_b.py 1 1.0 0.03 1.5 330 0.05:0.2 0.05:0.1 0.05:0.05 && $PY ../../../code/eh_qtg/codee/first_nonfinite.py genb_p1_hs0.05_m1_B0.03_k1.5_v330.json && cmp genb_p1_hs0.05_m1_B0.03_k1.5_v330.json ../../../code/eh_qtg/codeb/data/genb_p1_hs0.05_m1_B0.03_k1.5_v330.json && echo "run file byte-identical to the shipped copy"', ref=None, tier='full', needs=EP, est=100, work=True,
  note='code B at B = 0.03 on three meshes h_v = 0.2, 0.1, 0.05 (inputs of codee/logs/vb_B3e-2_B3e-4.log; the shipped copy codeb/data/genb_p1_hs0.05_m1_B0.03_k1.5_v330.json was recovered from the author scratch area)')
J('gen_b_B0.0003_v400', B_, '$PY ../../../code/eh_qtg/codeb/gen_b.py 1 1.0 0.0003 1.5 400 0.05:0.2 && $PY ../../../code/eh_qtg/codee/first_nonfinite.py genb_p1_hs0.05_m1_B0.0003_k1.5_v400.json && cmp genb_p1_hs0.05_m1_B0.0003_k1.5_v400.json ../../../code/eh_qtg/codeb/data/genb_p1_hs0.05_m1_B0.0003_k1.5_v400.json && echo "run file byte-identical to the shipped copy"', ref=None, tier='full', needs=EP, est=30, work=True,
  note='code B at B = 3e-4, h_v = 0.2 (second input of vb_B3e-2_B3e-4.log)')
GC = '../../../code/eh_qtg/codec/gen_c.py'
SCD = '../../../code/eh_qtg/codec/sc'
SPD = '../../../code/eh_qtg/codec/sp'
for P in ('0.01', '0.03', '0.05', '0.07', '0.08'):
    J(f'collapse_P{P}', SC, f'PU0MODE=zero TAG=P{P} $PY {GC} {SCD}/pt_P{P}.npz 1000 0.2:0.2', ref=f'{SC}/run_P{P}.log', tier='full', needs=EP, est=1200, work=True,
      note=f'code C collapse of the pulse of the scan at amplitude P = {P} (hs = hv = 0.2, v1 = 1000); writes genc_P{P}_hs0.2_hv0.2_v1000.json (shipped in codec/sc)')
J('collapse_P0.08_hv0.1', SC, f'PU0MODE=zero TAG=P0.08 $PY {GC} {SCD}/pt_P0.08.npz 1000 0.2:0.1', ref=f'{SC}/run_P0.08_hv0.1.log', tier='full', needs=EP, est=2500, work=True,
  note='finer-v mesh of the P = 0.08 collapse (codec/sc/runh.sh)')
J('collapse_P0.07_hs0.1', SC, f'PU0MODE=zero TAG=P0.07 $PY {GC} {SCD}/pt_P0.07.npz 1000 0.1:0.2', ref=f'{SC}/run_P0.07_hs0.1.log', tier='full', needs=EP, est=2500, work=True,
  note='finer-s mesh of the P = 0.07 collapse (codec/sc/runs.sh)')
for (tag, tab, mass, v1, est) in [('S5to10', 't_m5_mt10.npz', 10, 2000, 500), ('S0to10', 't_m0_mt10.npz', 10, 2000, 500), ('S5to15', 't_m5_mt15.npz', 15, 2800, 650)]:
    J(f'strong_{tag}', SP, f'MASS={mass} PU0MODE=zero TAG={tag} $PY {GC} {SPD}/{tab} {v1} 0.2:0.2', ref=f'{SP}/run_{tag}.log', tier='full', needs=EP, est=est, work=True,
      note=f'code E on the strong-pulse table {tab} (codec/sp/rune.sh); writes genc_{tag}_hs0.2_hv0.2_v{v1}.json (shipped in codec/sp)')
J('strong_S5to25', SP, f'MASS=25 PU0MODE=zero TAG=S5to25 $PY {GC} {SPD}/t_m5_mt25.npz 4000 0.2:0.2 0.1:0.2 0.2:0.1 0.1:0.1', ref=None, tier='full', needs=EP, est=6000, work=True,
  note='the four meshes of the m_f = 25 resolution test (shipped logs run_S5to25*.log list single meshes); writes the four genc_S5to25_*.json files (shipped in codec/sp)')




def build_step(log):
    """Compile the C libraries; returns True if everything needed was built."""
    ok = True
    cmds = [('code/build.sh', CODE, 'bash build.sh'), ('code/eh_qtg/setup.sh', EH, 'bash setup.sh'),
            ('codec/restore_archive.sh', os.path.join(EH, 'codec'), 'bash restore_archive.sh')]
    for name, cwd, cmd in cmds:
        t0 = time.time()
        p = subprocess.run(cmd, shell=True, cwd=cwd, executable='/bin/bash', capture_output=True, text=True, env=job_env())
        log.write(f'--- {name}  rc={p.returncode}  {time.time()-t0:.1f} s\n{p.stdout}{p.stderr}\n')
        if p.returncode != 0:
            ok = False
    return ok


def _rm(path):
    """remove a file; where deleting is not permitted (some mounted folders) truncate it instead"""
    try:
        os.remove(path)
    except OSError:
        try:
            open(path, 'w').close()
        except OSError:
            pass


def _mv(src, dst):
    try:
        os.replace(src, dst)
    except OSError:
        shutil.copyfile(src, dst)
        _rm(src)


def job_env():
    env = dict(os.environ)
    env['PY'] = PY
    env['QTG_CODE'] = CODE
    env['PYTHONPATH'] = os.pathsep.join([CODE, EH] + ([env['PYTHONPATH']] if env.get('PYTHONPATH') else []))
    env['OMP_NUM_THREADS'] = '1'
    env['OPENBLAS_NUM_THREADS'] = '1'
    env['MPLBACKEND'] = 'Agg'
    env['PYTHONHASHSEED'] = '0'
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    env.setdefault('STRONG_DR', '-0.3')                  # strong-pulse analyses of codec/sp (as in run_analysis.sh)
    env.setdefault('B_ASYM', '1.5')                      # amplitude asymmetry of the asym1 runs of codec/bcr (documented default of tailfit.py asym1)
    shim = os.path.join(VER, 'work', 'bin')               # scripts call plain python3: make it the interpreter that runs verify.py
    try:
        os.makedirs(shim, exist_ok=True)
        target = PY if os.path.isabs(PY) else shutil.which(PY) or sys.executable
        for nm in ('python3', 'python'):
            p = os.path.join(shim, nm)
            if os.path.islink(p) and os.readlink(p) == target:
                continue                                  # already there (the function is called by every job, in parallel)
            if os.path.lexists(p):
                _rm(p)
            os.symlink(target, p)
        env['PATH'] = shim + os.pathsep + env.get('PATH', '')
    except OSError:
        pass
    return env


def have(mod):
    try:
        importlib.import_module(mod)
        return True
    except Exception:
        return False


# --------------------------------------------------------------------------------------------------------------------------------------
# log comparison (numbers agree to 1.5 units of the last printed digit)
# --------------------------------------------------------------------------------------------------------------------------------------
NUM = re.compile(r'[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?')


def tok_tol(s):
    """1.5 units in the last printed digit of the number string s."""
    m = re.match(r'[-+]?(\d*)\.?(\d*)(?:[eE]([-+]?\d+))?$', s)
    if not m:
        return 0.0
    frac = m.group(2) or ''
    ex = int(m.group(3)) if m.group(3) else 0
    return 1.5 * 10.0 ** (ex - len(frac))


TIMING = re.compile(r'(?<![\w.])\d+(?:\.\d+)?\s?s\b(?![-\w(])')      # elapsed times printed by some scripts ("471 5s", "took 1370 s") are not reproducible: masked before comparing


def strip_warnings(lines):
    """Python warnings that a script writes to stderr (two lines: 'path:line: SomeWarning: text' and the source line) are not part of the comparison (they carry paths of the machine)"""
    out = []
    skip = False
    for l in lines:
        if skip and l.startswith(' '):
            skip = False
            continue
        skip = False
        if re.search(r'\w+Warning: ', l):
            skip = True
            continue
        out.append(l)
    return out


def compare_text(new, ref, atol=0.0, rtol=0.0):
    """-> ('identical'|'numeric'|'differs', detail)"""
    if new == ref:
        return 'identical', ''
    a = strip_warnings([TIMING.sub('<t>s', l.rstrip()) for l in new.replace('\r', '').rstrip().split('\n')])
    b = strip_warnings([TIMING.sub('<t>s', l.rstrip()) for l in ref.replace('\r', '').rstrip().split('\n')])
    if a == b:
        return 'identical', 'trailing blanks only'
    if len(a) != len(b):
        return 'differs', f'{len(a)} lines against {len(b)} shipped'
    nd = 0
    first = ''
    for i, (x, y) in enumerate(zip(a, b)):
        if x == y:
            continue
        tx, ty = NUM.findall(x), NUM.findall(y)
        sx, sy = NUM.sub('#', x), NUM.sub('#', y)
        ok = (sx == sy and len(tx) == len(ty))
        if ok:
            for p, q in zip(tx, ty):
                try:
                    dpq = abs(float(p) - float(q))
                    if dpq > max(tok_tol(p), tok_tol(q)) * (1 + 1e-9) and dpq > atol and dpq > rtol * max(abs(float(p)), abs(float(q))):
                        ok = False
                        break
                except ValueError:
                    ok = False
                    break
        if not ok:
            nd += 1
            if not first:
                first = f'line {i+1}: new "{x[:90]}" shipped "{y[:90]}"'
    if nd == 0:
        return 'numeric', 'last-digit differences only'
    return 'differs', f'{nd} of {len(a)} lines differ; first: {first}'


# --------------------------------------------------------------------------------------------------------------------------------------
# jobs that do not import scipy (static scan of the imports of their scripts); a job that nevertheless needs a missing package is reported SKIPPED from its error output
NO_SCIPY = set('slaving_pde_m1,slaving_pde_M3,rho_check,bounded_aniso,bounded_slaving,front_m1_B0.0003,plateau_m1_B0.0003,front_m1_B0.003,plateau_m1_B0.003,front_m1_B0.03,plateau_m1_B0.03,plateau_m2_B0.0003,front_m2_B0.0003,plateau_m2_B0.003,front_m2_B0.003,plateau_m2_B0.03,front_m2_B0.03,endpoint_m1_B0.003_v200,cmp_add_B0.003,cmp_add_B0.0003,width_m1,linbound,scan_zm,tailfit_results,s2a_results,convergence_h,nearext,np_lin_b'.split(','))


def run_job(job, mode):
    jid = job['id']
    out = os.path.join(LOGS, jid + '.log')
    err = os.path.join(LOGS, jid + '.err')
    rec = dict(id=jid, cmd=job['cmd'], cwd=job['cwd'], tier=job['tier'], status='', wall=0.0, cpu=0.0, rc=None, cmp='', cmp_detail='', ref=job['ref'])
    miss = [n for n in job['needs'] if not have(n) and not (n == 'scipy' and jid in NO_SCIPY)]
    if miss:
        imp = os.path.join(VER, 'imported', jid + '.log')
        if set(miss) <= {'sympy', 'mpmath'} and os.path.exists(imp):
            # the log of this job was produced by this script on another machine that has sympy/mpmath (verification/imported/PROVENANCE.txt); it is checked like a regenerated log
            shutil.copyfile(imp, out)
            rec['status'] = 'IMPORTED'
            rec['cmp_detail'] = 'log imported from verification/imported (missing here: %s)' % ', '.join(miss)
            ref = job['ref']
            if ref and os.path.exists(os.path.join(ROOT, ref)):
                rec['cmp'], d = compare_text(open(out, errors='replace').read(), open(os.path.join(ROOT, ref), errors='replace').read(), job.get('atol', 0.0), job.get('rtol', 0.0))
                rec['cmp_detail'] += '; ' + d
            return rec
        rec['status'] = 'SKIPPED'
        rec['cmp_detail'] = 'missing package(s): ' + ', '.join(miss)
        return rec
    t0 = time.time()
    cmd = job['cmd'].replace('$PY', '"$PY"')
    tmp = out + '.tmp'
    ru = None
    rc = -9
    try:
        if job.get('work'):
            os.makedirs(os.path.join(ROOT, job['cwd']), exist_ok=True)
        with open(tmp, 'w') as fo, open(err + '.tmp', 'w') as fe:
            p = subprocess.Popen(['bash', '-c', cmd], cwd=os.path.join(ROOT, job['cwd']), stdout=fo, stderr=fe, env=job_env(), start_new_session=True)
            limit = job.get('timeout', 8 * 3600)
            while True:
                pid, st, ru = os.wait4(p.pid, os.WNOHANG)
                if pid:
                    rc = os.waitstatus_to_exitcode(st)
                    break
                if time.time() - t0 > limit:
                    os.killpg(p.pid, 9)
                    os.wait4(p.pid, 0)
                    rc = -9
                    break
                time.sleep(0.2)
    except OSError as e:
        rc = -1
        open(tmp, 'a').write('OSError %s\n' % e)
    rec['wall'] = time.time() - t0
    rec['cpu'] = (ru.ru_utime + ru.ru_stime) if ru else 0.0     # CPU seconds of the job (all its processes), independent of machine load
    rec['rc'] = rc
    _mv(tmp, out)
    for fn_ in (out, err + '.tmp'):                    # no absolute paths in the saved logs (Python warnings print the path of the script)
        try:
            t_ = open(fn_, errors='replace').read()
            if ROOT in t_:
                open(fn_, 'w').write(t_.replace(ROOT + os.sep, '').replace(ROOT, '.'))
        except OSError:
            pass
    if os.path.getsize(err + '.tmp') > 0:
        _mv(err + '.tmp', err)
    else:
        _rm(err + '.tmp')
        if os.path.exists(err):
            _rm(err)
    new = open(out, errors='replace').read()
    errtxt = open(err, errors='replace').read() if os.path.exists(err) else ''
    mm = re.search(r"No module named '(scipy|sympy|mpmath|matplotlib|numpy)", errtxt)
    if rc != 0 and mm:
        rec['status'] = 'SKIPPED'                        # the job imports a package that is not installed (the needs= list of the job was incomplete)
        rec['cmp_detail'] = 'missing package(s): ' + mm.group(1)
    elif rc != 0:
        rec['status'] = 'FAILED'
        rec['cmp_detail'] = f'exit code {rc}; see verification/logs/{jid}.err'
    elif not new.strip():
        rec['status'] = 'FAILED'
        rec['cmp_detail'] = 'empty log'
    else:
        rec['status'] = 'OK'
    ref = job['ref']
    if ref and rec['status'] == 'OK':
        rp = os.path.join(ROOT, ref)
        if os.path.exists(rp):
            c, d = compare_text(new, open(rp, errors='replace').read(), job.get('atol', 0.0), job.get('rtol', 0.0))
            if job['cmp'] == 'text' and c == 'numeric':
                c = 'differs'
            rec['cmp'], rec['cmp_detail'] = c, d
        else:
            rec['cmp'], rec['cmp_detail'] = 'new', 'no shipped log'
    return rec


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group()
    g.add_argument('--quick', action='store_true')
    g.add_argument('--full', action='store_true')
    ap.add_argument('--jobs', type=int, default=int(os.environ.get('VERIFY_JOBS', '0')) or min(4, os.cpu_count() or 1))
    ap.add_argument('--only', default='', help='comma-separated substrings of job ids (development)')
    ap.add_argument('--no-build', action='store_true', help='skip compiling the C libraries (development)')
    ap.add_argument('--checks-only', action='store_true', help='do not run the jobs, evaluate the checks on the logs already in verification/logs')
    ap.add_argument('--list', action='store_true')
    args = ap.parse_args()
    mode = 'full' if args.full else 'quick'
    jobs = [j for j in JOBS + LONG_JOB_RECORDS() if (mode == 'full' or j['tier'] == 'quick') and (not args.only or any(o and o in j['id'] for o in args.only.split(',')))]
    if args.list:
        for j in jobs:
            print('%-6s %-34s %5ds  %s' % (j['tier'], j['id'], j['est'], j['cmd'][:100]))
        print('estimated one-core time: %.0f s' % sum(j['est'] for j in jobs))
        return 0
    os.makedirs(LOGS, exist_ok=True)
    t_start = time.time()
    recs = []
    if not args.checks_only:
        with open(os.path.join(LOGS, 'build.log'), 'a' if args.no_build else 'w') as lg:
            print('[verify] building C libraries ...' if not args.no_build else '[verify] build skipped', flush=True)
            build_ok = True if args.no_build else build_step(lg)
        if not build_ok:
            print('[verify] build FAILED (see verification/logs/build.log); jobs that need a compiled library will fail', flush=True)
        for stage in sorted(set(j['stage'] for j in jobs)):
            sj = [j for j in jobs if j['stage'] == stage]
            sj.sort(key=lambda j: -j['est'])
            print(f'[verify] stage {stage}: {len(sj)} jobs, {args.jobs} workers', flush=True)
            done = [0]
            lock = threading.Lock()

            def go(j):
                r = run_job(j, mode)
                with lock:
                    done[0] += 1
                    print('[verify] %3d/%d %-8s %-34s wall %6.1f s cpu %6.1f s  %s %s' % (done[0], len(sj), r['status'], r['id'], r['wall'], r['cpu'], r['cmp'], r['cmp_detail'][:80]), flush=True)
                return r
            with ThreadPoolExecutor(max_workers=args.jobs) as ex:
                recs += list(ex.map(go, sj))
    else:
        try:                                       # keep the timings and statuses of the previous run
            old = {r['id']: r for r in json.load(open(os.path.join(VER, 'jobs.json')))}
        except Exception:
            old = {}
        for j in jobs:
            op = os.path.join(LOGS, j['id'] + '.log')
            o = old.get(j['id'], {})
            st = o.get('status') if o.get('status') in ('OK', 'IMPORTED', 'SKIPPED', 'FAILED') else ('OK' if os.path.exists(op) else 'SKIPPED')
            if (not os.path.exists(op) or (os.path.getsize(op) == 0 and j['ref'] and st != 'FAILED')) and st in ('OK', 'IMPORTED'):
                st = 'SKIPPED'
            rec = dict(id=j['id'], cmd=j['cmd'], cwd=j['cwd'], tier=j['tier'], status=st, wall=o.get('wall', 0.0), cpu=o.get('cpu', 0.0), rc=0, cmp='', cmp_detail=o.get('cmp_detail', ''), ref=j['ref'])
            if st in ('OK', 'IMPORTED') and j['ref'] and os.path.exists(os.path.join(ROOT, j['ref'])):
                rec['cmp'], d = compare_text(open(op, errors='replace').read(), open(os.path.join(ROOT, j['ref']), errors='replace').read(), j.get('atol', 0.0), j.get('rtol', 0.0))
                rec['cmp_detail'] = d
            recs.append(rec)
    total_wall = time.time() - t_start
    # ---- checks
    sys.path.insert(0, VER)
    import importlib.util
    spec = importlib.util.spec_from_file_location('checks', os.path.join(VER, 'checks.py'))
    chk = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chk)
    shipped = {j['id']: j['ref'] for j in JOBS + LONG_JOB_RECORDS() if j['ref'] and j['id'] not in {r['id'] for r in recs}}
    byid = {r['id']: r for r in recs}
    if args.only:
        byid['__only__'] = True
    results = chk.evaluate(LOGS, ROOT, mode, byid, shipped)
    # a check that names a log without a generating job would silently disappear from the report: make it a failure
    known = {j['id'] for j in JOBS}
    for c in chk.CHECKS:
        bad = [lg for lg in c['log'].split('+') if lg not in known]
        if bad:
            results.append(dict(id=c['id'], quantity=c['quantity'], loc=c['loc'], paper=c['paper'], tol='', reason='', computed='n/a', status='FAIL',
                                detail='no job produces the log ' + ','.join(bad)))
    # reproduction checks (regenerated log = shipped log)
    for r in recs:
        if r['ref'] and r['status'] in ('OK', 'IMPORTED', 'FAILED', 'SKIPPED'):
            st = 'PASS' if r['cmp'] in ('identical', 'numeric') else ('SKIPPED' if r['status'] == 'SKIPPED' else 'FAIL')
            results.append(dict(id='repro:' + r['id'], quantity='regenerated log equals the shipped log', loc=r['ref'], paper='shipped log',
                                tol='last printed digit x 1.5', reason='deterministic scripts; the shipped log is the evidence the manuscript cites', computed=r['cmp'] or r['status'],
                                status=st, detail=r['cmp_detail']))
    # ---- write outputs
    write_outputs(mode, recs, results, total_wall)
    npass = sum(1 for x in results if x['status'] == 'PASS')
    nfail = sum(1 for x in results if x['status'] == 'FAIL')
    nskip = sum(1 for x in results if x['status'] == 'SKIPPED')
    nrun = npass + nfail
    jfail = [r['id'] for r in recs if r['status'] == 'FAILED']
    print()
    for x in results:
        if x['status'] == 'FAIL':
            print('FAIL  %-44s %s: computed %s, paper %s (tol %s)' % (x['id'], x['loc'], x['computed'], x['paper'], x['tol']))
    for j in jfail:
        print('JOB FAILED', j)
    if nskip:
        print(f'{nskip} checks SKIPPED (missing Python package; see verification/REPORT.md)')
    if nfail or jfail:
        print(f'RESULT {REPO}: FAILED {nfail} of {nrun} checks, {len(jfail)} jobs failed ({mode}{" subset --only " + args.only if args.only else ""})')
        return 1
    if nskip:
        print(f'RESULT {REPO}: INCOMPLETE {npass}/{nrun + nskip} checks ({nskip} skipped: missing package) ({mode}{" subset --only " + args.only if args.only else ""})')
        return 3
    print(f'RESULT {REPO}: PASSED {npass}/{nrun} checks ({mode}{" subset --only " + args.only if args.only else ""})')
    return 0


def LONG_JOB_RECORDS():
    return []


def env_info():
    d = {}
    d['python'] = sys.version.split()[0]
    for m in ('numpy', 'scipy', 'sympy', 'mpmath', 'matplotlib'):
        try:
            d[m] = importlib.import_module(m).__version__
        except Exception:
            d[m] = 'not installed'
    try:
        d['gcc'] = subprocess.run(['gcc', '--version'], capture_output=True, text=True).stdout.split('\n')[0]
    except Exception:
        d['gcc'] = 'not found'
    d['platform'] = platform.platform()
    d['machine'] = platform.machine()
    d['cpus'] = os.cpu_count()
    d['date'] = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    return d


def write_outputs(mode, recs, results, total_wall):
    env = env_info()
    json.dump(dict(repo=REPO, mode=mode, environment=env, wall_seconds=round(total_wall, 1), checks=results), open(os.path.join(VER, 'expected.json'), 'w'), indent=1)
    allrecs = {r['id']: r for r in recs}
    if '--only' in sys.argv:                       # a development subset run must not erase the records of the other jobs
        try:
            for r in json.load(open(os.path.join(VER, 'jobs.json'))):
                allrecs.setdefault(r['id'], r)
        except Exception:
            pass
    json.dump([{k: (round(v, 1) if isinstance(v, float) else v) for k, v in r.items()} for r in sorted(allrecs.values(), key=lambda r: r['id'])], open(os.path.join(VER, 'jobs.json'), 'w'), indent=1)
    npass = sum(1 for x in results if x['status'] == 'PASS')
    nfail = sum(1 for x in results if x['status'] == 'FAIL')
    nskip = sum(1 for x in results if x['status'] == 'SKIPPED')
    L = []
    L.append(f'# Verification report: {REPO} ({mode})\n')
    L.append(f'**Result: {npass} PASS, {nfail} FAIL, {nskip} SKIPPED** of {len(results)} checks.  Total wall time {total_wall/60:.1f} min.\n')
    L.append('## Environment\n')
    for k in ('python', 'numpy', 'scipy', 'sympy', 'mpmath', 'matplotlib', 'gcc', 'platform', 'machine', 'cpus', 'date'):
        L.append(f'- {k}: {env[k]}')
    L.append('')
    imp = [r['id'] for r in recs if r['status'] == 'IMPORTED']
    if imp:
        L.append('Jobs whose log was imported from `verification/imported/` (they need sympy/mpmath, which are not installed on this machine; the logs were produced by the same scripts on another machine, see `verification/imported/PROVENANCE.txt`): ' + ', '.join(imp) + '.\n')
    L.append('## Checks\n')
    L.append('Each row: a quantity quoted in `main.tex`, its location, the value in the manuscript, the tolerance (with the reason), the value computed from the regenerated log, PASS/FAIL. '
             'Tolerance rule unless stated: half a unit of the last quoted digit of the manuscript value plus half a unit of the last printed digit of the log (rounding only); '
             'for bounds ("at most", "below") the computed value must satisfy the bound.\n')
    L.append('| status | id | location | paper | tolerance (reason) | computed |')
    L.append('|---|---|---|---|---|---|')
    for x in results:
        L.append('| %s | %s | %s | %s | %s | %s |' % (x['status'], x['id'], str(x['loc']).replace('|', '/'), str(x['paper']).replace('|', '/'), (str(x['tol']) + (' (' + x['reason'] + ')' if x.get('reason') else '')).replace('|', '/'), str(x['computed']).replace('|', '/')))
    L.append('')
    fixes = [x for x in results if x.get('fix')]
    if fixes:
        L.append('## Proposed corrections of the manuscript (the script reproduces the corrected value; `main.tex` itself was not edited)\n')
        for x in fixes:
            L.append('- `%s` (%s): `%s` -> `%s`' % (x['id'], str(x['loc']).replace('|', '/'), x['fix'][0], x['fix'][1]))
        L.append('')
    L.append('## Scripts run\n')
    L.append('| job | status | wall s | cpu s | log comparison with the shipped log | log |')
    L.append('|---|---|---|---|---|---|')
    for r in sorted(recs, key=lambda r: r['id']):
        L.append('| %s | %s | %.1f | %.1f | %s %s | verification/logs/%s.log |' % (r['id'], r['status'], r['wall'], r['cpu'], r['cmp'], r['cmp_detail'][:70].replace('|', '/'), r['id']))
    L.append('')
    open(os.path.join(VER, 'REPORT.md'), 'w').write('\n'.join(L))


if __name__ == '__main__':
    sys.exit(main())
