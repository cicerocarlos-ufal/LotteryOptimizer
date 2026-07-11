from lottery_optimizer.lotteries.lotofacil import LOTOFACIL

from lottery_optimizer.reduction.cpsat_cover import (
    CPSATCover,
)

from lottery_optimizer.reduction.reduction_rules import (
    ReductionRules,
)


def build_rules():

    return ReductionRules(

        universe_size=25,

        source_size=17,

        target_size=15,

        n_games=2,

        guarantee=13,

    )


def test_reduce():

    reducer = CPSATCover(

        LOTOFACIL,

        build_rules(),

        time_limit=5,

    )

    pop = reducer.reduce(

        range(1,18),

    )

    assert pop.size == 2


def test_workers():

    reducer = CPSATCover(

        LOTOFACIL,

        build_rules(),

        workers=4,

    )

    assert reducer.workers == 4