#!/bin/bash
# Regenerates the k=2 (non-compact data) results of Paper F, Sec. "Collapse-generated horizon tails" (about 25 min on two cores; code-E runs ~7 min each, separate, see below).
cd "$(dirname "$0")"; ./build.sh; mkdir -p logs npdata ce
( python3 nplin.py 0 5 0.2 12800; python3 nplin.py 1 5 0.2 12800 ) > logs/nplin.log 2>&1; python3 nplin_fit.py nplin_m0_M5_h0.2.npz nplin_m1_M5_h0.2.npz >> logs/nplin.log
for a in "1 1.0" "1 -1.0" "1 0.0" "0 1.0" "1 0.5" "1 2.0"; do set -- $a; python3 np_nl.py $1 $2 0.1 0.1 60 12800 npdata/np_m$1_b$2_h1.npz > npdata/np_m$1_b$2_h1.log 2>&1; done
python3 np_fit.py npdata/np_m1_b1.0_h1.npz npdata/np_m0_b1.0_h1.npz npdata/np_m1_b-1.0_h1.npz npdata/np_m1_b0.5_h1.npz npdata/np_m1_b2.0_h1.npz > logs/np_fit.log
python3 np_lin_b.py > logs/np_lin_b.log
python3 overlap_np.py > logs/overlap_np.log 2>&1
for a in "1 1.0" "1 0.8" "1 1.2" "0 1.0"; do set -- $a; python3 linear_q.py $1 $2 0.2 12800; done > logs/linear_q.log 2>&1
# tables for code E (h_N=0.05, h_L=0.1, v_1=60, to v=2500), then code E (needs ../setup.sh, QTG_CODE and PYTHONPATH as in README):
python3 np_nl.py 1 1.0 0.05 0.1 60 2500 ce/np_m1_b1_v60.npz; python3 np_nl.py 1 0.1 0.05 0.1 60 2500 ce/np_m1_b0.1_v60.npz
#   cd ce; TAG=np1  python3 ../gen_c.py np_m1_b1_v60.npz 1500 0.2:0.2 0.2:0.1 ; TAG=np01 python3 ../gen_c.py np_m1_b0.1_v60.npz 1500 0.2:0.2
#   (gen_c.py writes genc_<TAG>_hs0.2_hv*_v1500.json into ce/); then python3 an_k.py ce/genc_np1_hs0.2_hv0.2_v1500.json 2 ; python3 conv_c.py <hv0.2.json> <hv0.1.json> ; python3 fig_collapse_k2.py
