# Paper II toolkit strengthenings

Date: October 11, 2026. Baseline commit:
`244c1fab380f6db03dd5f82d1d03d9a7bd35f16f`.

This focused revision adopts the two optional strengthenings identified by
the deep audit of Paper II.  It does not alter the active-uniform optimizer,
the terminal-cloud staircase, their equality cases, or any Paper I result.

## Exact integer concentration thresholds

For the defect count `U`, failure is the lattice event
`U >= n-k+1`, not merely a real-valued deviation past `n-k`.  Accordingly,
the Bernstein displacement is

`n-k+1-Lambda`.

For the recovered count `S`, failure is `S <= k-1`, so the lower-tail
displacement is

`mu-k+1`.

In the hard-threshold model these gaps coincide because `mu=n-Lambda` and
`v=V`.  The strengthened statement applies in the additional regime where
the mean lies between the old threshold and the first failing lattice point.
The manuscript retains the simple sufficient margin
`sqrt(2 v L) + 2 L / 3`; it does not add the slightly sharper exact quadratic
solution.

## Closed-simplex perturbative parametrization

The representation

`p_i=(1+epsilon_i)/n`

now assumes `epsilon_i >= -1`, exactly matching `p_i >= 0`.  Taylor's
formula and its cubic remainder remain valid at `epsilon_i=-1`, so the
one-read bias expansion now includes boundary laws with zero sampling
coordinates.  Its strict Jensen equality classification for positive budget
is unchanged.

## Statement impact

Only the Paper II formal statement environments `thm:terminal-cloud` and
`thm:uniform-penalty` change.  Their scopes are strengthened as described;
no principal optimizer or staircase statement changes.  Registry context and
whole-source hashes are regenerated with the source diff.

## Verification

Targeted regressions cover a one-Bernoulli lattice case in which the old
concentration condition was unavailable and the new bound applies, and the
boundary perturbation `epsilon=(-1,1)`.  The standard `make test`, `make pdf`,
and `make check` targets, matching PDF manifests, and affected-page visual
inspection are required before merge.  The regression calculations are
supplementary checks, not proofs of the general inequalities.
