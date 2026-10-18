#!/bin/bash
# stage 2a: strong-field dispersing data; eps in 0.01 0.04 0.06 0.08 0.10 at h=0.1 and 0.05
mkdir -p s2a
( for e in 0.01 0.04 0.06 0.08 0.10; do python3 bcr.py $e 0.1 300 400 s2a/h0.1_$e.npz; done ) > s2a/a.log 2>&1 &
( for e in 0.01 0.04 0.06 0.08 0.10; do python3 bcr.py $e 0.05 300 400 s2a/h0.05_$e.npz; done ) > s2a/b.log 2>&1 &
wait; touch s2a/done
