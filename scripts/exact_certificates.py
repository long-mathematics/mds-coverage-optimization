#!/usr/bin/env python3
"""Exact rational certificates for the two explicit v30 support examples.

Uses only Python's standard library. These finite checks verify the displayed
certificates; the manuscript's analytic proofs establish the general theorems.
"""
from fractions import Fraction
from math import comb, factorial
import json


def small_depth_example():
    k, tau = 10, 2
    derivative = lambda q: sum(
        (Fraction(q, q-j) for j in range(k)), Fraction(0)
    ) - tau*k
    ratio = Fraction(comb(12, k), comb(11, k))*Fraction(11, 12)**(tau*k)
    values = {
        "D_10_2_at_11": derivative(11),
        "D_10_2_at_12": derivative(12),
        "C_12_over_C_11": ratio,
    }
    return {
        "values": {key: str(value) for key, value in values.items()},
        "verified": (
            derivative(11) == Fraction(5591, 2520)
            and derivative(12) == Fraction(-1759, 2310)
            and ratio == 6*Fraction(11, 12)**20
            and ratio > 1
        ),
        "conclusion": "The unique small-depth optimal support is q=12 for n>=12, k=10, tau=2.",
        "scope": "Uses the proved unimodal localization and small-depth expansion.",
    }


def frozen_pair_example():
    lower = Fraction(6065306597126334, 10**16)
    upper = Fraction(6065306597126335, 10**16)
    taylor = lambda degree: sum(
        (Fraction((-1)**j, 2**j*factorial(j)) for j in range(degree+1)),
        Fraction(0),
    )
    alpha = Fraction(9999, 10000)
    theta = Fraction(10000, 10001)
    center_coefficients = {
        6: Fraction(-4, 10000), 20: Fraction(-11, 10000),
        13: Fraction(15, 10000), 26: alpha*Fraction(49, 4),
    }
    endpoint_coefficients = {
        0: Fraction(1, 10000), 6: Fraction(-4, 10000),
        20: Fraction(-11, 10000), 26: 14-44*alpha,
    }
    def polynomial_lower_bound(coefficients):
        return sum((coefficient*(lower if coefficient > 0 else upper)**power
                    for power, coefficient in coefficients.items()), Fraction(0))
    center_bound = polynomial_lower_bound(center_coefficients)
    endpoint_bound = polynomial_lower_bound(endpoint_coefficients)
    enclosure_verified = lower < taylor(21) < taylor(20) < upper
    return {
        "alpha": str(alpha), "feasible_shadow_theta": str(theta),
        "E_lower": str(lower), "E_upper": str(upper),
        "E_enclosure": "L < S_21 < exp(-1/2) < S_20 < U; alternating-series theorem.",
        "rational_enclosure_comparisons_verified": enclosure_verified,
        "J_3_minus_J_6_5_lower_bound": "9/1000000",
        "J_3_minus_J_0_lower_bound": "12/1000000",
        "verified": (
            enclosure_verified
            and alpha == 1-(1-theta)/theta
            and center_bound > Fraction(9, 10**6)
            and endpoint_bound > Fraction(12, 10**6)
        ),
        "conclusion": "Frozen-pair maxima need not occur at the midpoint or endpoints.",
        "scope": "This does not contradict the active-uniform global theorem.",
    }


if __name__ == "__main__":
    results = {
        "small_depth_example": small_depth_example(),
        "frozen_pair_example": frozen_pair_example(),
    }
    results["all_checks_passed"] = all(value["verified"] for value in results.values())
    print(json.dumps(results, indent=2, sort_keys=True))
    raise SystemExit(0 if results["all_checks_passed"] else 1)
