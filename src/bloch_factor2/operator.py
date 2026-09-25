"""Bloch operator for the periodic fluctuation potential.

V_fluc(x) = Δ [1 + cos(2 q_* x)]

Fourier content on the 2q_* lattice:
  diagonal shift  = Δ
  nearest-neighbor coupling = Δ/2

Plane-wave basis at crystal momentum k:

    ψ_n(x) = exp(i (k + 2 n q_*) x),   n = −N … N
"""

from __future__ import annotations

import numpy as np

from .model import ModelParams, delta_from_amplitude


def two_mode_eigenvalues(eps_star: float, delta: float) -> tuple[float, float]:
    """Analytic two-mode spectrum.

    Ω_±² = ε_* + Δ ± |V|,   V = Δ/2
    """
    V = 0.5 * delta
    mid = eps_star + delta
    return mid + abs(V), mid - abs(V)


def two_mode_minus(eps_star: float, delta: float) -> float:
    _, om_minus = two_mode_eigenvalues(eps_star, delta)
    return om_minus


def bloch_matrix(
    p: ModelParams,
    phi0_sq: float,
    k: float,
    n_max: int,
) -> np.ndarray:
    """Hermitian Bloch matrix in the {k + 2n q_*} basis, n = −n_max … n_max."""
    if n_max < 0:
        raise ValueError("n_max must be nonnegative")
    delta = delta_from_amplitude(p.lam, phi0_sq)
    ns = np.arange(-n_max, n_max + 1)
    dim = ns.size
    q_n = k + 2.0 * ns * p.qstar
    diag = np.array([p.K(q) + delta for q in q_n], dtype=float)
    mat = np.diag(diag)
    coupling = 0.5 * delta
    for i in range(dim - 1):
        mat[i, i + 1] = coupling
        mat[i + 1, i] = coupling
    return mat


def bloch_spectrum(
    p: ModelParams,
    phi0_sq: float,
    k: float,
    n_max: int,
) -> np.ndarray:
    mat = bloch_matrix(p, phi0_sq, k, n_max)
    return np.sort(np.linalg.eigvalsh(mat))


def brillouin_min_eigenvalue(
    p: ModelParams,
    phi0_sq: float,
    n_max: int,
    n_k: int = 65,
) -> float:
    """Minimum eigenvalue of the Bloch operator over the first Brillouin zone."""
    ks = np.linspace(-p.qstar, p.qstar, n_k)
    mins = [float(bloch_spectrum(p, phi0_sq, k, n_max)[0]) for k in ks]
    return min(mins)


def n_mode_count(n_max: int) -> int:
    """Number of plane-wave modes for a given n_max (2 n_max + 1)."""
    return 2 * n_max + 1
