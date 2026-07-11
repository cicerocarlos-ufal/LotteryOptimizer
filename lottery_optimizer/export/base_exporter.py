"""
Lottery Optimizer

Base exporter.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class BaseExporter(ABC):

    @abstractmethod
    def export(

        self,

        population,

        report,

        filename,

    ):

        raise NotImplementedError