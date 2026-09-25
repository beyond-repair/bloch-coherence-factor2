# Status — 14J.5F.1

**Date recorded.** 2026-09-25
**Branch.** `14J.5F.1-loop-correction`
**Baseline.** `main` @ freeze of Theorems A–C

## Result of inspecting the branch, not of assuming it

The loop experiment is **not uniquely defined** by the frozen
repository.

The branch protocol correctly requires a comparison of

\[
\varphi_{\rm loop}^2
\qquad\text{with}\qquad
\frac{16|\varepsilon_*|}{\lambda}.
\]

MODEL.md never supplies the objects that would make that comparison
unique: parent quantum action, regulator, spacetime dimension, or
renormalization condition. It explicitly chooses the quartic
normalization to reproduce the classical identities *independently
of the parent Lagrangian convention*.

That sentence is harmless classically. It is fatal at one loop.

## What this branch now contains

| file | role |
|---|---|
| [PARENT_ACTION.md](PARENT_ACTION.md) | uniqueness obstruction for a local \(\phi^4\) parent |
| [QUANTUM_PRESCRIPTION.md](QUANTUM_PRESCRIPTION.md) | seven locks; all blocked |
| [LOOP_CORRECTION.md](LOOP_CORRECTION.md) | protocol amended: no number until the locks close |

## What this branch does not contain

- no fabricated \(\varphi_{\rm loop}^2\)
- no guessed tadpole \(\lambda G(x,x)\)
- no edit to Theorems A–C
- no \(W\approx 0.08\), CFT-X, thrust, or AdS

## Boundary of the model

\[
\boxed{
\text{classical two-mode theorem is closed}
\neq
\text{its quantum extension is specified}.
}
\]

That is a real boundary, not a failed experiment.

The interpretation fork is untouched:
factor \(2\) remains a structural two-mode ratio, not a universal
constant. See [INTERPRETATION_FORK.md](INTERPRETATION_FORK.md).
