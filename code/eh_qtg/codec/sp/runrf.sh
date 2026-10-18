#!/bin/bash
cd "$(dirname "$0")/.."
for a in "$@"; do m0=${a%%:*}; mt=${a##*:}; python3 rowflux.py 1 $m0 $mt 0.1 0.1 sp/t_m${m0}_mt${mt}.npz; done
