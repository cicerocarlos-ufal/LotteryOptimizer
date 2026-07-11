"""
Lottery Optimizer

Coverage Validator.
"""

from __future__ import annotations

from dataclasses import dataclass

from lottery_optimizer.reduction.coverage_target import CoverageTarget
from lottery_optimizer.reduction.coverage_index import CoverageIndex


@dataclass(slots=True)
class CoverageResult:

    total: int

    covered: int

    uncovered: int

    coverage: float


class CoverageValidator:

    def __init__(

        self,

        guarantee: int,

    ):

        self.guarantee = guarantee

    # ---------------------------------------------------------

    def validate(

        self,

        source_numbers,

        population,

    ) -> CoverageResult:

        target = CoverageTarget(

            source_numbers,

            self.guarantee,

        )

        coverage = CoverageIndex(

            self.guarantee,

        )

        for game in population:

            coverage.add(game)

        covered = coverage.covered

        total = target.size

        uncovered = max(

            0,

            total - covered,

        )

        percentage = 0.0

        if total > 0:

            percentage = covered / total

        return CoverageResult(

            total=total,

            covered=covered,

            uncovered=uncovered,

            coverage=percentage,

        )