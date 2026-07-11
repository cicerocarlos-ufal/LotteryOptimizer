"""
Lottery Optimizer

CSV Exporter.
"""

from __future__ import annotations

import csv
from pathlib import Path

from lottery_optimizer.export.base_exporter import BaseExporter


class CSVExporter(BaseExporter):

    def export(
        self,
        population,
        report,
        filename,
    ):

        filename = Path(filename)

        filename.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with filename.open(
            "w",
            newline="",
            encoding="utf-8",
        ) as fp:

            writer = csv.writer(fp)

            #
            # Cabeçalho
            #

            writer.writerow(
                [
                    "Game",
                    "Numbers",
                ]
            )

            #
            # Jogos
            #

            for i, game in enumerate(
                population,
                start=1,
            ):

                writer.writerow(
                    [
                        i,
                        " ".join(
                            f"{n:02d}"
                            for n in game
                        ),
                    ]
                )

            #
            # Linha em branco
            #

            writer.writerow([])

            #
            # Estatísticas
            #

            writer.writerow(
                [
                    "Lottery",
                    report.lottery,
                ]
            )

            writer.writerow(
                [
                    "Algorithm",
                    report.algorithm,
                ]
            )

            writer.writerow(
                [
                    "Source Size",
                    report.source_size,
                ]
            )

            writer.writerow(
                [
                    "Target Size",
                    report.target_size,
                ]
            )

            writer.writerow(
                [
                    "Guarantee",
                    report.guarantee,
                ]
            )

            writer.writerow(
                [
                    "Games",
                    report.games,
                ]
            )

            writer.writerow(
                [
                    "Covered",
                    report.covered,
                ]
            )

            writer.writerow(
                [
                    "Target",
                    report.target,
                ]
            )

            writer.writerow(
                [
                    "Coverage %",
                    f"{100*report.coverage:.6f}",
                ]
            )

            writer.writerow(
                [
                    "Elapsed (s)",
                    f"{report.elapsed:.3f}",
                ]
            )

            if report.seed is not None:

                writer.writerow(
                    [
                        "Seed",
                        report.seed,
                    ]
                )