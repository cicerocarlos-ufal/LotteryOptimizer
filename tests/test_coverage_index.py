from lottery_optimizer.core.game import Game

from lottery_optimizer.reduction.coverage_index import (
    CoverageIndex,
)

from lottery_optimizer.lotteries.lotofacil import LOTOFACIL


def test_add():

    index = CoverageIndex(13)

    game = Game.from_numbers(

        LOTOFACIL,

        range(1,16),

    )

    gain = index.add(game)

    assert gain == 105

    assert len(index) == 105


def test_gain():

    index = CoverageIndex(13)

    game = Game.from_numbers(

        LOTOFACIL,

        range(1,16),

    )

    assert index.gain(game) == 105

    index.add(game)

    assert index.gain(game) == 0


def test_remove():

    index = CoverageIndex(13)

    game = Game.from_numbers(

        LOTOFACIL,

        range(1,16),

    )

    index.add(game)

    loss = index.remove(game)

    assert loss == 105

    assert len(index) == 0


def test_multiple():

    index = CoverageIndex(13)

    a = Game.from_numbers(

        LOTOFACIL,

        range(1,16),

    )

    b = Game.from_numbers(

        LOTOFACIL,

        range(2,17),

    )

    index.add(a)

    before = len(index)

    index.add(b)

    assert len(index) >= before