"""Parameter scans and the automated R =? 2 assertion helpers."""

from __future__ import annotations

from dataclasses import dataclass

from .model import (
    ModelParams,
    classical_ratio,
    saddle_amplitude_sq,
    stability_amplitude_sq,
)
from .operator import brillouin_min_eigenvalue, two_mode_minus


@dataclass(frozen=True)
class RatioResult:
    phi_saddle_sq: float
    phi_stable_sq: float
    R_analytic: float
    omega_minus_saddle: float
    omega_minus_stable: float
    delta_plus_eps_saddle: float


def analytic_ratio_bundle(p: ModelParams) -> RatioResult:
    eps = p.epsilon_star
    phi_s = saddle_amplitude_sq(p)
    phi_t = stability_amplitude_sq(p)
    delta_s = p.lam * phi_s / 8.0
    delta_t = p.lam * phi_t / 8.0
    return RatioResult(
        phi_saddle_sq=phi_s,
        phi_stable_sq=phi_t,
        R_analytic=phi_t / phi_s if phi_s != 0 else float("nan"),
        omega_minus_saddle=two_mode_minus(eps, delta_s),
        omega_minus_stable=two_mode_minus(eps, delta_t),
        delta_plus_eps_saddle=delta_s + eps,
    )


def numerical_stable_amplitude_sq(
    p: ModelParams,
    n_max: int,
    n_k: int = 33,
    lo_factor: float = 0.5,
    hi_factor: float = 4.0,
    tol: float = 1e-8,
    max_iter: int = 48,
) -> float:
    """Bisection for the smallest φ₀² with min_k Ω²(k) ≥ 0."""
    base = saddle_amplitude_sq(p)
    lo = lo_factor * base
    hi = hi_factor * base
    f_lo = brillouin_min_eigenvalue(p, lo, n_max, n_k=n_k)
    f_hi = brillouin_min_eigenvalue(p, hi, n_max, n_k=n_k)
    if f_hi < 0:
        raise RuntimeError("upper bracket still unstable; raise hi_factor")
    if f_lo >= 0:
        return lo
    for _ in range(max_iter):
        mid = 0.5 * (lo + hi)
        f_mid = brillouin_min_eigenvalue(p, mid, n_max, n_k=n_k)
        if f_mid >= 0:
            hi = mid
        else:
            lo = mid
        if hi - lo < tol * max(1.0, base):
            break
    return hi


def ratio_scan(
    p: ModelParams,
    n_max: int = 4,
    n_k: int = 33,
) -> dict:
    """Return analytic R and the multimode numerical R."""
    bundle = analytic_ratio_bundle(p)
    phi_num = numerical_stable_amplitude_sq(p, n_max=n_max, n_k=n_k)
    phi_s = bundle.phi_saddle_sq
    return {
        "epsilon_star": p.epsilon_star,
        "phi_saddle_sq": phi_s,
        "phi_stable_analytic_sq": bundle.phi_stable_sq,
        "phi_stable_numeric_sq": phi_num,
        "R_analytic": bundle.R_analytic,
        "R_numeric": phi_num / phi_s if phi_s != 0 else float("nan"),
        "R_target": classical_ratio(),
        "omega_minus_saddle": bundle.omega_minus_saddle,
        "omega_minus_stable": bundle.omega_minus_stable,
        "delta_plus_eps_saddle": bundle.delta_plus_eps_saddle,
        "n_max": n_max,
        "n_modes": 2 * n_max + 1,
    }


DEFAULT_GRID = {
    "W": (0.4, 0.8, 1.2),
    "lam": (0.5, 1.0, 2.0),
    "M": (0.7, 1.0, 1.5),
    "c": (0.5, 1.0, 2.0),
    "mu": (0.0, 0.2),
}


def condensing_params(
    W: float = 1.0,
    lam: float = 1.0,
    M: float = 1.0,
    c: float = 1.0,
    mu: float = 0.0,
) -> ModelParams:
    """Factory that rejects non-condensing (ε_* ≥ 0) tuples."""
    p = ModelParams(W=W, lam=lam, M=M, c=c, mu=mu)
    if p.epsilon_star >= 0:
        raise ValueError(f"ε_* = {p.epsilon_star} ≥ 0; no classical condensate")
    return p


def parameter_grid() -> list[ModelParams]:
    out: list[ModelParams] = []
    for W in DEFAULT_GRID["W"]:
        for lam in DEFAULT_GRID["lam"]:
            for M in DEFAULT_GRID["M"]:
                for c in DEFAULT_GRID["c"]:
                    for mu in DEFAULT_GRID["mu"]:
                        p = ModelParams(W=W, lam=lam, M=M, c=c, mu=mu)
                        if p.epsilon_star < 0:
                            out.append(p)
    return out


def two_mode_identity_residual(eps: float, delta: float) -> float:
    """Ω_-² − (ε_* + Δ/2). Vanishes for Δ ≥ 0, where |V| = Δ/2."""
    return two_mode_minus(eps, delta) - (eps + 0.5 * delta)
