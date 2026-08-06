import sys; sys.path.insert(0,"symbolic")
from thermal_calibration import derive
r=derive(); n=r["numeric"]; assert 0.8<n["Tc_over_TPlanck"]<0.82; assert 15<n["rho_c_over_rhoPlanck"]<16; assert 0.08<n["M_over_lPlanck"]<0.10
print("test_thermal PASS")
