#!/bin/bash
export QTG_CODE=/mnt/user-data/outputs/sources/paperF_qtg_dynamics/code
export PYTHONPATH=$QTG_CODE:/tmp/claude-0/-home-claude/717c308b-4c66-5933-99e1-d42d1016a975/scratchpad/ehq
cd "$(dirname "$0")/.."
# args: model then list "m0:mt"
model=$1; shift
for a in "$@"; do m0=${a%%:*}; mt=${a##*:}; python3 strong_table.py $model $m0 $mt 0.1 0.1 2900 sp/t${model}_m${m0}_mt${mt}.npz >> sp/runst2_${model}_$$.log 2>&1; done
