# Whole road — 14J.5F through C1–C3, against the drive freeze

This note looks at the entire factor-of-two line as one object,
then places it next to coherence-drive Stage 1. It does not
unlock thrust. It records what the mathematics actually did.

```text
thrust_validated            = false
energy_extraction_validated = false
experimental_validation     = false
phi_loop_sq                 = undefined_in_tested_space
factor_two_is_quantum       = not_demonstrated
cft_x_import                = false
ware_constant_0p08          = false
```

## The road, in order

1. Working note 14J.5F produced a two-mode identity:
   frozen saddle supplies half the Bloch gap.
2. That identity was isolated in `beyond-repair/bloch-coherence-factor2`
   so it could not silently become CFT-X or a drive law.
3. Theorems A–C on `main` are exact for a *named operator*,
   not for a unique parent action.
4. No local \(\beta\phi^4\) owns both frozen variations.
   On-shell, any such parent has \(\Omega_-^2=0\), not
   \(\varepsilon_*/2\).
5. P1–P4 is a matrix. No column was selected.
6. Named C1–C3 actions that were written independently of
   the target Hessian all fail both P3 constraints.
7. Therefore \(\varphi_{\rm loop}^2\) is undefined in the
   tested space. The discrepancy has not been shown to be
   quantum.

## What was missing, and is now visible

The missing object was never a loop prefactor.
It was a parent whose first and second variations agree.

That is the same *class* of error the drive freeze already
rejected in the hybrid ratio \(0.795:1:1.993\): two different
normalizations multiplied together and treated as physics.

Here the two normalizations are

\[
\beta_{\rm saddle}=\lambda/24,
\qquad
\beta_{\rm Hessian}=\lambda/48.
\]

Their ratio is 2 because the frozen saddle and the frozen
Hessian were not required to come from one action. Isolating
that fact is the reusable result of this repository.

## What this line cannot do for the drive

Coherence-drive Stage 1 is already explicit:

- vacuum power extraction is undefined,
- thrust is not validated,
- \(\kappa\) must not be fit to \(3\times10^{-8}\,\mathrm{N/W}\),
- next gate is numerical
  geometry \(\to\Psi\to\nabla\Psi\to\chi\to\mathcal{G}\to\Delta F\).

Proof 14J on that repo is “collective \(W\) via HS gap,
\(\kappa\) free, no thrust.” 14J.5F tried to give that gap a
scalar condensate. The condensate, if it is the extremum of a
local quartic, is two-mode *marginal*. A marginal resonant
pair is a zero mode of the Hessian. A zero mode is not a
reservoir you can drain.

The background used on this repo,
\(\phi=\varphi_0\cos(q_*x)\), is a standing wave. In one
spatial dimension it is parity-even. It does not produce a
net surface integral \(\mathcal{G}\) of the kind the drive
formula needs. Adding a periodic mass of either sign does
not break that parity.

So even a future INDEPENDENT-PASS for P3 would explain the
*operator pair*. It would not, by itself, be a propulsion
mechanism.

## Mathematics that is actually new here

Not a drive law. Three identities worth keeping:

**I1.** Local virial of \(\beta\phi^4\) in the single-mode
truncation: on-shell first variation implies on-shell
\(\Omega_-^2=0\).

**I2.** Portal obstruction (C2): the Fourier condition for
stationarity and the Fourier condition for a multiplicative
Hessian of shape \(1+\cos 2q_*x\) are incompatible.

**I3.** Kernel obstruction (C3): a translation-invariant
quartic kernel produces an integral Hessian. The frozen
\(V_{\rm fluc}\) is multiplication. Those agree only if the
kernel is local, which returns to I1.

## What would actually move the drive

Inside the drive constitution, not inside this repo:

- Stage 2 on the frozen 0.45 geometry, with \(\kappa\)
  independent of the design target,
- a derived \(\Delta T_W\) after classical Maxwell subtraction,
- momentum closure on the engine geometry,
- an honest report if \(\mathcal{G}\approx 0\).

Those gates do not use Theorems A–C. Importing the factor of
two into \(\Delta F\) would be another hybrid ratio.

## Allowed conclusion

\[
\boxed{
\text{This line closed a parent-theory inconsistency.}
\text{ It did not define a working coherence drive.}
}
\]
