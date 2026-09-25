# Parent action — uniqueness obstruction

**Claim.** There is no local potential \(V(\phi)=\beta\phi^4\) that
reproduces *both* frozen classical identities at once:

\[
\varphi_{\rm saddle}^2=\frac{8|\varepsilon_*|}{\lambda},
\qquad
V_{\rm fluc}(x)=\frac{\lambda\varphi_0^2}{8}\bigl[1+\cos(2q_*x)\bigr].
\]

The loop integrand \(\lambda G(x,x)\) is therefore not fixed by
`main`. Computing a number now would smuggle in a parent-action
choice that MODEL.md refused to make.

## Setup

Work in \(1+1\) only long enough to write the variational identities.
Dimension is not locked; see QUANTUM_PRESCRIPTION.md.

A local real scalar with the frozen kinetic kernel has action

\[
S[\phi]
=
\int\!dt\,dx\,
\Biggl[
\frac12(\partial_t\phi)^2
-\frac12\,\phi\,K(-i\partial_x)\,\phi
-\beta\phi^4
\Biggr],
\]

where \(K(q)=\mu^2-Wq^2+cq^4/M^2\) is the frozen kernel.
The quartic coefficient \(\beta\) is the only free normalization.

Background: \(\phi=\varphi_0\cos(q_*x)\), single-mode truncation
(third harmonic discarded, as on `main`).

## Identity from the equation of motion

\[
V'(\phi)=4\beta\phi^3,
\qquad
\cos^3\theta=\frac{3\cos\theta+\cos 3\theta}{4}.
\]

Project onto \(\cos(q_*x)\):

\[
\varepsilon_*\varphi_0+4\beta\varphi_0^3\cdot\frac34=0
\qquad\Longrightarrow\qquad
\varepsilon_*+3\beta\varphi_0^2=0.
\]

Condensing regime \(\varepsilon_*<0\):

\[
\varphi_0^2=\frac{|\varepsilon_*|}{3\beta}.
\]

Match the frozen saddle \(\varphi_0^2=8|\varepsilon_*|/\lambda\):

\[
\boxed{\beta_{\rm saddle}=\frac{\lambda}{24}=\frac{\lambda}{4!}.}
\]

The same stationarity condition is recovered from the spatially
averaged single-mode effective potential

\[
\mathcal{V}(\varphi_0)
=
\frac{\varepsilon_*}{4}\varphi_0^2
+\frac{\lambda}{64}\varphi_0^4,
\]

which is what MODEL.md means by “balancing the pocket against the
constant piece.”

## Identity from the Hessian

\[
V''(\phi)=12\beta\phi^2,
\qquad
\phi^2=\frac{\varphi_0^2}{2}\bigl[1+\cos(2q_*x)\bigr].
\]

So

\[
V''(x)=6\beta\varphi_0^2\bigl[1+\cos(2q_*x)\bigr].
\]

Match the frozen fluctuation potential
\(V_{\rm fluc}=(\lambda\varphi_0^2/8)[1+\cos(2q_*x)]\):

\[
6\beta=\frac{\lambda}{8}
\qquad\Longrightarrow\qquad
\boxed{\beta_{\rm Hessian}=\frac{\lambda}{48}.}
\]

## The two \(\beta\) values are not equal

\[
\beta_{\rm saddle}=\frac{\lambda}{24}
\;\neq\;
\beta_{\rm Hessian}=\frac{\lambda}{48}.
\]

They differ by exactly two. That is not a coincidence and it is
not a license to promote \(2\) to a constant of nature. It is the
statement that the frozen saddle and the frozen Hessian cannot
be the first and second variations of one local \(\phi^4\).

### If one trusts the local action that matches the saddle

\[
\beta=\frac{\lambda}{24}
\qquad\Longrightarrow\qquad
V''(x)=\frac{\lambda\varphi_0^2}{4}\bigl[1+\cos(2q_*x)\bigr].
\]

On the frozen saddle, \(\lambda\varphi_0^2/8=|\varepsilon_*|\), so
the *true* Hessian is twice the frozen \(V_{\rm fluc}\):

\[
\Delta_{\rm true}=2|\varepsilon_*|,
\qquad
V=\frac{\Delta_{\rm true}}{2}=|\varepsilon_*|,
\qquad
\Omega_-^2=\varepsilon_*+\Delta_{\rm true}-|V|=0.
\]

The classical two-mode pair is then *marginal*, not under-restored.
Adopting this parent would reinterpret Theorem A as a
half-counting of \(V''\). That reinterpretation is **forbidden on
`main`**. It is recorded here only as a parent-action option.

### If one trusts the local action that matches the Hessian

\[
\beta=\frac{\lambda}{48}
\qquad\Longrightarrow\qquad
\varphi_{\rm EOM}^2=\frac{|\varepsilon_*|}{3\beta}=\frac{16|\varepsilon_*|}{\lambda}.
\]

The stationary point of this potential already sits at the
two-mode stability bound of Theorem B. The frozen saddle
\(\varphi_{\rm saddle}^2=8|\varepsilon_*|/\lambda\) is then *not
an extremum*. Adopting this parent would abandon the frozen
saddle. Also forbidden on `main`.

## What a tadpole would have required

A Hartree / tadpole shift has the schematic form

\[
\delta m^2_{\rm 1L}
\sim
\frac{\partial^3 V}{\partial\phi^3}\,G(x,x)
\qquad\text{or}\qquad
\lambda_{\rm vertex}\,G(x,x),
\]

with

\[
G(x,x)
=
\int\frac{d\omega\,d^{d-1}k}{(2\pi)^d}\,
\bigl(\omega^2+H(k;x)\bigr)^{-1}
\]

in a Euclidean convention, or the analogous Lorentzian contour.

`main` specifies only the classical operator

\[
H=K(-i\partial_x)+V_{\rm fluc}(x).
\]

That determines a *candidate* propagator once dimension, contour,
and regulator are chosen. It does **not** determine the vertex
that multiplies \(G(x,x)\), because that vertex is \(V'''(\phi)\),
and \(V\) is not unique.

Using \(\beta_{\rm saddle}\) versus \(\beta_{\rm Hessian}\) changes
\(V'''\) by a factor of two. Using a non-local or collective
parent changes the tensor structure. Any number written down
before that choice is a fit, not a loop correction.

## Minimal closures still available

None of these may be applied silently.

1. **P1 — local action from the saddle.**
   \(S\supset -(\lambda/4!)\phi^4\). Recompute the Bloch operator
   from the true Hessian. Theorem A is then not the Hessian
   spectrum of this action. Do not write that back onto `main`.
2. **P2 — operator-defined theory.**
   Take frozen \(H\) as primitive. No local \(V(\phi)\).
   The tadpole vertex remains free. Still under-specified.
3. **P3 — extra sector.**
   Keep both frozen identities and add a collective coupling
   whose first variation supplies the missing half of the
   Hessian (or of the saddle). This is the fork already written
   in INTERPRETATION_FORK.md, now appearing one layer earlier:
   at the parent action, not after a loop number.
4. **P4 — local action from the Hessian.**
   Abandon the frozen saddle as an extremum. Forbidden as a
   silent edit; allowed only as an explicitly labelled variant.

## What is not a closure

- averaging P1 and P4 because they differ by two
- importing a CFT-X value of \(\lambda\) or \(W\)
- declaring the mismatch “a quantum effect”
- producing \(\varphi_{\rm loop}^2\) from a regulator that has
  not been written down
