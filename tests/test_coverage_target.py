from math import comb

from lottery_optimizer.reduction.coverage_target import (
    CoverageTarget,
)


def test_size():

    target = CoverageTarget(

        range(1,22),

        guarantee=13,

    )

    assert len(target) == comb(21,13)


def test_completion():

    target = CoverageTarget(

        range(1,22),

        guarantee=13,

    )

    value = target.completion(

        len(target)//2,

    )

    assert 0.49 < value < 0.51


def test_remaining():

    target = CoverageTarget(

        range(1,22),

        guarantee=13,

    )

    assert target.remaining(0) == len(target)


def test_finished():

    target = CoverageTarget(

        range(1,22),

        guarantee=13,

    )

    assert target.finished(

        len(target)

    )