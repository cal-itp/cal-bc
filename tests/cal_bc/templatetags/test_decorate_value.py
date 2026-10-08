
from cal_bc.projects.templatetags.decorate_value import decorate_value


class TestDecorateValue:
    def test_non_numeric_value(self):
        assert decorate_value("Anything else", "") == "Anything else"
    
    def test_non_numeric_unit_value(self):
        assert decorate_value("Anything else", "months") == "Anything else months"

    def test_non_numeric_dollar_value(self):
        assert decorate_value("Anything else", "$") == "$Anything else"

    def test_numeric_unit_value(self):
        assert decorate_value("3", "years") == "3 years"

    def test_decimal_value(self):
        assert decorate_value("55_333.50", "$") == "$55,333.50"

    def test_empty_value(self):
        assert decorate_value("", "") == ""

    def test_na_string_value(self):
        assert decorate_value("N/A", "$") == "N/A"

    def test_na_error_value(self):
        assert decorate_value("{'type': 'Error', 'kind': 'Na'}", "$") == "N/A"

    def test_div_error_value(self):
        assert decorate_value("{'type': 'Error', 'kind': 'Div'}", "$") == "DIV/0"

    def test_error_value(self):
        assert decorate_value("{'type': 'Error', 'kind': 'Oops'}", "$") == "Oops"
