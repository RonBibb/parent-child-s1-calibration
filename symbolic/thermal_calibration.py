#!/usr/bin/env python3
import json,os
import sympy as sp
OUT=os.path.join(os.path.dirname(__file__),"generated"); os.makedirs(OUT,exist_ok=True)

def derive(gstar=sp.Rational(427,4),gf=sp.Integer(90),w=sp.Rational(1,3),x=sp.Integer(2)):
    pi=sp.pi; z=sp.zeta(3)
    # Natural units hbar=c=k_B=1; unreduced Planck units: l_Pl=sqrt(G), T_Pl=1/sqrt(G).
    a=pi**2*gstar/30; b=3*z*gf/(4*pi**2)
    # alpha=kappa/32=pi*G/4. q := G*T_c^2 = (T_c/T_Pl)^2.
    q=sp.simplify(4*a/(pi*b**2))
    rho_ratio=sp.simplify(a*q**2) # rho_c * G^2 = rho_c/rho_Pl
    x_coeff=sp.simplify(8*pi*(1-w)*rho_ratio) # x=x_coeff*(M/l_Pl)^2
    mratio=sp.simplify(sp.sqrt(x/x_coeff))
    return {"g_star":str(gstar),"g_f":str(gf),"a_rho":str(a),"b_n":str(b),
      "Tc_over_TPlanck":str(sp.sqrt(q)),"rho_c_over_rhoPlanck":str(rho_ratio),
      "x_map":f"x=({sp.sstr(x_coeff)})*(M/l_Pl)^2","M_over_lPlanck_for_control":str(mratio),
      "numeric":{"Tc_over_TPlanck":float(sp.N(sp.sqrt(q))),
                 "rho_c_over_rhoPlanck":float(sp.N(rho_ratio)),
                 "x_coefficient":float(sp.N(x_coeff)),"M_over_lPlanck":float(sp.N(mratio))},
      "identities":["kappa=8*pi*G","alpha=kappa/32=pi*G/4 in natural units",
                    "rho=a*T^4","n=b*T^3","critical rho=alpha*n^2"],
      "interpretation":"SM thermal reference is Planckian/super-Planckian; x=2 maps to sub-Planckian M length"}
def main():
 r=derive(); json.dump(r,open(os.path.join(OUT,"thermal_calibration.json"),"w"),indent=2)
 print("THERMAL Tc/TPl",r["numeric"]["Tc_over_TPlanck"],"rho/rhoPl",r["numeric"]["rho_c_over_rhoPlanck"],"M/lPl",r["numeric"]["M_over_lPlanck"])
if __name__=="__main__": main()
