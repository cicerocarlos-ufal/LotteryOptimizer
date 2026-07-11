"""
Lottery Optimizer

Hill Climbing reduction algorithm.
"""

from __future__ import annotations

import random

from lottery_optimizer.core.population import Population

from lottery_optimizer.reduction.reducer import Reducer
from lottery_optimizer.reduction.coverage_index import CoverageIndex
from lottery_optimizer.reduction.combination_space import CombinationSpace


class HillCover(Reducer):

    def __init__(
        self,
        lottery,
        rules,
        max_iterations: int = 100,
        neighbors_per_iteration: int = 50,
        seed: int | None = None,
    ) -> None:

        super().__init__(lottery, rules)

        self.max_iterations = max_iterations
        self.neighbors_per_iteration = neighbors_per_iteration

        self.rng = random.Random(seed)

    # ---------------------------------------------------------

    def score(
        self,
        population: Population,
    ) -> int:

        coverage = CoverageIndex(

            self.rules.guarantee,

        )

        for game in population:

            coverage.add(game)

        return coverage.covered

    # ---------------------------------------------------------

    def improve(
        self,
        population: Population,
        space: CombinationSpace,
    ) -> Population:

        current = population

        current_score = self.score(current)

        for _ in range(self.max_iterations):

            improved = False

            for _ in range(self.neighbors_per_iteration):

                #
                # escolhe um jogo da redução
                #

                idx = self.rng.randrange(current.size)

                #
                # gera um candidato aleatório
                #

                replacement = space.random_game(self.rng)

                #
                # evita substituir por ele mesmo
                #

                if replacement.mask == current[idx].mask:

                    continue

                #
                # cria uma nova população
                #

                games = list(current.games)

                games[idx] = replacement

                trial = Population(

                    self.lottery,

                    games,

                )

                value = self.score(trial)

                if value > current_score:

                    current = trial

                    current_score = value

                    improved = True

                    break

            if not improved:

                break

        return current

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

            rules=self.lottery,

            source_numbers=numbers,

            target_size=self.rules.target_size,

        )

        #
        # solução inicial
        #

        population = Population(

            self.lottery,

        )

        iterator = iter(space)

        while population.size < self.rules.n_games:

            population.add(

                next(iterator)

            )

        #
        # melhoria
        #

        return self.improve(

            population,

            space,

        )