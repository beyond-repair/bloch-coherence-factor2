# C1–C3 audit protocol

Mechanical layer on top of [PARENT_P3.md](PARENT_P3.md).
No parent is selected. No loop is computed.

## Distinction this layer exists to enforce

\[
\boxed{
\text{derived collective sector}
\neq
\text{reverse-engineered counterterm}.
}
\]

A candidate is a *derived collective sector* only if \(S_{\rm extra}\)
is written down independently of \(V_{\rm fluc}^{\rm fr}\) and the
two P3 identities are then *computed*. If \(S_{\rm extra}\) is
defined by copying the desired Hessian into the action, the
structure has been parameterized, not explained.

## Sign of the Hessian constraint

The total \(\phi\)-Hessian must equal the frozen operator:

\[
K+V''_{\rm P1}+H_{\rm extra}
=
K+V_{\rm fluc}^{\rm fr}.
\]

With \(V''_{\rm P1}=2V_{\rm fluc}^{\rm fr}\) this is

\[
H_{\rm extra}
=
V_{\rm fluc}^{\rm fr}-V''_{\rm P1}
=
-V_{\rm fluc}^{\rm fr}.
\]

The combination \(-V_{\rm fluc}^{\rm fr}+V''_{\rm P1}\) equals
\(+V_{\rm fluc}^{\rm fr}\) and would *double* the surplus, not
cancel it. That ordering is not used.

## What is computed, for every named \(S_{\rm extra}\)

\[
E_{\rm extra}
=
\left.\frac{\delta S_{\rm extra}}{\delta\phi}\right|_{\phi_*},
\qquad
H_{\rm extra}
=
\left.\frac{\delta^2 S_{\rm extra}}{\delta\phi^2}\right|_{\phi_*}.
\]

Required: \(E_{\rm extra}=0\) and \(H_{\rm extra}=-V_{\rm fluc}^{\rm fr}\).

Then the same five questions.

## Verdicts

INDEPENDENT-FAIL, INDEPENDENT-PASS, COUNTERTERM, ILL-POSED.
COUNTERTERM is P2 in variational language.
