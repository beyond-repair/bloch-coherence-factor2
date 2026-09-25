"""Bloch coherence factor-of-two numerical kernel.

This package implements the *classical* W + λφ⁴ modulated-saddle reduction
and the associated Bloch operator. It does not import CFT-X parameters,
Ware-constant phenomenology, thrust models, or loop corrections.
"""

from .model import ModelParams, saddle_amplitude_sq, stability_amplitude_sq
from .operator import (
    bloch_matrix,
    brillouin_min_eigenvalue,
    two_mode_eigenvalues,
)
from .scan import ratio_scan

__all__ = [
    "ModelParams",
    "saddle_amplitude_sq",
    "stability_amplitude_sq",
    "bloch_matrix",
    "brillouin_min_eigenvalue",
    "two_mode_eigenvalues",
    "ratio_scan",
]
