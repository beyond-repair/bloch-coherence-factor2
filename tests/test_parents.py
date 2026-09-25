"""Parent-action falsification matrix, classical layer only."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from bloch_factor2.model import saddle_amplitude_sq, stability_amplitude_sq
from bloch_factor2.parents import (
    beta_ratio,
    local_delta,
    local_eom_amplitude_sq,
    report_p1,
    report_p2,
    report_p4,
)
from bloch_factor2.scan import condensing_params


def test_beta_saddle_is_twice_beta_hessian():
    p = condensing_params()
    assert beta_ratio(p) == pytest.approx(2.0)


def test_local_on_shell_two_mode_is_marginal():
    p = condensing_params()
    for beta in (p.lam / 24.0, p.lam / 48.0, p.lam / 12.0):
        phi = local_eom_amplitude_sq(p, beta)
        delta = local_delta(beta, phi)
        assert delta == pytest.approx(2.0 * p.abs_epsilon_star)
        assert p.epsilon_star + 0.5 * delta == pytest.approx(0.0)


def test_p1_owns_saddle_not_hessian():
    p = condensing_params()
    r = report_p1(p)
    assert r.phi_eom_sq == pytest.approx(saddle_amplitude_sq(p))
    assert r.delta_at_frozen_saddle == pytest.approx(2.0 * p.abs_epsilon_star)
    assert r.omega_minus_at_frozen_saddle == pytest.approx(0.0)
    assert r.q1_eom_at_frozen_saddle is True
    assert r.q2_hessian_matches_frozen is False
    assert r.q3_theorem_A_at_frozen_saddle is False
    assert r.q4_theorem_B_threshold is False
    assert r.q5_vertex_fixed is True


def test_p4_owns_hessian_not_saddle():
    p = condensing_params()
    r = report_p4(p)
    assert r.phi_eom_sq == pytest.approx(stability_amplitude_sq(p))
    assert r.delta_at_frozen_saddle == pytest.approx(p.abs_epsilon_star)
    assert r.omega_minus_at_frozen_saddle == pytest.approx(p.epsilon_star / 2.0)
    assert r.omega_minus_at_true_eom == pytest.approx(0.0)
    assert r.q1_eom_at_frozen_saddle is False
    assert r.q2_hessian_matches_frozen is True
    assert r.q3_theorem_A_at_frozen_saddle is True
    assert r.q4_theorem_B_threshold is True
    assert r.q5_vertex_fixed is True


def test_p2_has_no_vertex():
    p = condensing_params()
    r = report_p2(p)
    assert r.beta is None
    assert r.phi_eom_sq is None
    assert r.q1_eom_at_frozen_saddle is None
    assert r.omega_minus_at_frozen_saddle == pytest.approx(p.epsilon_star / 2.0)
    assert r.q5_vertex_fixed is False
