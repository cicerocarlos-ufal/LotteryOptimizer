from lottery_optimizer.engine.reduction_engine import (
    ReductionEngine,
)

from lottery_optimizer.reduction.reduction_rules import (
    ReductionRules,
)

from lottery_optimizer.lotteries.lotofacil import (
    LOTOFACIL,
)


def build_rules():

    return ReductionRules(

        universe_size=25,

        source_size=21,

        target_size=15,

        n_games=5,

        guarantee=13,

    )


def test_genetic():

    engine = ReductionEngine(

        LOTOFACIL,

        build_rules(),

    )

    pop = engine.reduce(

        range(1,22),

        algorithm="genetic",

        generations=3,

        population_size=6,

        seed=1,

    )

    assert pop.size == 5


def test_greedy():

    engine = ReductionEngine(

        LOTOFACIL,

        build_rules(),

    )

    pop = engine.reduce(

        range(1,22),

        algorithm="greedy",

    )

    assert pop.size == 5


def test_hill():

    engine = ReductionEngine(

        LOTOFACIL,

        build_rules(),

    )

    pop = engine.reduce(

        range(1,22),

        algorithm="hill",

        seed=1,

    )

    assert pop.size == 5