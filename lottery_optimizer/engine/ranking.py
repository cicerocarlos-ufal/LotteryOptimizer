"""
Lottery Optimizer

Ranking utilities.
"""

from __future__ import annotations


class Ranking:

    @staticmethod
    def by_time(results):

        return sorted(

            results,

            key=lambda r: r["elapsed"],

        )

    @staticmethod
    def by_games(results):

        return sorted(

            results,

            key=lambda r: r["games"],

        )