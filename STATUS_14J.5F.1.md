# Status — 14J.5F.1

**Date recorded.** 2026-09-25
**Branch.** `14J.5F.1-loop-correction`
**Baseline.** `main` @ freeze of Theorems A–C

## Order that is now enforced

\[
\boxed{
\text{CLASSICAL FREEZE}
\;\rightarrow\;
\text{PARENT-ACTION CONSISTENCY TEST}
\;\rightarrow\;
\text{QUANTIZATION}
}
\]

A guessed tadpole is not an experiment on this branch.

## Discovery that moved upstream

\[
\boxed{
\text{The frozen classical pair is internally incompatible with a single local }\beta\phi^4\text{ parent action.}
}
\]

\[
\beta_{\rm saddle}=\frac{\lambda}{24},
\qquad
\beta_{\rm Hessian}=\frac{\lambda}{48},
\qquad
\beta_{\rm saddle}=2\beta_{\rm Hessian}.
\]

The original question “can loops supply the missing factor of 2?”
is therefore the wrong next question. The first and second
variations already disagree.

Further, for every local \(\beta\phi^4\),

\[
\Omega_-^2=0
\quad\text{on any amplitude that solves the projected EOM.}
\]

A local quartic cannot under-restore its own two-mode pair.
Theorem A cannot be the on-shell spectrum of such a parent.

## Comparative archaeology, not a chosen parent

| parent | preserves | sacrifices |
|---|---|---|
| P1 | classical saddle | frozen Hessian normalization |
| P2 | frozen operator | unique local \(\phi^4\) interpretation |
| P3 | both identities, *if* an extra sector exists | minimal single-field closure |
| P4 | frozen Hessian | classical saddle as extremum |

P3 is a hypothesis that the scalar sector is incomplete. It is
not a rescue mechanism. The extra Hessian is derived as
\(-V_{\rm fluc}^{\rm fr}\), not inserted to make \(\Omega_-^2\) pretty.

Five questions per parent: EOM, Hessian, Theorem A, Theorem B,
quantization without an extra parameter.
Full matrix: [PARENT_FALSIFICATION.md](PARENT_FALSIFICATION.md).
P3 constraint: [PARENT_P3.md](PARENT_P3.md).

No parent is selected.

## Files on this branch

| file | role |
|---|---|
| [PARENT_ACTION.md](PARENT_ACTION.md) | uniqueness obstruction |
| [PARENT_FALSIFICATION.md](PARENT_FALSIFICATION.md) | P1–P4 matrix and five questions |
| [PARENT_P3.md](PARENT_P3.md) | extra sector as constraint |
| [QUANTUM_PRESCRIPTION.md](QUANTUM_PRESCRIPTION.md) | seven locks; all still blocked |
| [LOOP_CORRECTION.md](LOOP_CORRECTION.md) | no number until locks close |
| `src/bloch_factor2/parents.py` | exact P1/P2/P4 identities |
| `tests/test_parents.py` | matrix assertions, classical only |

## Still absent

- no \(\varphi_{\rm loop}^2\)
- no guessed tadpole
- no edit to Theorems A–C on `main`
- no \(W\approx 0.08\), CFT-X, thrust, or AdS
- no promotion of \(2\) to a constant of nature

## Interpretation fork

Untouched. Factor \(2\) remains a structural two-mode ratio in
the frozen operator. Whether any parent owns that operator is
the question this branch is now asking.
