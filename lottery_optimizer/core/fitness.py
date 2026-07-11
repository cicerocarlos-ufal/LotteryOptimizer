"""
Lottery Optimizer

Fitness object.

Stores all metrics used to evaluate a population or a game.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Fitness:
    """
    Immutable evaluation result.
    """

    score: float = 0.0

    coverage: float = 0.0

    diversity: float = 0.0

    redundancy: float = 0.0

    average_hits: float = 0.0

    max_hits: int = 0

    min_hits: int = 0

    evaluated_games: int = 0

    evaluated_draws: int = 0

    # ---------------------------------------------------------

    @property
    def valid(self) -> bool:

        return self.score >= 0

    # ---------------------------------------------------------

    def better_than(
        self,
        other: "Fitness",
    ) -> bool:

        return self.score > other.score

    # ---------------------------------------------------------

    def worse_than(
        self,
        other: "Fitness",
    ) -> bool:

        return self.score < other.score

    # ---------------------------------------------------------

    def to_dict(self) -> dict:

        return {

            "score": self.score,

            "coverage": self.coverage,

            "diversity": self.diversity,

            "redundancy": self.redundancy,

            "average_hits": self.average_hits,

            "max_hits": self.max_hits,

            "min_hits": self.min_hits,

            "evaluated_games": self.evaluated_games,

            "evaluated_draws": self.evaluated_draws,

        }

    # ---------------------------------------------------------

    def __lt__(
        self,
        other: "Fitness",
    ) -> bool:

        return self.score < other.score

    def __le__(
        self,
        other: "Fitness",
    ) -> bool:

        return self.score <= other.score

    def __gt__(
        self,
        other: "Fitness",
    ) -> bool:

        return self.score > other.score

    def __ge__(
        self,
        other: "Fitness",
    ) -> bool:

        return self.score >= other.score

    def __repr__(self) -> str:

        return (

            "Fitness("
            f"score={self.score:.4f}, "
            f"coverage={self.coverage:.4f}, "
            f"diversity={self.diversity:.4f}, "
            f"redundancy={self.redundancy:.4f}"
            ")"

        )