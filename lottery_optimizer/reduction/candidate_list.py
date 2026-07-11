"""
Lottery Optimizer

Restricted Candidate List (RCL).
"""

from __future__ import annotations

import heapq

from lottery_optimizer.reduction.coverage_index import CoverageIndex


class CandidateList:
    """
    Keeps the best candidate games according to
    their incremental coverage gain.
    """

    def __init__(
        self,
        index: CoverageIndex,
        max_size: int = 500,
    ) -> None:

        self.index = index

        self.max_size = max_size

        self._heap = []

    # -----------------------------------------------------

    def clear(self):

        self._heap.clear()

    # -----------------------------------------------------

    def build(
        self,
        games,
    ):

        self.clear()

        for game in games:

            gain = self.index.gain(game)

            item = (gain, game.mask, game)

            if len(self._heap) < self.max_size:

                heapq.heappush(self._heap, item)

            elif gain > self._heap[0][0]:

                heapq.heapreplace(
                    self._heap,
                    item,
                )

    # -----------------------------------------------------

    @property
    def size(self):

        return len(self._heap)

    # -----------------------------------------------------

    def best(self):

        if not self._heap:

            return None

        return max(

            self._heap,

            key=lambda x: x[0],

        )[2]

    # -----------------------------------------------------

    def best_gain(self):

        if not self._heap:

            return 0

        return max(

            self._heap,

            key=lambda x: x[0],

        )[0]

    # -----------------------------------------------------

    def games(self):

        return [

            item[2]

            for item in sorted(

                self._heap,

                reverse=True,

            )

        ]

    # -----------------------------------------------------

    def __len__(self):

        return len(self._heap)