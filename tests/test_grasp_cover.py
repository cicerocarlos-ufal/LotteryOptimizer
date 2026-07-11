from lottery_optimizer.lotteries.lotofacil import LOTOFACIL

from lottery_optimizer.reduction.grasp_cover import (
    GraspCover,
)

from lottery_optimizer.reduction.reduction_rules import (
    ReductionRules,
)


def build_rules():

    return ReductionRules(

        universe_size=25,

        source_size=21,

        target_size=15,

        n_games=5,

        guarantee=13,

    )


def test_reduce():

    reducer = GraspCover(

        LOTOFACIL,

        build_rules(),

        seed=123,

    )

    pop = reducer.reduce(

        range(1,22),

    )

    assert pop.size == 5


def test_choose():

    reducer = GraspCover(

        LOTOFACIL,

        build_rules(),

        seed=1,

    )

    assert reducer.alpha == 0.20