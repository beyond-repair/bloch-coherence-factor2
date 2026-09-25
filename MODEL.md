# Model

Exact classical construction. No imported scale.

## Dispersion kernel

\[
K(q)=\mu^2-Wq^2+\frac{cq^4}{M^2}.
\]

Stationary wavevector of the quadratic form:

\[
\partial_{q^2}K
=
-W+\frac{2cq^2}{M^2}=0
\qquad\Longrightarrow\qquad
q_*^2=\frac{WM^2}{2c}.
\]

On-shell value:

\[
\varepsilon_*
=
K(q_*)
=
\mu^2-W\cdot\frac{WM^2}{2c}+\frac{c}{M^2}\left(\frac{WM^2}{2c}\right)^2
=
\mu^2-\frac{W^2M^2}{4c}.
\]

Condensation of a monochromatic mode at \(q_*\) requires \(\varepsilon_*<0\).

## Background

\[
\phi(x)=\varphi_0\cos(q_*x).
\]

This is a real standing wave. Complex traveling-wave equivalents differ
by a global phase and are not used here.

## Quartic and fluctuation potential

The interaction used in this repository is the one that produces the
stated identities

\[
\varphi_{\rm saddle}^2=\frac{8|\varepsilon_*|}{\lambda},
\qquad
\Delta=\frac{\lambda\varphi_0^2}{8}.
\]

Those two equations fix the normalization of \(\lambda\) relative to
the second variation. Independently of the parent Lagrangian’s
factorial convention, the quadratic fluctuation potential about
\(\phi=\varphi_0\cos(q_*x)\) is taken to be

\[
V_{\rm fluc}(x)
=
\frac{\lambda\varphi_0^2}{8}
\bigl[1+\cos(2q_*x)\bigr].
\]

Derivation sketch. Use \(\cos^2\theta=\tfrac12\bigl(1+\cos 2\theta\bigr)\).
A local mass correction proportional to \(\phi^2\) then yields a
constant piece plus a piece oscillating at \(2q_*\). The coefficient
is chosen so that the constant piece equals \(\lambda\varphi_0^2/8\).

## Saddle amplitude

Balancing the negative quadratic pocket \(\varepsilon_*\) against the
constant piece of \(V_{\rm fluc}\) at leading order in the condensate
gives

\[
\Delta_{\rm saddle}=|\varepsilon_*|
\qquad\Longrightarrow\qquad
\varphi_{\rm saddle}^2=\frac{8|\varepsilon_*|}{\lambda}.
\]

This is the *classical saddle*, not the spectrally stable amplitude.

## Parameters that may vary

\(W,\lambda,M,c,\mu\) are free so long as \(W>0\), \(\lambda>0\),
\(c>0\), \(M\neq 0\), and \(\varepsilon_*<0\).

They are **not** pinned to any external phenomenology.
