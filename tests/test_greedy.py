from lottery_optimizer.algorithms.generator import CandidateGenerator
from lottery_optimizer.algorithms.greedy import Greedy

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


def test_greedy():

    evaluator = Evaluator(

        build_history()

    )

    generator = CandidateGenerator(

        LOTOFACIL,

        seed=123,

    )

    greedy = Greedy(

        evaluator,

        generator,

        candidate_pool=20,

    )

    pop = greedy.run(10)

    assert pop.size == 10


def test_best_candidate():

    evaluator = Evaluator(

        build_history()

    )

    generator = CandidateGenerator(

        LOTOFACIL,

        seed=42,

    )

    greedy = Greedy(

        evaluator,

        generator,

        candidate_pool=30,

    )

    game = greedy.best_candidate()

    assert game.size == 15