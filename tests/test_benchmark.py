from lottery_optimizer.engine.benchmark import Benchmark

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


def test_benchmark():

    benchmark = Benchmark(

        LOTOFACIL,

        build_rules(),

    )

    results = benchmark.run(

        range(1,22),

        algorithms=[

            "greedy",

            "hill",

        ],

        seed=1,

    )

    assert len(results) == 2

    assert results[0]["games"] == 5

    assert results[1]["games"] == 5