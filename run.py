"""
LotteryOptimizer

Main execution script.
"""

from __future__ import annotations

import time

from lottery_optimizer.app import config
from lottery_optimizer.app.load_config import build_rules

from lottery_optimizer.engine.reduction_engine import (
    ReductionEngine,
)

from lottery_optimizer.validation.coverage_validator import (
    CoverageValidator,
)

from lottery_optimizer.report.report_builder import (
    ReportBuilder,
)

from lottery_optimizer.export.csv_exporter import (
    CSVExporter,
)


def main():

    print("=" * 70)
    print("LotteryOptimizer")
    print("=" * 70)

    rules = build_rules()

    engine = ReductionEngine(

        config.LOTTERY,

        rules,

    )

    print(f"Lottery      : {config.LOTTERY.name}")
    print(f"Algorithm    : {config.ALGORITHM}")
    print(f"Source Size  : {len(config.SOURCE_NUMBERS)}")
    print(f"Target Size  : {config.TARGET_SIZE}")
    print(f"Guarantee    : {config.GUARANTEE}")
    print(f"Games        : {config.N_GAMES}")
    print()

    kwargs = {}

    if config.ALGORITHM in ("genetic", "memetic"):

        kwargs.update(

            population_size=config.POPULATION_SIZE,

            generations=config.GENERATIONS,

            mutation_rate=config.MUTATION_RATE,

            elite_size=config.ELITE_SIZE,

            tournament_size=config.TOURNAMENT_SIZE,

            seed=config.SEED,

        )

    elif config.ALGORITHM == "hill":

        kwargs.update(

            seed=config.SEED,

        )

    elif config.ALGORITHM == "grasp":

        kwargs.update(

            seed=config.SEED,

        )

    elif config.ALGORITHM == "cpsat":

        kwargs.update(

            workers=config.WORKERS,

            time_limit=config.TIME_LIMIT,

        )

    start = time.perf_counter()

    population = engine.reduce(

        config.SOURCE_NUMBERS,

        algorithm=config.ALGORITHM,

        **kwargs,

    )

    elapsed = time.perf_counter() - start

    validator = CoverageValidator(

        config.GUARANTEE,

    )

    validation = validator.validate(

        config.SOURCE_NUMBERS,

        population,

    )

    report = ReportBuilder.build(

        lottery=config.LOTTERY,

        rules=rules,

        source_numbers=config.SOURCE_NUMBERS,

        population=population,

        elapsed=elapsed,

        algorithm=config.ALGORITHM,

        seed=config.SEED,

    )

    print()

    print("=" * 70)

    print("RESULT")

    print("=" * 70)

    print(f"Coverage : {100*validation.coverage:.4f}%")

    print(f"Covered  : {validation.covered:,}")

    print(f"Missing  : {validation.uncovered:,}")

    print(f"Games    : {population.size}")

    print(f"Time     : {elapsed:.3f} s")

    print()

    filename = f"{config.OUTPUT_DIRECTORY}/resultado.csv"

    CSVExporter().export(

        population,

        report,

        filename,

    )

    print(f"CSV saved to {filename}")

    print()

    print("=" * 70)


if __name__ == "__main__":

    main()