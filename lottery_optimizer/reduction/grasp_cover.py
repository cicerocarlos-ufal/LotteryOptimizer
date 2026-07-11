"""
Lottery Optimizer

GRASP Set Cover Reduction.
"""

from __future__ import annotations

import random

from lottery_optimizer.core.population import Population

from lottery_optimizer.reduction.reducer import Reducer
from lottery_optimizer.reduction.coverage_index import CoverageIndex
from lottery_optimizer.reduction.coverage_target import CoverageTarget
from lottery_optimizer.reduction.candidate_list import CandidateList
from lottery_optimizer.reduction.combination_space import (
    CombinationSpace,
)


class GraspCover(Reducer):

    def __init__(
        self,
        lottery,
        rules,
        candidate_list_size: int = 500,
        alpha: float = 0.20,
        seed: int | None = None,
    ) -> None:

        super().__init__(lottery, rules)

        self.candidate_list_size = candidate_list_size
        self.alpha = alpha
        self.rng = random.Random(seed)

    # ---------------------------------------------------------

    def choose(self, rcl: CandidateList):

        games = rcl.games()

        if not games:
            return None

        limit = max(

            1,

            int(len(games) * self.alpha),

        )

        return self.rng.choice(

            games[:limit]

        )

    # ---------------------------------------------------------

    def reduce(
        self,
        numbers,
    ) -> Population:

        numbers = tuple(sorted(numbers))

        if len(numbers) != self.rules.source_size:

            raise ValueError(

                f"Expected {self.rules.source_size} numbers."

            )

        space = CombinationSpace(

            self.lottery,

            numbers,

            self.rules.target_size,

        )

        target = CoverageTarget(

            numbers,

            self.rules.guarantee,

        )

        coverage = CoverageIndex(

            self.rules.guarantee,

        )

        rcl = CandidateList(

            coverage,

            self.candidate_list_size,

        )

        population = Population(

            self.lottery,

        )

        selected = set()

        while (

            population.size < self.rules.n_games

            and

            not target.finished(

                coverage.covered

            )

        ):

            rcl.build(

                (

                    game

                    for game in space

                    if game.mask not in selected

                )

            )

            game = self.choose(

                rcl,

            )

            if game is None:

                break

            population.add(game)

            selected.add(

                game.mask,

            )

            coverage.add(

                game,

            )

        return population