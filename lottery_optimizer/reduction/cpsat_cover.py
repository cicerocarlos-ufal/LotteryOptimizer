"""
Lottery Optimizer

CP-SAT Reduction Solver.
"""

from __future__ import annotations

from ortools.sat.python import cp_model

from lottery_optimizer.core.population import Population

from lottery_optimizer.reduction.reducer import Reducer
from lottery_optimizer.reduction.combination_space import (
    CombinationSpace,
)


class CPSATCover(Reducer):

    def __init__(

        self,

        lottery,

        rules,

        time_limit: int = 300,

        workers: int = 0,

    ) -> None:

        super().__init__(

            lottery,

            rules,

        )

        self.time_limit = time_limit

        self.workers = workers

    # -----------------------------------------------------

    def build_model(

        self,

        space,

    ):

        model = cp_model.CpModel()

        games = list(space)

        x = [

            model.NewBoolVar(

                f"g{i}"

            )

            for i in range(

                len(games)

            )

        ]

        #
        # quantidade de jogos
        #

        model.Add(

            sum(x)

            ==

            self.rules.n_games

        )

        return model, games, x

    # -----------------------------------------------------

    def solve(

        self,

        model,

    ):

        solver = cp_model.CpSolver()

        solver.parameters.max_time_in_seconds = (

            self.time_limit

        )

        if self.workers > 0:

            solver.parameters.num_search_workers = (

                self.workers

            )

        status = solver.Solve(

            model

        )

        return solver, status

    # -----------------------------------------------------

    def reduce(

        self,

        numbers,

    ) -> Population:

        space = CombinationSpace(

            self.lottery,

            numbers,

            self.rules.target_size,

        )

        model, games, x = self.build_model(

            space,

        )

        solver, status = self.solve(

            model,

        )

        population = Population(

            self.lottery,

        )

        if status not in (

            cp_model.OPTIMAL,

            cp_model.FEASIBLE,

        ):

            return population

        for game, var in zip(

            games,

            x,

        ):

            if solver.Value(

                var

            ):

                population.add(

                    game

                )

        return population