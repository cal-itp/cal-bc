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


@pytest.mark.django_db
class TestProject:
    @pytest.fixture
    def user(self, django_user_model) -> User:
        return django_user_model.objects.create_user(username="caltrans")

    @pytest.fixture
    def model(self) -> Model:
        return Model.objects.create(
            name="Testing",
        )

    @pytest.fixture
    def version(self, model: Model) -> Version:
        return Version.objects.create(
            model=model,
            name="1",
            url="https://example.com",
        )

    @pytest.fixture
    def project(self, user: User, version: Version) -> Project:
        return Project.objects.create(
            version=version,
            user=user,
        )

    @pytest.fixture
    def section(self, version: Version) -> Section:
        return Section.objects.create(version=version, name="Info", code="1")

    @pytest.fixture
    def subsection(self, section: Section) -> Subsection:
        return Subsection.objects.create(
            section=section, name="Data", code="A", description="Some description"
        )

    @pytest.fixture
    def group(self, subsection: Subsection) -> Group:
        return Group.objects.create(
            subsection=subsection, name="General", description="General description"
        )

    @pytest.fixture
    def row(self, group: Group) -> Row:
        return Row.objects.create(group=group)

    @pytest.fixture
    def field(self, row: Row) -> Field:
        return Field.objects.create(row=row, name="Project Name")

    def test_default_name(self, project: Project) -> None:
        assert str(project) == "New Project"

    def test_named_by_field(self, project: Project, field: Field) -> None:
        Value.objects.create(project=project, field=field, value="Trails to Rails")
        assert str(project) == "Trails to Rails"

    def test_subsection_description(
        self, project: Project, subsection: Subsection
    ) -> None:
        assert str(subsection.description) == "Some description"

    def test_group_description(self, project: Project, group: Group) -> None:
        assert str(group.description) == "General description"
