"""
Lottery Optimizer

Population evaluator.
"""

from __future__ import annotations

from lottery_optimizer.core.population import Population
from lottery_optimizer.core.history import History
from lottery_optimizer.core.fitness import Fitness
from lottery_optimizer.core.objective import ObjectiveBuilder

class Evaluator:
    """
    Evaluates populations against historical draws.
    """

    def __init__(
        self,
        history: History,
    ) -> None:

        self.history = history

    # ---------------------------------------------------------

    @staticmethod
    def hits(
        game,
        draw,
    ) -> int:
        """
        Number of hits between a game
        and one official draw.
        """

        return game.intersection_size(draw)

    # ---------------------------------------------------------

    def evaluate_game(
        self,
        game,
    ) -> Fitness:

        total_hits = 0

        max_hits = 0

        min_hits = game.rules.draw_size

        coverage = 0

        for draw in self.history:

            hits = self.hits(game, draw)

            total_hits += hits

            max_hits = max(max_hits, hits)

            min_hits = min(min_hits, hits)

            if hits >= 11:
                coverage += 1

        n = len(self.history)

        if n == 0:

            return Fitness()

        average = total_hits / n

        fitness = Fitness(

            score=0.0,

            coverage=coverage / n,

            diversity=0.0,

            redundancy=0.0,

            average_hits=average,

            max_hits=max_hits,

            min_hits=min_hits,

            evaluated_games=1,

            evaluated_draws=n,

        )

        fitness.score = ObjectiveBuilder().score(fitness)

        return fitness

    # ---------------------------------------------------------

    def evaluate_population(
        self,
        population: Population,
    ) -> Fitness:

        if len(population) == 0:

            return Fitness()

        total = 0.0

        coverage = 0.0

        max_hits = 0

        min_hits = population.rules.draw_size

        for game in population:

            fit = self.evaluate_game(game)

            total += fit.score

            coverage += fit.coverage

            max_hits = max(max_hits, fit.max_hits)

            min_hits = min(min_hits, fit.min_hits)

        n = len(population)

        diversity = self.population_diversity(population)

        redundancy = 1.0 - diversity

        return Fitness(

            score=total / n,

            coverage=coverage / n,

            diversity=diversity,

            redundancy=redundancy,

            average_hits=total / n,

            max_hits=max_hits,

            min_hits=min_hits,

            evaluated_games=n,

            evaluated_draws=len(self.history),

        )

    # ---------------------------------------------------------

    @staticmethod
    def population_diversity(
        population: Population,
    ) -> float:
        """
        Average normalized Hamming distance.
        """

        if len(population) < 2:

            return 1.0

        distances = []

        games = list(population)

        max_distance = games[0].rules.draw_size * 2

        for i in range(len(games)):

            for j in range(i + 1, len(games)):

                d = games[i].hamming_distance(

                    games[j]

                )

                distances.append(

                    d / max_distance

                )

        return sum(distances) / len(distances)