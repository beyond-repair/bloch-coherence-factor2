# Multimode status

There is no claim that Theorem C is exact for the full Bloch
operator.

## What is proved

The two-mode block is exact as a *projection*. Every additional
plane-wave mode \(k+2nq_*\) with \(|n|\) large enough that
\(K(k+2nq_*)\) is far above \(|\varepsilon_*|\) is perturbatively
integrable and shifts \(\Omega_-^2\) by

\[
\delta\Omega_-^2
=
\mathcal{O}\!\left(\frac{(\Delta/2)^2}{K_{\rm distant}-\varepsilon_*}\right).
\]

That shift is not constrained to preserve \(R=2\).

## What is tested

The suite constructs \(H(k)\) for \(N=1,2,4,6\) (3, 5, 9, 13 modes),
minimizes the lowest eigenvalue over the first Brillouin zone, and
bisects \(\varphi_0^2\) until that minimum crosses zero.

Reported quantities:

- two-mode analytic eigenvalues,
- 9-mode Bloch diagonalization,
- convergence with mode count,
- full Brillouin-zone minimum,
- saddle amplitude,
- stability amplitude,
- \(R=\varphi_{\rm stable}^2/\varphi_{\rm saddle}^2\),
- \(\Delta+\varepsilon_*\),
- dependence on \(W,\lambda,M,c,\mu\).

## Decision rule

- If multimode \(R\) stays at 2 within the numerical tolerance of
  the bisection, the factor is exact for the truncated operator
  as well.
- If multimode \(R\) drifts, the two-mode theorem remains exact
  *as a two-mode theorem*. The drift is a property of the full
  operator and is recorded, not absorbed.

Do not “fix” a drift by changing the definition of
\(\varphi_{\rm saddle}^2\).
