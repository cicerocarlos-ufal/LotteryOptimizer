"""
Lottery Optimizer

Reduction module.
"""

from .reduction_rules import ReductionRules
from .reducer import Reducer

__all__ = [
    "ReductionRules",
    "Reducer",
]