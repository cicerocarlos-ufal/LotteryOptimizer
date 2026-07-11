"""
Official Lotofácil rules.
"""

from lottery_optimizer.core.lottery_rules import LotteryRules

LOTOFACIL = LotteryRules(
    name="Lotofácil",
    total_numbers=25,
    draw_size=15,
    minimum=1,
    maximum=25,
)
