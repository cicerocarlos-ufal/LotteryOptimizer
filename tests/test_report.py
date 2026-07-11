from lottery_optimizer.report.report import Report


def test_remaining():

    report = Report(

        lottery="Lotofácil",

        algorithm="greedy",

        source_size=21,

        target_size=15,

        guarantee=13,

        games=50,

        covered=100,

        target=200,

        coverage=0.5,

        elapsed=1.2,

    )

    assert report.remaining == 100


def test_dict():

    report = Report(

        lottery="Lotofácil",

        algorithm="greedy",

        source_size=21,

        target_size=15,

        guarantee=13,

        games=50,

        covered=100,

        target=200,

        coverage=0.5,

        elapsed=1.2,

    )

    assert report.to_dict()["games"] == 50