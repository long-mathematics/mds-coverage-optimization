#!/usr/bin/env python3
"""Deterministic finite diagnostics. These tests do not prove the theorems."""
import json
import random
from math import comb
import mpmath as mp

mp.mp.dps=55
TOL=mp.mpf('1e-40')
def F(t,z):
    return mp.gammainc(t,0,z)/mp.gamma(t) if z else mp.mpf(0)
def tail(ps,k):
    a=[mp.mpf(1)]
    for p in ps:
        b=[mp.mpf(0)]*(len(a)+1)
        for j,v in enumerate(a): b[j]+=v*(1-p);b[j+1]+=v*p
        a=b
    return mp.fsum(a[k:])
def bt(n,p,k):
    return mp.fsum(comb(n,j)*p**j*(1-p)**(n-j) for j in range(k,n+1))
def bisect(f,lo,hi):
    flo=f(lo);fhi=f(hi)
    if not flo*fhi<0: raise ValueError('Unbracketed root')
    for _ in range(170):
        mid=(lo+hi)/2;fm=f(mid)
        if fm==0:return mid
        if flo*fm>0:lo=mid;flo=fm
        else:hi=mid
    return (lo+hi)/2

def main():
    failures=[];gamma_cases=0;ratios=[]
    for ms in ['0.001','0.1','0.5','1','2.3','10','30']:
      m=mp.mpf(ms)
      for zs in ['0.01','0.1','0.5','1','3','10','30','100']:
        z=mp.mpf(zs);g=z**m*mp.exp(-z)/mp.gamma(m+1)
        sf=mp.gammainc(m+1,z,mp.inf)/mp.gamma(m+1);cf=F(m+1,z)
        eta=m-z+z*g/sf;zeta=z-m+z*g/cf;ratio=eta*zeta/m
        gamma_cases+=1;ratios.append(ratio)
        if not mp.mpf('.6')<ratio<1: failures.append(['Gamma_ratio',ms,zs])
    rng=random.Random(20261011);allocation_cases=0;comparisons=0;largest=mp.mpf(0)
    for ts in ['0.2','0.75','1','1.2','2','3.5']:
      t=mp.mpf(ts)
      for n in range(2,7):
       for Ms in ['0.1','1','5','15']:
        M=mp.mpf(Ms);candidates={k:max(bt(q,F(t,M/q),k) for q in range(k,n+1)) for k in range(1,n+1)}
        for _ in range(8):
          q=rng.randrange(1,n+1);ws=[mp.mpf(str(rng.random()+.001)) for _ in range(q)]
          lam=[M*w/mp.fsum(ws) for w in ws]+[mp.mpf(0)]*(n-q)
          ps=[F(t,z) for z in lam];allocation_cases+=1
          for k in range(1,n+1):
            excess=tail(ps,k)-candidates[k];largest=max(largest,excess);comparisons+=1
            if excess>TOL:failures.append(['allocation',ts,n,Ms,k,mp.nstr(excess,12)])
    rho_values={};phase_cases=0;crossings=0;cloud_cases=0
    for t in [2,3,5,8]:
      density=lambda x:x**(t-1)*mp.exp(-x)/mp.factorial(t-1)
      f=lambda x:F(t,x)-x*density(x)
      lo=mp.mpf(t-1);hi=mp.mpf(2*t)
      while f(hi)<=0:hi*=2
      rho=bisect(f,lo,hi);rho_values[str(t)]=mp.nstr(rho,22)
      n=8;beta=[mp.mpf(0)]
      for q in range(1,n):
        b=bisect(lambda M:q*F(t,M/q)-(q+1)*F(t,M/(q+1)),q*rho,(q+1)*rho)
        beta.append(b);crossings+=1
        if abs(q*F(t,b/q)-(q+1)*F(t,b/(q+1)))>TOL:failures.append(['crossing',t,q])
      beta.append((n+1)*rho)
      if any(beta[j]>=beta[j+1] for j in range(n)):failures.append(['phase_order',t])
      for q in range(1,n+1):
        M=(beta[q-1]+beta[q])/2
        vals=[r*F(t,M/r) for r in range(1,n+1)]
        if max(range(n),key=lambda j:vals[j])+1!=q:failures.append(['phase_choice',t,q])
        phase_cases+=1
        for _ in range(8):
          ws=[mp.mpf(str(rng.random()+.001)) for _ in range(n)];sm=mp.fsum(ws)
          achieved=mp.fsum(F(t,M*w/sm) for w in ws);cloud_cases+=1
          if achieved>max(vals)+TOL:failures.append(['cloud_allocation',t,q])
    result={'scope':'Deterministic finite numerical diagnostics, not proofs.',
      'precision_decimal_digits':mp.mp.dps,'seed':20261011,'gamma_ratio_cases':gamma_cases,
      'gamma_ratio_min':mp.nstr(min(ratios),18),'gamma_ratio_max':mp.nstr(max(ratios),18),
      'allocation_vectors':allocation_cases,'allocation_tail_comparisons':comparisons,
      'largest_positive_excess':mp.nstr(largest,8),'cloud_phase_interiors':phase_cases,
      'cloud_adjacent_crossings':crossings,'cloud_allocation_vectors':cloud_cases,
      'rho_values':rho_values,'failures':failures,'all_checks_passed':not failures}
    print(json.dumps(result,indent=2,sort_keys=True));return int(bool(failures))
if __name__=='__main__':raise SystemExit(main())
