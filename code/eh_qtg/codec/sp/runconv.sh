#!/bin/bash
export QTG_CODE="$(cd "$(dirname "$0")/../../.." && pwd)"     # code/ directory of the repository
export PYTHONPATH=$QTG_CODE:$QTG_CODE/eh_qtg${PYTHONPATH:+:$PYTHONPATH}
cd "$(dirname "$0")/.."
python3 strong_table.py 1 5 10 0.1  0.1  1500 sp/c_h0.1_L0.1.npz  >  sp/conv_tables.log 2>&1
python3 strong_table.py 1 5 10 0.05 0.1  1500 sp/c_h0.05_L0.1.npz >> sp/conv_tables.log 2>&1
python3 strong_table.py 1 5 10 0.1  0.05 1500 sp/c_h0.1_L0.05.npz >> sp/conv_tables.log 2>&1
python3 strong_table.py 1 5 10 0.025 0.1 1500 sp/c_h0.025_L0.1.npz >> sp/conv_tables.log 2>&1
