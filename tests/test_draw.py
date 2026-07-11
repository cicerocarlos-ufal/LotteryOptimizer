from datetime import date

from lottery_optimizer.core.draw import Draw
from lottery_optimizer.lotteries.lotofacil import LOTOFACIL


def test_draw_creation():

    draw = Draw.from_numbers(

        LOTOFACIL,

        range(1, 16),

        contest=100,

        draw_date=date(2025, 1, 1),

    )

    assert draw.size == 15

    assert draw.contest == 100

    assert draw.year == 2025

    assert draw.month == 1

    assert draw.day == 1


def test_draw_numbers():

    draw = Draw.from_numbers(

        LOTOFACIL,

        range(1, 16),

    )

    assert draw.minimum == 1

    assert draw.maximum == 15


def test_is_official():

    draw = Draw.from_numbers(

        LOTOFACIL,

        range(1, 16),

        contest=3000,

    )

    assert draw.is_official()


def test_to_dict():

    draw = Draw.from_numbers(

        LOTOFACIL,

        range(1, 16),

    )

    d = draw.to_dict()

    assert d["mask"] == draw.mask

    assert len(d["numbers"]) == 15