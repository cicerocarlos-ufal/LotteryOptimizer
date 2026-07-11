"""
Lottery Optimizer

Configuration Loader.
"""

from lottery_optimizer.app import config

from lottery_optimizer.reduction.reduction_rules import (
    ReductionRules,
)


def build_rules():

    return ReductionRules(

        universe_size=config.LOTTERY.total_numbers,

        source_size=len(config.SOURCE_NUMBERS),

        target_size=config.TARGET_SIZE,

        n_games=config.N_GAMES,

        guarantee=config.GUARANTEE,

    )