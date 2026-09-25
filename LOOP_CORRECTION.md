# Loop correction — 14J.5F.1

**This file is a protocol, not a result.**

Loop corrections are forbidden from altering Theorems A–C.
This file lives on branch `14J.5F.1-loop-correction`.
On `main` the sibling file is the shorter freeze notice.

## Current state

The comparison

\[
\varphi_{\rm loop}^2
\quad\text{versus}\quad
\frac{16|\varepsilon_*|}{\lambda}
\]

is **not yet well-posed**.

Reason: MODEL.md defines the fluctuation normalization without a
parent quantum action, regulator, spacetime dimension, or
renormalization prescription. A tadpole of the form
\(\lambda G(x,x)\) therefore has no unique meaning.
See [PARENT_ACTION.md](PARENT_ACTION.md) and
[QUANTUM_PRESCRIPTION.md](QUANTUM_PRESCRIPTION.md).

No value of \(\varphi_{\rm loop}^2\) is reported in this commit.
Fabricating one would reintroduce the model-dependent assumption
this repository exists to isolate.

## Purpose, once the seven locks close

Compute the one-loop (or Hartree / tadpole) object named in lock 7
and compare it to the classical stability bound

\[
\varphi_{\rm stable}^2=\frac{16|\varepsilon_*|}{\lambda}.
\]

## Allowed output, once the locks close

One of two inequalities, plus the numbers that produced it, plus
the locked prescription that made them unique:

\[
\varphi_{\rm loop}^2
\;\ge\;
\frac{16|\varepsilon_*|}{\lambda}
\qquad\text{or}\qquad
\varphi_{\rm loop}^2
\;<\;
\frac{16|\varepsilon_*|}{\lambda}.
\]

## Forbidden output

- any edit to \(\varphi_{\rm saddle}^2=8|\varepsilon_*|/\lambda\)
- any edit to \(R=2\) as a two-mode identity on `main`
- any import of \(W\approx 0.08\), thrust, AdS, or CFT-X
- any retuning of \(\lambda\) to force the inequality
- any \(\varphi_{\rm loop}^2\) written while a lock in
  QUANTUM_PRESCRIPTION.md is still BLOCKED

## Correct next move

Not another classical iteration.
Not a guessed tadpole.

Reconstruct *one* minimal parent quantum action consistent with
a stated subset of the frozen classical data, lock the seven
entries, derive the one-loop shift from that action, and only
then let the inequality decide Branch L versus Branch U.

If the chosen parent cannot keep both frozen identities, that
fact is the result. It is not a cue to average the two
\(\beta\) values because they differ by two.
