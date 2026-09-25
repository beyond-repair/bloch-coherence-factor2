# Loop correction — 14J.5F.1

**This file is a protocol, not a result.**

Loop corrections are forbidden from altering Theorems A–C.
The experiment lives on branch `14J.5F.1-loop-correction`.

## Purpose

Compute a one-loop (or Hartree / tadpole) shift of the condensate
amplitude, call it \(\varphi_{\rm loop}^2\), and compare it to the
classical stability bound

\[
\varphi_{\rm stable}^2=\frac{16|\varepsilon_*|}{\lambda}.
\]

## Allowed output

One of two inequalities, plus the numbers that produced it:

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
- any edit to \(R=2\) as a two-mode identity
- any import of \(W\approx 0.08\), thrust, AdS, or CFT-X
- any retuning of \(\lambda\) to force the inequality the
  author prefers

## Why this is a separate branch

14J.5F.1 is an experiment *on top of* a frozen baseline.
If the loop shift is mixed into `main`, the baseline it is
supposed to test will move under the experiment.

Create the branch from the commit that froze Theorems A–C.
Do not merge it back until the inequality is reported and
the classical files are byte-identical to `main`.
