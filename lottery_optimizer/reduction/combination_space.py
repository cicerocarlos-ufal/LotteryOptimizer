"""
Lottery Optimizer

Lazy combination generator.
"""

from __future__ import annotations

from itertools import combinations
from math import comb
import random

from lottery_optimizer.core.game import Game
from lottery_optimizer.core.lottery_rules import LotteryRules


class CombinationSpace:

    """
    Lazy combination space.

    Never stores all combinations in memory.
    """

    def __init__(
        self,
        rules: LotteryRules,
        source_numbers,
        target_size: int,
    ) -> None:

        self.rules = rules

        self.source_numbers = tuple(sorted(source_numbers))

        self.target_size = target_size

    # -----------------------------------------------------

    @property
    def size(self) -> int:

        return comb(

            len(self.source_numbers),

            self.target_size,

        )

    # -----------------------------------------------------

    def __len__(self):

        return self.size

    # -----------------------------------------------------

    def __iter__(self):

        for values in combinations(

            self.source_numbers,

            self.target_size,

        ):

            yield Game.from_numbers(

                self.rules,

                values,

            )

    # -----------------------------------------------------

    def random_game(

        self,

        rng=None,

    ):

        if rng is None:

            rng = random.Random()

        values = rng.sample(

            self.source_numbers,

            self.target_size,

        )

        values.sort()

        return Game.from_numbers(

            self.rules,

            values,

        )

    # -----------------------------------------------------

    def sample(

        self,

        n,

        rng=None,

    ):

        if rng is None:

            rng = random.Random()

        seen = set()

        while len(seen) < n:

            game = self.random_game(rng)

            seen.add(game)

        return list(seen)