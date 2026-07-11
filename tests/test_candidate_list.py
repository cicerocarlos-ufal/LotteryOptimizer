from lottery_optimizer.core.game import Game

from lottery_optimizer.reduction.coverage_index import CoverageIndex
from lottery_optimizer.reduction.candidate_list import CandidateList

from lottery_optimizer.lotteries.lotofacil import LOTOFACIL


def build_games():

    return [

        Game.from_numbers(

            LOTOFACIL,

            range(i, i + 15),

        )

        for i in range(1, 7)

    ]


def test_build():

    index = CoverageIndex(13)

    rcl = CandidateList(

        index,

        max_size=3,

    )

    rcl.build(

        build_games()

    )

    assert len(rcl) == 3


def test_best():

    index = CoverageIndex(13)

    rcl = CandidateList(

        index,

        max_size=5,

    )

    rcl.build(

        build_games()

    )

    game = rcl.best()

    assert game.size == 15


def test_games():

    index = CoverageIndex(13)

    rcl = CandidateList(

        index,

        max_size=5,

    )

    rcl.build(

        build_games()

    )

    assert len(

        rcl.games()

    ) == 5