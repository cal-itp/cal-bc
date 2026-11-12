from decimal import Decimal

import pytest

from cal_bc.models.models.model import (
    Field,
    Group,
    Model,
    Row,
    Section,
    Subsection,
    Version,
)
from cal_bc.projects.models.project import Calculation, Project
from cal_bc.projects.templatetags.percentage import (
    handle_percentage,
    to_decimal,
    to_percentage,
)


@pytest.mark.django_db(transaction=True)
class TestPercentage:
    @pytest.fixture
    def calculation(self, django_user_model) -> Project:
        model = Model.objects.create(name="Cal-B/C Test")
        version = Version.objects.create(model=model, name="1")
        section = Section.objects.create(name="Testing", code="1", version=version)
        subsection = Subsection.objects.create(name="Testing", code="A", section=section)
        group = Group.objects.create(name="Testing", subsection=subsection)
        row = Row.objects.create(name="Test Row", group=group)
        field = Field.objects.create(name="Test Field", cell="3) Test Locator!A56", row=row, unit="%")
        user = django_user_model.objects.create_user(username="caltrans")
        project = Project.objects.create(version=version, user=user)
        return  Calculation.objects.create(project=project, field=field, value="4.5")


    def test_to_percentage(self):
        assert to_percentage("0.28") == Decimal(28)

    def test_to_percentage_given_integer(self):
        assert to_percentage(5) == Decimal(500)

    def test_to_percentage_given_none(self):
        assert to_percentage(None) == None

    def test_to_percentage_given_word(self):
        assert to_percentage("forty") == "forty"

    def test_to_percentage_with_fraction(self):
        assert to_percentage("0.12025") == Decimal('12.025')

    def test_to_decimal(self):
        assert to_decimal("300") == 3

    def test_to_decimal_given_integer(self):
        assert to_decimal(12) == Decimal('0.12')

    def test_to_decimal_given_none(self):
        assert to_decimal(None) == None

    def test_to_decimal_given_word(self):
        assert to_decimal("forty") == "forty"

    def test_to_decimal_with_many_decimal_places(self):
        assert to_decimal("24.002") == Decimal('0.24002')

    def test_handle_percentage(self, calculation):
        assert handle_percentage(calculation) == 450

    def test_handle_percentage_given_none(self):
        assert handle_percentage(None) == ""
