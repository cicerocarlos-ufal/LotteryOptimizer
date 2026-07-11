"""
Lottery Optimizer

Genetic Algorithm for Reduction.
"""

from __future__ import annotations

import random

from lottery_optimizer.core.population import Population

from lottery_optimizer.reduction.reducer import Reducer
from lottery_optimizer.reduction.coverage_index import CoverageIndex
from lottery_optimizer.reduction.coverage_target import CoverageTarget
from lottery_optimizer.reduction.combination_space import (
    CombinationSpace,
)
from lottery_optimizer.reduction.reduction_solution import (
    ReductionSolution,
)


class GeneticCover(Reducer):
    """
    Genetic Algorithm for Set Cover reduction.
    """

    def __init__(
        self,
        lottery,
        rules,
        population_size: int = 40,
        generations: int = 100,
        mutation_rate: float = 0.10,
        elite_size: int = 2,
        tournament_size: int = 3,
        seed: int | None = None,
    ) -> None:

        super().__init__(lottery, rules)

        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.elite_size = elite_size
        self.tournament_size = tournament_size

        self.rng = random.Random(seed)

    # ---------------------------------------------------------

    def evaluate(
        self,
        population: Population,
        target: CoverageTarget,
    ) -> ReductionSolution:
        """
        Evaluates one reduction.
        """

        coverage = CoverageIndex(

            self.rules.guarantee,

        )

        for game in population:

            coverage.add(game)

        covered = coverage.covered

        return ReductionSolution(

            population=population,

            covered=covered,

            target=target.size,

            score=covered / target.size,

            algorithm="GeneticCover",

        )

    # ---------------------------------------------------------

    def random_solution(
        self,
        space: CombinationSpace,
        target: CoverageTarget,
    ) -> ReductionSolution:
        """
        Creates one random reduction.
        """

        games = space.sample(

            self.rules.n_games,

            rng=self.rng,

        )

        population = Population(

            self.lottery,

            games,

        )

        return self.evaluate(

            population,

            target,

        )

    # ---------------------------------------------------------

    def initialize_population(
        self,
        space: CombinationSpace,
        target: CoverageTarget,
    ) -> list[ReductionSolution]:
        """
        Initial GA population.
        """

        return [

            self.random_solution(

                space,

                target,

            )

            for _ in range(

                self.population_size

            )

        ]

    # ---------------------------------------------------------

    def tournament(
        self,
        population: list[ReductionSolution],
    ) -> ReductionSolution:
        """
        Tournament selection.
        """

        competitors = self.rng.sample(

            population,

            self.tournament_size,

        )

        competitors.sort(

            key=lambda s: s.score,

            reverse=True,

        )

        return competitors[0]
        # ---------------------------------------------------------

    def _remove_duplicates(
        self,
        games,
    ):
        """
        Removes duplicated games preserving order.
        """

        unique = {}
        result = []

        for game in games:

            if game.mask in unique:
                continue

            unique[game.mask] = True

            result.append(game)

        return result

    # ---------------------------------------------------------

    def _fill_population(
        self,
        games,
        space: CombinationSpace,
    ):
        """
        Completes a reduction until it reaches
        n_games unique games.
        """

        used = {

            game.mask

            for game in games

        }

        while len(games) < self.rules.n_games:

            candidate = space.random_game(

                self.rng,

            )

            if candidate.mask in used:

                continue

            used.add(

                candidate.mask,

            )

            games.append(

                candidate,

            )

        return games

    # ---------------------------------------------------------

    def crossover(
        self,
        father: ReductionSolution,
        mother: ReductionSolution,
        space: CombinationSpace,
        target: CoverageTarget,
    ) -> ReductionSolution:
        """
        One-point crossover.
        """

        cut = self.rng.randint(

            1,

            self.rules.n_games - 1,

        )

        child_games = (

            list(

                father.population.games[:cut]

            )

            +

            list(

                mother.population.games[cut:]

            )

        )

        child_games = self._remove_duplicates(

            child_games,

        )

        child_games = self._fill_population(

            child_games,

            space,

        )

        child = Population(

            self.lottery,

            child_games,

        )

        return self.evaluate(

            child,

            target,

        )

    # ---------------------------------------------------------

    def mutate(
        self,
        solution: ReductionSolution,
        space: CombinationSpace,
        target: CoverageTarget,
    ) -> ReductionSolution:
        """
        Random mutation.
        """

        games = list(

            solution.population.games

        )

        index = self.rng.randrange(

            self.rules.n_games,

        )

        used = {

            game.mask

            for game in games

        }

        while True:

            candidate = space.random_game(

                self.rng,

            )

            if candidate.mask not in used:

                break

        games[index] = candidate

        population = Population(

            self.lottery,

            games,

        )

        return self.evaluate(

            population,

            target,

        )
        # ---------------------------------------------------------

    def reduce(
        self,
        numbers,
    ) -> Population:
        """
        Executes the Genetic Algorithm.

        Parameters
        ----------
        numbers
            Source numbers selected by the user.

        Returns
        -------
        Population
            Best reduction found.
        """

        numbers = tuple(sorted(numbers))

        if len(numbers) != self.rules.source_size:

            raise ValueError(

                f"Expected {self.rules.source_size} numbers, "
                f"received {len(numbers)}."

            )

        #
        # Search space
        #

        space = CombinationSpace(

            rules=self.lottery,

            source_numbers=numbers,

            target_size=self.rules.target_size,

        )

        #
        # Coverage target
        #

        target = CoverageTarget(

            numbers,

            self.rules.guarantee,

        )

        #
        # Initial population
        #

        population = self.initialize_population(

            space,

            target,

        )

        #
        # Evolution
        #

        for _ in range(self.generations):

            #
            # Sort (best first)
            #

            population.sort(

                key=lambda solution: solution.score,

                reverse=True,

            )

            #
            # Elitism
            #

            next_population = population[: self.elite_size]

            #
            # Generate offspring
            #

            while len(next_population) < self.population_size:

                father = self.tournament(

                    population,

                )

                mother = self.tournament(

                    population,

                )

                child = self.crossover(

                    father,

                    mother,

                    space,

                    target,

                )

                if self.rng.random() < self.mutation_rate:

                    child = self.mutate(

                        child,

                        space,

                        target,

                    )

                next_population.append(

                    child,

                )

            population = next_population

        #
        # Best solution
        #

        population.sort(

            key=lambda solution: solution.score,

            reverse=True,

        )

        return population[0].population        