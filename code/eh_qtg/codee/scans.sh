#!/bin/bash
# Scans of code E (Paper F, Sec. "Curvature and slaving to kappa_+ v ~ 70"): analysis of the shipped thinned data.  usage: bash scans.sh > logs/scans.log
export QTG_CODE=${QTG_CODE:-$(cd ../.. && pwd)}; export PYTHONPATH=$QTG_CODE:${PYTHONPATH}
cd "$(dirname "$0")"
a() { python3 scan_an.py data/$1 $2 $3 $4; echo; }
a gene_p1_hs0.2_m1_B0.003_k0.5_v1200_ray2.json 0.5 5 1100
a gene_p1_hs0.2_m1_B0.003_k1_v1200_ray2.json   1.0 5 1100
a gene_p1_hs0.2_m1_B0.003_k1.5_v1500_ray2.json 1.5 5 1400
a gene_p1_hs0.2_m1_B0.003_k2_v1200_ray2.json   2.0 5 1100
a gene_p1_hs0.2_m1_B0.003_k3_v1200_ray2.json   3.0 5 1100
a gene_p1_hs0.2_m1_B0.0003_k1.5_v1200_ray2.json 1.5 5 1100
a gene_p1_hs0.2_m1_B0.03_k1.5_v1200_ray2.json  1.5 5 1100
a gene_p1_hs0.2_m1_B0.003_k1.5_v700_M3_ray2.json 1.5 3 660
a gene_p1_hs0.2_m1_B0.003_k1.5_v2000_M10_ray2.json 1.5 10 1900
python3 dm_limit.py
