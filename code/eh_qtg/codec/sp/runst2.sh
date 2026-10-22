#!/bin/bash
export QTG_CODE="$(cd "$(dirname "$0")/../../.." && pwd)"     # code/ directory of the repository
export PYTHONPATH=$QTG_CODE:$QTG_CODE/eh_qtg${PYTHONPATH:+:$PYTHONPATH}
cd "$(dirname "$0")/.."
# args: model then list "m0:mt"
model=$1; shift
for a in "$@"; do m0=${a%%:*}; mt=${a##*:}; python3 strong_table.py $model $m0 $mt 0.1 0.1 2900 sp/t${model}_m${m0}_mt${mt}.npz >> sp/runst2_${model}_$$.log 2>&1; done
