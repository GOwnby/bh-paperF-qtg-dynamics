#!/bin/bash
# collapse with scalar charge at infinity: runtc.sh tag model m0 mt c vrel
export QTG_CODE="$(cd "$(dirname "$0")/../../.." && pwd)"     # code/ directory of the repository
export PYTHONPATH=$QTG_CODE:$QTG_CODE/eh_qtg${PYTHONPATH:+:$PYTHONPATH}
cd "$(dirname "$0")/.."
TAIL_C=$5 python3 strong_table.py $2 $3 $4 0.1 0.1 $6 sp/tc_$1.npz > sp/runtc_$1.log 2>&1
