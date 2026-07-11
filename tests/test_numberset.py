from lottery_optimizer.core.numberset import NumberSet
from lottery_optimizer.lotteries.lotofacil import LOTOFACIL


def test_creation():

    game = NumberSet.from_numbers(

        LOTOFACIL,

        range(1, 16)

    )

    assert game.size == 15

    assert game.minimum == 1

    assert game.maximum == 15


def test_mask():

    game = NumberSet.from_numbers(

        LOTOFACIL,

        range(1, 16)

    )

    restored = NumberSet.from_mask(

        LOTOFACIL,

        game.mask

    )

    assert restored == game


def test_contains():

    game = NumberSet.from_numbers(

        LOTOFACIL,

        range(1, 16)

    )

    assert game.contains(10)

    assert not game.contains(20)


def test_intersection():

    a = NumberSet.from_numbers(

        LOTOFACIL,

        range(1, 16)

    )

    b = NumberSet.from_numbers(

        LOTOFACIL,

        range(11, 26)

    )

    assert a.intersection_size(b) == 5


def test_difference():

    a = NumberSet.from_numbers(

        LOTOFACIL,

        range(1, 16)

    )

    b = NumberSet.from_numbers(

        LOTOFACIL,

        range(11, 26)

    )

    diff = a.difference(b)

    assert diff == tuple(range(1, 11))


def test_hamming():

    a = NumberSet.from_numbers(

        LOTOFACIL,

        range(1, 16)

    )

    b = NumberSet.from_numbers(

        LOTOFACIL,

        range(11, 26)

    )

    assert a.hamming_distance(b) == 20


def test_export():

    game = NumberSet.from_numbers(

        LOTOFACIL,

        range(1, 16)

    )

    assert isinstance(game.to_csv(), str)

    assert isinstance(game.to_txt(), str)


def test_iter():

    game = NumberSet.from_numbers(

        LOTOFACIL,

        range(1, 16)

    )

    values = list(game)

    assert len(values) == 15

    assert values[0] == 1

    assert values[-1] == 15


def test_hash():

    a = NumberSet.from_numbers(

        LOTOFACIL,

        range(1, 16)

    )

    b = NumberSet.from_numbers(

        LOTOFACIL,

        range(1, 16)

    )

    assert hash(a) == hash(b)


def test_summary():

    game = NumberSet.from_numbers(

        LOTOFACIL,

        range(1, 16)

    )

    summary = game.summary()

    assert summary["size"] == 15

    assert summary["minimum"] == 1

    assert summary["maximum"] == 15