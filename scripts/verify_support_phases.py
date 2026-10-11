#!/usr/bin/env python3
"""Finite diagnostics for the Gamma MDS staircase; not a proof of the theorem.

The parameter lists and root brackets are fixed, with no random sampling.
Success and failure tails are evaluated separately, so comparisons remain
meaningful when success probabilities round to one at the working precision.
"""

import json
from math import comb

import mpmath as mp


mp.mp.dps = 80
IDENTITY_TOL = mp.mpf("1e-60")
ROOT_TOL = mp.mpf("1e-55")
STRICT_REL_TOL = mp.mpf("1e-40")
ROOT_ITERATIONS = 200


def number(value, digits=35):
    return mp.nstr(value, digits)


def recovery(shape, x):
    """Compute both Gamma tails directly, without subtracting either from one."""
    normalizer = mp.gamma(shape)
    return (
        mp.gammainc(shape, 0, x) / normalizer,
        mp.gammainc(shape, x, mp.inf) / normalizer,
    )


def probabilities(k, shape, support, budget):
    p, u = recovery(shape, budget / support)
    if support == int(support):
        q = int(support)
        success = mp.fsum(comb(q, j) * p**j * u**(q-j)
                          for j in range(k, q+1))
        failure = mp.fsum(comb(q, j) * p**j * u**(q-j)
                          for j in range(k))
    else:
        # The analytic extension in real q > k-1 uses the regularized beta CDF.
        success = mp.betainc(k, support-k+1, 0, p, regularized=True)
        failure = mp.betainc(support-k+1, k, 0, u, regularized=True)
    return success, failure


def log_probabilities(k, shape, support, budget):
    success, failure = probabilities(k, shape, support, budget)
    log_success = mp.log1p(-failure) if failure < mp.mpf(".5") else mp.log(success)
    log_failure = mp.log1p(-success) if success < mp.mpf(".5") else mp.log(failure)
    return log_success, log_failure


def logit(k, shape, support, budget):
    log_success, log_failure = log_probabilities(k, shape, support, budget)
    return log_success-log_failure


def density(k, shape, support, budget):
    x = budget / support
    p, u = recovery(shape, x)
    gamma_density = x**(shape-1) * mp.exp(-x) / mp.gamma(shape)
    return (k * comb(support, k) / mp.mpf(support) * gamma_density
            * p**(k-1) * u**(support-k))


def leading_log_coefficient(k, shape, support):
    return mp.log(comb(support, k))-shape*k*mp.log(support)


def bisect(function, lower, upper):
    lower, upper = mp.mpf(lower), mp.mpf(upper)
    f_lower, f_upper = function(lower), function(upper)
    if not f_lower < 0 < f_upper:
        raise ValueError("Expected a strictly negative-to-positive bracket")
    for _ in range(ROOT_ITERATIONS):
        middle = (lower+upper)/2
        f_middle = function(middle)
        if f_middle == 0:
            return middle
        if f_middle < 0:
            lower = middle
        else:
            upper = middle
    return (lower+upper)/2


def main():
    failures = []

    def check(condition, label, **details):
        if not condition:
            failures.append({"check": label, **details})

    def positive(value, scale=mp.mpf(1)):
        return value > STRICT_REL_TOL*abs(scale)

    identity_records = []
    for shape_text, x_text in [("1.2", ".2"), ("2", "2"), ("3.5", "20")]:
        shape, x = mp.mpf(shape_text), mp.mpf(x_text)
        p, u = recovery(shape, x)
        h = x**(shape-1)*mp.exp(-x)/mp.gamma(shape)/u
        integral = mp.quad(lambda t: mp.exp(-t)*(1+t/x)**(shape-1), [0, 1, mp.inf])
        relative_residual = abs(h*integral-1)
        cumulative_hazard = -mp.log1p(-p) if p < mp.mpf(".5") else -mp.log(u)
        elasticity = x*h/cumulative_hazard
        geometric_curvature = elasticity*(shape-x+x*h-elasticity)
        check(relative_residual < IDENTITY_TOL, "inverse_hazard_integral",
              shape=shape_text, x=x_text, residual=number(relative_residual))
        check(positive(-geometric_curvature), "cumulative_hazard_geometric_concavity",
              shape=shape_text, x=x_text)
        identity_records.append({
            "identity": "inverse Gamma hazard integral and cumulative-hazard curvature",
            "shape": shape_text, "x": x_text,
            "relative_residual": number(relative_residual),
            "second_logarithmic_derivative_of_cumulative_hazard": number(geometric_curvature),
        })

    def exp_log_density(k, support, x):
        return (mp.log(k*comb(support, k))
                +(k-1)*mp.log(-mp.expm1(-x))-(support-k+1)*x)

    def phi(x):
        return (x/(2*mp.sinh(x/2)))**2

    for k, q, r, c_text, x_text in [
        (2, 2, 4, ".4", ".3"), (3, 4, 7, ".75", "3"), (5, 6, 9, ".8", "30")
    ]:
        c, x = mp.mpf(c_text), mp.mpf(x_text)
        direct = mp.diff(lambda z: mp.log(c)+exp_log_density(k, r, c*z)
                         -exp_log_density(k, q, z), x, 2)
        formula = (k-1)*(phi(x)-phi(c*x))/x**2
        residual = abs(direct-formula)
        check(residual < IDENTITY_TOL, "exponential_density_ratio_curvature_identity")
        check(positive(-formula), "exponential_density_ratio_strict_log_concavity")
        identity_records.append({
            "identity": "scaled exponential order-statistic density-ratio curvature",
            "k": k, "q": q, "r": r, "scale": c_text, "x": x_text,
            "absolute_residual": number(residual), "curvature": number(formula),
        })

    # This checks the real-support exponential-spacing transform used in Prékopa.
    for k, q_text, s_text in [(2, "2.5", ".7"), (4, "5.25", "3")]:
        q, s = mp.mpf(q_text), mp.mpf(s_text)
        beta_transform = (mp.gamma(q+1)*mp.gamma(q-k+1+s)
                          /mp.gamma(q-k+1)/mp.gamma(q+1+s))
        spacing_transform = mp.fprod((q-j)/(q-j+s) for j in range(k))
        residual = abs(beta_transform/spacing_transform-1)
        check(residual < IDENTITY_TOL, "real_support_exponential_spacing_transform")
        identity_records.append({
            "identity": "real-support beta and exponential-spacing Laplace transforms",
            "k": k, "support": q_text, "laplace_parameter": s_text,
            "relative_residual": number(residual),
        })

    def crossing(k, shape, q, r, bracket):
        difference = lambda budget: logit(k, shape, r, budget)-logit(k, shape, q, budget)
        budget = bisect(difference, *bracket)
        success, failure = probabilities(k, shape, q, budget)
        other_success, other_failure = probabilities(k, shape, r, budget)
        residual = abs(difference(budget))
        density_q, density_r = density(k, shape, q, budget), density(k, shape, r, budget)
        slope_difference = density_r-density_q
        scaled_derivative = slope_difference/(success*failure)
        analytic_derivative = density_r/(other_success*other_failure)-density_q/(success*failure)
        direct_derivative = mp.diff(difference, budget)
        derivative_residual = abs(analytic_derivative-direct_derivative)/abs(direct_derivative)
        crossing_scaling_residual = abs(scaled_derivative-analytic_derivative)/abs(analytic_derivative)
        before = difference(budget*mp.mpf(".99"))
        after = difference(budget*mp.mpf("1.01"))
        check(residual < ROOT_TOL, "crossing_logit_residual", k=k, q=q, r=r)
        check(positive(-before) and positive(after), "crossing_orientation", k=k, q=q, r=r)
        check(positive(scaled_derivative), "crossing_transversality", k=k, q=q, r=r)
        check(derivative_residual < IDENTITY_TOL, "crossing_derivative_identity", k=k, q=q, r=r)
        check(crossing_scaling_residual < ROOT_TOL, "crossing_common_probability_scaling", k=k, q=q, r=r)
        return budget, {
            "from_support": q, "to_support": r,
            "bracket": list(bracket), "budget": number(budget, 50),
            "success_probability": number(success), "failure_probability": number(failure),
            "absolute_logit_residual": number(residual),
            "slope_difference": number(slope_difference),
            "logit_difference_derivative": number(scaled_derivative),
            "derivative_relative_residual": number(derivative_residual),
            "common_probability_scaling_relative_residual": number(crossing_scaling_residual),
            "logit_advantage_at_99_percent_budget": number(before),
            "logit_advantage_at_101_percent_budget": number(after),
        }

    staircase_records = []
    for k, n, expected_initial, brackets in [
        (10, 16, 12, [("3", "5"), ("8", "10"), ("13", "16"), ("19", "22")]),
        (2, 6, 2, [("5", "8"), ("15", "20"), ("30", "36"), ("50", "60")]),
    ]:
        shape = mp.mpf(2)
        initial = max(range(k, n+1), key=lambda q: (leading_log_coefficient(k, shape, q), q))
        check(initial == expected_initial, "initial_support", k=k, n=n)
        budgets, transitions, third_support_gaps = [], [], []
        for q, bracket in zip(range(expected_initial, n), brackets):
            budget, record = crossing(k, shape, q, q+1, bracket)
            budgets.append(budget)
            transitions.append(record)
            tied_value = logit(k, shape, q, budget)
            other_values = [logit(k, shape, support, budget)
                            for support in range(k, n+1) if support not in (q, q+1)]
            third_support_gaps.append(tied_value-max(other_values))
        check(all(budgets[j] < budgets[j+1] for j in range(len(budgets)-1)),
              "adjacent_crossings_strictly_ordered", k=k, n=n)
        check(all(positive(gap) for gap in third_support_gaps),
              "only_two_maximizers_at_transition", k=k, n=n)
        interior_budgets = ([budgets[0]/2]
                            +[(a+b)/2 for a, b in zip(budgets, budgets[1:])]
                            +[2*budgets[-1]])
        interior_records = []
        for expected_support, budget in zip(range(expected_initial, n+1), interior_budgets):
            values = {q: logit(k, shape, q, budget) for q in range(k, n+1)}
            winner = max(values, key=values.get)
            gap = values[winner]-max(value for q, value in values.items() if q != winner)
            check(winner == expected_support and positive(gap),
                  "all_supports_visit_phase_interiors", k=k, n=n, expected=expected_support)
            interior_records.append({"budget": number(budget), "winner": winner,
                                     "logit_gap_to_second_best": number(gap)})
        staircase_records.append({
            "k": k, "shape": "2", "n": n, "initial_support": initial,
            "transitions": transitions, "sampled_phase_interiors": interior_records,
            "minimum_logit_gap_to_a_third_support_at_a_transition": number(min(third_support_gaps)),
        })

    # A nonadjacent crossing at a genuinely noninteger shape exercises the
    # real-Gamma case independently of the two integer-shape staircase tables.
    _, noninteger_crossing = crossing(3, mp.mpf("1.5"), 4, 7, ("1", "100"))
    noninteger_crossing.update({"k": 3, "shape": "1.5"})

    dominance_records = []
    tied_shape = mp.log(3)/(2*mp.log(mp.mpf(3)/2))
    for name, k, shape, q, r in [
        ("strict_leading_coefficient", 10, mp.mpf(2), 10, 12),
        ("equal_leading_coefficients", 2, tied_shape, 2, 3),
    ]:
        leading_ratio = leading_log_coefficient(k, shape, r)-leading_log_coefficient(k, shape, q)
        if name == "equal_leading_coefficients":
            check(abs(leading_ratio) < IDENTITY_TOL, "equal_leading_coefficient_construction")
        else:
            check(positive(leading_ratio), "strict_leading_coefficient_construction")
        samples = []
        for budget_text in [".0001", ".5", "5", "20", "200"]:
            budget = mp.mpf(budget_text)
            advantage = logit(k, shape, r, budget)-logit(k, shape, q, budget)
            check(positive(advantage), "larger_support_strict_dominance", case=name, budget=budget_text)
            samples.append({"budget": budget_text, "larger_support_logit_advantage": number(advantage)})
        dominance_records.append({
            "case": name, "k": k, "shape": number(shape), "q": q, "r": r,
            "shape_formula": "log(3)/(2*log(3/2))" if name == "equal_leading_coefficients" else "2",
            "log_leading_coefficient_ratio": number(leading_ratio), "samples": samples,
        })

    concavity_records = []
    for k, shape_text, budget_text, q, r, theta_text in [
        (3, "1.1", "2", 3, 7, ".4"),
        (4, "1.5", "12", 4, 10, ".5"),
        (5, "2.3", "30", 5, 9, ".6"),
        (2, "3.5", "60", 2, 8, ".5"),
        (2, "1.2", "200", 2, 7, ".3"),
    ]:
        shape, budget, theta = map(mp.mpf, (shape_text, budget_text, theta_text))
        middle = mp.exp(theta*mp.log(q)+(1-theta)*mp.log(r))
        endpoint_mean = (theta*log_probabilities(k, shape, q, budget)[0]
                         +(1-theta)*log_probabilities(k, shape, r, budget)[0])
        middle_value = log_probabilities(k, shape, middle, budget)[0]
        gain = middle_value-endpoint_mean
        check(positive(gain, max(abs(middle_value), abs(endpoint_mean))),
              "strict_geometric_support_concavity", k=k, shape=shape_text, budget=budget_text)
        concavity_records.append({
            "k": k, "shape": shape_text, "budget": budget_text, "q": q, "r": r,
            "theta": theta_text, "geometric_intermediate_support": number(middle),
            "log_success_concavity_gain": number(gain),
        })

    result = {
        "scope": ("Deterministic finite checks of proof identities, representative pair comparisons, "
                  "transition budgets and real-support concavity. These diagnostics do not prove "
                  "a continuum inequality, all-pair crossing theorem or global support staircase."),
        "precision_decimal_digits": mp.mp.dps,
        "random_sampling": False,
        "tolerances": {
            "identity_absolute_or_stated_relative_error": str(IDENTITY_TOL),
            "absolute_logit_residual_at_crossing": str(ROOT_TOL),
            "relative_common_probability_scaling_error_at_crossing": str(ROOT_TOL),
            "strict_inequality_margin_relative_to_stated_scale": str(STRICT_REL_TOL),
            "strict_inequality_scale": ("1 unless specified; geometric-concavity tests use the "
                                         "maximum absolute log success in the comparison"),
            "root_bisection_iterations": ROOT_ITERATIONS,
        },
        "tail_evaluation": ("Separate lower and upper regularized Gamma integrals; separate "
                            "finite binomial success/failure sums for integer support and "
                            "regularized beta tails for real support; log1p for the near-one side."),
        "identity_checks": identity_records,
        "staircase_examples": staircase_records,
        "noninteger_shape_nonadjacent_crossing": noninteger_crossing,
        "dominance_examples": dominance_records,
        "real_support_concavity_examples": concavity_records,
        "failures": failures,
        "all_checks_passed": not failures,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
