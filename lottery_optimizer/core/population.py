"""
Lottery Optimizer

Population of candidate games.
"""

from __future__ import annotations

import random
from typing import Iterable, Iterator

from lottery_optimizer.core.game import Game
from lottery_optimizer.core.lottery_rules import LotteryRules


class Population:

    def __init__(
        self,
        rules: LotteryRules,
        games: Iterable[Game] | None = None,
    ) -> None:

        self.rules = rules

        self._games: list[Game] = []

        if games is not None:

            self.extend(games)

    # ---------------------------------------------------------

    def add(
        self,
        game: Game,
    ) -> None:

        if game.rules != self.rules:

            raise ValueError(
                "Game belongs to another lottery."
            )

        self._games.append(game)

    # ---------------------------------------------------------

    def extend(
        self,
        games: Iterable[Game],
    ) -> None:

        for game in games:

            self.add(game)

    # ---------------------------------------------------------

    def clear(self) -> None:

        self._games.clear()

    # ---------------------------------------------------------

    @property
    def size(self) -> int:

        return len(self._games)

    # ---------------------------------------------------------

    @property
    def games(self) -> tuple[Game, ...]:

        return tuple(self._games)

    # ---------------------------------------------------------

    def random(
        self,
        rng: random.Random | None = None,
    ) -> Game:

        if not self._games:

            raise ValueError(
                "Population is empty."
            )

        if rng is None:

            rng = random.Random()

        return rng.choice(self._games)

    # ---------------------------------------------------------

    def sample(
        self,
        k: int,
        rng: random.Random | None = None,
    ) -> list[Game]:

        if rng is None:

            rng = random.Random()

        return rng.sample(self._games, k)

    # ---------------------------------------------------------

    def unique(self) -> "Population":

        seen = set()

        result = Population(self.rules)

        for game in self._games:

            if game.mask not in seen:

                seen.add(game.mask)

                result.add(game)

        return result

    # ---------------------------------------------------------

    def sort(self) -> None:

        self._games.sort()

    # ---------------------------------------------------------

    def shuffle(
        self,
        rng: random.Random | None = None,
    ) -> None:

        if rng is None:

            rng = random.Random()

        rng.shuffle(self._games)

    # ---------------------------------------------------------

    def frequency(self) -> dict[int, int]:

        freq = {

            n: 0

            for n in self.rules.numbers

        }

        for game in self._games:

            for n in game:

                freq[n] += 1

        return freq

    # ---------------------------------------------------------

    def masks(self) -> list[int]:

        return [

            g.mask

            for g in self._games

        ]

    # ---------------------------------------------------------

    def __len__(self) -> int:

        return self.size

    def __iter__(self) -> Iterator[Game]:

        return iter(self._games)

    def __getitem__(
        self,
        index: int,
    ) -> Game:

        return self._games[index]

    def __repr__(self) -> str:

        return (

            f"Population({self.size} games)"

        )