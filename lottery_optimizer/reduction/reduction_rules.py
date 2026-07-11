"""
Lottery Optimizer

Reduction configuration.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ReductionRules:
    """
    Parameters used by reduction algorithms.
    """

    # Universo da loteria (25 na Lotofácil)
    universe_size: int

    # Quantidade de dezenas escolhidas pelo usuário
    source_size: int

    # Tamanho do jogo reduzido (15 na Lotofácil)
    target_size: int

    # Quantidade de jogos desejada
    n_games: int

    # Garantia desejada
    guarantee: int

    # Permitir jogos repetidos
    allow_duplicates: bool = False