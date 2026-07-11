"""
Lottery Optimizer

Reduction Engine.
"""

from __future__ import annotations

import inspect

from lottery_optimizer.reduction.greedy_cover import GreedyCover
from lottery_optimizer.reduction.grasp_cover import GraspCover
from lottery_optimizer.reduction.hill_cover import HillCover
from lottery_optimizer.reduction.genetic_cover import GeneticCover
from lottery_optimizer.reduction.memetic_cover import MemeticCover
from lottery_optimizer.reduction.cpsat_cover import CPSATCover


class ReductionEngine:

    ALGORITHMS = {
        "greedy": GreedyCover,
        "grasp": GraspCover,
        "hill": HillCover,
        "genetic": GeneticCover,
        "memetic": MemeticCover,
        "cpsat": CPSATCover,
    }

    def __init__(
        self,
        lottery,
        rules,
    ):

        self.lottery = lottery
        self.rules = rules

    # ---------------------------------------------------------

    def _build_reducer(
        self,
        cls,
        kwargs,
    ):
        """
        Instantiate a reducer passing only the
        parameters accepted by its constructor.
        """

        signature = inspect.signature(cls.__init__)

        accepted = {}

        for name in signature.parameters:

            if name in ("self", "lottery", "rules"):
                continue

            if name in kwargs:
                accepted[name] = kwargs[name]

        return cls(
            self.lottery,
            self.rules,
            **accepted,
        )

    # ---------------------------------------------------------

    def reduce(
        self,
        numbers,
        algorithm="genetic",
        **kwargs,
    ):

        cls = self.ALGORITHMS[algorithm]

        reducer = self._build_reducer(
            cls,
            kwargs,
        )

        return reducer.reduce(numbers)