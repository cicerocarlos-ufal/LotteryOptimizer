from lottery_optimizer.algorithms.generator import CandidateGenerator
from lottery_optimizer.algorithms.lns import LargeNeighborhoodSearch

from lottery_optimizer.core.draw import Draw
from lottery_optimizer.core.history import History
from lottery_optimizer.core.evaluator import Evaluator

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


def test_lns():

    evaluator = Evaluator(build_history())

    generator = CandidateGenerator(
        LOTOFACIL,
        seed=1,
    )

    pop = generator.population(20)

    lns = LargeNeighborhoodSearch(
        evaluator,
        iterations=20,
        seed=1,
    )

    result = lns.run(pop)

    assert result.size == 20


def test_improve():

    evaluator = Evaluator(build_history())

    generator = CandidateGenerator(
        LOTOFACIL,
        seed=2,
    )

    game = generator.game()

    lns = LargeNeighborhoodSearch(
        evaluator,
        iterations=10,
        seed=2,
    )

    improved = lns.improve(game)

    assert improved.is_valid()

    assert improved.size == 15