import json
r=json.load(open("outputs/gate_status.json")); assert "mathematically valid" in r["scoped_ruling"]; assert len(r["open_alternatives"])>=4
print("test_scope PASS")
