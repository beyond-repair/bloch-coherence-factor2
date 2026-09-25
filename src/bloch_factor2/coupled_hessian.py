"""C5 on-shell coupled Hessian for the cubic two-sector theory."""

from __future__ import annotations

import math
from dataclasses import dataclass

from .model import ModelParams


def k_ratio_two_qstar(p: ModelParams) -> float:
    """K(2q*)/K(0) if someone sets ω=K. Not identically 3/2."""
    k0 = p.K(0.0)
    if k0 == 0.0:
        raise ZeroDivisionError("K(0)=0")
    return p.K(2.0 * p.qstar) / k0


def k_ratio_formula(p: ModelParams) -> float:
    return 1.0 + 2.0 * (p.W**2) * (p.M**2) / (p.c * p.mu**2)


def on_shell_epsilon(gamma_sq: float, omega0: float, omega2: float) -> float:
    """ε_* implied by projected even EOM. γ = g φ0."""
    return 0.25 * gamma_sq * (1.0 / omega0 + 0.5 / omega2)


def odd_block(gamma: float, omega2: float) -> tuple[tuple[float, float], tuple[float, float]]:
    hbb = (gamma * gamma) / (4.0 * omega2)
    mix = 0.5 * gamma
    return ((hbb, mix), (mix, omega2))


def odd_eigenvalues(gamma: float, omega2: float) -> tuple[float, float]:
    """Identically {0, ω2 + γ²/(4 ω2)} on shell."""
    other = omega2 + (gamma * gamma) / (4.0 * omega2)
    return (0.0, other)


def even_char_poly_coeffs(gamma: float, omega0: float, omega2: float) -> tuple[float, float, float, float]:
    """
    λ(ω0-λ)(ω2-λ) + (γ²/2)(ω2-λ) + (γ²/4)(ω0-λ) = 0
    → λ³ + a λ² + b λ + c = 0 after expansion and a sign flip.
    Stored as monic λ³ - (w0+w2)λ² + ... for numeric roots.
    """
    g2 = gamma * gamma
    # Expand λ(w0-λ)(w2-λ) + (g2/2)(w2-λ) + (g2/4)(w0-λ) = 0
    # λ(w0 w2 - (w0+w2)λ + λ²) + (g2/2)w2 - (g2/2)λ + (g2/4)w0 - (g2/4)λ = 0
    # λ³ - (w0+w2)λ² + w0 w2 λ + (g2/2)w2 + (g2/4)w0 - (g2/2 + g2/4) λ = 0
    # λ³ - (w0+w2)λ² + (w0 w2 - 3 g2/4) λ + (g2/4)(2 w2 + w0) = 0
    a = -(omega0 + omega2)
    b = omega0 * omega2 - 0.75 * g2
    c = 0.25 * g2 * (2.0 * omega2 + omega0)
    return (1.0, a, b, c)


def even_eigenvalues(gamma: float, omega0: float, omega2: float) -> list[float]:
    coeffs = even_char_poly_coeffs(gamma, omega0, omega2)
    return [float(z.real) for z in _poly_roots(coeffs) if abs(z.imag) < 1e-9]


def _poly_roots(coeffs: tuple[float, float, float, float]) -> list[complex]:
    # companion matrix of monic cubic
    a, b, c = coeffs[1], coeffs[2], coeffs[3]
    # λ³ + a λ² + b λ + c = 0
    companion = [
        [0.0, 0.0, -c],
        [1.0, 0.0, -b],
        [0.0, 1.0, -a],
    ]
    # numpy-free 3x3 eig via Cardano-ish trig for this depressed path is messy;
    # use explicit cubic formula for real coefficients.
    return _cubic_roots(1.0, a, b, c)


def _cubic_roots(a0: float, a1: float, a2: float, a3: float) -> list[complex]:
    # a0 λ³ + a1 λ² + a2 λ + a3 = 0, a0=1
    a, b, c = a1 / a0, a2 / a0, a3 / a0
    p = b - a * a / 3.0
    q = 2.0 * a * a * a / 27.0 - a * b / 3.0 + c
    disc = (q / 2.0) ** 2 + (p / 3.0) ** 3
    shift = a / 3.0
    if disc >= 0:
        sdisc = math.sqrt(disc)
        u = _cbrt(-q / 2.0 + sdisc)
        v = _cbrt(-q / 2.0 - sdisc)
        r0 = u + v - shift
        # two remaining: complex or repeated
        re = -0.5 * (u + v) - shift
        im = math.sqrt(3.0) / 2.0 * (u - v)
        return [complex(r0, 0.0), complex(re, im), complex(re, -im)]
    # three real roots
    r = math.sqrt(-p / 3.0)
    arg = math.acos(max(-1.0, min(1.0, (-q / 2.0) / (r ** 3))))
    return [
        complex(2.0 * r * math.cos((arg + 2.0 * math.pi * k) / 3.0) - shift, 0.0)
        for k in range(3)
    ]


def _cbrt(x: float) -> float:
    return math.copysign(abs(x) ** (1.0 / 3.0), x)


@dataclass(frozen=True)
class CoupledSpectrum:
    epsilon_star: float
    odd: tuple[float, float]
    even: list[float]


def spectrum(gamma: float, omega0: float, omega2: float) -> CoupledSpectrum:
    return CoupledSpectrum(
        epsilon_star=on_shell_epsilon(gamma * gamma, omega0, omega2),
        odd=odd_eigenvalues(gamma, omega2),
        even=even_eigenvalues(gamma, omega0, omega2),
    )
