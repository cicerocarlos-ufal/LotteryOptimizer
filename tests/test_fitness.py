from lottery_optimizer.core.fitness import Fitness


def test_creation():

    f = Fitness()

    assert f.score == 0.0

    assert f.valid


def test_compare():

    a = Fitness(score=10)

    b = Fitness(score=20)

    assert b.better_than(a)

    assert a.worse_than(b)


def test_dict():

    f = Fitness(

        score=5,

        coverage=0.8,

        diversity=0.9,

    )

    d = f.to_dict()

    assert d["score"] == 5

    assert d["coverage"] == 0.8


def test_order():

    a = Fitness(score=10)

    b = Fitness(score=20)

    assert b > a