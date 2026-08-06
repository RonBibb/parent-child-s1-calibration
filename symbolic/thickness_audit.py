#!/usr/bin/env python3
import json,os
import sympy as sp
OUT=os.path.join(os.path.dirname(__file__),"generated"); os.makedirs(OUT,exist_ok=True)
def main():
 ell,mu,w=sp.symbols("ell mu w",real=True); f=sp.Function("f")(ell)
 # Naive smooth critical interpolation n=f*n0, rho=alpha*n^2=mu*f^2.
 rho=mu*f**2; p=(w-1)*rho; residual=sp.simplify(sp.diff(p,ell))
 out={"profile":"n=f(ell)n0; rho=alpha*n^2=mu*f^2; rho_eff=0",
      "normal_conservation_residual":str(residual),
      "closes_without_extra_stress":bool(residual==0),
      "meaning":"a nontrivial finite-thickness profile needs additional anisotropic stress, flux, or dynamics; sharp A_B is not recovered by naive smoothing alone"}
 json.dump(out,open(os.path.join(OUT,"thickness_audit.json"),"w"),indent=2)
 print("THICKNESS residual",residual)
if __name__=="__main__": main()
