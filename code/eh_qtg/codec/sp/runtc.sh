#!/bin/bash
# collapse with scalar charge at infinity: runtc.sh tag model m0 mt c vrel
export QTG_CODE=/mnt/user-data/outputs/sources/paperF_qtg_dynamics/code
export PYTHONPATH=$QTG_CODE:/tmp/claude-0/-home-claude/717c308b-4c66-5933-99e1-d42d1016a975/scratchpad/ehq
cd "$(dirname "$0")/.."
TAIL_C=$5 python3 strong_table.py $2 $3 $4 0.1 0.1 $6 sp/tc_$1.npz > sp/runtc_$1.log 2>&1
