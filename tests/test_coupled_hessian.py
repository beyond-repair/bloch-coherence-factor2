from bloch_factor2.coupled_hessian import (
    even_eigenvalues,
    k_ratio_formula,
    k_ratio_two_qstar,
    odd_eigenvalues,
    on_shell_epsilon,
    spectrum,
)
from bloch_factor2.model import ModelParams
from bloch_factor2.two_sector import theorem_a_tuning_ratio


def test_k_does_not_fix_three_halves():
    samples = [
        ModelParams(W=1.0, lam=1.0, M=1.0, c=1.0, mu=0.3),
        ModelParams(W=0.4, lam=1.0, M=2.0, c=0.8, mu=0.5),
        ModelParams(W=2.0, lam=1.0, M=1.0, c=3.0, mu=1.0),
    ]
    ratios = []
    for p in samples:
        r = k_ratio_two_qstar(p)
        assert abs(r - k_ratio_formula(p)) < 1e-12
        ratios.append(r)
    assert any(abs(r - theorem_a_tuning_ratio()) > 1e-6 for r in ratios)
    assert max(ratios) - min(ratios) > 1e-6


def test_odd_coupled_zero_identically():
    for omega2 in (0.4, 1.0, -1.0, 2.5):
        z, other = odd_eigenvalues(gamma=1.7, omega2=omega2)
        assert z == 0.0
        assert abs(other - (omega2 + 1.7**2 / (4.0 * omega2))) < 1e-12


def test_odd_min_is_not_half_epsilon():
    gamma, w0, w2 = 1.2, 0.8, 1.1
    spec = spectrum(gamma, w0, w2)
    half = 0.5 * spec.epsilon_star
    assert spec.odd[0] == 0.0
    assert abs(spec.odd[0] - half) > 1e-9
    # ε_* > 0 for ω>0, so ε_*/2 > 0 as well; still not the odd zero
    assert spec.epsilon_star > 0.0


def test_positive_omega_cannot_host_negative_epsilon():
    eps = on_shell_epsilon(gamma_sq=2.0, omega0=1.0, omega2=1.5)
    assert eps > 0.0


def test_auxiliary_sign_gives_negative_epsilon_but_odd_still_zero():
    gamma, w0, w2 = 1.0, -1.0, -1.0
    spec = spectrum(gamma, w0, w2)
    assert spec.epsilon_star < 0.0
    assert spec.odd[0] == 0.0
    assert abs(spec.odd[0] - 0.5 * spec.epsilon_star) > 1e-9


def test_even_amplitude_is_massive_when_gamma_nonzero():
    ev = even_eigenvalues(gamma=1.0, omega0=1.0, omega2=1.0)
    assert all(abs(x) > 1e-9 for x in ev) or min(abs(x) for x in ev) > 1e-9
    # characteristic at λ=0 is (g²/4)(2 w2 + w0) ≠ 0
    assert abs(min(ev, key=abs)) > 1e-9 or True
    # stronger: product of roots = -c / a0 with c = (g²/4)(2w2+w0) ≠ 0
    # so 0 is not an even root
    assert all(abs(x) > 1e-8 for x in ev)
