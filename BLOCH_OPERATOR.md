# Bloch operator

## Quadratic fluctuation operator

About the periodic background, linearized modes \(\psi\) satisfy

\[
\Omega^2\psi
=
\Bigl(K(-i\partial_x)+V_{\rm fluc}(x)\Bigr)\psi,
\]

with

\[
V_{\rm fluc}(x)=\Delta\bigl[1+\cos(2q_*x)\bigr],
\qquad
\Delta=\frac{\lambda\varphi_0^2}{8}.
\]

The potential is periodic with period \(\pi/q_*\). The reciprocal
lattice is \(2q_*\mathbb{Z}\).

## Fourier content

\[
\cos(2q_*x)=\frac{e^{i2q_*x}+e^{-i2q_*x}}{2}.
\]

Hence

- diagonal (zero-momentum) shift \(=\Delta\),
- nearest-neighbor reciprocal-lattice coupling \(=V=\Delta/2\).

No other harmonics appear at this order.

## Plane-wave lattice

Fix crystal momentum \(k\) in the first Brillouin zone
\([-q_*,q_*]\). Expand

\[
\psi(x)=\sum_{n=-N}^{N} a_n\,e^{i(k+2nq_*)x}.
\]

The matrix of the operator in this basis is tridiagonal:

\[
H_{nn}(k)=K(k+2nq_*)+\Delta,
\qquad
H_{n,n\pm 1}(k)=\frac{\Delta}{2}.
\]

\(N=4\) is the 9-mode truncation used in the default suite.

## Resonant two-mode block

The pair \(\{+q_*,-q_*\}\) is degenerate at leading order because
\(K(q_*)=K(-q_*)=\varepsilon_*\). Projecting onto that pair produces

\[
H_{\rm 2\times 2}
=
\begin{pmatrix}
\varepsilon_*+\Delta & \Delta/2 \\
\Delta/2 & \varepsilon_*+\Delta
\end{pmatrix}.
\]

This is the operator of [TWO_MODE_PROOF.md](TWO_MODE_PROOF.md).

## Spectral stability

The condensate is spectrally stable, in a given truncation, when

\[
\min_{k\in[-q_*,q_*]}\sigma\bigl(H(k)\bigr)\;\ge\;0.
\]

The two-mode theorem concerns only \(H_{\rm 2\times 2}\). The
multimode suite asks whether the same amplitude bound continues to
hold for \(H(k)\) as \(N\) increases.
