#!/bin/bash
# One-time setup for the event-horizon-regular QTG runs (Paper F, Sections 9-12).  Run from this directory; needs gcc, numpy, scipy, matplotlib.
set -e
cd "$(dirname "$0")"
E=../../../paperE_inner_horizon/code
gcc -O3 -shared -fPIC -o ../libqtg.so ../qtg_dn.c -lm                       # Paper F evolution routines (incl. evolve_stream_qtg_cy)
(cd $E/nonlinear && gcc -O3 -shared -fPIC -o libdouble_null.so double_null.c -lm)   # background class used by qtg_lib.py
cp -n $E/eh_init/*.py $E/eh_init/*.c $E/eh_init/*.npy .                     # data-construction modules of Paper E (dnU.py, dn2lib.py, kernel_lib.py, transfer.py, ...)
gcc -O3 -shared -fPIC -o libdouble_null.so double_null.c -lm
gcc -O3 -shared -fPIC -o libstream.so stream.c -lm
gcc -O3 -shared -fPIC -o libstream2.so stream2.c -lm
(cd codeb && gcc -O3 -Wall -shared -fPIC -o libqtgb.so qtg_b.c -lm)          # code B (second implementation), Paper F Sec. "A second implementation"
(cd codee && gcc -O3 -Wall -shared -fPIC -o libqtge.so qtg_e.c -lm && gcc -O3 -Wall -shared -fPIC -o libqtgel.so qtg_el.c -lm)   # code E (horizon-subtracted variables), double and long double
echo "setup done"
