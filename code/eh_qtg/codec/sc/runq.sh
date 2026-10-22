#!/bin/bash
export QTG_CODE="$(cd "$(dirname "$0")/../../.." && pwd)"     # code/ directory of the repository
export PYTHONPATH=$QTG_CODE:$QTG_CODE/eh_qtg${PYTHONPATH:+:$PYTHONPATH}
cd "$(dirname "$0")"
for P in "$@"; do PU0MODE=zero TAG=P$P python3 ../gen_c.py pt_P$P.npz 1000 0.2:0.2 > run_P$P.log 2>&1; done
