# Stability bound

## Two-mode condition

From [TWO_MODE_PROOF.md](TWO_MODE_PROOF.md),

\[
\Omega_-^2=\varepsilon_*+\frac{\Delta}{2}.
\]

Require \(\Omega_-^2\ge 0\) and \(\varepsilon_*<0\):

\[
\Delta\ge -2\varepsilon_*=2|\varepsilon_*|.
\]

## Translation into amplitude

\[
\Delta=\frac{\lambda\varphi_0^2}{8}
\qquad\Longrightarrow\qquad
\frac{\lambda\varphi_0^2}{8}\ge 2|\varepsilon_*|
\qquad\Longrightarrow\qquad
\varphi_0^2\ge\frac{16|\varepsilon_*|}{\lambda}.
\]

Define

\[
\varphi_{\rm saddle}^2=\frac{8|\varepsilon_*|}{\lambda},
\qquad
\varphi_{\rm stable}^2=\frac{16|\varepsilon_*|}{\lambda}.
\]

Then Theorem C:

\[
\boxed{
\frac{\varphi_{\rm stable}^2}{\varphi_{\rm saddle}^2}=2.
}
\]

The upper two-mode eigenvalue \(\Omega_+^2=\varepsilon_*+3\Delta/2\)
is automatically nonnegative once \(\Delta\ge 2|\varepsilon_*|\).
The bound is therefore controlled by the lower branch alone.

## What this bound is not

- It is not a statement about the full Hill operator.
- It is not a one-loop result.
- It is not a claim that nature prefers the number 2.

If a later sector (loops, extra fields, collective couplings)
changes \(\Delta(\varphi_0)\) or adds off-diagonal structure, the
bound must be re-derived. It must not be patched by retuning
\(\lambda\).
