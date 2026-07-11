from lottery_optimizer.core.game import Game

from lottery_optimizer.reduction.coverage import Coverage

from lottery_optimizer.lotteries.lotofacil import LOTOFACIL


def test_add():

    cov = Coverage(13)

    game = Game.from_numbers(

        LOTOFACIL,

        range(1,16),

    )

    new = cov.add(game)

    assert new == 105

    assert cov.covered == 105


def test_copy():

    cov = Coverage(13)

    game = Game.from_numbers(

        LOTOFACIL,

        range(1,16),

    )

    cov.add(game)

    other = cov.copy()

    assert other.covered == cov.covered


def test_evaluate():

    cov = Coverage(13)

    games = [

        Game.from_numbers(

            LOTOFACIL,

            range(1,16),

        ),

        Game.from_numbers(

            LOTOFACIL,

            range(2,17),

        )

    ]

    total = cov.evaluate(

        games

    )

    assert total >= 105


def test_clear():

    cov = Coverage(13)

    game = Game.from_numbers(

        LOTOFACIL,

        range(1,16),

    )

    cov.add(game)

    cov.clear()

    assert cov.covered == 0