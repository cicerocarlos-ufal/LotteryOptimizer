"""
Lottery Optimizer

Reduction Solution.
"""

from __future__ import annotations

from dataclasses import dataclass

from lottery_optimizer.core.population import Population


@dataclass(slots=True)
class ReductionSolution:

    population: Population

    covered: int = 0

    target: int = 0

    score: float = 0.0

    algorithm: str = ""

    iteration: int = 0

    elapsed: float = 0.0

    @property
    def completion(self) -> float:

        if self.target == 0:

            return 0.0

        return self.covered / self.target

    @property
    def remaining(self) -> int:

        return max(

            0,

            self.target - self.covered,

        )

    @property
    def finished(self) -> bool:

        return self.covered >= self.target