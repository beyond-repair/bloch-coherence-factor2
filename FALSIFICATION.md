# Falsification protocol

The theorem is useful only if it can fail in public.

## Primary assertion

On the two-mode reduction,

\[
R
:=
\frac{\varphi_{\rm stable}^2}{\varphi_{\rm saddle}^2}
\stackrel{?}{=}
2
\]

must hold as an identity for every condensing parameter tuple
\((W,\lambda,M,c,\mu)\).

Failure mode: any condensing tuple with analytic \(R\neq 2\).
That would mean the algebra in TWO_MODE_PROOF.md is wrong.

## Secondary assertion

On the \(N\)-mode Bloch operator,

\[
R_N
:=
\frac{\varphi_{\rm stable,N}^2}{\varphi_{\rm saddle}^2}
\]

is measured, not assumed. A drift away from 2 does **not** falsify
Theorems A–C. It falsifies the stronger, unstated claim
“the factor of two survives projection to the full operator.”

## Required observables

| symbol | meaning |
|---|---|
| \(\varepsilon_*\) | \(K(q_*)\) |
| \(\varphi_{\rm saddle}^2\) | \(8|\varepsilon_*|/\lambda\) |
| \(\varphi_{\rm stable}^2\) | smallest amplitude with \(\min_k\Omega^2\ge 0\) |
| \(R\) | ratio of those amplitudes |
| \(\Omega_-^2\) | lower two-mode eigenvalue |
| \(\Delta+\varepsilon_*\) | must vanish on the saddle |
| \(N\) | mode half-count; 9-mode means \(N=4\) |

## Sweep

Vary \(W,\lambda,M,c,\mu\) over a grid that stays in
\(\varepsilon_*<0\). No grid point may pin \(W\) to \(0.08\).

## Pass / fail

- **PASS (theorem).** Analytic \(R=2\) and
  \(\Omega_-^2=\varepsilon_*/2\) on the saddle, for every
  condensing tuple.
- **REPORT (operator).** Print \(R_N\) versus \(N\). Do not
  rewrite Theorem C to match \(R_N\).
- **FAIL.** Analytic identities broken, or a code path that
  injects CFT-X / \(0.08\) / thrust / AdS / loop shifts into
  the classical observables.

## What would actually kill the scalar channel

That question is not answered on `main`. It is the
interpretation fork after 14J.5F.1
([INTERPRETATION_FORK.md](INTERPRETATION_FORK.md),
[LOOP_CORRECTION.md](LOOP_CORRECTION.md)).
