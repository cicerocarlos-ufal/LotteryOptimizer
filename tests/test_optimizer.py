from lottery_optimizer.optimizer import LotteryOptimizer

from lottery_optimizer.core.draw import Draw
from lottery_optimizer.core.history import History

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


def test_greedy():

    opt = LotteryOptimizer(build_history())

    pop = opt.run("greedy")

    assert pop.size > 0


def test_grasp():

    opt = LotteryOptimizer(build_history())

    pop = opt.run("grasp")

    assert pop.size > 0


def test_genetic():

    opt = LotteryOptimizer(build_history())

    pop = opt.run("genetic")

    assert pop.size > 0


def test_memetic():

    opt = LotteryOptimizer(build_history())

    pop = opt.run("memetic")

    assert pop.size > 0


def test_cpsat():

    opt = LotteryOptimizer(build_history())

    pop = opt.run("cpsat")

    assert pop.size > 0