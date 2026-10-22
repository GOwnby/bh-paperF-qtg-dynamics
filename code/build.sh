#!/bin/bash
# Builds the two compiled libraries needed by the interior-data runs (Sections 3-8): libqtg.so (qtg_dn.c) and vendor_E/libdouble_null.so (copy of Paper E's double_null.c).
set -e
cd "$(dirname "$0")"
gcc -O2 -shared -fPIC -o libqtg.so qtg_dn.c -lm
(cd vendor_E && gcc -O3 -shared -fPIC -o libdouble_null.so double_null.c -lm)
echo "build done"
