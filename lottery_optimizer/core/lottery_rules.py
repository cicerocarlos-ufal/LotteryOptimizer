"""
Lottery Optimizer

Core definitions for lottery rules.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True, slots=True)
class LotteryRules:
    """
    Defines the rules of a lottery.
    """

    name: str
    total_numbers: int
    draw_size: int
    minimum: int = 1
    maximum: int | None = None

    def __post_init__(self) -> None:

        if self.maximum is None:
            object.__setattr__(
                self,
                "maximum",
                self.minimum + self.total_numbers - 1,
            )

        if self.total_numbers <= 0:
            raise ValueError("total_numbers must be greater than zero.")

        if self.draw_size <= 0:
            raise ValueError("draw_size must be greater than zero.")

        if self.draw_size > self.total_numbers:
            raise ValueError("draw_size cannot be greater than total_numbers.")

        if self.minimum > self.maximum:
            raise ValueError("minimum cannot be greater than maximum.")

        expected = self.maximum - self.minimum + 1

        if expected != self.total_numbers:
            raise ValueError(
                "minimum/maximum interval is inconsistent with total_numbers."
            )

    @property
    def numbers(self) -> tuple[int, ...]:
        """
        Valid numbers of the lottery.
        """

        return tuple(
            range(
                self.minimum,
                self.maximum + 1,
            )
        )

    def contains(
        self,
        number: int,
    ) -> bool:

        return self.minimum <= number <= self.maximum

    def validate(
        self,
        numbers: Iterable[int],
    ) -> tuple[int, ...]:

        values = tuple(sorted(set(numbers)))

        if len(values) != self.draw_size:
            raise ValueError(
                f"Expected {self.draw_size} unique numbers."
            )

        for n in values:

            if not self.contains(n):
                raise ValueError(
                    f"Invalid number: {n}"
                )

        return values

    def mask(
        self,
        numbers: Iterable[int],
    ) -> int:
        """
        Converts a sequence of numbers into a bit mask.
        """

        values = self.validate(numbers)

        mask = 0

        for n in values:
            mask |= 1 << (n - self.minimum)

        return mask

    def numbers_from_mask(
        self,
        mask: int,
    ) -> tuple[int, ...]:
        """
        Converts a mask into numbers.
        """

        result = []

        bit = 1

        for n in self.numbers:

            if mask & bit:
                result.append(n)

            bit <<= 1

        return tuple(result)

    def validate_mask(
        self,
        mask: int,
    ) -> int:

        if mask.bit_count() != self.draw_size:
            raise ValueError("Invalid mask.")

        return mask

    def __contains__(
        self,
        number: int,
    ) -> bool:

        return self.contains(number)

    def __len__(self) -> int:

        return self.total_numbers

    def __repr__(self) -> str:

        return (
            f"{self.name}"
            f"(N={self.total_numbers}, "
            f"K={self.draw_size})"
        )
