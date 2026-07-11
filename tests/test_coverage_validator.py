from lottery_optimizer.validation.coverage_validator import (
    CoverageValidator,
)

from lottery_optimizer.core.population import Population
from lottery_optimizer.core.game import Game

from lottery_optimizer.lotteries.lotofacil import LOTOFACIL


def test_validator():

    numbers = list(range(1,22))

    pop = Population(

        LOTOFACIL,

    )

    pop.add(

        Game.from_numbers(

            LOTOFACIL,

            numbers[:15],

        )

    )

    validator = CoverageValidator(

        guarantee=13,

    )

    result = validator.validate(

        numbers,

        pop,

    )

    assert result.total > 0

    assert result.covered > 0

    assert result.uncovered >= 0

    assert 0.0 <= result.coverage <= 1.0