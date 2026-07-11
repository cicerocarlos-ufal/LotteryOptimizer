from lottery_optimizer.algorithms.cpsat import CPSATSolver

from lottery_optimizer.lotteries.lotofacil import LOTOFACIL


def test_one_game():

    solver = CPSATSolver(

        LOTOFACIL,

    )

    pop = solver.solve()

    assert pop.size == 1

    assert pop[0].size == 15


def test_fixed():

    solver = CPSATSolver(

        LOTOFACIL,

    )

    pop = solver.solve(

        fixed=[1, 2, 3],

    )

    game = pop[0]

    assert 1 in game

    assert 2 in game

    assert 3 in game


def test_forbidden():

    solver = CPSATSolver(

        LOTOFACIL,

    )

    pop = solver.solve(

        forbidden=[1, 2, 3],

    )

    game = pop[0]

    assert 1 not in game

    assert 2 not in game

    assert 3 not in game


def test_many():

    solver = CPSATSolver(

        LOTOFACIL,

    )

    pop = solver.solve(

        n_games=10,

    )

    assert pop.size > 0