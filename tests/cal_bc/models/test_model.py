import pytest
from cal_bc.projects.models.model import Model


@pytest.mark.django_db
class TestModel:
    @pytest.fixture
    def model(self) -> Model:
        return Model.objects.create(
            name="Testing 0.0",
            url="https://example.com",
        )

    def test_string_representation(self, model: Model) -> None:
        assert str(model) == "Testing 0.0"
