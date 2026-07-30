import pytest
from django.contrib.auth.models import User

from cal_bc.models.models.model import (
    Field,
    Group,
    Model,
    Row,
    Section,
    Subsection,
    Version,
)
from cal_bc.projects.models.project import Project, Value


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
        return model.version_set.create(name="1", url="https://example.com")

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

    def test_default_name(self, project: Project) -> None:
        assert str(project) == "New Project"

    def test_named_by_field(self, project: Project, field: Field) -> None:
        Value.objects.create(project=project, field=field, value="Trails to Rails")
        assert str(project) == "Trails to Rails"

    def test_value_string_representation(self, value: Value):
        assert str(value) == "Testing v1 § 1A Project Name Point Lobos Train"
