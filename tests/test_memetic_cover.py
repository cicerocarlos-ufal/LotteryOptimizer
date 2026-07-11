from lottery_optimizer.lotteries.lotofacil import LOTOFACIL

from lottery_optimizer.reduction.memetic_cover import (
    MemeticCover,
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

    reducer = MemeticCover(

        LOTOFACIL,

        build_rules(),

        population_size=10,

        generations=5,

        seed=123,

    )

    pop = reducer.reduce(

        range(1,22),

    )

    assert pop.size == 5


def test_probability():

    reducer = MemeticCover(

        LOTOFACIL,

        build_rules(),

    )

    assert reducer.local_search_probability == 0.30