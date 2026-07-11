from lottery_optimizer.algorithms.generator import CandidateGenerator
from lottery_optimizer.algorithms.genetic import GeneticAlgorithm

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


def test_genetic():

    evaluator = Evaluator(

        build_history()

    )

    generator = CandidateGenerator(

        LOTOFACIL,

        seed=10,

    )

    pop = generator.population(40)

    ga = GeneticAlgorithm(

        evaluator,

        population_size=40,

        generations=5,

        seed=10,

    )

    result = ga.run(pop)

    assert result.size > 0


def test_evolve():

    evaluator = Evaluator(

        build_history()

    )

    generator = CandidateGenerator(

        LOTOFACIL,

        seed=5,

    )

    pop = generator.population(30)

    ga = GeneticAlgorithm(

        evaluator,

        population_size=30,

        generations=1,

        seed=5,

    )

    result = ga.evolve(pop)

    assert result.size > 0