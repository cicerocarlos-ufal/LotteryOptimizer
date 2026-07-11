from lottery_optimizer.core.fitness import Fitness
from lottery_optimizer.core.objective import (
    ObjectiveBuilder,
)


def test_score():

    fit = Fitness(

        average_hits=10,

        coverage=0.8,

        diversity=0.5,

        redundancy=0.2,

        max_hits=14,

        min_hits=8,

    )

    score = ObjectiveBuilder().score(fit)

    assert score > 0