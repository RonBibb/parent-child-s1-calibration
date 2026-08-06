#!/usr/bin/env python3
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); G=os.path.join(ROOT,"symbolic","generated")
def L(n): return json.load(open(os.path.join(G,n)))
def main():
 t=L("thermal_calibration.json"); s=L("species_validity.json"); f=L("thickness_audit.json"); p=L("perturbation_declaration.json")
 n=t["numeric"]; controlled=n["Tc_over_TPlanck"]<0.1 and n["rho_c_over_rhoPlanck"]<0.01 and n["M_over_lPlanck"]>10
 gates=[{"gate":"G0","status":"pass","result":"reversible natural-unit map preserves kappa and alpha relation"},
 {"gate":"G1","status":"pass_conditional","result":"zero-chemical-potential ultrarelativistic SM thermal closure declared"},
 {"gate":"G2","status":"pass","result":f"Tc/TPl={n['Tc_over_TPlanck']}; rho/rhoPl={n['rho_c_over_rhoPlanck']}"},
 {"gate":"G3","status":"fail_physical_control","result":f"x=2 implies M/lPl={n['M_over_lPlanck']}"},
 {"gate":"G4","status":"fail" if not controlled else "pass","result":"no parametrically sub-Planckian overlap for SM thermal reference under conservative criterion"},
 {"gate":"G5","status":"fail_naive_smoothing","result":f["meaning"]},
 {"gate":"G6","status":"declared_not_solved","result":p["key_risk"]},
 {"gate":"G7","status":"withheld","result":"numerical parameter map stopped by physical-validity gate"}]
 out={"test":"TEST_008_S1_PHYSICAL_CALIBRATION_VALIDITY","classification":"P3 for standard thermal SM-like Weyssenhoff realization under conservative EFT control",
  "gates":gates,"scan_executed":False,
  "scoped_ruling":"the dimensionless S1 equations remain mathematically valid reconnaissance; their standard thermal physical realization lacks controlled overlap",
  "open_alternatives":["nonthermal matter closure","very large species model with revised gravitational cutoff","finite-thickness action","quantum-gravity completion","different EC spin matter"]}
 os.makedirs(os.path.join(ROOT,"outputs"),exist_ok=True); json.dump(out,open(os.path.join(ROOT,"outputs","gate_status.json"),"w"),indent=2)
 for g in gates: print(g["gate"],g["status"],g["result"])
 print("CLASSIFICATION",out["classification"],"SCAN",out["scan_executed"])
if __name__=="__main__": main()
