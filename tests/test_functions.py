import pytest

from calbc.functions import TREND
from xlcalculator.xlfunctions.xl import func_xltypes


class TestFunctions:
    @pytest.fixture()
    def known_ys(self) -> func_xltypes.Array:
        return func_xltypes.Array([-3.0, -2.0, -1.0])

    @pytest.fixture()
    def known_xs(self) -> func_xltypes.Array:
        return func_xltypes.Array([-3.0, -2.0, -1.0])

    @pytest.fixture()
    def new_xs(self) -> func_xltypes.Array:
        return func_xltypes.Array([1.0, 2.0, 3.0])

    def test_trend(
        self,
        known_ys: func_xltypes.Array,
        known_xs: func_xltypes.Array,
        new_xs: func_xltypes.Array
    ) -> None:
        trend = TREND(known_xs, known_ys, new_xs)
        assert isinstance(trend, func_xltypes.Array)
        assert [round(n) for n in trend.flatten()] == [1.0, 2.0, 3.0]

    def test_trend_with_number(
        self,
        known_ys: func_xltypes.Array,
        known_xs: func_xltypes.Array,
        new_xs: func_xltypes.Array
    ) -> None:
        trend = TREND(known_xs, known_ys, 3.0)
        assert isinstance(trend, float)
        assert round(trend) == 3.0
