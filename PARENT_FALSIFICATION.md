# Parent-action falsification matrix

**Order of work on this branch**

\[
\boxed{
\text{CLASSICAL FREEZE}
\;\rightarrow\;
\text{PARENT-ACTION CONSISTENCY TEST}
\;\rightarrow\;
\text{QUANTIZATION}
}
\]

not

\[
\text{CLASSICAL FREEZE}\rightarrow\text{guessed tadpole}.
\]

No parent is selected here. Each column is a hypothesis.
P3 is not a rescue. It is the statement that a single local
scalar is incomplete, and it is allowed to fail.

## Frozen data (from `main`, not renegotiated)

\[
K(q)=\mu^2-Wq^2+\frac{cq^4}{M^2},
\qquad
\phi=\varphi_0\cos(q_*x),
\]

\[
\varphi_{\rm saddle}^2=\frac{8|\varepsilon_*|}{\lambda},
\qquad
V_{\rm fluc}^{\rm fr}(x)
=\frac{\lambda\varphi_0^2}{8}\bigl[1+\cos(2q_*x)\bigr].
\]

Theorem A: at the frozen saddle, \(\Omega_-^2=\varepsilon_*/2<0\).
Theorem B: two-mode stability at \(\varphi^2=16|\varepsilon_*|/\lambda\).

## Chain required of every parent

\[
S[\phi,\ldots]
\;\longrightarrow\;
\frac{\delta S}{\delta\phi}
\;\longrightarrow\;
\frac{\delta^2 S}{\delta\phi^2}
\;\longrightarrow\;
H_{\rm Bloch}
\;\longrightarrow\;
\Omega_-^2.
\]

## Five questions, asked of every parent

1. Does the stated condensate actually solve the EOM?
2. Does the derived Hessian equal the frozen \(V_{\rm fluc}\)?
3. Does the two-mode gap reproduce Theorem A?
4. Does the resulting stability threshold reproduce Theorem B?
5. Does quantization of that parent become well-defined without
   adding an arbitrary parameter?

“Arbitrary parameter” here means an extra coupling or vertex
not fixed by \(S\). Regulator choices are a later lock. They do
not count as closing Q5.

## Local \(\phi^4\) identity (P1 and P4)

For \(V=\beta\phi^4\) in single-mode truncation,

\[
\varepsilon_*+3\beta\varphi_0^2=0
\qquad\text{on shell},
\]

\[
V''(x)=6\beta\varphi_0^2\bigl[1+\cos(2q_*x)\bigr],
\qquad
\Delta=6\beta\varphi_0^2.
\]

Therefore, on any amplitude that solves the projected EOM,

\[
\Delta=2|\varepsilon_*|,
\qquad
\Omega_-^2=\varepsilon_*+\frac{\Delta}{2}=0.
\]

A local \(\phi^4\) theory cannot under-restore its own two-mode
pair. Theorem A is incompatible with “this background is an
extremum of a local \(\beta\phi^4\).”

That is why \(\beta_{\rm saddle}=2\beta_{\rm Hessian}\) moved
the factor-of-two problem upstream of quantization.

## Matrix

Evaluated at the *frozen* condensate
\(\varphi_0^2=8|\varepsilon_*|/\lambda\), except where a row
explicitly says “true extremum.”

| | P1 | P2 | P3 | P4 |
|---|---|---|---|---|
| Preserves | classical saddle | frozen operator \(H\) | both frozen identities, if extra sector exists | frozen Hessian |
| Sacrifices | frozen Hessian normalization | unique local \(\phi^4\) | minimal single-field closure | saddle as extremum |
| \(\beta\) or primitive | \(\lambda/24\) | \(H\) primitive | \(S_\phi+S_{\rm extra}\) | \(\lambda/48\) |
| Q1 EOM at frozen \(\varphi_{\rm saddle}\) | yes | no EOM | yes, if \(\delta S_{\rm extra}/\delta\phi=0\) | no |
| Q2 Hessian \(=V_{\rm fluc}^{\rm fr}\) | no (\(2\times\)) | yes, by definition | yes, if extra Hessian \(=-V_{\rm fluc}^{\rm fr}\) | yes |
| Q3 Theorem A at frozen saddle | no (\(\Omega_-^2=0\)) | yes | yes, under that constraint | yes as operator, off-shell |
| Q4 Theorem B threshold | no (\(R=1\)) | yes | yes, under that constraint | threshold \(=\) true extremum |
| Q5 quantization w/o extra parameter | vertex fixed; regulator still open | **no** — vertex free | **no** — \(S_{\rm extra}\) not unique | vertex fixed; regulator still open |

Derived details sit in the sections below and in
[PARENT_ACTION.md](PARENT_ACTION.md),
[PARENT_P3.md](PARENT_P3.md).

## P1 — local action from the saddle

\[
S_{\rm P1}
=\int\!dt\,dx
\Biggl[
\frac12(\partial_t\phi)^2
-\frac12\,\phi\,K(-i\partial_x)\,\phi
-\frac{\lambda}{24}\phi^4
\Biggr].
\]

Projected EOM: \(\varphi_0^2=8|\varepsilon_*|/\lambda\). Q1 holds.
Derived Hessian \(\Delta=\lambda\varphi_0^2/4=2|\varepsilon_*|\).
Q2 fails. Q3 fails: \(\Omega_-^2=0\neq\varepsilon_*/2\).
Q4 fails: \(R=1\). Q5: vertex fixed; regulator still open.

## P4 — local action from the Hessian

\[
S_{\rm P4}
=\int\!dt\,dx
\Biggl[
\frac12(\partial_t\phi)^2
-\frac12\,\phi\,K(-i\partial_x)\,\phi
-\frac{\lambda}{48}\phi^4
\Biggr].
\]

True extremum: \(\varphi_{\rm EOM}^2=16|\varepsilon_*|/\lambda\).
Frozen saddle does not solve the EOM. Q1 fails. Q2 holds.
Theorem A holds only off-shell at the frozen amplitude.
At the true extremum, \(\Omega_-^2=0\).
Q4: Theorem B threshold is P4's own saddle, not a lift of it.
Q5: vertex fixed; regulator still open.

## P2 — operator-defined theory

\(H=K+V_{\rm fluc}^{\rm fr}\) is primitive. No EOM. Q2–Q4 hold
by definition. Q5 fails: a tadpole needs a vertex \(H\) does
not determine.

## P3 — extra sector

Not a model. A consistency condition. Both frozen identities
survive iff, on the frozen background,

\[
\frac{\delta S_{\rm extra}}{\delta\phi}=0,
\qquad
\frac{\delta^2 S_{\rm extra}}{\delta\phi^2}=-V_{\rm fluc}^{\rm fr}.
\]

The minus sign is derived from \(V''_{\rm P1}-V_{\rm fluc}^{\rm fr}\).
Q1–Q4 hold only if that remainder is realized. Q5 fails until
\(S_{\rm extra}\) is named. P3 may fail. See PARENT_P3.md.

## Forbidden readings

- averaging P1 and P4 because \(\beta_{\rm saddle}=2\beta_{\rm Hessian}\)
- treating P3 as already supplying the Bloch gap
- promoting \(2\) from this matrix to a constant of nature
- writing \(\varphi_{\rm loop}^2\) from any column
