#!/usr/bin/env bash
# Self-verification of Paper F.  Usage:  bash verify.sh [--quick | --full] [verify.py options]
#   --quick (default): rebuilds the C libraries, re-runs the affordable computations and re-derives every
#                      number quoted in main.tex from shipped data/logs (see verification/REPORT.md).
#   --full           : additionally re-runs the multi-hour jobs (code/README.md lists the durations).
# Needs: Python >= 3.10, numpy >= 2, scipy >= 1.11, sympy, mpmath, matplotlib, gcc.  No network, no absolute paths.
# Without scipy the scipy-dependent jobs print SKIPPED and the exit code is non-zero (a skipped check is not a pass).
set -u
cd "$(dirname "$0")" || exit 2
# amplitude asymmetry of the 'asym1' runs of code/eh_qtg/codec/bcr/tailfit.py (documented default)
export B_ASYM="${B_ASYM:-1.5}"
export PYTHONDONTWRITEBYTECODE=1
exec "${PYTHON:-python3}" verify.py "$@"
