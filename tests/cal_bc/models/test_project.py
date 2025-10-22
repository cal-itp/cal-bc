import pytest
from cal_bc.projects.models.model_version import ModelVersion
from cal_bc.projects.models.project import Project


@pytest.mark.django_db
class TestProject:
    @pytest.fixture
    def model_version(self) -> ModelVersion:
        return ModelVersion.objects.create(
            name="Testing",
            version="1",
            url="https://example.com",
        )

    def test_string_representation(self, model_version: ModelVersion) -> None:
        project = Project.objects.create(
            model_version=model_version,
            name="Geary Boulevard MUNI Train",
        )
        assert str(project) == "Geary Boulevard MUNI Train"
