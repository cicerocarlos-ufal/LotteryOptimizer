"""
Lottery Optimizer

Game Index.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class GameInfo:

    game: object

    gain: int = 0

    selected: bool = False

    version: int = 0


class GameIndex:

    """
    Stores metadata about candidate games.
    """

    def __init__(self):

        self._games = {}

    # ---------------------------------------------------------

    def add(

        self,

        game,

        gain=0,

    ):

        self._games[game.mask] = GameInfo(

            game=game,

            gain=gain,

        )

    # ---------------------------------------------------------

    def get(

        self,

        game,

    ):

        return self._games.get(

            game.mask

        )

    # ---------------------------------------------------------

    def update_gain(

        self,

        game,

        gain,

    ):

        info = self._games[game.mask]

        info.gain = gain

        info.version += 1

    # ---------------------------------------------------------

    def mark_selected(

        self,

        game,

    ):

        self._games[game.mask].selected = True

    # ---------------------------------------------------------

    def __contains__(

        self,

        game,

    ):

        return game.mask in self._games

    # ---------------------------------------------------------

    def __len__(

        self,

    ):

        return len(

            self._games

        )

    # ---------------------------------------------------------

    def values(

        self,

    ):

        return self._games.values()