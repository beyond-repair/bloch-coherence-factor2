# P3 — extra sector as a constraint, not a rescue

P3 is the hypothesis that the scalar field is not the complete
parent. It is not a mechanism invented to save the factor of two.

## What must be true if both frozen identities are kept

Start from the unique local action that owns the frozen saddle,

\[
S_{\rm P1}[\phi]
=\int
\Biggl[
\frac12(\partial_t\phi)^2
-\frac12\,\phi\,K\phi
-\frac{\lambda}{24}\phi^4
\Biggr],
\]

and add whatever else is needed:

\[
S_{\rm P3}=S_{\rm P1}[\phi]+S_{\rm extra}[\phi,\psi,\ldots].
\]

On the frozen background \(\phi=\varphi_0\cos(q_*x)\) with
\(\varphi_0^2=8|\varepsilon_*|/\lambda\),

\[
V''_{\rm P1}(x)
=
\frac{\lambda\varphi_0^2}{4}\bigl[1+\cos(2q_*x)\bigr]
=
2\,V_{\rm fluc}^{\rm fr}(x).
\]

Demand stationarity of \(S_{\rm P3}\) at the frozen saddle and
equality of the \(\phi\)-Hessian with the frozen operator.
P1 is already on-shell, so

\[
\left.\frac{\delta S_{\rm extra}}{\delta\phi}\right|_*=0,
\qquad
\left.\frac{\delta^2 S_{\rm extra}}{\delta\phi^2}\right|_*
=
V_{\rm fluc}^{\rm fr}-V''_{\rm P1}
=
-V_{\rm fluc}^{\rm fr}.
\]

\[
\boxed{
S_{\rm extra}
\text{ must be stationary in }\phi\text{ on the frozen saddle}
\text{ and contribute }-V_{\rm fluc}^{\rm fr}
\text{ to the }\phi\text{-Hessian.}
}
\]

The minus sign is derived. Nobody put a two into \(S_{\rm extra}\)
by hand.

## Realization classes (not selected)

**C1.** Constraint / multiplier.
**C2.** Second scalar with a locked background.
**C3.** Non-local quartic in \(\phi\) alone.

Any concrete realization MUST be checked against the five
questions. The coupling is either fixed by the constraint
above or the class is rejected. No post-hoc retuning of \(g\)
to make \(\Omega_-^2=\varepsilon_*/2\).

## Failure modes that would kill P3

- no \(\psi\)-background satisfies both extra-variation conditions
- the \(\psi\)-sector itself has \(\Omega^2<0\) worse than the scalar pair
- the only realizations reintroduce an unfixed coupling (P3 collapses to P2)

If P3 fails as a classical parent, there is nothing for a scalar
tadpole to repair.
