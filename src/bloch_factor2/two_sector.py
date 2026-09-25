"""C4 two-sector cubic. Coefficients are not fit to Theorem C."""

from __future__ import annotations

from dataclasses import dataclass

from .model import ModelParams


@dataclass(frozen=True)
class TwoSectorSpectra:
    omega0: float
    omega2: float


def chi_components(g: float, phi0_sq: float, spec: TwoSectorSpectra) -> tuple[float, float]:
    if spec.omega0 == 0.0 or spec.omega2 == 0.0:
        raise ValueError("collective kernel must be invertible on {0, 2q*}")
    pre = -g * phi0_sq / 4.0
    return pre / spec.omega0, pre / spec.omega2


def projected_eom_residual(
    epsilon_star: float, g: float, chi0: float, chi2: float
) -> float:
    return epsilon_star + g * chi0 + 0.5 * g * chi2


def fixed_chi_delta_pair(g: float, chi0: float, chi2: float) -> tuple[float, float]:
    """DC piece and cosine piece of H = K + g χ."""
    return g * chi0, g * chi2


def omega_minus_sq_fixed_chi(epsilon_star: float, dc: float, cos_piece: float) -> float:
    """Two-mode lower eigenvalue at frozen χ: ε + DC − |cos|/2."""
    return epsilon_star + dc - abs(cos_piece) / 2.0


def ultralocal_fixed_chi_ratio() -> float:
    """Δ / |ε*| when ω(0)=ω(2q*) and χ is held fixed."""
    return 2.0 / 3.0


def schur_local_omega_minus_sq() -> float:
    """Integrate ultra-local auxiliary χ: local βφ4, on-shell Ω_-^{2} = 0."""
    return 0.0


def same_kernel_omega(p: ModelParams) -> TwoSectorSpectra:
    return TwoSectorSpectra(omega0=p.K(0.0), omega2=p.K(2.0 * p.qstar))


def shape_matches_frozen(dc: float, cos_piece: float, tol: float = 1e-12) -> bool:
    return abs(dc - cos_piece) <= tol


def theorem_a_tuning_ratio() -> float:
    """ω(2q*)/ω(0) that forces Theorem A at fixed χ. Not a derived kernel."""
    return 1.5


def would_need_fit_for_theorem_a(spec: TwoSectorSpectra, tol: float = 1e-12) -> bool:
    if spec.omega0 == 0.0:
        return True
    return abs(spec.omega2 / spec.omega0 - theorem_a_tuning_ratio()) > tol
