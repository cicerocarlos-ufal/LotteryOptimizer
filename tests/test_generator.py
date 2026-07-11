from lottery_optimizer.algorithms.generator import CandidateGenerator
from lottery_optimizer.lotteries.lotofacil import LOTOFACIL


def test_game():

    gen = CandidateGenerator(LOTOFACIL)

    game = gen.game()

    assert game.size == 15


def test_games():

    gen = CandidateGenerator(LOTOFACIL)

    games = gen.games(10)

    assert len(games) == 10


def test_population():

    gen = CandidateGenerator(LOTOFACIL)

    pop = gen.population(20)

    assert pop.size == 20


def test_unique():

    gen = CandidateGenerator(LOTOFACIL)

    games = gen.unique_games(50)

    masks = {

        g.mask

        for g in games

    }

    assert len(masks) == 50


def test_unique_population():

    gen = CandidateGenerator(LOTOFACIL)

    pop = gen.unique_population(100)

    assert pop.size == 100