"""
Lottery Optimizer

Coverage Engine.
"""

from __future__ import annotations

from itertools import combinations

from lottery_optimizer.core.game import Game


class Coverage:

    """
    Incremental coverage calculator.
    """

    def __init__(

        self,

        guarantee: int,

    ) -> None:

        self.guarantee = guarantee

        self._covered = set()

    # ---------------------------------------------------------

    @property
    def covered(self) -> int:

        return len(self._covered)

    # ---------------------------------------------------------

    def clear(self):

        self._covered.clear()

    # ---------------------------------------------------------

    def add(

        self,

        game: Game,

    ) -> int:
        """
        Adds one game.

        Returns the number of NEW subsets covered.
        """

        before = len(self._covered)

        for subset in combinations(

            game.numbers,

            self.guarantee,

        ):

            self._covered.add(subset)

        return len(self._covered) - before

    # ---------------------------------------------------------

    def remove(

        self,

        game: Game,

    ):

        raise NotImplementedError(

            "Incremental remove will be implemented later."

        )

    # ---------------------------------------------------------

    def evaluate(

        self,

        games,

    ) -> int:

        self.clear()

        for game in games:

            self.add(game)

        return self.covered

    # ---------------------------------------------------------

    def copy(self):

        other = Coverage(

            self.guarantee,

        )

        other._covered = self._covered.copy()

        return other

    # ---------------------------------------------------------

    def __len__(self):

        return self.covered

    # ---------------------------------------------------------

    def __repr__(self):

        return (

            f"Coverage({self.covered})"

        )