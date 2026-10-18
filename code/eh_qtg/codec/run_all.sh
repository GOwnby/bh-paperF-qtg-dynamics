#!/bin/bash
# Regenerates the logs of Paper F, Sec. "Collapse-generated horizon tails" (stages N and L; about 10 minutes on one core).  Code E runs (gen_c.py) are separate (see README).
cd "$(dirname "$0")"; ./build.sh; mkdir -p logs data
python3 interior.py 0.05 39.0 70 > logs/interior.log
python3 overlap.py > logs/overlap.log
python3 tables.py > logs/tables.log
python3 fit_tables.py > logs/fit_tables.log
python3 mscale.py > logs/mscale.log 2>&1
python3 ascale.py > logs/ascale.log 2>&1
python3 linear.py > logs/linear.log 2>&1
