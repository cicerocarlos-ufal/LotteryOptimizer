"""
Lottery Optimizer

Reduction Pipeline.
"""

from __future__ import annotations

import time


class ReductionPipeline:

    def __init__(

        self,

        engine,

    ):

        self.engine = engine

    # ---------------------------------------------------------

    def run(

        self,

        numbers,

        algorithm="genetic",

        **kwargs,

    ):

        start = time.perf_counter()

        population = self.engine.reduce(

            numbers,

            algorithm=algorithm,

            **kwargs,

        )

        elapsed = (

            time.perf_counter()

            - start

        )

        return {

            "population": population,

            "games": population.size,

            "elapsed": elapsed,

            "algorithm": algorithm,

        }