"""
Lottery Optimizer

Coverage Target.
"""

from __future__ import annotations

from itertools import combinations
from math import comb


class CoverageTarget:
    """
    Represents the universe that must be covered.
    """

    def __init__(

        self,

        source_numbers,

        guarantee: int,

    ) -> None:

        self.source_numbers = tuple(sorted(source_numbers))

        self.guarantee = guarantee

        self.total = comb(

            len(self.source_numbers),

            guarantee,

        )

    # -----------------------------------------------------

    @property
    def size(self):

        return self.total

    # -----------------------------------------------------

    def subsets(self):

        yield from combinations(

            self.source_numbers,

            self.guarantee,

        )

    # -----------------------------------------------------

    def completion(

        self,

        covered: int,

    ) -> float:

        if self.total == 0:

            return 0.0

        return covered / self.total

    # -----------------------------------------------------

    def remaining(

        self,

        covered: int,

    ) -> int:

        return max(

            0,

            self.total - covered,

        )

    # -----------------------------------------------------

    def finished(

        self,

        covered: int,

    ) -> bool:

        return covered >= self.total

    # -----------------------------------------------------

    def __len__(self):

        return self.total

    # -----------------------------------------------------

    def __repr__(self):

        return (

            f"CoverageTarget(total={self.total})"

        )