# Quantum prescription — seven locks

Status of every lock: **BLOCKED**.
A one-loop inequality computed with any lock still open is not
an output of this repository.

The comparison requested by LOOP_CORRECTION.md is

\[
\varphi_{\rm loop}^2
\;\stackrel{?}{\ge}\;
\frac{16|\varepsilon_*|}{\lambda}.
\]

That comparison is well-posed only after the following seven
entries are filled with a single internally consistent choice.
Filling them with a guess is a phenomenological fit, which this
repository forbids.

## 1. Parent action / contour

**Status.** BLOCKED.

Required: one action \(S[\phi,\ldots]\) and a statement of
Lorentzian versus Euclidean contour.

Frozen kinetic piece, if a local scalar is kept:

\[
S_{\rm kin}
=
\int\!dt\,dx\,
\Biggl[
\frac12(\partial_t\phi)^2
-\frac12\,\phi\,K(-i\partial_x)\,\phi
\Biggr].
\]

Interaction piece is not unique. See PARENT_ACTION.md.
Options on the table: P1, P2, P3, P4. None selected.

## 2. Spacetime dimension

**Status.** BLOCKED.

The classical operator is written in one spatial dimension.
A tadpole \(G(x,x)\) in \(d=1+1\) is logarithmically sensitive
to the IR of the Goldstone / resonant pair and to the UV of
\(K(q)\sim q^4\). In any other \(d\) the degree changes.

No dimension is inherited from CFT-X. None is adopted here.

## 3. Exact quartic normalization

**Status.** BLOCKED.

MODEL.md fixes \(\lambda\) by the pair of classical identities,
not by \(\mathcal{L}_{\rm int}=\lambda\phi^4/4!\) or
\(\lambda\phi^4/4\).

Those two conventions are incompatible with the frozen pair
(PARENT_ACTION.md). Until one parent is chosen, \(\lambda\) in a
loop integrand is an undefined symbol.

## 4. Fluctuation propagator around the periodic saddle

**Status.** BLOCKED pending (1)–(3).

Candidate, *if* one takes the frozen operator as primitive:

\[
G=\bigl(\partial_t^2+H\bigr)^{-1},
\qquad
H=K(-i\partial_x)+V_{\rm fluc}(x).
\]

This is well-defined as a classical Green function of \(H\).
It becomes the loop propagator only after the action that owns
\(H\) is named, because the measure and the vertices live in
that action, not in \(H\).

## 5. UV regulator

**Status.** BLOCKED.

\(K(q)\sim (c/M^2)q^4\) already improves the UV relative to a
second-order kinetic term. That is not a regulator of the loop.
A cutoff, Pauli–Villars partner, heat kernel, or dimensional
regulator must be named. None is named.

## 6. Renormalization condition

**Status.** BLOCKED.

Possible conditions, none adopted:

- subtract \(G\) so that the quadratic pocket \(\varepsilon_*\)
  stays at its classical value;
- subtract at vanishing condensate;
- subtract at the two-mode threshold \(\Omega_-^2=0\).

Different subtractions move \(\varphi_{\rm loop}^2\) across the
line \(16|\varepsilon_*|/\lambda\). Choosing one after seeing
the number is a fit.

## 7. Meaning of \(\varphi_{\rm loop}^2\)

**Status.** BLOCKED.

The protocol must say which of the following is intended:

\[
\varphi_{\rm loop}^2
=
\varphi_{\rm saddle}^2+\delta\varphi^2,
\]

with \(\delta\varphi^2\) the shift of the *extremum* of the
effective potential;

or the amplitude at which the *one-loop* Bloch operator first
satisfies \(\min_k\Omega^2\ge 0\);

or a Hartree self-consistent condensate including
\(\langle\psi^2\rangle\).

Those three objects are not equal. The inequality in
LOOP_CORRECTION.md names only one symbol.

## Closure rule

All seven locks SHALL be marked OPEN with an explicit choice
before any file in this branch may contain a numerical or
symbolic value of \(\varphi_{\rm loop}^2\).

Partial closures are allowed in working notes only if they
carry the label `PROVISIONAL` and do not update
INTERPRETATION_FORK.md.

## Forbidden shortcuts

- “use dimensional regularization in \(d=4\) because that is
  standard”
- “use \(d=1+1\) because the Bloch operator is 1D” without
  writing the IR treatment of \(\Omega_-^2\approx 0\)
- “take \(\lambda G(0)\) with a hard cutoff at \(M\)”
- any numerical prefactor inherited from CFT-X, Ware-constant
  phenomenology, or a previous failed model iteration
