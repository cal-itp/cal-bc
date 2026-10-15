
from cal_bc.projects.templatetags.subtract import subtract


class TestSubtract:
    def test_same_numbers(self) -> None:
        assert subtract(2, 2) == 0

    def test_different_numbers(self) -> None:
        assert subtract(1, 2) == -1

    def test_string_coercion(self) -> None:
        assert subtract(1, "-2") == 3

    def test_string_coercion_failure(self) -> None:
        assert subtract(1, "beans") == ""

    def test_array(self) -> None:
        assert subtract([1, 2], 2) == ""
