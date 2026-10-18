#!/bin/bash
export QTG_CODE=/mnt/user-data/outputs/sources/paperF_qtg_dynamics/code
export PYTHONPATH=$QTG_CODE:/tmp/claude-0/-home-claude/717c308b-4c66-5933-99e1-d42d1016a975/scratchpad/ehq
cd "$(dirname "$0")/.."
python3 strong_table.py 1 5 10 0.1  0.1  1500 sp/c_h0.1_L0.1.npz  >  sp/conv_tables.log 2>&1
python3 strong_table.py 1 5 10 0.05 0.1  1500 sp/c_h0.05_L0.1.npz >> sp/conv_tables.log 2>&1
python3 strong_table.py 1 5 10 0.1  0.05 1500 sp/c_h0.1_L0.05.npz >> sp/conv_tables.log 2>&1
python3 strong_table.py 1 5 10 0.025 0.1 1500 sp/c_h0.025_L0.1.npz >> sp/conv_tables.log 2>&1
