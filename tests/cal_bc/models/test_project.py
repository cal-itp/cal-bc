import pytest
from django.contrib.auth.models import User
from django.tasks.base import TaskResultStatus
from django_tasks_db.models import DBTaskResult

from cal_bc.models.models.model import (
    Field,
    Group,
    Model,
    Row,
    Section,
    Subsection,
    Version,
)
from cal_bc.projects.models.project import Project, RefreshTask, Value


@pytest.mark.django_db(transaction=True)
class TestProject:
    @pytest.fixture
    def user(self, django_user_model) -> User:
        return django_user_model.objects.create_user(username="caltrans")

    @pytest.fixture
    def model(self) -> Model:
        return Model.objects.create(name="Testing")

    @pytest.fixture
    def version(self, model: Model) -> Version:
        return model.version_set.create(name="1", url="https://dot.ca.gov/-/media/dot-media/programs/transportation-planning/documents/new-state-planning/transportation-economics/cal-bc/2023-cal-bc/2023-non-federal-model/cal-bc-8-1-sketch-a11y.xlsm")

    @pytest.fixture
    def project(self, user: User, version: Version) -> Project:
        return version.project_set.create(user=user)

    @pytest.fixture
    def value(self, project: Project, field: Field) -> Value:
        return Value.objects.create(
            project=project,
            field=field,
            value="Point Lobos Train"
        )

    @pytest.fixture
    def section(self, version: Version) -> Section:
        return version.section_set.create(name="Info", code="1")

    @pytest.fixture
    def subsection(self, section: Section) -> Subsection:
        return section.subsection_set.create(name="Data", code="A")

    @pytest.fixture
    def group(self, subsection: Subsection) -> Group:
        return subsection.group_set.create(name="General")

    @pytest.fixture
    def row(self, group: Group) -> Row:
        return group.row_set.create()

    @pytest.fixture
    def field(self, row: Row) -> Field:
        return row.field_set.create(name="Project Name")

    @pytest.fixture
    def summary_value(self, project: Project, subsection: Subsection) -> Value:
        summary_group = subsection.group_set.create(name="General", is_summary=True)
        summary_row = summary_group.row_set.create()
        summary_field = summary_row.field_set.create(name="Cost Per Mile")

        return Value.objects.create(
            project=project,
            field=summary_field,
            value="333"
        )

    def test_default_name(self, project: Project) -> None:
        assert str(project) == "New Project"

    def test_named_by_field(self, project: Project, field: Field) -> None:
        Value.objects.create(project=project, field=field, value="Trails to Rails")
        assert str(project) == "Trails to Rails"

    def test_value_string_representation(self, value: Value) -> None:
        assert str(value) == "Point Lobos Train"

    def test_summary_value_set(self, project: Project, summary_value: Value) -> None:
        assert list(project.summary_value_set) == [summary_value]

    def test_ready_project_refresh_task_is_active(self, project: Project) -> None:
        db_task_result = DBTaskResult.objects.create(
            args_kwargs={"args": [["exit", "1"]], "kwargs": {}},
        )
        refresh_task = RefreshTask.objects.create(project=project, db_task_result=db_task_result)
        assert list(project.refreshtask_set.active().all()) == [refresh_task]

    def test_processing_project_refresh_task_is_active(self, project: Project) -> None:
        db_task_result = DBTaskResult.objects.create(
            args_kwargs={"args": [["exit", "1"]], "kwargs": {}},
        )
        db_task_result.status = TaskResultStatus.RUNNING
        db_task_result.save()
        refresh_task = RefreshTask.objects.create(project=project, db_task_result=db_task_result)
        assert list(project.refreshtask_set.active().all()) == [refresh_task]

    def test_failed_project_refresh_task_is_not_active(self, project: Project) -> None:
        db_task_result = DBTaskResult.objects.create(
            args_kwargs={"args": [["exit", "1"]], "kwargs": {}},
        )
        db_task_result.status = TaskResultStatus.FAILED
        db_task_result.save()
        RefreshTask.objects.create(project=project, db_task_result=db_task_result)
        assert list(project.refreshtask_set.active().all()) == []

    def test_successful_project_refresh_task_is_not_active(self, project: Project) -> None:
        db_task_result = DBTaskResult.objects.create(
            args_kwargs={"args": [["exit", "1"]], "kwargs": {}},
        )
        db_task_result.status = TaskResultStatus.SUCCESSFUL
        db_task_result.save()
        RefreshTask.objects.create(project=project, db_task_result=db_task_result)
        assert list(project.refreshtask_set.active().all()) == []
