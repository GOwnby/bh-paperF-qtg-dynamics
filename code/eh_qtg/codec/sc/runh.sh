#!/bin/bash
export QTG_CODE=/mnt/user-data/outputs/sources/paperF_qtg_dynamics/code
export PYTHONPATH=$QTG_CODE:/tmp/claude-0/-home-claude/717c308b-4c66-5933-99e1-d42d1016a975/scratchpad/ehq
cd "$(dirname "$0")"
PU0MODE=zero TAG=P$1 python3 ../gen_c.py pt_P$1.npz 1000 0.2:0.1 > run_P$1_hv0.1.log 2>&1
