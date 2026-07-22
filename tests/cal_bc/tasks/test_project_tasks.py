import pytest
from cal_bc.models.models.model import Model, Version, Section, Subsection, Group, Row, Field
from cal_bc.projects.models.project import Project
from django.contrib.auth.models import User
from cal_bc.projects.tasks import calculate_project_fields
from django.tasks import TaskResultStatus

@pytest.mark.django_db
class TestProjectTasks:
    @pytest.fixture
    def user(self, django_user_model) -> User:
        return django_user_model.objects.create_user(username="caltrans")

    @pytest.fixture
    def model(self) -> Model:
        return Model.objects.create(name="Testing")

    @pytest.fixture
    def version(self, model: Model) -> Version:
        return model.version_set.create(
            name="1",
            url="https://dot.ca.gov/-/media/dot-media/programs/transportation-planning/documents/new-state-planning/transportation-economics/cal-bc/2023-cal-bc/2023-non-federal-model/cal-bc-8-1-sketch-a11y.xlsm"
        )

    @pytest.fixture
    def project(self, user: User, version: Version) -> Project:
        return version.project_set.create(user=user)

    @pytest.fixture
    def section(self, version: Version) -> Section:
        return version.section_set.create(name="Info", code="1")

    @pytest.fixture
    def subsection(self, section: Section) -> Subsection:
        return section.subsection_set.create(name="Data", code="A", description="Some description")

    @pytest.fixture
    def group(self, subsection: Subsection) -> Group:
        return subsection.group_set.create(name="General", description="General description")

    @pytest.fixture
    def row(self, group: Group) -> Row:
        return group.row_set.create()

    @pytest.fixture
    def field(self, row: Row) -> Field:
        return row.field_set.create(name="Project Name", cell="ProjName")

    def test_calculate_project_fields_creates_value(self, project: Project, field: Field) -> None:
        assert project.value_set.count() == 0
        result = calculate_project_fields.enqueue(project.pk)
        assert result.status == TaskResultStatus.SUCCESSFUL
        assert project.value_set.count() == 1

    def test_calculate_project_fields_preserves_value(self, project: Project, field: Field) -> None:
        name_value = project.value_set.create(field=field, value="Nombre")
        result = calculate_project_fields.enqueue(project.pk)
        assert result.status == TaskResultStatus.SUCCESSFUL
        assert project.value_set.get(pk=name_value.pk).value == "Nombre"
