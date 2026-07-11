from lottery_optimizer.lotteries.lotofacil import LOTOFACIL

from lottery_optimizer.reduction.hill_cover import HillCover

from lottery_optimizer.reduction.reduction_rules import ReductionRules


def build_rules():

    return ReductionRules(

        universe_size=25,

        source_size=21,

        target_size=15,

        n_games=5,

        guarantee=13,

    )


def test_reduce():

    reducer = HillCover(

        LOTOFACIL,

        build_rules(),

        seed=1,

    )

    pop = reducer.reduce(

        range(1,22),

    )

    assert pop.size == 5


def test_score():

    reducer = HillCover(

        LOTOFACIL,

        build_rules(),

    )

    pop = reducer.reduce(

        range(1,22),

    )

    assert reducer.score(pop) > 0