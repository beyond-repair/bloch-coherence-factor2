# Bloch Coherence Phase — Factor-of-Two Stability Bound

Narrow, falsifiable repository for one classical result.

> For the \(W+\lambda\phi^4\) modulated saddle, the classical condensate
> supplies exactly half the Bloch gap required for spectral stability.

This repository **does not** claim that the factor of two is a
fundamental constant of nature. It records a structural ratio of a
specific model and a test that can break it.

```text
claim_class            = classical_two_mode_theorem
factor_of_two_status   = structural_ratio_in_this_model
universal_constant     = false
cft_x_import           = false
phenomenological_fit   = false
thrust                 = false
ads_rescue             = false
ware_constant_0p08     = false
loop_correction        = deferred_to_branch_14J.5F.1
```

## Why this repo exists

14J.5F crossed from “another failed model iteration” into a reusable
mathematical result. The result is small enough to freeze, and sharp
enough to falsify.

It is **not** a CFT-X repository.

## Central theorem

Start from

\[
K(q)=\mu^2-Wq^2+\frac{cq^4}{M^2},\qquad
q_*^2=\frac{WM^2}{2c},\qquad
\varepsilon_*=K(q_*)=\mu^2-\frac{W^2M^2}{4c}.
\]

The classical saddle \(\phi(x)=\varphi_0\cos(q_*x)\) produces

\[
V_{\rm fluc}(x)=\frac{\lambda\varphi_0^2}{8}\bigl[1+\cos(2q_*x)\bigr],
\qquad
\Delta=\frac{\lambda\varphi_0^2}{8}.
\]

On the saddle, \(\varphi_0^2=8|\varepsilon_*|/\lambda\), hence
\(\Delta=|\varepsilon_*|\). The resonant Bloch matrix has off-diagonal
\(V=\Delta/2\), so

\[
\Omega_-^2=\varepsilon_*+\Delta-|V|=\varepsilon_*+\frac{\Delta}{2}=\frac{\varepsilon_*}{2}<0.
\]

Spectral stability of the same two-mode reduction requires
\(\Delta\ge 2|\varepsilon_*|\), therefore

\[
\frac{\varphi_{\rm stable}^2}{\varphi_{\rm saddle}^2}=2.
\]

Proofs: [THEOREM_FACTOR2.md](THEOREM_FACTOR2.md),
[TWO_MODE_PROOF.md](TWO_MODE_PROOF.md),
[STABILITY_BOUND.md](STABILITY_BOUND.md).

## Frozen exclusions

The following are **out of scope** on `main`. Do not add them.

- no \(W\approx 0.08\)
- no phenomenological fitting
- no thrust
- no AdS rescue
- no CFT-X parameter import
- no assumption that factor-of-two = fundamental constant

Loop corrections live on a separate branch and must not rewrite the
classical identities. See [LOOP_CORRECTION.md](LOOP_CORRECTION.md).

## Layout

```text
bloch-coherence-factor2/
├── README.md
├── THEOREM_FACTOR2.md
├── MODEL.md
├── BLOCH_OPERATOR.md
├── TWO_MODE_PROOF.md
├── MULTIMODE_PROOF.md
├── STABILITY_BOUND.md
├── FALSIFICATION.md
├── NUMERICS.md
├── INTERPRETATION_FORK.md
├── LOOP_CORRECTION.md          # 14J.5F.1 protocol only
├── src/bloch_factor2/
├── tests/test_factor2.py
└── data/
```

## What the suite asserts

The key automated assertion is

\[
R \stackrel{?}{=} 2
\qquad\text{where}\qquad
R=\frac{\varphi_{\rm stable}^2}{\varphi_{\rm saddle}^2}.
\]

On the two-mode reduction this is an identity, not a fit. On the
truncated multimode Bloch operator it is an empirical question: if
higher modes move \(R\) off 2, the suite reports the drift instead of
redefining the theorem.

Run:

```bash
pip install -r requirements.txt
PYTHONPATH=src pytest
```

## Interpretation fork (recorded, not decided)

If a later one-loop shift still satisfies
\(\varphi_{\rm loop}^2\ge 16|\varepsilon_*|/\lambda\), the scalar
realization survives and must face the six-condition gatekeeper.

If instead \(\varphi_{\rm loop}^2<16|\varepsilon_*|/\lambda\)
everywhere, the scalar quartic channel systematically under-restores
its own spectral instability. That is a result, not a license to add
another scalar coupling.

See [INTERPRETATION_FORK.md](INTERPRETATION_FORK.md).

## Provenance

Derived from working note 14J.5F. Isolated here so that 14J.5F.1
cannot silently alter the baseline it is supposed to test.

© 2026 Brian Ware / AtomicDreamlabs. All rights reserved.
