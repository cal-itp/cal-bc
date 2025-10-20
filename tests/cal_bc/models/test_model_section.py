import pytest
from cal_bc.projects.models.model import Model
from cal_bc.projects.models.model_section import ModelSection


@pytest.mark.django_db
class TestModelSection:
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

    def test_string_representation(self, section: ModelSection) -> None:
        assert str(section) == "1A"
