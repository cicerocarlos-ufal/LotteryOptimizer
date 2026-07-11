"""
Lottery Optimizer

History of official draws.
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable, Iterator

from lottery_optimizer.core.draw import Draw
from lottery_optimizer.core.lottery_rules import LotteryRules


class History:
    """
    Collection of official lottery draws.
    """

    def __init__(
        self,
        rules: LotteryRules,
        draws: Iterable[Draw] | None = None,
    ) -> None:

        self.rules = rules

        self._draws: list[Draw] = []

        if draws is not None:

            for draw in draws:

                self.add(draw)

    # ---------------------------------------------------------

    def add(
        self,
        draw: Draw,
    ) -> None:

        if draw.rules != self.rules:

            raise ValueError(
                "Draw belongs to another lottery."
            )

        self._draws.append(draw)

    # ---------------------------------------------------------

    def extend(
        self,
        draws: Iterable[Draw],
    ) -> None:

        for draw in draws:

            self.add(draw)

    # ---------------------------------------------------------

    @property
    def draws(self) -> tuple[Draw, ...]:

        return tuple(self._draws)

    # ---------------------------------------------------------

    @property
    def size(self) -> int:

        return len(self._draws)

    # ---------------------------------------------------------

    def contests(self) -> list[int]:

        return [

            d.contest

            for d in self._draws

        ]

    # ---------------------------------------------------------

    def latest(self) -> Draw | None:

        if not self._draws:

            return None

        return max(

            self._draws,

            key=lambda d: d.contest,

        )

    # ---------------------------------------------------------

    def get(
        self,
        contest: int,
    ) -> Draw | None:

        for draw in self._draws:

            if draw.contest == contest:

                return draw

        return None

    # ---------------------------------------------------------

    def load_csv(
        self,
        filename: str | Path,
    ) -> None:
        """
        Expected format

        contest,n1,n2,...,n15
        """

        with open(

            filename,

            newline="",

            encoding="utf8",

        ) as f:

            reader = csv.reader(f)

            next(reader)

            for row in reader:

                contest = int(row[0])

                numbers = list(

                    map(

                        int,

                        row[1:1 + self.rules.draw_size],

                    )

                )

                self.add(

                    Draw.from_numbers(

                        self.rules,

                        numbers,

                        contest=contest,

                    )

                )

    # ---------------------------------------------------------

    def __len__(self) -> int:

        return self.size

    def __iter__(self) -> Iterator[Draw]:

        return iter(self._draws)

    def __getitem__(

        self,

        index: int,

    ) -> Draw:

        return self._draws[index]

    def __repr__(self) -> str:

        return (

            f"History({self.size} draws)"

        )