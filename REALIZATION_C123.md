# C1–C3 realization audit

Every candidate below is an action written *before* the Hessian
target. Couplings are not adjusted to manufacture
\(\Omega_-^2=\varepsilon_*/2\).

P3 target: \(E_{\rm extra}=0\) and
\(H_{\rm extra}=-V_{\rm fluc}^{\rm fr}\).

## Summary

| id | independent? | \(E=0\) | \(H=-V_{\rm fluc}\) | verdict |
|---|---|---|---|---|
| C1a | yes | yes if \(\pi\) monochromatic | no (\(H=0\)) | INDEPENDENT-FAIL |
| C1b | yes | yes on the kernel | no (vanishes on the resonant pair) | INDEPENDENT-FAIL |
| C1c | no | by construction | by construction | COUNTERTERM |
| C2a | yes | only if \(\psi_*=0\) or \(g=0\) | then \(H=0\) | INDEPENDENT-FAIL |
| C2b | yes | force \(\propto\langle\cos^2,\psi^2\rangle\ge 0\) | \(H=g\psi^2\) dies with the force | INDEPENDENT-FAIL |
| C3a | yes | only if \(\gamma=0\) | no | INDEPENDENT-FAIL |
| C3b | yes | already in P1 | wrong sign and size | INDEPENDENT-FAIL |
| C3c | kernel named first | only if \(\tilde U\) fitted | integral operator \(\neq\) multiplication | INDEPENDENT-FAIL or COUNTERTERM |

No INDEPENDENT-PASS.

\[
\boxed{
\text{No admissible independently defined parent identified in C1–C3}
\;\Rightarrow\;
\text{loop experiment remains undefined}.
}
\]

No-go for *these named actions*, not for every extra sector.
Copying \(-V_{\rm fluc}^{\rm fr}\) into the Lagrangian is not a derivation.

## C2a contradiction

Projected stationarity: \(\psi_0+\frac12\psi_{2q_*}=0\).
Hessian shape \(-V_{\rm fluc}^{\rm fr}\propto 1+\cos 2q_*x\):
\(\psi_0=\psi_{2q_*}\).
Incompatible unless \(\psi=0\).

## C2b contradiction

\(\langle\cos^2,\psi^2\rangle\ge 0\), vanishing only at \(\psi=0\),
which kills \(H_{\rm extra}\).

## C1a/C1b

Linear or quadratic monochromatic projectors annihilate the
resonant pair. They cannot supply a multiplicative periodic mass.

## C3c

A named translation-invariant \(U\) gives an integral Hessian.
Matching the multiplication operator requires \(U\propto\delta\)
(local, already failed) or fitting \(\tilde U(0)\) and
\(\tilde U(2q_*)\) (counterterm).
