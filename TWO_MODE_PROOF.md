# Two-mode proof

## Matrix

\[
H
=
\begin{pmatrix}
\varepsilon_*+\Delta & V \\
V & \varepsilon_*+\Delta
\end{pmatrix},
\qquad
V=\frac{\Delta}{2}.
\]

## Eigenvalues

\[
\Omega_\pm^2
=
\varepsilon_*+\Delta\pm|V|
=
\varepsilon_*+\Delta\pm\frac{\Delta}{2}.
\]

Explicitly

\[
\Omega_+^2=\varepsilon_*+\frac{3\Delta}{2},
\qquad
\Omega_-^2=\varepsilon_*+\frac{\Delta}{2}.
\]

## Saddle substitution

Classical saddle: \(\Delta=|\varepsilon_*|\). In the condensing
regime \(\varepsilon_*<0\), so \(\Delta=-\varepsilon_*\) and

\[
\Omega_-^2
=
\varepsilon_*+\frac{|\varepsilon_*|}{2}
=
\varepsilon_*-\frac{\varepsilon_*}{2}
=
\frac{\varepsilon_*}{2}<0.
\]

That is Theorem A:

\[
\boxed{\Omega_-^2=\frac{\varepsilon_*}{2}<0.}
\]

The classical condensate therefore restores only half of the gap
needed to lift the resonant pair above zero.

## Identity check

The algebraic relation

\[
\Omega_-^2-\Bigl(\varepsilon_*+\frac{\Delta}{2}\Bigr)=0
\]

holds for every \((\varepsilon_*,\Delta)\) with \(\Delta\ge 0\), not
only on the saddle. The numerical suite asserts this residual is
machine zero.
