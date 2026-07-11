"""
Lottery Optimizer

Coverage Index.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations

from lottery_optimizer.core.game import Game


class CoverageIndex:
    """
    Incremental coverage index.

    Stores how many times each guarantee subset
    is covered.
    """

    def __init__(

        self,

        guarantee: int,

    ) -> None:

        self.guarantee = guarantee

        #
        # subset -> count
        #

        self._counter = defaultdict(int)

        self.covered = 0

    # -----------------------------------------------------

    def clear(self):

        self._counter.clear()

        self.covered = 0

    # -----------------------------------------------------

    def add(

        self,

        game: Game,

    ) -> int:

        gain = 0

        for subset in combinations(

            game.numbers,

            self.guarantee,

        ):

            if self._counter[subset] == 0:

                gain += 1

                self.covered += 1

            self._counter[subset] += 1

        return gain

    # -----------------------------------------------------

    def remove(

        self,

        game: Game,

    ) -> int:

        loss = 0

        for subset in combinations(

            game.numbers,

            self.guarantee,

        ):

            self._counter[subset] -= 1

            if self._counter[subset] == 0:

                del self._counter[subset]

                self.covered -= 1

                loss += 1

        return loss

    # -----------------------------------------------------

    def gain(

        self,

        game: Game,

    ) -> int:
        """
        Calculates gain WITHOUT
        modifying the index.
        """

        gain = 0

        for subset in combinations(

            game.numbers,

            self.guarantee,

        ):

            if subset not in self._counter:

                gain += 1

        return gain

    # -----------------------------------------------------

    def contains(

        self,

        subset,

    ) -> bool:

        return subset in self._counter

    # -----------------------------------------------------

    def __len__(self):

        return self.covered

    def __repr__(self):

        return (

            f"CoverageIndex({self.covered})"

        )