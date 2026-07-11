from lottery_optimizer.engine.pipeline import (
    ReductionPipeline,
)

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


def test_pipeline():

    engine = ReductionEngine(

        LOTOFACIL,

        build_rules(),

    )

    pipeline = ReductionPipeline(

        engine,

    )

    result = pipeline.run(

        range(1,22),

        algorithm="greedy",

    )

    assert result["games"] == 5

    assert result["elapsed"] >= 0