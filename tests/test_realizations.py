"""C1–C3 audit: independent actions vs counterterms."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from bloch_factor2.realizations import (
    any_independent_pass,
    c2a_projected_conflict,
    c2b_inner_product_cos2,
    c3a_projected_force,
    named_verdicts,
    p1_surplus_delta,
    p3_target_delta,
)
from bloch_factor2.scan import condensing_params


def test_no_independent_pass_in_this_pass():
    assert any_independent_pass() is False


def test_c1c_is_counterterm():
    row = next(r for r in named_verdicts() if r.id == "C1c")
    assert row.independent is False
    assert row.verdict == "COUNTERTERM"


def test_independent_fails_are_independent():
    for row in named_verdicts():
        if row.verdict == "INDEPENDENT-FAIL":
            assert row.independent is True
            assert row.h_matches_target is False


def test_c2a_stationarity_conflicts_with_hessian_shape():
    assert c2a_projected_conflict(psi0=1.0, psi2=1.0) is True
    assert c2a_projected_conflict(psi0=1.0, psi2=-2.0) is True
    assert c2a_projected_conflict(psi0=0.0, psi2=0.0) is False


def test_c2b_inner_product_nonnegative():
    assert c2b_inner_product_cos2(0.3) >= 0.0
    assert c2b_inner_product_cos2(-1.0) == 0.0


def test_c3a_force_vanishes_only_at_gamma_zero():
    assert c3a_projected_force(0.0, 2.0) == 0.0
    assert c3a_projected_force(1.0, 2.0) != 0.0


def test_p3_target_is_minus_frozen_not_plus_surplus():
    p = condensing_params()
    assert p3_target_delta(p) == pytest.approx(-p.abs_epsilon_star)
    assert p1_surplus_delta(p) == pytest.approx(p.abs_epsilon_star)
    assert p3_target_delta(p) != pytest.approx(p1_surplus_delta(p))
