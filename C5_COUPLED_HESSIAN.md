# C5 — on-shell coupled Hessian

C4 killed the shortcut “freeze \(\chi\), read the \(\phi\) matrix.”
This file asks the remaining conventional question.

Do not invent \(\omega(2q_*)/\omega(0)=3/2\).

## 1. \(K(q)\) does not determine the collective kernel

\[
S_\chi=\frac12\int\frac{dq}{2\pi}\,\chi(-q)\,\omega(q)\,\chi(q),
\qquad
S_{\rm int}=\frac g2\int dx\,\chi\phi^2.
\]

Imposed only:

- real fields \(\Rightarrow\omega(q)=\omega(-q)\in\mathbb{R}\)
- translational invariance \(\Rightarrow\omega=\omega(|q|)\)
- positivity of a propagating \(\chi\) \(\Rightarrow\omega(q)>0\) on the
  retained harmonics, *or* auxiliary sign recorded as C4-A
- \(S_\phi\) recovers the frozen \(K(q)\) when \(\chi=0\)
- no coefficient taken from Theorems A–C

None of those conditions is an equation for the pair
\((\omega(0),\omega(2q_*))\).

\(2q_*\) is a scale of the \(\phi\) kernel,
\(q_*^2=WM^2/(2c)\). It is not a zero, pole, or threshold of a
generic independent \(\omega\).

If one *sets* \(\omega=K\), then

\[
\frac{K(2q_*)}{K(0)}
=
1+\frac{2W^2M^2}{c\mu^2},
\]

which ranges over an interval as \((W,c,M,\mu)\) vary and is not
identically \(3/2\).

\[
\boxed{
K(q)\text{ does not determine the collective-sector kernel at }0,2q_*.
}
\]

Therefore \(3/2\) is an independent assumption, not a corollary of
the frozen dispersion.

## 2. Coupled backgrounds, then the full Hessian

Same cubic as C4. Galerkin backgrounds

\[
\phi_*=\varphi_0\cos(q_*x),
\qquad
\chi_*=\chi_0+\chi_2\cos(2q_*x)
\]

solve the projected EOM first. Only then form

\[
\mathcal H
=
\begin{pmatrix}
S_{\phi\phi}&S_{\phi\chi}\\
S_{\chi\phi}&S_{\chi\chi}
\end{pmatrix}.
\]

Even sector \(\{\cos q_*,\,1,\,\cos 2q_*\}\) and odd sector
\(\{\sin q_*,\,\sin 2q_*\}\) decouple.

On shell the even \(\phi\) diagonal vanishes (it *is* the EOM).
The odd \(\phi\) diagonal is \(-g\chi_2\).

Orthonormal odd block:

\[
\begin{pmatrix}
\gamma^2/(4\omega_2) & \gamma/2 \\
\gamma/2 & \omega_2
\end{pmatrix},
\qquad
\gamma=g\varphi_0.
\]

Its characteristic equation is

\[
\lambda\bigl(\lambda-\omega_2-\gamma^2/(4\omega_2)\bigr)=0.
\]

\[
\boxed{
\Omega_{\rm odd,min}^2=0
\quad\text{identically, on shell, for any }\omega(2q_*)\neq 0.
}
\]

That zero is the sliding mode of a periodic condensate once
\(\chi\) is allowed to move with it. It is not \(\varepsilon_*/2\).

The other odd eigenvalue is \(\omega_2+\gamma^2/(4\omega_2)\).
The even amplitude mode is massive and depends on
\((\omega(0),\omega(2q_*),\gamma)\).

## 3. Diagnostic, in the required order

1. Solve the projected EOM.
2. Read

\[
\Omega_{\rm min}^2=f(\varepsilon_*,\omega(0),\omega(2q_*),g).
\]

3. Ask whether \(f=\varepsilon_*/2\) on an open set.

Result:

- Odd minimum is \(0\) on the entire on-shell surface.
- \(\varepsilon_*/2\) is negative. It is not that zero.
- Matching \(\varepsilon_*/2\) in a *fixed-\(\chi\)* matrix still
  requires the fit \(\omega(2q_*)/\omega(0)=3/2\), which §1 forbids
  as a derivation from \(K\).
- C4-P (\(\omega>0\) on both harmonics) cannot sit on
  \(\varepsilon_*<0\) at all: the cubic with positive \(\omega\)
  produces \(\varepsilon_*>0\) on shell.
- C4-A (\(\omega=-\mu^2\)) can sit on \(\varepsilon_*<0\), but then
  \(\chi\) itself is unbounded below, and the odd coupled minimum
  is still \(0\), not \(\varepsilon_*/2\).

\[
\boxed{
\text{On-shell coupled cubic: }\Omega_{\rm min}^2=0\neq\varepsilon_*/2.
}
\]

No open region of \((\omega(0),\omega(2q_*),g)\) produces the
frozen two-mode value as a coupled eigenvalue.

## 4. Hierarchy, updated

```text
operator identity          frozen on main
consistent parent          not found in C1–C5 conventional families
on-shell coupled spectrum  Ω_odd = 0, not ε*/2
multimode / quantum        blocked (no parent)
propulsion                 not this repository
```

A later theory may still *define* an emergent Bloch-gap ratio of
*that* theory. C5 says the conventional cubic two-sector theory
does not have the frozen ratio as an on-shell eigenvalue.

\(\mathcal{G}\simeq 0\Rightarrow\Delta F\simeq 0\) remains allowed.
