#!/bin/bash
# code E on a strong-pulse table: rune.sh table.npz tag mass v1 hs:hv
export QTG_CODE="$(cd "$(dirname "$0")/../../.." && pwd)"     # code/ directory of the repository
export PYTHONPATH=$QTG_CODE:$QTG_CODE/eh_qtg${PYTHONPATH:+:$PYTHONPATH}
cd "$(dirname "$0")"
MASS=$3 PU0MODE=zero TAG=$2 python3 ../gen_c.py $1 $4 $5 > run_$2.log 2>&1
