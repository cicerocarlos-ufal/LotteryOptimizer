from lottery_optimizer.reduction.reduction_rules import (
    ReductionRules,
)


def test_creation():

    rules = ReductionRules(

        universe_size=25,

        source_size=21,

        target_size=15,

        n_games=50,

        guarantee=13,

    )

    assert rules.universe_size == 25

    assert rules.source_size == 21

    assert rules.target_size == 15

    assert rules.n_games == 50

    assert rules.guarantee == 13