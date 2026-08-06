#!/usr/bin/env python3
import json,os
OUT=os.path.join(os.path.dirname(__file__),"generated"); os.makedirs(OUT,exist_ok=True)
def main():
 out={"background":"anisotropic Kantowski-Sachs N2 segment",
  "required_variables":["gauge-invariant scalar metric modes","density perturbation delta_rho",
    "number perturbation delta_n","velocity perturbations","spin-correlation perturbation delta<s^2>",
    "vector modes","two tensor polarizations"],
  "required_equations":["linearized EC effective Einstein equations","perturbed matter conservation",
    "perturbed number conservation","perturbed Cartan/averaging closure","linearized boundary conditions"],
  "key_risk":"mode coupling from anisotropic background; homogeneous grid does not test these modes",
  "status":"problem formulated; no mode-stability result"}
 json.dump(out,open(os.path.join(OUT,"perturbation_declaration.json"),"w"),indent=2)
 print("PERTURBATIONS declared; stability untested")
if __name__=="__main__": main()
