"""
Lottery Optimizer

Draw object.

Represents one official lottery draw.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Iterable

from lottery_optimizer.core.numberset import NumberSet
from lottery_optimizer.core.lottery_rules import LotteryRules


@dataclass(frozen=True)
class Draw(NumberSet):
    """
    Represents an official lottery draw.

    Attributes
    ----------
    contest
        Contest number.

    draw_date
        Official draw date.
    """

    contest: int = 0

    draw_date: date | None = None

    @classmethod
    def from_numbers(
        cls,
        rules: LotteryRules,
        numbers: Iterable[int],
        contest: int = 0,
        draw_date: date | None = None,
    ) -> "Draw":
        """
        Creates a Draw from a sequence of numbers.
        """

        values = rules.validate(numbers)

        return cls(
            rules=rules,
            _mask=rules.mask(values),
            contest=contest,
            draw_date=draw_date,
        )

    @property
    def year(self) -> int | None:
        """
        Draw year.
        """

        if self.draw_date is None:
            return None

        return self.draw_date.year

    @property
    def month(self) -> int | None:
        """
        Draw month.
        """

        if self.draw_date is None:
            return None

        return self.draw_date.month

    @property
    def day(self) -> int | None:
        """
        Draw day.
        """

        if self.draw_date is None:
            return None

        return self.draw_date.day

    def is_official(self) -> bool:
        """
        Returns True if the draw has
        contest number greater than zero.
        """

        return self.contest > 0

    def to_dict(self) -> dict:
        """
        Dictionary representation.
        """

        return {

            "contest": self.contest,

            "date": (
                self.draw_date.isoformat()
                if self.draw_date
                else None
            ),

            "numbers": self.to_list(),

            "mask": self.mask,

            "sum": self.total,

            "even": self.even,

            "odd": self.odd,

        }

    def __repr__(self) -> str:

        if self.draw_date is None:

            return (
                f"Draw(contest={self.contest}, "
                f"numbers={self.to_txt()})"
            )

        return (

            f"Draw(contest={self.contest}, "
            f"date={self.draw_date.isoformat()}, "
            f"numbers={self.to_txt()})"

        )