"""
Lottery Optimizer

Quina rules.
"""

from lottery_optimizer.core.lottery_rules import LotteryRules


REDUCAO = LotteryRules(

    name="Reducao",

    total_numbers=12,

    numbers_per_draw=7,

    min_number=1,

    max_number=12,

)