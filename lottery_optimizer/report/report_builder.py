"""
Lottery Optimizer

Report Builder.
"""

from __future__ import annotations

from lottery_optimizer.report.report import Report

from lottery_optimizer.reduction.coverage_index import CoverageIndex
from lottery_optimizer.reduction.coverage_target import CoverageTarget


class ReportBuilder:

    @staticmethod
    def build(
        lottery,
        rules,
        source_numbers,
        population,
        elapsed,
        algorithm,
        seed=None,
    ) -> Report:
        """
        Build a report from a reduction result.
        """

        source_numbers = tuple(sorted(source_numbers))

        #
        # Compute achieved coverage
        #

        coverage = CoverageIndex(

            rules.guarantee,

        )

        for game in population:

            coverage.add(game)

        #
        # Compute target coverage
        #

        target = CoverageTarget(

            source_numbers,

            rules.guarantee,

        )

        covered = coverage.covered

        percentage = 0.0

        if target.size > 0:

            percentage = covered / target.size

        return Report(

            lottery=lottery.name,

            algorithm=algorithm,

            source_size=len(source_numbers),

            target_size=rules.target_size,

            guarantee=rules.guarantee,

            games=population.size,

            covered=covered,

            target=target.size,

            coverage=percentage,

            elapsed=elapsed,

            seed=seed,

        )