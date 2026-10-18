#!/bin/bash
export QTG_CODE=/mnt/user-data/outputs/sources/paperF_qtg_dynamics/code
export PYTHONPATH=$QTG_CODE:/tmp/claude-0/-home-claude/717c308b-4c66-5933-99e1-d42d1016a975/scratchpad/ehq
cd "$(dirname "$0")"
for P in "$@"; do PU0MODE=zero TAG=P$P python3 ../gen_c.py pt_P$P.npz 1000 0.2:0.2 > run_P$P.log 2>&1; done
