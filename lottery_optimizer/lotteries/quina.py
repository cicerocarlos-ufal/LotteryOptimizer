"""
Lottery Optimizer

Quina rules.
"""

from lottery_optimizer.core.lottery_rules import LotteryRules


QUINA = LotteryRules(

    name="Quina",

    total_numbers=80,

    numbers_per_draw=5,

    min_number=1,

    max_number=80,

)