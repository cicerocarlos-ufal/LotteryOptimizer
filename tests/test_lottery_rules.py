from lottery_optimizer.lotteries.lotofacil import LOTOFACIL


def test_basic_rules():

    assert LOTOFACIL.total_numbers == 25

    assert LOTOFACIL.draw_size == 15

    assert LOTOFACIL.minimum == 1

    assert LOTOFACIL.maximum == 25


def test_mask():

    numbers = tuple(range(1, 16))

    mask = LOTOFACIL.mask(numbers)

    restored = LOTOFACIL.numbers_from_mask(mask)

    assert restored == numbers


def test_contains():

    assert 1 in LOTOFACIL

    assert 25 in LOTOFACIL

    assert 26 not in LOTOFACIL


def test_validate():

    numbers = tuple(range(1, 16))

    assert LOTOFACIL.validate(numbers) == numbers
