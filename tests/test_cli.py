"""Command-line entry point: exit codes and output shape."""

from __future__ import annotations

import json
import subprocess
import sys

import pytest

from bloch_factor2.__main__ import main


def test_default_run_prints_identity(capsys):
    assert main([]) == 0
    out = capsys.readouterr().out
    assert "parameters: W=1.0 λ=1.0 M=1.0 c=1.0 μ=0.0" in out
    assert "R_analytic: 2.0" in out
    assert "assertion R_analytic == 2: True" in out


def test_json_matches_documented_default_point(capsys):
    assert main(["--json"]) == 0
    data = json.loads(capsys.readouterr().out)
    assert data["epsilon_star"] == pytest.approx(-0.25)
    assert data["phi_saddle_sq"] == pytest.approx(2.0)
    assert data["phi_stable_analytic_sq"] == pytest.approx(4.0)
    assert data["omega_minus_saddle"] == pytest.approx(-0.125)
    assert data["R_analytic_equals_2"] is True
    assert data["n_modes"] == 9
    assert 1.5 < data["R_numeric"] < 2.6


def test_other_condensing_point_still_gives_two(capsys):
    assert main(["--W", "0.8", "--lam", "2", "--M", "1.5", "--c", "0.5", "--mu", "0.2", "--json"]) == 0
    data = json.loads(capsys.readouterr().out)
    assert data["R_analytic"] == pytest.approx(2.0)
    assert data["parameters"]["lam"] == 2.0


def test_noncondensing_point_exits_2(capsys):
    assert main(["--mu", "1.0"]) == 2
    assert "no classical condensate" in capsys.readouterr().err


@pytest.mark.parametrize("argv", [["--lam", "0"], ["--c", "-1"], ["--n-max", "0"]])
def test_invalid_input_exits_2(argv, capsys):
    assert main(argv) == 2
    assert "error:" in capsys.readouterr().err


def test_module_entry_point_runs():
    proc = subprocess.run(
        [sys.executable, "-m", "bloch_factor2", "--json"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    assert json.loads(proc.stdout)["R_analytic_equals_2"] is True
