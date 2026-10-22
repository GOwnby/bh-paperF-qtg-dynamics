#!/bin/bash
# One-time setup for the event-horizon-regular QTG runs (Paper F, Sections 9-14).  Needs gcc, numpy, scipy, matplotlib.  Builds every compiled library of the repository.
set -e
cd "$(dirname "$0")"
gcc -O3 -shared -fPIC -o ../libqtg.so ../qtg_dn.c -lm                       # Paper F evolution routines (incl. evolve_stream_qtg_cy)
(cd ../vendor_E && gcc -O3 -shared -fPIC -o libdouble_null.so double_null.c -lm)   # background class used by qtg_lib.py (copy of Paper E's dn2lib/double_null)
# The data-construction modules of Paper E (dnU.py, dn2lib.py, kernel_lib.py, transfer.py, stream.c, ...) are shipped in this directory (copies, doi 10.5281/zenodo.23455587); nothing is copied from outside the repository.
gcc -O3 -shared -fPIC -o libdouble_null.so double_null.c -lm
gcc -O3 -shared -fPIC -o libstream.so stream.c -lm
gcc -O3 -shared -fPIC -o libstream2.so stream2.c -lm
(cd codeb && gcc -O3 -Wall -shared -fPIC -o libqtgb.so qtg_b.c -lm)          # code B (second implementation), Paper F Sec. "A second implementation"
(cd codee && gcc -O3 -Wall -shared -fPIC -o libqtge.so qtg_e.c -lm && gcc -O3 -Wall -shared -fPIC -o libqtgel.so qtg_el.c -lm)   # code E (horizon-subtracted variables), double and long double
(cd codec && bash build.sh)                                                  # collapse libraries: stage N (libqtgcol.so) and stage L (libqtgL.so)
echo "setup done"
