#!/bin/bash
# hs=0.1, hv=0.2 mesh check: runs.sh P
export QTG_CODE="$(cd "$(dirname "$0")/../../.." && pwd)"     # code/ directory of the repository
export PYTHONPATH=$QTG_CODE:$QTG_CODE/eh_qtg${PYTHONPATH:+:$PYTHONPATH}
cd "$(dirname "$0")"
PU0MODE=zero TAG=P$1 python3 ../gen_c.py pt_P$1.npz 1000 0.1:0.2 > run_P$1_hs0.1.log 2>&1
