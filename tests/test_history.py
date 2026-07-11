from lottery_optimizer.core.draw import Draw
from lottery_optimizer.core.history import History
from lottery_optimizer.lotteries.lotofacil import LOTOFACIL


def test_history():

    history = History(LOTOFACIL)

    history.add(

        Draw.from_numbers(

            LOTOFACIL,

            range(1,16),

            contest=1,

        )

    )

    assert history.size == 1

    assert len(history) == 1


def test_latest():

    history = History(LOTOFACIL)

    history.add(

        Draw.from_numbers(

            LOTOFACIL,

            range(1,16),

            contest=10,

        )

    )

    history.add(

        Draw.from_numbers(

            LOTOFACIL,

            range(2,17),

            contest=20,

        )

    )

    assert history.latest().contest == 20


def test_get():

    history = History(LOTOFACIL)

    draw = Draw.from_numbers(

        LOTOFACIL,

        range(1,16),

        contest=100,

    )

    history.add(draw)

    assert history.get(100) == draw


def test_iter():

    history = History(LOTOFACIL)

    history.add(

        Draw.from_numbers(

            LOTOFACIL,

            range(1,16),

            contest=1,

        )

    )

    assert len(list(history)) == 1