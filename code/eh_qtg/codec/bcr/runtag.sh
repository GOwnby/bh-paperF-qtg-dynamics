#!/bin/bash
# usage: runtag.sh TAG   (env B_S0 B_W B_ASYM)
TAG=$1; mkdir -p $TAG
( for e in 0.04 0.02 0.01; do python3 bcr.py $e 0.1 300 400 $TAG/h0.1_$e.npz; done; python3 bcr.py 0.02 0.05 300 400 $TAG/h0.05_0.02.npz ) > $TAG/a.log 2>&1 &
( python3 bcr.py 0.01 0.05 300 400 $TAG/h0.05_0.01.npz ) > $TAG/b.log 2>&1 &
wait
touch $TAG/done
