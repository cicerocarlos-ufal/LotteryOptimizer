from lottery_optimizer.core.game import Game
from lottery_optimizer.core.population import Population
from lottery_optimizer.lotteries.lotofacil import LOTOFACIL


def test_population():

    pop = Population(LOTOFACIL)

    pop.add(

        Game.random(LOTOFACIL)

    )

    assert pop.size == 1


def test_random():

    pop = Population(LOTOFACIL)

    for _ in range(5):

        pop.add(

            Game.random(LOTOFACIL)

        )

    assert pop.random().size == 15


def test_frequency():

    pop = Population(LOTOFACIL)

    pop.add(

        Game.from_numbers(

            LOTOFACIL,

            range(1,16),

        )

    )

    freq = pop.frequency()

    assert freq[1] == 1

    assert freq[25] == 0


def test_unique():

    game = Game.from_numbers(

        LOTOFACIL,

        range(1,16),

    )

    pop = Population(

        LOTOFACIL,

        [game, game, game],

    )

    assert pop.unique().size == 1


def test_masks():

    pop = Population(LOTOFACIL)

    pop.add(

        Game.random(LOTOFACIL)

    )

    assert len(pop.masks()) == 1