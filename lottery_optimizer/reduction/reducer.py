"""
Lottery Optimizer

Base class for reduction algorithms.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from lottery_optimizer.core.lottery_rules import LotteryRules
from lottery_optimizer.reduction.reduction_rules import ReductionRules


class Reducer(ABC):

    def __init__(
        self,
        lottery: LotteryRules,
        rules: ReductionRules,
    ) -> None:

        self.lottery = lottery
        self.rules = rules

    @abstractmethod
    def reduce(self, numbers):
        """
        Performs the reduction.

        Parameters
        ----------
        numbers
            Numbers selected by the user.

        Returns
        -------
        Population
        """
        raise NotImplementedError