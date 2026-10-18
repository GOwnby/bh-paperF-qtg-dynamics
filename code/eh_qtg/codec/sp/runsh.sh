#!/bin/bash
# pulse-shape variants: runsh.sh tag PULSE_A PULSE_B PULSE_V1 model:m0:mt ...
export QTG_CODE=/mnt/user-data/outputs/sources/paperF_qtg_dynamics/code
export PYTHONPATH=$QTG_CODE:/tmp/claude-0/-home-claude/717c308b-4c66-5933-99e1-d42d1016a975/scratchpad/ehq
cd "$(dirname "$0")/.."
tag=$1; export PULSE_A=$2 PULSE_B=$3 PULSE_V1=$4; shift 4
for a in "$@"; do IFS=: read mo m0 mt <<< "$a"; python3 strong_table.py $mo $m0 $mt 0.1 0.1 2900 sp/sh_${tag}_m${mo}_${m0}_${mt}.npz >> sp/runsh_$tag.log 2>&1; done
