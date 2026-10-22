#!/bin/bash
export QTG_CODE="$(cd "$(dirname "$0")/../../.." && pwd)"     # code/ directory of the repository
export PYTHONPATH=$QTG_CODE:$QTG_CODE/eh_qtg${PYTHONPATH:+:$PYTHONPATH}
cd "$(dirname "$0")"
(STRONG_DR=${DR:--0.3} python3 ../horizon_ray.py 4 12 20 t_m5_mt5.01.npz t_m5_mt5.5.npz t_m5_mt6.5.npz t_m5_mt8.npz t_m5_mt10.npz t_m5_mt15.npz t_m5_mt25.npz t_m0_mt10.npz t_m2.5_mt10.npz t1_m2.5_mt12.5.npz t1_m5_mt20.npz t1_m7.5_mt15.npz t1_m10_mt20.npz t0_m0_mt10.npz t0_m2.5_mt10.npz t0_m5_mt10.npz t0_m5_mt25.npz
STRONG_DR=${DR:--0.3} python3 ../horizon_ray.py 4 8 20 sh_narrow_m0_0_10.npz sh_narrow_m0_2.5_10.npz sh_narrow_m0_5_10.npz | tail -3
STRONG_DR=${DR:--0.3} python3 ../horizon_ray.py 4 20 28 sh_wide_m0_0_10.npz sh_wide_m0_2.5_10.npz sh_wide_m0_5_10.npz | tail -3) > "${LOGDIR:-.}/horizon_ray.log" 2>&1
