"""
Lottery Optimizer

Objective function builder.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ObjectiveWeights:
    """
    Weights used by the objective function.
    """

    average_hits: float = 1.0
    coverage: float = 5.0
    diversity: float = 2.0
    redundancy: float = -2.0
    max_hits: float = 3.0
    min_hits: float = 1.0


class ObjectiveBuilder:

    def __init__(
        self,
        weights: ObjectiveWeights | None = None,
    ) -> None:

        self.weights = weights or ObjectiveWeights()

    def score(
        self,
        fitness,
    ) -> float:

        w = self.weights

        return (

            fitness.average_hits * w.average_hits +

            fitness.coverage * w.coverage +

            fitness.diversity * w.diversity +

            fitness.redundancy * w.redundancy +

            fitness.max_hits * w.max_hits +

            fitness.min_hits * w.min_hits

        )