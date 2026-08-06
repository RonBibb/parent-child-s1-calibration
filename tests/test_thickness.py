import json
r=json.load(open("symbolic/generated/thickness_audit.json")); assert not r["closes_without_extra_stress"]; assert "Derivative" in r["normal_conservation_residual"]
print("test_thickness PASS")
