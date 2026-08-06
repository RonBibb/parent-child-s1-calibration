#!/usr/bin/env python3
import json,os,math
OUT=os.path.join(os.path.dirname(__file__),"generated"); os.makedirs(OUT,exist_ok=True)
def thermal(gstar,gf):
 z=1.202056903159594; pi=math.pi
 q=32*pi**5*gstar/(135*z*z*gf*gf)
 rho=(pi*pi*gstar/30)*q*q
 return math.sqrt(q),rho
def main():
 # A simple all-fermion-like scaling reference gstar=(7/8)gf shows rho_c~1/gf.
 rows=[]
 for gf in (90,1000,10000,100000,1000000):
  gstar=28+0.875*gf
  T,rho=thermal(gstar,gf); rows.append({"g_f":gf,"g_star":gstar,"T_over_TPl":T,"rho_over_rhoPl":rho})
 # Conservative declared control criterion, not a universal theorem.
 criterion={"T_over_TPl_max":0.1,"rho_over_rhoPl_max":0.01,
  "status":"audit convention requiring parametrically sub-Planckian temperature and density"}
 first=next((r for r in rows if r["T_over_TPl"]<0.1 and r["rho_over_rhoPl"]<0.01),None)
 out={"rows":rows,"conservative_criterion":criterion,"first_sample_meeting_both":first,
  "warning":"large species count changes gravitational cutoff/species scale and is a different microphysical model; this table does not establish validity"}
 json.dump(out,open(os.path.join(OUT,"species_validity.json"),"w"),indent=2)
 print("SPECIES first sampled sub-Planck audit",first)
if __name__=="__main__": main()
