from lottery_optimizer.algorithms.generator import CandidateGenerator
from lottery_optimizer.algorithms.hill import HillClimbing

from lottery_optimizer.core.draw import Draw
from lottery_optimizer.core.history import History
from lottery_optimizer.core.evaluator import Evaluator

from lottery_optimizer.lotteries.lotofacil import LOTOFACIL


def build_history():

    history = History(LOTOFACIL)

    history.add(

        Draw.from_numbers(

            LOTOFACIL,

            range(1, 16),

            contest=1,

        )

    )

    history.add(

        Draw.from_numbers(

            LOTOFACIL,

            range(2, 17),

            contest=2,

        )

    )

    return history


def test_hill():

    evaluator = Evaluator(

        build_history()

    )

    generator = CandidateGenerator(

        LOTOFACIL,

        seed=123,

    )

    pop = generator.population(10)

    hill = HillClimbing(

        evaluator,

        max_iterations=20,

    )

    improved = hill.run(pop)

    assert improved.size == 10


def test_improve():

    evaluator = Evaluator(

        build_history()

    )

    generator = CandidateGenerator(

        LOTOFACIL,

        seed=1,

    )

    hill = HillClimbing(

        evaluator,

        max_iterations=20,

    )

    game = generator.game()

    improved = hill.improve(game)

    assert improved.size == 15

    assert improved.is_valid()