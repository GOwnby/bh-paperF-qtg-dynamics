#!/bin/bash
# Regenerates every log and data file of Sections 9-12 of Paper F (about 90 minutes on one core; the runs are independent and can be started in parallel).
# usage: bash setup.sh && bash run_eh.sh
set -e
cd "$(dirname "$0")"; mkdir -p logs data
export QTG_CODE="$(cd .. && pwd)"
J=data
# --- validation of the pipeline
python3 static_gen.py                           > logs/static_gen.log
python3 t_static_q.py                           > logs/t_static_free.log        # free evolution, U<=10: non-finite
python3 t_static_free.py                        > logs/t_static_free_U3.log     # free evolution, U<=3
for M in 1 2 3; do MODE=$M python3 t_static_cy.py > logs/t_static_cy_mode$M.log; done
python3 t_static_b.py 1.0                       > logs/t_static_b_a1.log        # m=5 (poor, not used)
MASS=1.5 python3 t_static_b.py 1.0              > logs/t_static_b_a1_M1.5.log
python3 free_vs_con.py                          > logs/free_vs_con.log
python3 check_curv_static.py                    > logs/check_curv_static.log
python3 check_ruv_q.py 0.003 110 0.05 0.025 0.0125 -- 40 60 80 100 > logs/check_ruv_B0.003.log
# --- four-mesh runs (gen_q.py model L2 B k v1 h1 h2 ...), JSON written in the current directory then moved to data/
H="0.05 0.025 0.0125 0.00625"
for B in 0.0003 0.003 0.03; do python3 gen_q.py 1 1.0 $B 1.5 110 $H > logs/gq_B$B.log; done
for B in 0.003 0.03;        do python3 gen_q.py 1 1.0 $B 1.5 200 $H > logs/gq_B${B}_v200.log; done
for B in 0.0003 0.003 0.03; do MASS=1.5 python3 gen_q.py 2 1.0 $B 1.5 110 $H > logs/gq_b_a1_M1.5_B$B.log; done
mv -f genq_*.json $J/
# --- analyses (Romberg extrapolation inside analyze_q.py)
KM=(0.7956493155 0.7956534352 0.7960655916)      # kappa_-(m_f) of the Hayward runs, from kap_check
i=0
for B in 0.0003 0.003 0.03; do
  F=$J/genq_m1_B${B}_k1.5_v110.json
  python3 late_q.py $F 1 1.0 60 70 80 90 100 108 > logs/late_m1_B$B.log
  python3 kernel_ratio_q.py $F                     > logs/kernel_ratio_B$B.log
  python3 masslaw_q.py $F 1 1.0                    > logs/masslaw_m1_B$B.log
  python3 kap_check.py $F                          > logs/kap_check_m1_B$B.log
  python3 curv_q.py $F                             > logs/curv_m1_B$B.log
  python3 front_q.py $F 0.048968742118989196       > logs/front_m1_B$B.log
  python3 width_q.py $F                            > logs/width_m1_B$B.log
  python3 plateau_q.py $F ${KM[$i]}                > logs/plateau_m1_B$B.log
  i=$((i+1))
done
cat logs/width_m1_B*.log > logs/width_m1.log
for B in 0.003 0.03; do python3 late_q.py $J/genq_m1_B${B}_k1.5_v200.json 1 1.0 60 80 100 120 140 160 180 198 > logs/late_m1_B${B}_v200.log; done
python3 endpoint_q.py $J/genq_m1_B0.003_k1.5_v200.json > logs/endpoint_m1_B0.003_v200.log
python3 curv_terms_q.py $J/genq_m1_B0.003_k1.5_v200.json 80 100 120 140 160 > logs/curv_terms_m1_B0.003.log
python3 cmp_add.py $J/genq_m1_B0.003_k1.5_v110.json 0.003   > logs/cmp_add_B0.003.log
python3 cmp_add.py $J/genq_m1_B0.0003_k1.5_v110.json 0.0003 > logs/cmp_add_B0.0003.log
KB=(0.79700775 0.79701569 0.79780932)            # kappa_-(m_f) of the bounded runs, from kap_check_b
i=0
for B in 0.0003 0.003 0.03; do
  F=$J/genq_m2_a1_M1.5_B${B}_k1.5_v110.json
  python3 late_q.py $F 2 1.0 40 50 60 70 80 90 100 108 > logs/late_m2_M1.5_B$B.log
  python3 kap_check_b.py $F 1.5 1.0                      > logs/kap_check_m2_M1.5_B$B.log
  python3 masslaw_q.py $F 2 1.0                          > logs/masslaw_m2_M1.5_B$B.log
  python3 plateau_q.py $F ${KB[$i]} 20                   > logs/plateau_m2_B$B.log
  python3 front_q.py $F 0.16135947                       > logs/front_m2_B$B.log
  i=$((i+1))
done
python3 fig_eh.py
# --- Paper F, Sec. 10-11 additions (anisotropic refinement; each run takes minutes to ~1.5 h; start long jobs with `setsid nohup`)
# usage: gen_q2.py model L2 B k v1 hs:hv [hs:hv ...]   (the levels used for each file are the first lines of logs/g2_*.log; v1 = 300-400 for Hayward)
# example (m=3 inner profile, as run):
#   MASS=3 python3 gen_q2.py 1 1.0 0.003 1.5 250 0.05:0.0125 0.05:0.00625 0.05:0.003125 0.05:0.0015625 > logs/g2_M3_v250.log
# merge files with disjoint levels: python3 merge_levels.py out.json a.json b.json
# analyses (arguments: see the script headers and the logs): endpoint_table.py, ktable.py, hs_extrap.py, vb_law.py, slaving_pde.py, slaving_prof.py, gpred_q.py, modecmp.py, c3_sensitivity.py, check_compat_pole.py
# --- derivation of the null-coordinate equations from the reduced 2D Horndeski action (exact arithmetic, about 10 minutes)
python3 action_check.py 10  > logs/action_check.log     # static-reduction action; Raychaudhuri-coefficient propagation test
python3 action_check2.py 6  > logs/action_check2.log    # literature action (a_2 = 0)
python3 action_check3.py 4  > logs/action_check3.log    # literature action with a psi^2 term (logarithm in G_4)
# --- code B, reduction check, tidal analysis (Paper F, Secs. 'A second implementation', 'curvature to v=400'); minutes to ~15 min per run on one core
python3 lift_check_4d.py 0 > logs/lift_check_4d_seed0.log   # (the shipped log has seeds 0-4)
(cd codeb && mkdir -p logs data && python3 t_static_b4.py > logs/t_static_b4.log && PROJ=0 python3 t_static_b4.py > logs/t_static_b4_proj0.log
  python3 gen_b.py 1 1.0 0.003 1.5 400 0.05:0.1 0.05:0.05                      # -> genb_p1_hs0.05_m1_B0.003_k1.5_v400.json (rename to data/genb_hs0.05_v400.json)
  python3 gen_b.py 1 1.0 0.003 1.5 600 0.05:0.0125                              # 630 s; first non-finite v = 477
  python3 cmp_table.py > logs/cmp_table.log; python3 kstudy.py data/genb_hs0.05_v600.json 0.0125 > logs/kstudy_v600.log
  python3 tidal.py data/genb_hs0.05_v600.json 0.0125 400 data/genb_hs0.05_v480.json 0.025 > logs/tidal_v600.log )

# --- code E (Paper F Secs. 'Why the window closes ...', 'The seed of the late-time departure'): see README item 12; the data shipped in codee/data are thinned copies (python3 thin_data.py in.json out.json) of these runs
# (cd codee && python3 gen_e.py 1 1.0 3e-3 1.5 1500 0.2:0.1 ; 1200 with 0.2:0.05, 0.1:0.1; k in 0.5 1 2 3 and B=3e-4,3e-2 with v1=1200; MASS=3 v1=700; MASS=10 v1=2000; gen_el.py (long double) v1=1200 ; 2-5 min each;
#  seed series: DELTA0_OFFSET=eps python3 gen_e.py 1 1.0 3e-3 1.5 1000 0.2:0.1 for eps = 0, 1e-15, 1e-14, 1e-13, 1e-12)
# (cd codee && python3 t_static_e.py > logs/t_static_e.log; python3 mech_vb.py 600 3e-3 1.5; python3 vb_prediction.py; bash scans.sh > logs/scans.log; python3 conv_e.py > logs/conv_e.log; python3 conv_e2.py > logs/conv_e2.log; python3 seed_amplitude.py > logs/seed_amplitude.log; python3 kstudy2.py data/gene_p1_hs0.2_m1_B0.003_k1.5_v1500_ray2.json 0.1 1400 > logs/kstudy2_double_v1500.log)
