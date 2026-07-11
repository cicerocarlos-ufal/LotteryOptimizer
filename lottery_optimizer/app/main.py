"""
Lottery Optimizer

Application entry point.
"""

from __future__ import annotations

import time

from lottery_optimizer.app import config
from lottery_optimizer.app.load_config import build_rules

from lottery_optimizer.engine.reduction_engine import (
    ReductionEngine,
)


def run():

    rules = build_rules()

    engine = ReductionEngine(

        config.LOTTERY,

        rules,

    )

    print()

    print("=" * 60)

    print("LotteryOptimizer")

    print("=" * 60)

    print()

    print(f"Lottery      : {config.LOTTERY.name}")

    print(f"Algorithm    : {config.ALGORITHM}")

    print(f"Numbers      : {len(config.SOURCE_NUMBERS)}")

    print(f"Target Size  : {config.TARGET_SIZE}")

    print(f"Guarantee    : {config.GUARANTEE}")

    print(f"Games        : {config.N_GAMES}")

    print()

    start = time.perf_counter()

    population = engine.reduce(

        config.SOURCE_NUMBERS,

        algorithm=config.ALGORITHM,

        seed=config.SEED,

        population_size=config.POPULATION_SIZE,

        generations=config.GENERATIONS,

        mutation_rate=config.MUTATION_RATE,

        elite_size=config.ELITE_SIZE,

        tournament_size=config.TOURNAMENT_SIZE,

        workers=config.WORKERS,

        time_limit=config.TIME_LIMIT,

        local_search_probability=config.LOCAL_SEARCH_PROBABILITY,

    )

    elapsed = time.perf_counter() - start

    print()

    print("Reduction completed.")

    print()

    print(f"Games generated : {population.size}")

    print(f"Execution time  : {elapsed:.2f} s")

    print()

    return population


def main():

    run()


if __name__ == "__main__":

    main()