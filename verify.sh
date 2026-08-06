#!/usr/bin/env bash
set -euo pipefail; cd "$(dirname "$0")"
PY=../parent-child-s1-evolution/.venv/bin/python; [ -x "$PY" ] || PY=python3
mkdir -p logs outputs symbolic/generated
{ for f in thermal_calibration species_validity thickness_audit perturbation_declaration; do "$PY" "symbolic/$f.py"; done; } 2>&1 | tee logs/analytic.log
"$PY" src/run_gates.py 2>&1 | tee logs/gates.log
{ for f in test_thermal test_thickness test_scan_stop test_scope; do "$PY" "tests/$f.py"; done; } 2>&1 | tee logs/tests.log
echo "ALL TEST 008 AUTHORIZED VERIFICATION PASSED"
