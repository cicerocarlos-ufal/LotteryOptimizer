from lottery_optimizer.app.main import run


def test_run():

    population = run()

    assert population.size > 0