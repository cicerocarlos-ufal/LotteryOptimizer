from lottery_optimizer.app.load_config import (
    build_rules,
)


def test_build_rules():

    rules = build_rules()

    assert rules.source_size == 21

    assert rules.target_size == 15

    assert rules.n_games == 50

    assert rules.guarantee == 13