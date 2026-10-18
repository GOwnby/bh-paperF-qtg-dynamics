#!/bin/bash
# Build the collapse libraries (Paper F, Sec. collapse) and run the tests.  Needs gcc, numpy, scipy, matplotlib.  The code-E driver gen_c.py needs eh_qtg/setup.sh done first (libqtge.so in ../codee).
set -e; cd "$(dirname "$0")"
gcc -O3 -shared -fPIC -o libqtgcol.so qtg_col.c -lm      # stage N: free double-null evolution + snapshots + apparent-horizon tracker (includes ../../qtg_dn.c)
gcc -O3 -shared -fPIC -o libqtgL.so qtg_L.c -lm          # stage L: linear l=0 scalar on the static exterior (Gundlach-Price-Pullin scheme)
