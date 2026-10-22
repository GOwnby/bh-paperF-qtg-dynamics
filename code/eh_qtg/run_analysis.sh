#!/bin/bash
# Analysis logs of Paper F (Sections 9-14) that run_eh.sh does not produce: every command below regenerates one shipped log from shipped data.
# Each result is written to $OUT/<path of the shipped log> and compared with the shipped log:  "same" = identical text, "differs" = see "Status of the re-runs" in code/README.md
# (older versions of a script, extra rows, a missing input table; the quoted numbers agree).  Nothing in the shipped tree is overwritten.
#   usage:  bash setup.sh; bash codec/restore_archive.sh; bash run_analysis.sh            (default part; the elapsed time of each entry is printed; measured times: code/README.md)
#           ONLY=endpoint bash run_analysis.sh                                          (only the entries whose log name contains the string)
#           RUN_LONG=1 bash run_analysis.sh                                              (also starts the PDE and collapse runs that make the data; hours, see the list at the end)
set -u
cd "$(dirname "$0")"; HERE=$PWD
export QTG_CODE="$(cd .. && pwd)"; export PYTHONPATH=$QTG_CODE:$HERE${PYTHONPATH:+:$PYTHONPATH}
OUT=${OUT:-$HERE/rerun_logs}; mkdir -p "$OUT"
mk() {   # mk <shipped log (path relative to eh_qtg)> <directory to run in> <command ...>   (stdout -> log, stderr -> log.err)
  local ref=$1 dir=$2; shift 2; local out="$OUT/$ref"
  if [ -n "${ONLY:-}" ] && [[ $ref != *$ONLY* ]]; then return; fi       # ONLY=<substring of a log name> runs only the matching entries
  mkdir -p "$(dirname "$out")"
  local t0=$SECONDS
  ( cd "$dir" && "$@" ) > "$out" 2> "$out.err"
  local dt=$((SECONDS-t0))
  if diff -q --strip-trailing-cr "$ref" "$out" > /dev/null 2>&1; then echo "same     $ref   (${dt} s)"; else echo "differs  $ref   (${dt} s)"; fi
}
G=genq2_hs0.05_m1                       # anisotropic runs in data/ (h_s = 0.05, h_v halved), Hayward h, m = 5

# ---- 1. anisotropic constrained runs, Sections 10-11 (inputs: data/genq2_*.json; run in data/) ----------------------------------------------
mk logs/endpoint_B0.0003.log       data env VB_LAW=1 python3 ../endpoint_table.py ${G}_B0.0003_k1.5_v300.json 0.0003 1.5 0.795649
mk logs/endpoint_B0.003.log        data env VB_LAW=1 python3 ../endpoint_table.py ${G}_B0.003_k1.5_v400.json 0.003 1.5 0.795653
mk logs/endpoint_B0.003_merged.log data env VB_LAW=1 python3 ../endpoint_table.py ${G}_B0.003_k1.5_merged.json 0.003 1.5 0.795653    # header line of the shipped log is cut
mk logs/endpoint_B0.03.log         data env VB_LAW=1 python3 ../endpoint_table.py ${G}_B0.03_k1.5_v300.json 0.03 1.5 0.796066         # shipped log lacks the column dm/dv(closed) (older script)
mk logs/endpoint_k0.5.log          data python3 ../endpoint_table.py ${G}_B0.003_k0.5_v300.json 0.003 0.5 0.7957
mk logs/endpoint_k3.log            data env VB_LAW=1 python3 ../endpoint_table.py ${G}_B0.003_k3_v300.json 0.003 3 0.79565
mk logs/ktable.log                 logs python3 ../ktable.py                                   # reads the shipped logs/endpoint_*.log
mk logs/hs_extrap.log              data python3 ../hs_extrap.py ${G}_B0.003_k1.5_v400.json genq2_hs0.025_m1_B0.003_k1.5_v400.json 0.003 1.5 0.795653
mk logs/vb_law.log                 data python3 ../vb_law.py ${G}_B0.003_k1.5_v400.json ${G}_B0.03_k1.5_v300.json ${G}_B0.0003_k1.5_v300.json
mk logs/slaving_pde_m1.log         data python3 ../slaving_pde.py ${G}_B0.003_k1.5_merged.json         # shipped log stops at v = 280
mk logs/slaving_pde_M3.log         data python3 ../slaving_pde.py ${G}_M3_B0.003_k1.5_v250.json
mk logs/gpred_final.log            data python3 ../gpred_q.py 0.003 1.5 0.7957 ${G}_B0.003_k1.5_v400.json     # shipped log stops at v = 320
mk logs/rho_check.log              data python3 ../rho_check.py ${G}_B0.003_k1.5_v400.json            # shipped log is the first table only (older script)
mk logs/balance_check.log          data python3 ../balance_check.py ${G}_B0.003_k1.5_v400.json 0.7956534
mk logs/bounded_aniso.log          data python3 ../bounded_aniso.py genq2_hs0.05_m2_a1_M1.5_B0.0003_k1.5_v200.json
mk logs/bounded_slaving.log        data python3 ../bounded_slaving.py genq_m2_a1_M1.5_B0.0003_k1.5_v110.json genq_m2_a1_M1.5_B0.003_k1.5_v110.json
mk logs/curv_hv.log                data python3 ../curv_hv.py ${G}_B0.003_k1.5_v400.json 4 2 241
mk logs/curv_hv_B0.0003.log        data python3 ../curv_hv.py ${G}_B0.0003_k1.5_v300.json 4 2 281
mk logs/check_compat_pole.log      .    python3 check_compat_pole.py                               # 80-digit arithmetic
# The generators of slaving.log (slaving_q.py), modecmp.log, c3_sensitivity.log (PDE runs), errprof.log (err_prof.py), slaving_prof.log (prof2.py, then slaving_prof.py in the directory of its output)
# and seed_search.log (codee/seed_search.py) are shipped; bash ../../verify.sh (verify.py) runs every one of them (the hours-long ones with --full) and compares with the shipped logs.

# ---- 2. blow-up law (Sec. 'What limits the window'): native-resolution first non-finite sample (a PDE run each: minutes) ------------------------
mk vb1.log . bash -c "python3 blowup_probe.py 0.003 0.05 0.05 250; python3 blowup_probe.py 0.003 0.05 0.05 400"
# blow1.log-blow3.log are the longer printouts of isotropic runs h = 0.025, 0.0125, 0.00625 (first line: first non-finite v = 233.575, 261.9, 290.20625), written by
#   python3 blow_trace.py 0.003 300 h     (verify.py --full jobs blow1-blow3: about 2, 8 and 33 CPU-minutes with scipy)

# ---- 3. code B (codeb/) and code E (codee/) --------------------------------------------------------------------------------------------------
mk codeb/logs/cmp_AB_final.log codeb python3 cmp_AB_final.py
mk codeb/logs/cmp_hs.log       codeb python3 cmp_hs.py
mk codee/logs/kstudy2_longdouble_v1200.log codee python3 kstudy2.py data/genel_p1_hs0.2_m1_B0.003_k1.5_v1200_ray2.json 0.1 1100 0
mk codee/logs/mech_vb_B3e-3.log codee python3 mech_vb.py 600 3e-3 1.5       # writes mech_vb_B0.003_k1.5.npz here (3 MB); needed by vb_prediction.py
mk codee/logs/mech_vb_B3e-2.log codee python3 mech_vb.py 600 3e-2 1.5
mk codee/logs/mech_vb_B3e-4.log codee python3 mech_vb.py 600 3e-4 1.5
mk codee/logs/vb_prediction.log codee python3 vb_prediction.py
# vb_B3e-2_B3e-4.log: python3 first_nonfinite.py <genb_p1_hs0.05_m1_B0.03_k1.5_v330.json and the B = 3e-4 file>; these code-B run files were not archived (gen_b.py, see the end).

# ---- 4. collapse-generated tails (codec/): analyses of shipped tables and runs ----------------------------------------------------------------
export STRONG_DR=-0.3
T17="t_m5_mt5.01.npz t_m5_mt5.5.npz t_m5_mt6.5.npz t_m5_mt8.npz t_m5_mt10.npz t_m5_mt15.npz t_m5_mt25.npz t_m0_mt10.npz t_m2.5_mt10.npz t1_m2.5_mt12.5.npz t1_m5_mt20.npz t1_m7.5_mt15.npz t1_m10_mt20.npz t0_m0_mt10.npz t0_m2.5_mt10.npz t0_m5_mt10.npz t0_m5_mt25.npz"
TSH="sh_narrow_m0_0_10.npz sh_narrow_m0_2.5_10.npz sh_narrow_m0_5_10.npz sh_wide_m0_0_10.npz sh_wide_m0_2.5_10.npz sh_wide_m0_5_10.npz"
TLB="t_m0_mt10.npz t_m2.5_mt10.npz t_m5_mt10.npz t_m5_mt15.npz t_m5_mt25.npz t_m5_mt5.01.npz t_m5_mt5.5.npz t_m5_mt6.5.npz t_m5_mt8.npz t0_m0_mt10.npz t0_m2.5_mt10.npz t0_m5_mt10.npz t0_m5_mt25.npz t1_m10_mt20.npz t1_m2.5_mt12.5.npz t1_m5_mt20.npz t1_m7.5_mt15.npz tc_E_m0_5_c0.02.npz tc_H_m0_10_c0.02.npz tc_H_m0_5_c0.01.npz tc_H_m0_5_c0.02.npz tc_H_m0_5_c0.04.npz tc_H_m2.5_5_c0.02.npz $TSH w_dr-0.3_5.01.npz w_dr-0.3_5.5.npz"
[ -e codec/sp/t_m5_mt10.npz ] || { echo "run codec/restore_archive.sh first (tables of the second archive)"; exit 1; }
mk codec/sp/linbound.log     codec/sp python3 ../linbound.py $TLB                    # the shipped log has one more row only if tc_E_m0_5.npz (c = 0 table, in ../archive/.../strong, restored by restore_archive.sh) is present
mk codec/sp/weak_limit.log   codec/sp python3 ../weak_limit.py 4 12 20 t_m5_mt5.01.npz t_m5_mt5.5.npz t_m5_mt6.5.npz t_m5_mt8.npz
mk codec/sp/fit_corr.log     codec/sp python3 ../fit_corr.py 1000 2900 $T17 sh_narrow_m0_0_10.npz sh_narrow_m0_2.5_10.npz sh_narrow_m0_5_10.npz sh_wide_m0_2.5_10.npz sh_wide_m0_5_10.npz
mk codec/sp/strong_fit.log   codec/sp python3 ../strong_fit.py t_m5_mt5.01.npz t_m5_mt5.5.npz t_m5_mt6.5.npz t_m5_mt8.npz t_m5_mt10.npz t_m5_mt15.npz t_m5_mt25.npz t_m0_mt10.npz t_m2.5_mt10.npz t1_m2.5_mt12.5.npz t1_m5_mt20.npz t1_m7.5_mt15.npz t1_m10_mt20.npz t0_m5_mt10.npz t0_m2.5_mt10.npz t0_m5_mt25.npz t0_m0_mt10.npz
mk codec/sp/charge_row.log   codec/sp python3 ../charge_row.py 4 12 20 $T17 $TSH       # shipped log is from an earlier version of the script (Q_S, F_pred differ); horizon_ray.log below supersedes it
mk codec/sp/strong_conv.log  codec/sp python3 ../strong_conv.py c_h0.1_L0.1.npz c_h0.05_L0.1.npz c_h0.025_L0.1.npz c_h0.1_L0.05.npz
mk codec/sp/tc_fit.log       codec bash -c "python3 tc_fit.py sp/tc_*.npz"    # the shipped log also contains two Python warnings (stderr) and differs in one last digit
rowflux_all() { for a in 5:5.01 5:5.5 5:6.5 5:8 5:10 0:10 2.5:10 5:15 5:25; do m0=${a%%:*}; mt=${a##*:}; python3 rowflux.py 1 $m0 $mt 0.1 0.1 sp/t_m${m0}_mt${mt}.npz | grep -v direct; done; }
mk codec/sp/rowflux.log      codec rowflux_all                                          # about 1 minute per table
rowflux_direct() { for a in 10 25; do python3 rowflux.py 1 5 $a 0.1 0.1 sp/t_m5_mt${a}.npz | grep direct; done; }
mk codec/sp/rowflux_direct.log codec rowflux_direct                                     # the shipped file has the two lines prefixed by sp/rowflux_a.log: and sp/rowflux_b.log:
hr() { python3 ../horizon_ray.py 4 12 20 $T17; python3 ../horizon_ray.py 4 8 20 sh_narrow_m0_0_10.npz sh_narrow_m0_2.5_10.npz sh_narrow_m0_5_10.npz | tail -3; python3 ../horizon_ray.py 4 20 28 sh_wide_m0_0_10.npz sh_wide_m0_2.5_10.npz sh_wide_m0_5_10.npz | tail -3; }
mk codec/sp/horizon_ray.log  codec/sp hr
mk codec/sp/eik2.log         codec/sp python3 ../eik2.py 4 12 20 t_m5_mt5.01.npz t_m5_mt5.5.npz t_m5_mt6.5.npz t_m5_mt8.npz t_m5_mt10.npz t_m5_mt15.npz t_m5_mt25.npz t_m0_mt10.npz t_m2.5_mt10.npz t1_m2.5_mt12.5.npz t1_m5_mt20.npz t1_m7.5_mt15.npz t1_m10_mt20.npz
# codec/sp/eik_test.log: bash codec/sp/runeik.sh  (writes eik_test.log into $LOGDIR, default the current directory; same for runhr.sh -> horizon_ray.log and runeik2.sh -> eik2.log)
SC="genc_P0.01_hs0.2_hv0.2_v1000.json genc_P0.03_hs0.2_hv0.2_v1000.json genc_P0.05_hs0.2_hv0.2_v1000.json genc_P0.07_hs0.2_hv0.2_v1000.json genc_P0.08_hs0.2_hv0.2_v1000.json"
mk codec/sc/scan_zm.log      codec/sc python3 ../pscan_zm.py $SC
mk codec/sc/scan_an.log      codec/sc python3 ../pscan_an.py $SC
mk codec/sc/scan_summary.log codec/sc python3 ../pscan_summary.py 0.01 0.03 0.05 0.07 0.08      # needs scipy solve_ivp events (horizon_c)
mk codec/sc/horizon_map.log  codec/sc python3 ../horizon_map.py
mk codec/sc/vaidya_estimate.log codec/sc python3 ../vaidya_estimate.py
strongE() {   # Sec. 'Why the fold does not occur, and code E' (strong pulses, code E on the tables)
 echo "== m_f=25 resolution (hs,hv)=(0.2,0.2),(0.1,0.2),(0.2,0.1),(0.1,0.1)"
 F25="genc_S5to25_hs0.2_hv0.2_v4000.json genc_S5to25_hs0.1_hv0.2_v4000.json genc_S5to25_hs0.2_hv0.1_v4000.json genc_S5to25_hs0.1_hv0.1_v4000.json"
 python3 ../pscan_freeze.py 25 $F25; VS=4.4444 python3 ../pscan_zm.py $F25; VS=4.4444 python3 ../pscan_an.py $F25
 echo "== m_f=15"; python3 ../pscan_freeze.py 15 genc_S5to15_hs0.2_hv0.2_v2800.json; VS=3.1111 python3 ../pscan_zm.py genc_S5to15_hs0.2_hv0.2_v2800.json; VS=3.1111 python3 ../pscan_an.py genc_S5to15_hs0.2_hv0.2_v2800.json
 echo "== m_f=10 (S5to10, S0to10)"; F10="genc_S5to10_hs0.2_hv0.2_v2000.json genc_S0to10_hs0.2_hv0.2_v2000.json"
 python3 ../pscan_freeze.py 10 $F10; VS=2 python3 ../pscan_zm.py $F10; VS=2 python3 ../pscan_an.py $F10
}
mk codec/sp/strong_codeE.log codec/sp strongE
mk codec/logs/collapse_E.log codec python3 collapse_E.py
mk codec/conv_c.log          codec python3 conv_c.py data/collapseE_profile_hv0.2.json data/collapseE_profile_hv0.1.json    # last digit of one entry differs
mk codec/logs/conv_c_k2.log  codec python3 conv_c.py ce/genc_np1_hs0.2_hv0.2_v1500.json ce/genc_np1_hs0.2_hv0.1_v1500.json
# collapse_E_k2.log: an_k.py ce/genc_np1_hs0.2_hv0.2_v1500.json 2 <ray 0,1,2> (and the np01 run), sections concatenated
mk codec/bcr/tailfit_results.log codec/bcr bash -c "python3 tailfit.py base; B_ASYM=1.5 python3 tailfit.py asym1"     # B_ASYM=1.5 is the amplitude asymmetry of the asym1 runs (runtag.sh)
mk codec/bcr/s2a/s2a_results.log codec/bcr python3 s2a_an.py
mk codec/bcr/convergence_h.log   codec/bcr python3 convergence_h.py

# ---- 5. runs that make the data (hours; RUN_LONG=1).  Wall times are those printed in the shipped run logs (one core, scipy-based data construction). ----
# Output goes to $OUT/long/ (the shipped data/ and logs/ are not touched), except the codec/sc and codec/sp scripts, which write into their own directories.
if [ "${RUN_LONG:-0}" = 1 ]; then
  mkdir -p "$OUT/long" && cd "$OUT/long"
  # anisotropic Hayward runs (gen_q2.py model L2 B k v1 hs:hv ...; every level 1 min - 80 min; logs/g2_*.log lists the levels of the shipped files)
  python3 $HERE/gen_q2.py 1 1.0 0.003 1.5 400 0.05:0.05 0.05:0.025 0.05:0.0125 0.05:0.00625 0.05:0.003125 0.05:0.0015625 > g2_hs0.05_v400.log      # -> genq2_hs0.05_m1_B0.003_k1.5_v400.json
  python3 $HERE/gen_q2.py 1 1.0 0.003 1.5 400 0.025:0.05 0.025:0.025 0.025:0.0125 0.025:0.00625 0.025:0.003125 > g2_hs0.025_v400.log                # -> genq2_hs0.025_m1_B0.003_k1.5_v400.json
  python3 $HERE/gen_q2.py 1 1.0 0.003 1.5 360 0.05:0.00078125 0.05:0.000390625 > g2_A_v360.log                                                   # 2856 s + 4749 s; merge_levels.py joins it with the v400 file -> *_merged.json
  python3 $HERE/gen_q2.py 1 1.0 0.0003 1.5 300 0.05:0.0125 0.05:0.00625 0.05:0.003125 0.05:0.0015625 > g2_B0.0003_v300.log
  python3 $HERE/gen_q2.py 1 1.0 0.03 1.5 300 0.05:0.0125 0.05:0.00625 0.05:0.003125 0.05:0.0015625 > g2_B0.03_v300.log
  python3 $HERE/gen_q2.py 1 1.0 0.003 0.5 300 0.05:0.025 0.05:0.0125 0.05:0.00625 0.05:0.003125 > g2_k0.5_v300.log
  python3 $HERE/gen_q2.py 1 1.0 0.003 3 300 0.05:0.025 0.05:0.0125 0.05:0.00625 0.05:0.003125 > g2_k3_v300.log
  MASS=3 python3 $HERE/gen_q2.py 1 1.0 0.003 1.5 250 0.05:0.0125 0.05:0.00625 0.05:0.003125 0.05:0.0015625 > g2_M3_v250.log                     # the shipped g2_M3_v250.log lists three levels (the fourth was added later)
  MASS=1.5 python3 $HERE/gen_q2.py 2 1.0 0.0003 1.5 200 0.05:0.0125 0.05:0.00625 0.05:0.003125 0.05:0.0015625 > g2_b_B0.0003_v200.log           # bounded h, alpha = 1, m = 1.5
  # code B (needs libqtgb.so from setup.sh)
  python3 $HERE/codeb/gen_b.py 1 1.0 0.003 1.5 480 0.05:0.025 > gen_b_v480.log       # 227 s; output genb_*_v480.json (shipped as codeb/data/genb_hs0.05_v480.json)
  python3 $HERE/codeb/gen_b.py 1 1.0 0.003 1.5 600 0.05:0.0125 > gen_b_v600.log      # 627 s; shipped as codeb/data/genb_hs0.05_v600.json
  # collapse pulse scan and strong pulses (code E on the tables; write into codec/sc and codec/sp)
  ( cd $HERE/codec/sc && bash runq.sh 0.01 0.03 0.05 0.07 0.08 && bash runh.sh 0.08 && bash runs.sh 0.07 )
  ( cd $HERE/codec/sp && bash rune.sh t_m5_mt10.npz S5to10 10 2000 0.2:0.2 )     # the other runs: S0to10 (t_m0_mt10.npz), S5to15 (t_m5_mt15.npz, 15, 2800), S5to25 (t_m5_mt25.npz, 25, 4000, four meshes)
fi
echo "done; compare the 'differs' lines with code/README.md, section 'Status of the re-runs'"
