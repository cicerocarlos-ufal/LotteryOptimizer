from math import comb

from lottery_optimizer.reduction.combination_space import (
    CombinationSpace,
)

from lottery_optimizer.lotteries.lotofacil import LOTOFACIL


def test_size():

    numbers = range(1,22)

    space = CombinationSpace(

        LOTOFACIL,

        numbers,

        15,

    )

    assert space.size == comb(21,15)


def test_random():

    numbers = range(1,22)

    space = CombinationSpace(

        LOTOFACIL,

        numbers,

        15,

    )

    game = space.random_game()

    assert game.size == 15


def test_sample():

    numbers = range(1,22)

    space = CombinationSpace(

        LOTOFACIL,

        numbers,

        15,

    )

    games = space.sample(100)

    assert len(games) == 100


def test_iterator():

    numbers = range(1,18)

    space = CombinationSpace(

        LOTOFACIL,

        numbers,

        15,

    )

    total = 0

    for _ in space:

        total += 1

    assert total == comb(17,15)