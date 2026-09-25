"""Named C1–C3 actions. Independent definitions only.

Nothing in this module is allowed to set a coupling from Ω_-².
"""

from __future__ import annotations

from dataclasses import dataclass

from .model import ModelParams, saddle_amplitude_sq
from .parents import local_delta


@dataclass(frozen=True)
class RealizationVerdict:
    id: str
    independent: bool
    e_extra_vanishes: bool
    h_matches_target: bool
    verdict: str


def frozen_vfluc_delta(p: ModelParams) -> float:
    return p.abs_epsilon_star


def p3_target_delta(p: ModelParams) -> float:
    return -frozen_vfluc_delta(p)


def c2a_projected_conflict(psi0: float, psi2: float) -> bool:
    stationary = abs(psi0 + 0.5 * psi2) < 1e-15
    hessian_shape = abs(psi0 - psi2) < 1e-15
    if abs(psi0) < 1e-15 and abs(psi2) < 1e-15:
        return False
    return not (stationary and hessian_shape)


def c2b_inner_product_cos2(psi_sq_mean: float) -> float:
    return max(0.0, psi_sq_mean)


def c3a_projected_force(gamma: float, phi0_sq: float) -> float:
    return gamma * phi0_sq / 2.0


def named_verdicts() -> list[RealizationVerdict]:
    return [
        RealizationVerdict("C1a", True, True, False, "INDEPENDENT-FAIL"),
        RealizationVerdict("C1b", True, True, False, "INDEPENDENT-FAIL"),
        RealizationVerdict("C1c", False, True, True, "COUNTERTERM"),
        RealizationVerdict("C2a", True, False, False, "INDEPENDENT-FAIL"),
        RealizationVerdict("C2b", True, False, False, "INDEPENDENT-FAIL"),
        RealizationVerdict("C3a", True, False, False, "INDEPENDENT-FAIL"),
        RealizationVerdict("C3b", True, True, False, "INDEPENDENT-FAIL"),
        RealizationVerdict("C3c", True, False, False, "INDEPENDENT-FAIL"),
    ]


def any_independent_pass(rows: list[RealizationVerdict] | None = None) -> bool:
    rows = rows if rows is not None else named_verdicts()
    return any(r.verdict == "INDEPENDENT-PASS" for r in rows)


def p1_surplus_delta(p: ModelParams) -> float:
    beta = p.lam / 24.0
    phi_s = saddle_amplitude_sq(p)
    return local_delta(beta, phi_s) - frozen_vfluc_delta(p)
