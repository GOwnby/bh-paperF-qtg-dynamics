#!/bin/bash
export QTG_CODE=/mnt/user-data/outputs/sources/paperF_qtg_dynamics/code
export PYTHONPATH=$QTG_CODE:/tmp/claude-0/-home-claude/717c308b-4c66-5933-99e1-d42d1016a975/scratchpad/ehq
cd "$(dirname "$0")"; export STRONG_DR=-0.3
(python3 ../eik_test.py 4 12 20 t_m5_mt5.01.npz t_m5_mt5.5.npz t_m5_mt6.5.npz t_m5_mt8.npz t_m5_mt10.npz t_m5_mt15.npz t_m5_mt25.npz t_m0_mt10.npz t_m2.5_mt10.npz t1_m2.5_mt12.5.npz t1_m5_mt20.npz t1_m7.5_mt15.npz t1_m10_mt20.npz t0_m0_mt10.npz t0_m2.5_mt10.npz t0_m5_mt10.npz t0_m5_mt25.npz
python3 ../eik_test.py 4 8 20 sh_narrow_m0_0_10.npz sh_narrow_m0_2.5_10.npz sh_narrow_m0_5_10.npz
python3 ../eik_test.py 4 20 28 sh_wide_m0_2.5_10.npz sh_wide_m0_5_10.npz) > eik_test.log 2>&1
