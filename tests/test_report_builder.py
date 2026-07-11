from lottery_optimizer.lotteries.lotofacil import LOTOFACIL

from lottery_optimizer.core.population import Population
from lottery_optimizer.core.game import Game

from lottery_optimizer.report.report_builder import ReportBuilder

from lottery_optimizer.reduction.reduction_rules import (
    ReductionRules,
)


def test_builder():

    numbers = [

        2,4,5,6,8,

        9,10,12,13,15,

        17,18,19,20,21,

        22,23,24,25,1,7,

    ]

    rules = ReductionRules(

        universe_size=25,

        source_size=len(numbers),

        target_size=15,

        n_games=5,

        guarantee=13,

    )

    pop = Population(

        LOTOFACIL,

    )

    pop.add(

        Game.from_numbers(

            LOTOFACIL,

            numbers[:15],

        )

    )

    report = ReportBuilder.build(

        lottery=LOTOFACIL,

        rules=rules,

        source_numbers=numbers,

        population=pop,

        elapsed=1.0,

        algorithm="greedy",

        seed=123,

    )

    assert report.games == 1

    assert report.source_size == 21

    assert report.target > 0

    assert report.coverage > 0

    assert report.seed == 123