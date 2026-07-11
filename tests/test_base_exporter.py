import pytest

from lottery_optimizer.export.base_exporter import (
    BaseExporter,
)


def test_abstract():

    with pytest.raises(TypeError):

        BaseExporter()