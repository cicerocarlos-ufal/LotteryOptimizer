from lottery_optimizer.engine.ranking import Ranking


def test_time():

    results = [

        {"elapsed": 5.0},

        {"elapsed": 2.0},

        {"elapsed": 7.0},

    ]

    ordered = Ranking.by_time(results)

    assert ordered[0]["elapsed"] == 2.0


def test_games():

    results = [

        {"games": 10},

        {"games": 5},

        {"games": 8},

    ]

    ordered = Ranking.by_games(results)

    assert ordered[0]["games"] == 5