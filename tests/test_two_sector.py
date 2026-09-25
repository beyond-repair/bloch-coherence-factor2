"""C4: conventional two-sector cubic does not yield the frozen 2."""

from bloch_factor2.model import ModelParams
from bloch_factor2.two_sector import (
    TwoSectorSpectra,
    chi_components,
    fixed_chi_delta_pair,
    omega_minus_sq_fixed_chi,
    projected_eom_residual,
    same_kernel_omega,
    schur_local_omega_minus_sq,
    shape_matches_frozen,
    theorem_a_tuning_ratio,
    ultralocal_fixed_chi_ratio,
    would_need_fit_for_theorem_a,
)


def _on_shell_ultralocal(eps: float, g: float, mu_sq: float) -> tuple[float, float, float]:
    """Choose φ0^{2} so the projected EOM vanishes; ω=μ^{2} at both harmonics."""
    spec = TwoSectorSpectra(omega0=mu_sq, omega2=mu_sq)
    # ε + (3/2) g χ0 = 0, χ0 = -g φ0^{2} / (4 μ^{2})
    # ε - 3 g^{2} φ0^{2} / (8 μ^{2}) = 0
    phi0_sq = -eps * 8.0 * mu_sq / (3.0 * g * g)
    chi0, chi2 = chi_components(g, phi0_sq, spec)
    return phi0_sq, chi0, chi2


def test_ultralocal_shape_matches_but_ratio_is_two_thirds():
    eps = -1.0
    g = 1.0
    mu_sq = 1.0
    _, chi0, chi2 = _on_shell_ultralocal(eps, g, mu_sq)
    dc, cos_piece = fixed_chi_delta_pair(g, chi0, chi2)
    assert shape_matches_frozen(dc, cos_piece)
    assert abs(dc / abs(eps) - ultralocal_fixed_chi_ratio()) < 1e-12
    assert abs(omega_minus_sq_fixed_chi(eps, dc, cos_piece) + (2.0 / 3.0) * abs(eps)) < 1e-12


def test_projected_eom_holds_on_that_shell():
    eps = -1.0
    _, chi0, chi2 = _on_shell_ultralocal(eps, 1.0, 1.0)
    assert abs(projected_eom_residual(eps, 1.0, chi0, chi2)) < 1e-12


def test_schur_recovers_marginal_local_quartic():
    assert schur_local_omega_minus_sq() == 0.0


def test_same_kernel_is_not_the_theorem_a_ratio():
    p = ModelParams(W=1.0, lam=1.0, M=1.0, c=1.0, mu=0.3)
    assert p.epsilon_star < 0
    spec = same_kernel_omega(p)
    assert would_need_fit_for_theorem_a(spec)
    assert spec.omega0 != spec.omega2


def test_theorem_a_ratio_is_marked_as_a_fit_not_a_kernel():
    # ω(2q*)/ω(0) = 3/2 reproduces Theorem A at fixed χ.
    # That number is stored only so the test can refuse it as derived.
    assert theorem_a_tuning_ratio() == 1.5
    fitted = TwoSectorSpectra(omega0=2.0, omega2=3.0)
    assert not would_need_fit_for_theorem_a(fitted)
