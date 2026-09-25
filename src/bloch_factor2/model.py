"""Exact classical construction for the W + λφ⁴ modulated saddle.

Frozen identities (see MODEL.md, THEOREM_FACTOR2.md):

    K(q) = μ² − W q² + c q⁴ / M²
    q_*² = W M² / (2c)
    ε_*  = K(q_*) = μ² − W² M² / (4c)

    V_fluc(x) = (λ φ₀² / 8) [1 + cos(2 q_* x)]
    Δ = λ φ₀² / 8

Saddle amplitude:     φ_saddle²  = 8 |ε_*| / λ
Stability amplitude:  φ_stable²  = 16 |ε_*| / λ
Ratio:                R          = φ_stable² / φ_saddle² = 2
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ModelParams:
    """Dimensionless parameter tuple. No CFT-X import. No W≈0.08 freeze."""

    W: float
    lam: float
    M: float
    c: float
    mu: float

    def validate(self) -> None:
        if self.W <= 0:
            raise ValueError("W must be positive for a finite q_*")
        if self.lam <= 0:
            raise ValueError("λ must be positive")
        if self.M == 0:
            raise ValueError("M must be nonzero")
        if self.c <= 0:
            raise ValueError("c must be positive")

    @property
    def qstar_sq(self) -> float:
        self.validate()
        return self.W * self.M**2 / (2.0 * self.c)

    @property
    def qstar(self) -> float:
        return self.qstar_sq**0.5

    def K(self, q: float) -> float:
        """Dispersion kernel K(q)."""
        self.validate()
        q2 = q * q
        return self.mu**2 - self.W * q2 + self.c * q2 * q2 / self.M**2

    @property
    def epsilon_star(self) -> float:
        """ε_* = K(q_*). Condensation requires ε_* < 0."""
        return self.mu**2 - (self.W**2 * self.M**2) / (4.0 * self.c)

    @property
    def abs_epsilon_star(self) -> float:
        return abs(self.epsilon_star)


def delta_from_amplitude(lam: float, phi0_sq: float) -> float:
    """Δ = λ φ₀² / 8."""
    return lam * phi0_sq / 8.0


def saddle_amplitude_sq(p: ModelParams) -> float:
    """Classical saddle: φ₀² = 8 |ε_*| / λ."""
    if p.lam <= 0:
        raise ValueError("λ must be positive")
    return 8.0 * p.abs_epsilon_star / p.lam


def stability_amplitude_sq(p: ModelParams) -> float:
    """Two-mode spectral bound: φ₀² ≥ 16 |ε_*| / λ."""
    if p.lam <= 0:
        raise ValueError("λ must be positive")
    return 16.0 * p.abs_epsilon_star / p.lam


def classical_ratio() -> float:
    """Structural ratio claimed by the two-mode theorem. Not a constant of nature."""
    return 2.0
