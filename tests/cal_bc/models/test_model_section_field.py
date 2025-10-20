import pytest
from cal_bc.projects.models.model import Model
from cal_bc.projects.models.model_section import ModelSection
from cal_bc.projects.models.model_section_field import ModelSectionField


@pytest.mark.django_db
class TestModelSectionField:
    @pytest.fixture
    def model(self) -> Model:
        return Model.objects.create(
            name="Testing 0.0",
            url="https://example.com",
        )

    @pytest.fixture
    def section(self, model: Model) -> ModelSection:
        return ModelSection.objects.create(
            name="1A",
            help_text="Do a barrel roll",
            model=model,
        )

    @pytest.fixture
    def field(self, section: ModelSection) -> ModelSectionField:
        return ModelSectionField.objects.create(
            name="Distance",
            cell="ProjectDistance",
            help_text="Jump in a lake",
            model_section=section,
        )

    def test_string_representation(self, field: ModelSectionField) -> None:
        assert str(field) == "Distance"
