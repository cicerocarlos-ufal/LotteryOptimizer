from lottery_optimizer.algorithms.generator import CandidateGenerator
from lottery_optimizer.algorithms.grasp import GRASP

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


def test_grasp():

    evaluator = Evaluator(build_history())

    generator = CandidateGenerator(
        LOTOFACIL,
        seed=123,
    )

    grasp = GRASP(
        evaluator=evaluator,
        generator=generator,
        candidate_pool=20,
        iterations=5,
        alpha=0.30,
        seed=123,
    )

    pop = grasp.run(10)

    assert pop.size == 10


def test_randomized_candidate():

    evaluator = Evaluator(build_history())

    generator = CandidateGenerator(
        LOTOFACIL,
        seed=1,
    )

    grasp = GRASP(
        evaluator,
        generator,
        candidate_pool=20,
        iterations=2,
    )

    game = grasp.randomized_candidate()

    assert game.size == 15