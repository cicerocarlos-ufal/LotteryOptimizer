from lottery_optimizer.algorithms.annealing import SimulatedAnnealing
from lottery_optimizer.algorithms.generator import CandidateGenerator

from lottery_optimizer.core.draw import Draw
from lottery_optimizer.core.evaluator import Evaluator
from lottery_optimizer.core.history import History

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


def test_improve():

    evaluator = Evaluator(

        build_history()

    )

    generator = CandidateGenerator(

        LOTOFACIL,

        seed=10,

    )

    sa = SimulatedAnnealing(

        evaluator,

        max_iterations=100,

        seed=10,

    )

    game = generator.game()

    improved = sa.improve(game)

    assert improved.size == 15

    assert improved.is_valid()


def test_population():

    evaluator = Evaluator(

        build_history()

    )

    generator = CandidateGenerator(

        LOTOFACIL,

        seed=5,

    )

    pop = generator.population(20)

    sa = SimulatedAnnealing(

        evaluator,

        max_iterations=100,

        seed=5,

    )

    improved = sa.run(pop)

    assert improved.size == 20