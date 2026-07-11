from lottery_optimizer.core.game import Game
from lottery_optimizer.lotteries.lotofacil import LOTOFACIL


def test_random():

    game = Game.random(LOTOFACIL)

    assert game.size == 15

    assert game.is_valid()


def test_swap():

    game = Game.from_numbers(

        LOTOFACIL,

        range(1, 16),

    )

    other = game.swap(

        1,

        20,

    )

    assert 20 in other

    assert 1 not in other

    assert other.size == 15


def test_neighbor():

    game = Game.from_numbers(

        LOTOFACIL,

        range(1, 16),

    )

    other = game.random_neighbor()

    assert other.size == 15

    assert other != game


def test_mutation():

    game = Game.from_numbers(

        LOTOFACIL,

        range(1, 16),

    )

    mutated = game.mutate()

    assert mutated.size == 15


def test_crossover():

    a = Game.from_numbers(

        LOTOFACIL,

        range(1, 16),

    )

    b = Game.from_numbers(

        LOTOFACIL,

        range(11, 26),

    )

    child = a.crossover(b)

    assert child.size == 15

    assert child.is_valid()


def test_distance():

    a = Game.from_numbers(

        LOTOFACIL,

        range(1, 16),

    )

    b = Game.from_numbers(

        LOTOFACIL,

        range(11, 26),

    )

    assert a.distance(b) == 20
    