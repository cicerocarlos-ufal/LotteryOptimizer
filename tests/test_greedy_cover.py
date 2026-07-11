from lottery_optimizer.lotteries.lotofacil import LOTOFACIL

from lottery_optimizer.reduction.greedy_cover import GreedyCover
from lottery_optimizer.reduction.reduction_rules import ReductionRules
from lottery_optimizer.reduction.coverage_target import CoverageTarget


def build_rules():

    return ReductionRules(

        universe_size=25,

        source_size=21,

        target_size=15,

        n_games=5,

        guarantee=13,

    )


def test_reduce():

    reducer = GreedyCover(

        LOTOFACIL,

        build_rules(),

    )

    population = reducer.reduce(

        range(1, 22),

    )

    assert population.size == 5

    for game in population:

        assert game.size == 15

        assert game.is_valid()


def test_progress():

    reducer = GreedyCover(

        LOTOFACIL,

        build_rules(),

    )

    target = CoverageTarget(

        range(1, 22),

        guarantee=13,

    )

    progress = reducer.progress(

        covered=100,

        target=target,

    )

    assert 0.0 <= progress <= 1.0


def test_invalid_source_size():

    reducer = GreedyCover(

        LOTOFACIL,

        build_rules(),

    )

    try:

        reducer.reduce(

            range(1, 20),

        )

        assert False

    except ValueError:

        assert True


def test_empty_progress():

    reducer = GreedyCover(

        LOTOFACIL,

        build_rules(),

    )

    target = CoverageTarget(

        range(1, 22),

        guarantee=13,

    )

    assert reducer.progress(

        0,

        target,

    ) == 0.0


def test_complete_progress():

    reducer = GreedyCover(

        LOTOFACIL,

        build_rules(),

    )

    target = CoverageTarget(

        range(1, 22),

        guarantee=13,

    )

    assert reducer.progress(

        len(target),

        target,

    ) == 1.0