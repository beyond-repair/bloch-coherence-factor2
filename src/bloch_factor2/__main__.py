"""Analytic + truncated multimode Bloch scan for one condensing point.

Default run reproduces the documented point W=λ=M=c=1, μ=0 with a
9-mode (n_max=4) Brillouin scan. Exit codes:

0  analytic two-mode ratio R equals 2 (the frozen classical identity)
1  analytic R moved off 2 (the identity broke; a falsification signal)
2  bad input: non-condensing parameters (ε_* ≥ 0) or invalid options
3  multimode bisection could not bracket stability (fails loudly)
"""

from __future__ import annotations

import argparse
import json
import math
import sys

from . import __version__
from .scan import condensing_params, ratio_scan

R_TOL = 1e-12


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="bloch-factor2",
        description=(
            "Classical W+λφ⁴ factor-of-two check: analytic two-mode ratio "
            "plus a truncated multimode Bloch scan. Classical model only."
        ),
    )
    ap.add_argument("--W", type=float, default=1.0, help="gradient coupling W (default 1)")
    ap.add_argument("--lam", type=float, default=1.0, help="quartic coupling λ > 0 (default 1)")
    ap.add_argument("--M", type=float, default=1.0, help="scale M > 0 (default 1)")
    ap.add_argument("--c", type=float, default=1.0, help="quartic-gradient coefficient c > 0 (default 1)")
    ap.add_argument("--mu", type=float, default=0.0, help="mass parameter μ (default 0)")
    ap.add_argument("--n-max", type=int, default=4, help="Fourier cutoff; modes = 2*n_max+1 (default 4)")
    ap.add_argument("--n-k", type=int, default=33, help="Brillouin samples on [-q*, q*] (default 33)")
    ap.add_argument("--json", action="store_true", help="print the result as JSON")
    ap.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return ap


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.n_max < 1 or args.n_k < 3:
        print("error: need --n-max >= 1 and --n-k >= 3", file=sys.stderr)
        return 2
    try:
        p = condensing_params(W=args.W, lam=args.lam, M=args.M, c=args.c, mu=args.mu)
        p.validate()
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    try:
        result = ratio_scan(p, n_max=args.n_max, n_k=args.n_k)
    except RuntimeError as exc:
        print(f"error: multimode scan failed: {exc}", file=sys.stderr)
        return 3

    holds = math.isclose(result["R_analytic"], 2.0, rel_tol=R_TOL, abs_tol=0.0)
    if args.json:
        payload = {"parameters": dict(p.__dict__), **result, "R_analytic_equals_2": holds}
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print("bloch-coherence-factor2  one-shot scan")
        print("parameters: W={W} λ={lam} M={M} c={c} μ={mu}".format(**p.__dict__))
        for key, val in result.items():
            print(f"  {key}: {val}")
        print("assertion R_analytic == 2:", holds)
    return 0 if holds else 1


if __name__ == "__main__":
    raise SystemExit(main())
