#!/usr/bin/env python3
"""Exact symbolic identities supporting both papers; not a formal proof."""
import json
import sympy as s

def main():
    z,m,e,v,w,d=s.symbols('z m eta zeta W Delta',positive=True)
    h=z-m+1
    de=e**2+h*e-m;dv=-v**2+h*v+m
    checks={
      'product_Riccati':v*de+e*dv-(2*h*e*v-(e*v+m)*(v-e)),
      'difference_Riccati':dv-de-(-(v-e)**2-2*e*v+h*(v-e)+2*m),
      'L2_log_derivative':de/e-dv/v+e+v-(e+v)*(2-m/(e*v)),
      'three_fifths_square_completion':z-s.Rational(16,15)*m-h*h/4+(z-m-1)**2/4+m/15,
    }
    dd=-d*d-2*w+h*d+2*m
    second=(2*z*w-(w+m)*dd).subs(d,2*h*w/(w+m))
    checks['critical_second_derivative']=second-2*w*(z-(m*m/w-w)-(m-w)/(m+w)*h*h)
    theta,A,B,C=s.symbols('theta A B C')
    beta=(1-theta)*A+theta*B;gamma=(1-theta)*B+theta*C
    checks['pair_shadow_derivative']=s.diff(1-gamma/beta,theta)-(B*B-A*C)/(beta*beta)
    x,alpha=s.symbols('x alpha');F=s.Function('F')(x);g=s.diff(F,x);u=s.diff(g,x)/g;D=1-alpha*F
    checks['marginal_numerator_cancellation']=s.diff(u*D+alpha*g,x)-s.diff(u,x)*D
    a,b,p,gd=s.symbols('a b p gd')
    eta=m-z+z*gd/(1-p);zeta=z-m+z*gd/p
    checks['constrained_Hessian']=((m/z-1+a*gd/(1-p)-b*gd/p)-(a*eta-b*zeta)/z).subs(b,1-a)
    checks['normalized_two_point_derivative']=s.diff(s.exp(-x)*sum(x**j/s.factorial(j) for j in range(4)),x)+s.exp(-x)*x**3/s.factorial(3)
    # Exact Poisson-tail curvature at several integer thresholds.
    for t in range(2,8):
        psi=s.exp(-x)*sum(x**j/s.factorial(j) for j in range(t))
        checks[f'cloud_curvature_t{t}']=s.diff(psi,x,2)-s.exp(-x)*x**(t-2)*(x-(t-1))/s.factorial(t-1)
    residuals={k:str(s.factor(s.simplify(val))) for k,val in checks.items()}
    result={'scope':'Finite exact symbolic identities; no continuum or optimizer certification.',
            'identities':len(residuals),'residuals':residuals,'all_checks_passed':all(v=='0' for v in residuals.values())}
    print(json.dumps(result,indent=2,sort_keys=True))
    return 0 if result['all_checks_passed'] else 1
if __name__=='__main__':
    raise SystemExit(main())
