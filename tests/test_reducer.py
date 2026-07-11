import pytest

from lottery_optimizer.reduction import ReductionRules
from lottery_optimizer.reduction.reducer import Reducer


class DummyReducer(Reducer):

    def reduce(self, numbers):

        return numbers


def test_dummy():

    rules = ReductionRules(

    universe_size=25,

    source_size=21,

    target_size=15,

    n_games=5,

    guarantee=13,

)

reducer = GreedyCover(

    LOTOFACIL,

    rules,

)