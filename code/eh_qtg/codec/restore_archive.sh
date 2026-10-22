#!/bin/bash
# Copies the pulse-scan tables and run files shipped in ../../../archive/paperF_pulse_scan_data into sc/ and sp/ (where the scripts expect them) and
# decompresses the code-E run files (*.json.xz -> *.json).  Run once, before sc/*.sh, sp/*.sh and run_analysis.sh.  Needs xz.  Existing files are not overwritten.
set -e
cd "$(dirname "$0")"
A=../../../archive/paperF_pulse_scan_data
unx() { for f in "$1"/genc_*.json.xz; do o="$2/$(basename "$f" .xz)"; [ -e "$o" ] || xz -dkc "$f" > "$o"; done; }
for f in $A/pt_P*.npz; do [ -e "sc/$(basename "$f")" ] || cp "$f" sc/; done      # pulse-strength tables (Table 14)
unx $A sc                                  # code-E runs of the scan (genc_P*_v1000.json)
for f in $A/strong/*.npz; do [ -e "sp/$(basename "$f")" ] || cp "$f" sp/; done   # strong-pulse, pulse-shape, charge-at-infinity and convergence tables (Tables 15-17)
unx $A/strong sp                           # code-E runs genc_S*.json
echo "archive restored into codec/sc and codec/sp"
