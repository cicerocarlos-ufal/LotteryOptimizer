"""
Lottery Optimizer

Report.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Report:

    lottery: str

    algorithm: str

    source_size: int

    target_size: int

    guarantee: int

    games: int

    covered: int

    target: int

    coverage: float

    elapsed: float

    seed: int | None = None

    def to_dict(self):

        return {

            "lottery": self.lottery,

            "algorithm": self.algorithm,

            "source_size": self.source_size,

            "target_size": self.target_size,

            "guarantee": self.guarantee,

            "games": self.games,

            "covered": self.covered,

            "target": self.target,

            "coverage": self.coverage,

            "elapsed": self.elapsed,

            "seed": self.seed,

        }

    @property
    def remaining(self):

        return max(

            0,

            self.target - self.covered,

        )