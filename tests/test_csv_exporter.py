from pathlib import Path

from lottery_optimizer.export.csv_exporter import (
    CSVExporter,
)

from lottery_optimizer.report.report import (
    Report,
)

from lottery_optimizer.core.population import Population
from lottery_optimizer.core.game import Game

from lottery_optimizer.lotteries.lotofacil import (
    LOTOFACIL,
)


def test_export(tmp_path: Path):

    pop = Population(

        LOTOFACIL,

    )

    pop.add(

        Game.from_numbers(

            LOTOFACIL,

            range(1,16),

        )

    )

    report = Report(

        lottery="Lotofácil",

        algorithm="genetic",

        source_size=21,

        target_size=15,

        guarantee=13,

        games=1,

        covered=105,

        target=203490,

        coverage=105/203490,

        elapsed=0.523,

        seed=123,

    )

    filename = tmp_path / "resultado.csv"

    CSVExporter().export(

        pop,

        report,

        filename,

    )

    assert filename.exists()

    assert filename.stat().st_size > 0