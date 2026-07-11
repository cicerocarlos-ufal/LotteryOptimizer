"""
Lottery Optimizer

Benchmark Engine.
"""

from __future__ import annotations

import time

from lottery_optimizer.engine.reduction_engine import ReductionEngine


class Benchmark:

    def __init__(
        self,
        lottery,
        rules,
    ) -> None:

        self.engine = ReductionEngine(
            lottery,
            rules,
        )

    # ---------------------------------------------------------

    def run(
        self,
        numbers,
        algorithms,
        **kwargs,
    ):

        results = []

        for algorithm in algorithms:

            start = time.perf_counter()

            population = self.engine.reduce(
                numbers,
                algorithm=algorithm,
                **kwargs,
            )

            elapsed = time.perf_counter() - start

            results.append(
                {
                    "algorithm": algorithm,
                    "games": population.size,
                    "elapsed": elapsed,
                    "population": population,
                }
            )

        return results