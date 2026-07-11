from lottery_optimizer.core.population import Population

from lottery_optimizer.reduction.reduction_solution import (
    ReductionSolution,
)

from lottery_optimizer.lotteries.lotofacil import LOTOFACIL


def test_solution():

    pop = Population(

        LOTOFACIL,

    )

    sol = ReductionSolution(

        population=pop,

        covered=50,

        target=100,

    )

    assert sol.completion == 0.5

    assert sol.remaining == 50

    assert not sol.finished


def test_finished():

    pop = Population(

        LOTOFACIL,

    )

    sol = ReductionSolution(

        population=pop,

        covered=100,

        target=100,

    )

    assert sol.finished