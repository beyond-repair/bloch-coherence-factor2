# Theorem — Factor of Two

**Status.** Classical. Two-mode. Exact for the resonant reduction
defined in this repository.

**Non-claim.** This is a structural ratio in the \(W+\lambda\phi^4\)
modulated-saddle model. It is not promoted to a universal constant.

## Statement

Let

\[
K(q)=\mu^2-Wq^2+\frac{cq^4}{M^2},
\qquad
W>0,\;c>0,\;M\neq 0,\;\lambda>0,
\]

and assume the condensing regime

\[
\varepsilon_*
:=
K(q_*)
=
\mu^2-\frac{W^2M^2}{4c}
<0,
\qquad
q_*^2=\frac{WM^2}{2c}.
\]

Let \(\phi(x)=\varphi_0\cos(q_*x)\) be a real monochromatic condensate.
The quadratic fluctuation operator about this background has periodic
potential

\[
V_{\rm fluc}(x)
=
\Delta\bigl[1+\cos(2q_*x)\bigr],
\qquad
\Delta=\frac{\lambda\varphi_0^2}{8}.
\]

**Theorem A (saddle under-restores).**
The classical saddle amplitude

\[
\varphi_{\rm saddle}^2=\frac{8|\varepsilon_*|}{\lambda}
\]

produces \(\Delta=|\varepsilon_*|\). The resonant two-mode Bloch
matrix then has lower eigenvalue

\[
\boxed{\Omega_-^2=\frac{\varepsilon_*}{2}<0.}
\]

**Theorem B (stability bound).**
The same two-mode reduction is spectrally nonnegative if and only if

\[
\Delta\ge 2|\varepsilon_*|
\qquad\Longleftrightarrow\qquad
\varphi_0^2\ge\frac{16|\varepsilon_*|}{\lambda}.
\]

**Theorem C (factor of two).**
Writing \(\varphi_{\rm stable}^2=16|\varepsilon_*|/\lambda\),

\[
\boxed{
\frac{\varphi_{\rm stable}^2}{\varphi_{\rm saddle}^2}=2.
}
\]

## Scope

Exact on the two-mode resonant reduction
(\{\(+q_*,-q_*\)\} with Fourier component \(V=\Delta/2\)).

Not automatically exact for the full Hill / Bloch operator. That is
an empirical question delegated to the multimode suite
([MULTIMODE_PROOF.md](MULTIMODE_PROOF.md),
[FALSIFICATION.md](FALSIFICATION.md)).

## Forbidden promotions

- Do not set \(W=0.08\).
- Do not treat \(2\) as a measured constant of nature.
- Do not import CFT-X, thrust, AdS, or loop-corrected amplitudes
  into the statement of Theorems A–C.

## Proof pointers

Construction: [MODEL.md](MODEL.md).
Operator: [BLOCH_OPERATOR.md](BLOCH_OPERATOR.md).
Two-mode algebra: [TWO_MODE_PROOF.md](TWO_MODE_PROOF.md).
Bound: [STABILITY_BOUND.md](STABILITY_BOUND.md).
