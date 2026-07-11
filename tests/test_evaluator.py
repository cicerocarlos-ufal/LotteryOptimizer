from lottery_optimizer.core.draw import Draw
from lottery_optimizer.core.evaluator import Evaluator
from lottery_optimizer.core.game import Game
from lottery_optimizer.core.history import History
from lottery_optimizer.core.population import Population
from lottery_optimizer.lotteries.lotofacil import LOTOFACIL


def build_history():

    history = History(LOTOFACIL)

    history.add(

        Draw.from_numbers(

            LOTOFACIL,

            range(1,16),

            contest=1,

        )

    )

    history.add(

        Draw.from_numbers(

            LOTOFACIL,

            range(2,17),

            contest=2,

        )

    )

    return history


def test_hits():

    history = build_history()

    evaluator = Evaluator(history)

    game = Game.from_numbers(

        LOTOFACIL,

        range(1,16),

    )

    assert evaluator.hits(

        game,

        history[0],

    ) == 15


def test_game():

    evaluator = Evaluator(

        build_history()

    )

    fit = evaluator.evaluate_game(

        Game.from_numbers(

            LOTOFACIL,

            range(1,16),

        )

    )

    assert fit.max_hits == 15

    assert fit.average_hits > 0


def test_population():

    pop = Population(

        LOTOFACIL,

        [

            Game.random(LOTOFACIL),

            Game.random(LOTOFACIL),

            Game.random(LOTOFACIL),

        ]

    )

    evaluator = Evaluator(

        build_history()

    )

    fit = evaluator.evaluate_population(pop)

    assert fit.evaluated_games == 3


def test_diversity():

    pop = Population(

        LOTOFACIL,

        [

            Game.random(LOTOFACIL),

            Game.random(LOTOFACIL),

        ]

    )

    d = Evaluator.population_diversity(pop)

    assert 0 <= d <= 1