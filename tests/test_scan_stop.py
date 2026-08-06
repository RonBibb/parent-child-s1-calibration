import json
r=json.load(open("outputs/gate_status.json")); assert r["classification"].startswith("P3"); assert r["scan_executed"] is False
print("test_scan_stop PASS")
