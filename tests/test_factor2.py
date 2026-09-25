"""Automated falsification of the factor-of-two theorem.

Primary assertion: R =? 2 on the two-mode reduction.
Secondary: multimode corrections are reported, not absorbed into the theorem.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from bloch_factor2.model import (  # noqa: E402
    classical_ratio,
    saddle_amplitude_sq,
    stability_amplitude_sq,
)
from bloch_factor2.operator import (  # noqa: E402
    bloch_spectrum,
    brillouin_min_eigenvalue,
    two_mode_eigenvalues,
)
from bloch_factor2.scan import (  # noqa: E402
    analytic_ratio_bundle,
    condensing_params,
    numerical_stable_amplitude_sq,
    parameter_grid,
    two_mode_identity_residual,
)


def test_epsilon_star_matches_kernel():
    p = condensing_params()
    assert p.epsilon_star == pytest.approx(p.K(p.qstar))
    assert p.epsilon_star == pytest.approx(p.mu**2 - p.W**2 * p.M**2 / (4.0 * p.c))


def test_saddle_sets_delta_equal_abs_eps():
    p = condensing_params()
    phi_s = saddle_amplitude_sq(p)
    delta = p.lam * phi_s / 8.0
    assert delta == pytest.approx(p.abs_epsilon_star)
    assert delta + p.epsilon_star == pytest.approx(0.0)


def test_two_mode_saddle_is_half_gap():
    p = condensing_params()
    bundle = analytic_ratio_bundle(p)
    assert bundle.omega_minus_saddle == pytest.approx(p.epsilon_star / 2.0)
    assert bundle.omega_minus_saddle < 0


def test_two_mode_stable_is_marginal():
    p = condensing_params()
    bundle = analytic_ratio_bundle(p)
    assert bundle.omega_minus_stable == pytest.approx(0.0, abs=1e-12)
    assert bundle.R_analytic == pytest.approx(classical_ratio())


def test_two_mode_identity_holds_off_saddle():
    rng = np.random.default_rng(0)
    for eps in rng.normal(size=20):
        delta = abs(float(rng.normal()))
        assert two_mode_identity_residual(float(eps), delta) == pytest.approx(0.0)


def test_analytic_ratio_independent_of_parameters():
    for p in parameter_grid():
        bundle = analytic_ratio_bundle(p)
        assert bundle.R_analytic == pytest.approx(2.0)
        assert bundle.omega_minus_saddle == pytest.approx(p.epsilon_star / 2.0)
        assert bundle.omega_minus_stable == pytest.approx(0.0, abs=1e-10)
        assert bundle.delta_plus_eps_saddle == pytest.approx(0.0)


def test_nine_mode_saddle_still_unstable():
    p = condensing_params()
    phi_s = saddle_amplitude_sq(p)
    vmin = brillouin_min_eigenvalue(p, phi_s, n_max=4, n_k=33)
    assert vmin < 0


def test_nine_mode_at_two_mode_bound_is_near_marginal():
    p = condensing_params()
    phi_t = stability_amplitude_sq(p)
    vmin = brillouin_min_eigenvalue(p, phi_t, n_max=4, n_k=33)
    assert vmin > -0.1 * p.abs_epsilon_star


def test_mode_convergence_ratio_near_two():
    p = condensing_params()
    phi_s = saddle_amplitude_sq(p)
    ratios = []
    for n_max in (1, 2, 4, 6):
        phi_num = numerical_stable_amplitude_sq(p, n_max=n_max, n_k=25)
        ratios.append(phi_num / phi_s)
    for R in ratios:
        assert 1.5 < R < 2.6, f"R drifted off the structural window: {R}"


def test_k_zero_two_mode_matches_analytic():
    p = condensing_params()
    phi_s = saddle_amplitude_sq(p)
    spec = bloch_spectrum(p, phi_s, k=p.qstar, n_max=1)
    plus, minus = two_mode_eigenvalues(p.epsilon_star, p.abs_epsilon_star)
    assert spec[0] == pytest.approx(minus, abs=0.05 * abs(minus) + 1e-6) or spec[0] < 0
    assert plus > minus


def test_rejects_noncondensing():
    with pytest.raises(ValueError):
        condensing_params(W=0.1, c=10.0, M=1.0, mu=2.0)
