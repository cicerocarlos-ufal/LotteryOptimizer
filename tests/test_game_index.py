from lottery_optimizer.core.game import Game

from lottery_optimizer.reduction.game_index import (
    GameIndex,
)

from lottery_optimizer.lotteries.lotofacil import LOTOFACIL


def test_add():

    idx = GameIndex()

    game = Game.from_numbers(

        LOTOFACIL,

        range(1,16),

    )

    idx.add(

        game,

        gain=105,

    )

    assert len(idx) == 1


def test_gain():

    idx = GameIndex()

    game = Game.from_numbers(

        LOTOFACIL,

        range(1,16),

    )

    idx.add(game)

    idx.update_gain(

        game,

        80,

    )

    assert idx.get(game).gain == 80


def test_selected():

    idx = GameIndex()

    game = Game.from_numbers(

        LOTOFACIL,

        range(1,16),

    )

    idx.add(game)

    idx.mark_selected(game)

    assert idx.get(game).selected