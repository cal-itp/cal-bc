import pytest
from cal_bc.projects.models.project import Project
from cal_bc.projects.models.model import Model


@pytest.mark.django_db
class TestProject:
    @pytest.fixture
    def model(self) -> Model:
        return Model.objects.create(
            name="Testing 0.0",
            url="https://example.com",
        )

    @pytest.fixture
    def project(self, model: Model) -> Project:
        return Project.objects.create(
            name="Geary LRT",
            district=Project.District.FOUR,
            model=model,
        )

    def test_string_representation(self, project: Project) -> None:
        assert str(project) == "Geary LRT"
