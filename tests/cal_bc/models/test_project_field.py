import pytest
from cal_bc.projects.models.project_field import ProjectField
from cal_bc.projects.models.project import Project
from cal_bc.projects.models.model import Model
from cal_bc.projects.models.model_section import ModelSection
from cal_bc.projects.models.model_section_field import ModelSectionField


@pytest.mark.django_db
class TestProjectField:
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

    @pytest.fixture
    def project(self, model: Model) -> Project:
        return Project.objects.create(
            name="Geary LRT",
            district=Project.District.FOUR,
            model=model,
        )

    @pytest.fixture
    def project_field(self, project: Project, field: ModelSectionField) -> ProjectField:
        return ProjectField.objects.create(
            project=project, model_section_field=field, value="Okay"
        )

    def test_string_representation(self, project_field: ProjectField) -> None:
        assert str(project_field) == "Okay"
