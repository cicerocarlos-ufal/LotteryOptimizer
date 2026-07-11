"""
Lottery Optimizer

Game object.
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Iterable

from lottery_optimizer.core.numberset import NumberSet
from lottery_optimizer.core.lottery_rules import LotteryRules


@dataclass(frozen=True)
class Game(NumberSet):
    """
    Represents a candidate lottery game.
    """

    @classmethod
    def from_numbers(
        cls,
        rules: LotteryRules,
        numbers: Iterable[int],
    ) -> "Game":

        values = rules.validate(numbers)

        return cls(
            rules=rules,
            _mask=rules.mask(values),
        )

    @classmethod
    def random(
        cls,
        rules: LotteryRules,
        rng: random.Random | None = None,
    ) -> "Game":

        if rng is None:
            rng = random.Random()

        numbers = rng.sample(
            rules.numbers,
            rules.draw_size,
        )

        return cls.from_numbers(
            rules,
            numbers,
        )

    def clone(self) -> "Game":

        return Game.from_mask(
            self.rules,
            self.mask,
        )
    # ==========================================================
    # Basic manipulation
    # ==========================================================

    def add(
        self,
        number: int,
    ) -> "Game":

        if number in self:
            return self

        values = set(self.numbers)
        values.add(number)

        if len(values) != self.rules.draw_size:
            raise ValueError(
                "Game size would become invalid."
            )

        return Game.from_numbers(
            self.rules,
            values,
        )

    def remove(
        self,
        number: int,
    ) -> "Game":

        if number not in self:
            return self

        values = set(self.numbers)
        values.remove(number)

        if len(values) != self.rules.draw_size:
            raise ValueError(
                "Game size would become invalid."
            )

        return Game.from_numbers(
            self.rules,
            values,
        )
    # ==========================================================
    # Neighborhood
    # ==========================================================

    def swap(
        self,
        remove: int,
        add: int,
    ) -> "Game":
        """
        Removes one number and adds another.

        Returns a new Game.
        """

        if remove not in self:
            raise ValueError(
                f"{remove} is not in the game."
            )

        if add in self:
            raise ValueError(
                f"{add} is already in the game."
            )

        if add not in self.rules:
            raise ValueError(
                f"{add} is not a valid number."
            )

        values = set(self.numbers)

        values.remove(remove)

        values.add(add)

        return Game.from_numbers(
            self.rules,
            values,
        )

    def neighbors(self):
        """
        Generates all neighbors with
        one swap.
        """

        outside = [

            n

            for n in self.rules.numbers

            if n not in self

        ]

        for remove in self.numbers:

            for add in outside:

                yield self.swap(
                    remove,
                    add,
                )

    def random_neighbor(
        self,
        rng: random.Random | None = None,
    ) -> "Game":
        """
        Returns one random neighbor.
        """

        if rng is None:

            rng = random.Random()

        remove = rng.choice(
            self.numbers
        )

        outside = [

            n

            for n in self.rules.numbers

            if n not in self

        ]

        add = rng.choice(outside)

        return self.swap(
            remove,
            add,
        )
    # ==========================================================
    # Mutation
    # ==========================================================

    def mutate(
        self,
        n_swaps: int = 1,
        rng: random.Random | None = None,
    ) -> "Game":
        """
        Performs one or more random swaps.
        """

        if rng is None:

            rng = random.Random()

        game = self

        for _ in range(n_swaps):

            game = game.random_neighbor(rng)

        return game
    # ==========================================================
    # Genetic operators
    # ==========================================================

    def crossover(
        self,
        other: "Game",
        rng: random.Random | None = None,
    ) -> "Game":
        """
        Uniform crossover.
        """

        self._check_rules(other)

        if rng is None:
            rng = random.Random()

        child = set()

        for n in self.numbers:

            if rng.random() < 0.5:
                child.add(n)

        for n in other.numbers:

            if rng.random() < 0.5:
                child.add(n)

        # completa caso faltem dezenas
        while len(child) < self.rules.draw_size:

            child.add(

                rng.choice(

                    tuple(

                        n

                        for n in self.rules.numbers

                        if n not in child

                    )

                )

            )

        # remove excedentes
        while len(child) > self.rules.draw_size:

            child.remove(

                rng.choice(

                    tuple(child)

                )

            )

        return Game.from_numbers(

            self.rules,

            child,

        )

    # ==========================================================
    # Utilities
    # ==========================================================

    def distance(
        self,
        other: "Game",
    ) -> int:
        """
        Alias para Hamming Distance.
        """

        return self.hamming_distance(other)

    def is_valid(self) -> bool:
        """
        Verifica consistência do jogo.
        """

        try:

            self.rules.validate(

                self.numbers

            )

            return True

        except ValueError:

            return False

    def __repr__(self) -> str:

        return (

            f"Game({self.to_txt()})"

        )
                                        