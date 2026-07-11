"""
Lottery Optimizer

Memetic Algorithm for Reduction.
"""

from __future__ import annotations

from lottery_optimizer.reduction.genetic_cover import (
    GeneticCover,
)

from lottery_optimizer.reduction.hill_cover import (
    HillCover,
)

from lottery_optimizer.reduction.reduction_solution import (
    ReductionSolution,
)


class MemeticCover(GeneticCover):

    def __init__(
        self,
        lottery,
        rules,
        *,
        local_search_probability: float = 0.30,
        hill_iterations: int = 20,
        **kwargs,
    ) -> None:

        super().__init__(

            lottery,

            rules,

            **kwargs,

        )

        self.local_search_probability = (

            local_search_probability

        )

        self.hill = HillCover(

            lottery,

            rules,

            max_iterations=hill_iterations,

            seed=kwargs.get(

                "seed",

                None,

            ),

        )

    # ---------------------------------------------------------

    def local_search(

        self,

        solution: ReductionSolution,

        space,

        target,

    ) -> ReductionSolution:

        improved = self.hill.improve(

            solution.population,

            space,

        )

        return self.evaluate(

            improved,

            target,

        )

    # ---------------------------------------------------------

    def mutate(

        self,

        solution,

        space,

        target,

    ):

        solution = super().mutate(

            solution,

            space,

            target,

        )

        if self.rng.random() < self.local_search_probability:

            solution = self.local_search(

                solution,

                space,

                target,

            )

        return solution