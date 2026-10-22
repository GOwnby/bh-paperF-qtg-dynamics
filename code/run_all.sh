#!/bin/bash
# Regenerates the logs of the interior-data runs (Sections 3-8).  Requires gcc, numpy, scipy.  Runtime: see README.md.
set -e
cd "$(dirname "$0")"
bash build.sh
python3 check_gr_limit.py        > check_gr_limit.log
python3 check_static_identity.py > check_static_identity.log
MODEL=1 L2=1.0 VMAX2=55.2 python3 run_qtg_validate.py > validate_model1.log
MODEL=2 L2=1.0 MASS=1.0 VMAX2=60 python3 run_qtg_validate.py > validate_model2.log
python3 ray_blowup.py            > ray_blowup.log
python3 run_scan_u.py 0.005 66 2e-4  > scan_u_h0.005.log
python3 run_scan_u.py 0.0025 66 2e-4 > scan_u_h0.0025.log
for h in 0.01 0.005 0.0025 0.00125 0.000625; do python3 run_conv.py $h 70 2e-4 B2e-4; done > conv_B2e-4.log
python3 run_model2.py 0.02 76 2e-3 0.02 1.0 > model2_h0.02.log
python3 run_pde_blowup2.py 0.02 56.5 0.02 0.002 > pde_blowup_h0.02.log
python3 check_mass_law.py > check_mass_law.log
python3 check_psi_identity.py > check_psi_identity.log
python3 check_compat.py > check_compat.log
# Event-horizon-regular runs (Sections 9-14): see README.md (bash eh_qtg/setup.sh; bash eh_qtg/run_eh.sh; bash eh_qtg/run_analysis.sh)
