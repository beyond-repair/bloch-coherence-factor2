# C4 — smallest two-sector parent

**Status.** Experiment under [CLOSURE_CRITERION.md](CLOSURE_CRITERION.md).
Does not unfreeze propulsion, 0.08, or a universal 2.

\[
\boxed{
\text{Does a consistent action actually produce the factor }2?
}
\]

The obstruction was never “no Lagrangian can contain a 2.”
It was: the frozen pair is not the on-shell Hessian of one local
\(\beta\phi^4\).

## What C4 is allowed to assume

Conventional, independently stated:

- translationally invariant microscopic action
- real fields
- bounded-below Euclidean action where the quadratic form of
  each *propagating* field is positive
- well-defined variational derivatives
- an independent collective field \(\chi\)
- specified kernels \(K_\phi\), \(K_\chi\)
- recover \(K(q)\) for \(\phi\) when \(\chi=0\)
- no coefficient fixed by demanding Theorem C

The cosine profile is a **Galerkin / mean-field truncation**,
not an exact pointwise solution of a single-field EOM.

## Action (named before any target Hessian)

\[
S[\phi,\chi]
=
\int\!dx\,
\Bigl[
\tfrac12\,\phi\,K(-i\partial_x)\phi
+
\tfrac12\,\chi\,\omega(-i\partial_x)\chi
+
\tfrac g2\,\chi\,\phi^2
\Bigr].
\]

Two quadratic conventions for \(\chi\):

- **C4-P** — \(\omega\) positive (propagating collective).
  Bounded below in \(\chi\). Effective quartic for \(\phi\) after
  integrating \(\chi\) is *negative*.
- **C4-A** — \(\omega=-\mu^2\) ultra-local (auxiliary / HS).
  Recovers \(+\beta\phi^4\) after eliminating \(\chi\).
  Euclidean form is not bounded below in \(\chi\) alone;
  it is a constraint sector.

Ansatz (mean-field, not pointwise identity):

\[
\phi=\varphi_0\cos(q_*x),
\qquad
\chi=\chi_0+\chi_2\cos(2q_*x).
\]

## Projected stationarity (derived)

\[
\varepsilon_*+g\chi_0+\tfrac12 g\chi_2=0,
\qquad
\omega(0)\,\chi_0+\tfrac g4\varphi_0^2=0,
\qquad
\omega(2q_*)\,\chi_2+\tfrac g4\varphi_0^2=0.
\]

Hence

\[
\chi_0=-\frac{g\varphi_0^2}{4\,\omega(0)},
\qquad
\chi_2=-\frac{g\varphi_0^2}{4\,\omega(2q_*)}.
\]

Fixed-\(\chi\) Hessian:

\[
H_{\phi\phi}=K+g\chi_0+g\chi_2\cos(2q_*x).
\]

Shape of frozen \(V_{\rm fluc}\) (equal DC and first cosine) holds
iff \(\chi_0=\chi_2\), iff \(\omega(0)=\omega(2q_*)\).

## What the algebra returns (no fit)

**Ultra-local same \(\omega\), fixed \(\chi\):**

\[
\frac{\Delta}{|\varepsilon_*|}=\frac23,
\qquad
\Omega_-^2=-\frac23\,|\varepsilon_*|.
\]

Not \(1\), not Theorem A.

**Ultra-local auxiliary, Schur / integrate \(\chi\):**

recovers local \(\beta\phi^4\), hence I1:

\[
\Omega_-^2=0.
\]

**Same kernel \(\omega=K\):**
\(\omega(0)=\mu^2\) and \(\omega(2q_*)=K(2q_*)\) are not equal
except on a measure-zero surface in \((W,c,M,\mu)\). The potential
is then \(A+B\cos\) with \(A\neq B\), not frozen \(V_{\rm fluc}\).

**Dispersion ratio that would force Theorem A** at fixed \(\chi\):

\[
\frac{\omega(2q_*)}{\omega(0)}=\frac32.
\]

That ratio is not implied by recovering \(K(q)\). Using it is a
fit to Theorem C. Recorded as COUNTERTERM, not a pass.

## Other routes, not run as parents here

1. Nonlocal \(\phi^2 K\phi^2\) — I3: integral Hessian unless
   \(K\propto\delta\), which is local \(\phi^4\).
4. Derivative vertices — Hessian is not a multiplication operator.
   Matching frozen \(V_{\rm fluc}\) requires those extra pieces to
   vanish, which returns to a multiplicative vertex.

## Decision recorded in tests

\[
\boxed{
\text{C4 conventional two-sector cubic does not produce the frozen factor }2.
}
\]

The identity remains an operator-level artifact of the named
\(H\) on `main`, unless a *new independently motivated*
\(\omega(q)\) is supplied. That \(\omega\) is not written here.

## Still not a drive

Even a future pass would be an operator property.
\(\mathcal{G}\simeq 0\Rightarrow\Delta F\simeq 0\) remains allowed.
