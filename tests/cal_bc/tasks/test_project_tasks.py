import pytest
from django.contrib.auth.models import User
from django.tasks import TaskResultStatus

from cal_bc.models.models.model import (
    Field,
    FieldDisplayType,
    Group,
    Model,
    Row,
    Section,
    Subsection,
    Version,
)
from cal_bc.projects.models.project import Project
from cal_bc.projects.tasks import refresh_project_fields


@pytest.mark.django_db(transaction=True)
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

    @pytest.fixture
    def summary_group(self, subsection: Subsection) -> Group:
        return subsection.group_set.create(name="Summary", description="Summary Group", is_summary=True)

    @pytest.fixture
    def summary_row(self, summary_group: Group) -> Row:
        return summary_group.row_set.create()

    def test_refresh_project_fields_creates_value(self, project: Project, field: Field) -> None:
        assert project.value_set.count() == 0
        result = refresh_project_fields.enqueue(project.pk)
        assert result.status == TaskResultStatus.SUCCESSFUL
        assert project.value_set.count() == 1

    def test_refresh_project_fields_preserves_value(self, project: Project, field: Field) -> None:
        project.value_set.create(field=field, value="Nombre")
        result = refresh_project_fields.enqueue(project.pk)
        assert result.status == TaskResultStatus.SUCCESSFUL
        assert project.value_set.get(field=field).value == "Nombre"

    def test_refresh_project_fields_does_not_set_blank_values(self, project: Project, row: Row) -> None:
        formula_field = row.field_set.create(name="Ramp Design Speed (Build)", cell="RampFFSpdB", display_type=FieldDisplayType.NOT_REQUIRED)
        formula_dependency = row.field_set.create(name="Ramp Design Speed (No Build)", cell="RampFFSpdNB")
        project.value_set.create(field=formula_dependency, value="")
        result = refresh_project_fields.enqueue(project.pk)
        assert result.status == TaskResultStatus.SUCCESSFUL
        assert project.value_set.get(field=formula_field).value == "35"

    def test_refresh_project_fields_does_not_write_read_only_values(self, project: Project, row: Row) -> None:
        formula_field = row.field_set.create(name="Ramp Design Speed (Build)", cell="RampFFSpdB", display_type=FieldDisplayType.READ_ONLY)
        project.value_set.create(field=formula_field, value="40")
        result = refresh_project_fields.enqueue(project.pk)
        assert result.status == TaskResultStatus.SUCCESSFUL
        assert project.value_set.get(field=formula_field).value == "35"

    def test_refresh_project_fields_overwrites_formulas(self, project: Project, row: Row) -> None:
        formula_field = row.field_set.create(name="Ramp Design Speed (Build)", cell="RampFFSpdB")
        project.value_set.create(field=formula_field, value="40")
        result = refresh_project_fields.enqueue(project.pk)
        assert result.status == TaskResultStatus.SUCCESSFUL
        assert project.value_set.get(field=formula_field).value == "40"

    def test_refresh_project_dependent_fields(self, project: Project, row: Row) -> None:
        year1_field = row.field_set.create(name="Mitigation Year 1", cell="1) Project Information!AB15", display_type=FieldDisplayType.REQUIRED)
        year2_field = row.field_set.create(name="Mitigation Year 2", cell="1) Project Information!AB16", display_type=FieldDisplayType.NOT_REQUIRED)
        result_field = row.field_set.create(name="Mitigation Total", cell="1) Project Information!AB44", display_type=FieldDisplayType.READ_ONLY)
        project.value_set.create(field=year1_field, value="100")
        project.value_set.create(field=year2_field, value="200")
        project.value_set.create(field=result_field, value="50")
        result = refresh_project_fields.enqueue(project.pk)
        assert result.status == TaskResultStatus.SUCCESSFUL
        assert project.value_set.get(field=result_field).value == "300.0"

    def test_refresh_project_fields_does_not_overwrite_summary_values(self, project: Project, row: Row, summary_row: Row) -> None:
        year1_field = row.field_set.create(name="Mitigation Year 1", cell="1) Project Information!AB15", display_type=FieldDisplayType.REQUIRED)
        year2_field = row.field_set.create(name="Mitigation Year 2", cell="1) Project Information!AB16", display_type=FieldDisplayType.NOT_REQUIRED)
        summary_field = summary_row.field_set.create(name="Mitigation Total", cell="1) Project Information!AB44", display_type=FieldDisplayType.REQUIRED)
        project.value_set.create(field=year1_field, value="110")
        project.value_set.create(field=year2_field, value="210")
        project.value_set.create(field=summary_field, value="50")
        result = refresh_project_fields.enqueue(project.pk)
        assert result.status == TaskResultStatus.SUCCESSFUL
        assert project.value_set.get(field=summary_field).value == "320.0"
