"""Classical parent-action identities for P1, P2, P4.

P3 is a constraint, not a coefficient tuple. See PARENT_P3.md.
This module is exact algebra on the single-mode truncation.
It does not compute loops.
"""

from __future__ import annotations

from dataclasses import dataclass

from .model import ModelParams, saddle_amplitude_sq, stability_amplitude_sq
from .operator import two_mode_minus


@dataclass(frozen=True)
class ParentReport:
    name: str
    beta: float | None
    phi_eom_sq: float | None
    delta_at_frozen_saddle: float
    omega_minus_at_frozen_saddle: float
    omega_minus_at_true_eom: float | None
    q1_eom_at_frozen_saddle: bool | None
    q2_hessian_matches_frozen: bool
    q3_theorem_A_at_frozen_saddle: bool
    q4_theorem_B_threshold: bool
    q5_vertex_fixed: bool


def frozen_delta(p: ModelParams, phi0_sq: float) -> float:
    return p.lam * phi0_sq / 8.0


def local_delta(beta: float, phi0_sq: float) -> float:
    """Δ from V = β φ⁴: V'' = 6 β φ₀² (1 + cos 2θ)."""
    return 6.0 * beta * phi0_sq


def local_eom_amplitude_sq(p: ModelParams, beta: float) -> float:
    """φ₀² from projected EOM: ε_* + 3 β φ₀² = 0."""
    if beta <= 0:
        raise ValueError("beta must be positive")
    return p.abs_epsilon_star / (3.0 * beta)


def report_p1(p: ModelParams) -> ParentReport:
    beta = p.lam / 24.0
    phi_s = saddle_amplitude_sq(p)
    phi_eom = local_eom_amplitude_sq(p, beta)
    delta_s = local_delta(beta, phi_s)
    delta_eom = local_delta(beta, phi_eom)
    return ParentReport(
        name="P1",
        beta=beta,
        phi_eom_sq=phi_eom,
        delta_at_frozen_saddle=delta_s,
        omega_minus_at_frozen_saddle=two_mode_minus(p.epsilon_star, delta_s),
        omega_minus_at_true_eom=two_mode_minus(p.epsilon_star, delta_eom),
        q1_eom_at_frozen_saddle=True,
        q2_hessian_matches_frozen=False,
        q3_theorem_A_at_frozen_saddle=False,
        q4_theorem_B_threshold=False,
        q5_vertex_fixed=True,
    )


def report_p4(p: ModelParams) -> ParentReport:
    beta = p.lam / 48.0
    phi_s = saddle_amplitude_sq(p)
    phi_eom = local_eom_amplitude_sq(p, beta)
    delta_s = local_delta(beta, phi_s)
    delta_eom = local_delta(beta, phi_eom)
    q4 = abs(phi_eom - stability_amplitude_sq(p)) <= 1e-12 * max(1.0, abs(phi_eom))
    return ParentReport(
        name="P4",
        beta=beta,
        phi_eom_sq=phi_eom,
        delta_at_frozen_saddle=delta_s,
        omega_minus_at_frozen_saddle=two_mode_minus(p.epsilon_star, delta_s),
        omega_minus_at_true_eom=two_mode_minus(p.epsilon_star, delta_eom),
        q1_eom_at_frozen_saddle=False,
        q2_hessian_matches_frozen=True,
        q3_theorem_A_at_frozen_saddle=True,
        q4_theorem_B_threshold=q4,
        q5_vertex_fixed=True,
    )


def report_p2(p: ModelParams) -> ParentReport:
    phi_s = saddle_amplitude_sq(p)
    delta_s = frozen_delta(p, phi_s)
    return ParentReport(
        name="P2",
        beta=None,
        phi_eom_sq=None,
        delta_at_frozen_saddle=delta_s,
        omega_minus_at_frozen_saddle=two_mode_minus(p.epsilon_star, delta_s),
        omega_minus_at_true_eom=None,
        q1_eom_at_frozen_saddle=None,
        q2_hessian_matches_frozen=True,
        q3_theorem_A_at_frozen_saddle=True,
        q4_theorem_B_threshold=True,
        q5_vertex_fixed=False,
    )


def beta_ratio(p: ModelParams) -> float:
    """β_saddle / β_Hessian. Structural for local φ⁴; not a constant of nature."""
    return (p.lam / 24.0) / (p.lam / 48.0)
