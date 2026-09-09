
from cal_bc.projects.templatetags.decorate_value import decorate_value


class TestDecorateValue:
    def test_non_numeric_value(self):
        assert decorate_value("Anything else", "$") == "$Anything else"

    def test_dollar_unit_value(self):
        assert decorate_value("55_333.50", "$") == "$55,333.50"

    def test_empty_value(self):
        assert decorate_value("", "") == ""

    def test_na_value(self):
        assert decorate_value("N/A", "$") == "N/A"
