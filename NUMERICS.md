# Numerics

## Package

```text
src/bloch_factor2/model.py      K(q), ε_*, amplitudes
src/bloch_factor2/operator.py   two-mode + N-mode Bloch
src/bloch_factor2/scan.py       R scan, parameter grid
tests/test_factor2.py           assertions
```

No external physics library. NumPy + pytest only.

## Default condensing point

\[
W=1,\;\lambda=1,\;M=1,\;c=1,\;\mu=0
\qquad\Longrightarrow\qquad
\varepsilon_*=-\tfrac14.
\]

Then

\[
\varphi_{\rm saddle}^2=2,
\qquad
\varphi_{\rm stable}^2=4,
\qquad
R=2,
\qquad
\Omega_-^2=-\tfrac18.
\]

This point is a convenience, not a fit.

## Brillouin sampling

Default: 33 to 65 points on \(k\in[-q_*,q_*]\).
The zone-edge \(k=\pm q_*\) is included.

## Bisection for \(\varphi_{\rm stable,N}^2\)

Bracket relative to \(\varphi_{\rm saddle}^2\), typically
\([0.5,4]\times\varphi_{\rm saddle}^2\). Bisection stops when the
bracket width is \(10^{-8}\) relative to the saddle amplitude.

If the upper bracket remains negative, the run fails loudly.
That is a signal, not a cue to raise \(\lambda\).

## Reproducing

```bash
pip install -r requirements.txt
PYTHONPATH=src pytest -q
```

Optional one-shot scan:

```bash
PYTHONPATH=src python -m bloch_factor2
```
