#!/bin/bash
# code E on a strong-pulse table: rune.sh table.npz tag mass v1 hs:hv
export QTG_CODE=/mnt/user-data/outputs/sources/paperF_qtg_dynamics/code
export PYTHONPATH=$QTG_CODE:/tmp/claude-0/-home-claude/717c308b-4c66-5933-99e1-d42d1016a975/scratchpad/ehq
cd "$(dirname "$0")"
MASS=$3 PU0MODE=zero TAG=$2 python3 ../gen_c.py $1 $4 $5 > run_$2.log 2>&1
