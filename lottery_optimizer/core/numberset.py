"""
Lottery Optimizer

Core NumberSet class.

Immutable mathematical representation of a lottery number set.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property
from typing import Iterable, Iterator

from lottery_optimizer.core.lottery_rules import LotteryRules


@dataclass(frozen=True)
class NumberSet:
    """
    Immutable set of lottery numbers.

    This class is the mathematical basis for
    Game and Draw.

    Internally it stores only a bit mask.
    """

    rules: LotteryRules

    _mask: int

    # ==========================================================
    # Constructors
    # ==========================================================

    @classmethod
    def from_numbers(
        cls,
        rules: LotteryRules,
        numbers: Iterable[int],
    ) -> "NumberSet":

        values = rules.validate(numbers)

        return cls(
            rules=rules,
            _mask=rules.mask(values),
        )

    @classmethod
    def from_mask(
        cls,
        rules: LotteryRules,
        mask: int,
    ) -> "NumberSet":

        rules.validate_mask(mask)

        return cls(
            rules=rules,
            _mask=mask,
        )

    # ==========================================================
    # Basic properties
    # ==========================================================

    @property
    def mask(self) -> int:
        """
        Bit mask representation.
        """
        return self._mask

    @cached_property
    def numbers(self) -> tuple[int, ...]:
        """
        Ordered numbers.
        """
        return self.rules.numbers_from_mask(
            self._mask
        )

    @property
    def size(self) -> int:
        """
        Number of selected values.
        """
        return self._mask.bit_count()

    @cached_property
    def minimum(self) -> int:

        return self.numbers[0]

    @cached_property
    def maximum(self) -> int:

        return self.numbers[-1]

    @cached_property
    def total(self) -> int:

        return sum(self.numbers)

    @cached_property
    def even(self) -> int:

        return sum(
            n % 2 == 0
            for n in self.numbers
        )

    @cached_property
    def odd(self) -> int:

        return self.size - self.even

    # ==========================================================
    # Membership
    # ==========================================================

    def contains(
        self,
        number: int,
    ) -> bool:

        if number not in self.rules:

            return False

        bit = 1 << (
            number - self.rules.minimum
        )

        return bool(
            self._mask & bit
        )

    def __contains__(
        self,
        number: int,
    ) -> bool:

        return self.contains(number)

    # ==========================================================
    # Conversion
    # ==========================================================

    def to_list(self) -> list[int]:

        return list(self.numbers)

    def to_tuple(self) -> tuple[int, ...]:

        return self.numbers

    def to_set(self) -> set[int]:

        return set(self.numbers)

    # ==========================================================
    # Set operations
    # ==========================================================

    def intersection_mask(
        self,
        other: "NumberSet",
    ) -> int:

        self._check_rules(other)

        return self._mask & other._mask

    def union_mask(
        self,
        other: "NumberSet",
    ) -> int:

        self._check_rules(other)

        return self._mask | other._mask

    def xor_mask(
        self,
        other: "NumberSet",
    ) -> int:

        self._check_rules(other)

        return self._mask ^ other._mask

    # ==========================================================
    # Cardinalities
    # ==========================================================

    def intersection_size(
        self,
        other: "NumberSet",
    ) -> int:

        return self.intersection_mask(
            other
        ).bit_count()

    def union_size(
        self,
        other: "NumberSet",
    ) -> int:

        return self.union_mask(
            other
        ).bit_count()

    def symmetric_difference_size(
        self,
        other: "NumberSet",
    ) -> int:

        return self.xor_mask(
            other
        ).bit_count()

    def hamming_distance(
        self,
        other: "NumberSet",
    ) -> int:

        return self.symmetric_difference_size(
            other
        )

    # ==========================================================
    # Number operations
    # ==========================================================

    def intersection(
        self,
        other: "NumberSet",
    ) -> tuple[int, ...]:

        self._check_rules(other)

        return tuple(
            n
            for n in self.numbers
            if other.contains(n)
        )

    def difference(
        self,
        other: "NumberSet",
    ) -> tuple[int, ...]:

        self._check_rules(other)

        return tuple(
            n
            for n in self.numbers
            if not other.contains(n)
        )

    def symmetric_difference(
        self,
        other: "NumberSet",
    ) -> tuple[int, ...]:

        self._check_rules(other)

        return tuple(
            sorted(
                set(self.numbers)
                ^
                set(other.numbers)
            )
        )

    # ==========================================================
    # Relations
    # ==========================================================

    def overlaps(
        self,
        other: "NumberSet",
    ) -> bool:

        return self.intersection_size(
            other
        ) > 0

    def disjoint(
        self,
        other: "NumberSet",
    ) -> bool:

        return self.intersection_size(
            other
        ) == 0

    def is_subset(
        self,
        other: "NumberSet",
    ) -> bool:

        self._check_rules(other)

        return (
            self._mask & other._mask
        ) == self._mask

    def is_superset(
        self,
        other: "NumberSet",
    ) -> bool:

        self._check_rules(other)

        return (
            self._mask | other._mask
        ) == self._mask
    # ==========================================================
    # Special methods
    # ==========================================================

    def __len__(self) -> int:
        """
        Number of selected values.
        """
        return self.size

    def __iter__(self) -> Iterator[int]:
        """
        Iterate over numbers in ascending order.
        """
        return iter(self.numbers)

    def __hash__(self) -> int:
        """
        Hash based on lottery and bit mask.
        """
        return hash(
            (
                self.rules.name,
                self._mask,
            )
        )

    def __eq__(
        self,
        other: object,
    ) -> bool:

        if not isinstance(other, NumberSet):
            return NotImplemented

        return (
            self.rules == other.rules
            and
            self._mask == other._mask
        )

    def __lt__(
        self,
        other: "NumberSet",
    ) -> bool:

        self._check_rules(other)

        return self.numbers < other.numbers

    def __le__(
        self,
        other: "NumberSet",
    ) -> bool:

        self._check_rules(other)

        return self.numbers <= other.numbers

    def __gt__(
        self,
        other: "NumberSet",
    ) -> bool:

        self._check_rules(other)

        return self.numbers > other.numbers

    def __ge__(
        self,
        other: "NumberSet",
    ) -> bool:

        self._check_rules(other)

        return self.numbers >= other.numbers

    # ==========================================================
    # Mathematical operators
    # ==========================================================

    def __and__(
        self,
        other: "NumberSet",
    ) -> int:
        """
        Number of common elements.
        """
        return self.intersection_size(other)

    def __or__(
        self,
        other: "NumberSet",
    ) -> int:
        """
        Union size.
        """
        return self.union_size(other)

    def __xor__(
        self,
        other: "NumberSet",
    ) -> int:
        """
        Hamming distance.
        """
        return self.hamming_distance(other)

    # ==========================================================
    # Export
    # ==========================================================

    def to_csv(self) -> str:
        """
        CSV representation.
        """
        return ",".join(
            str(n)
            for n in self.numbers
        )

    def to_txt(self) -> str:
        """
        Human readable representation.
        """
        return " ".join(
            f"{n:02d}"
            for n in self.numbers
        )

    def __str__(self) -> str:

        return self.to_txt()

    def __repr__(self) -> str:

        return (
            f"{self.__class__.__name__}"
            f"({self.to_txt()})"
        )
    # ==========================================================
    # Internal methods
    # ==========================================================

    def _check_rules(
        self,
        other: "NumberSet",
    ) -> None:
        """
        Ensures both objects belong to the same lottery.
        """

        if self.rules != other.rules:

            raise ValueError(
                "Both NumberSet objects must use the same LotteryRules."
            )

    # ==========================================================
    # Utilities
    # ==========================================================

    def copy(self) -> "NumberSet":
        """
        NumberSet is immutable.

        Returns itself.
        """

        return self

    def clone(self) -> "NumberSet":
        """
        Alias of copy().
        """

        return self

    # ==========================================================
    # Statistics
    # ==========================================================

    @property
    def mean(self) -> float:
        """
        Arithmetic mean.
        """

        return self.total / self.size

    @property
    def range(self) -> int:
        """
        Difference between largest and smallest number.
        """

        return self.maximum - self.minimum

    @property
    def consecutive_pairs(self) -> int:
        """
        Number of consecutive pairs.

        Example

        1 2
        7 8
        20 21
        """

        values = self.numbers

        total = 0

        for i in range(len(values) - 1):

            if values[i + 1] == values[i] + 1:

                total += 1

        return total

    # ==========================================================
    # Summary
    # ==========================================================

    def summary(self) -> dict:
        """
        Returns a summary of the object.
        """

        return {

            "numbers": self.to_list(),

            "mask": self.mask,

            "size": self.size,

            "sum": self.total,

            "minimum": self.minimum,

            "maximum": self.maximum,

            "even": self.even,

            "odd": self.odd,

            "mean": self.mean,

            "range": self.range,

            "consecutive_pairs": self.consecutive_pairs,

        }

    def to_dict(self) -> dict:
        """
        Dictionary representation.
        """

        return self.summary()

    # ==========================================================
    # Boolean
    # ==========================================================

    def __bool__(self) -> bool:
        """
        A NumberSet is always valid.

        Therefore it is always True.
        """

        return True
# ==========================================================
# End of NumberSet
# ==========================================================                        

