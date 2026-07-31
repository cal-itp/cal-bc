import pytest
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse_lazy
from unbrowsed import parse_html, query_by_text

from cal_bc.models.models.model import (
    Field,
    Group,
    Model,
    Row,
    Section,
    Subsection,
    Version,
)
from cal_bc.projects.models.project import Project


@pytest.mark.django_db(transaction=True)
class TestProjectValueViews:
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
        return model.version_set.create(
            name="1",
            url="https://dot.ca.gov/-/media/dot-media/programs/transportation-planning/documents/new-state-planning/transportation-economics/cal-bc/2023-cal-bc/2023-non-federal-model/cal-bc-8-1-sketch-a11y.xlsm",
        )

    @pytest.fixture
    def project(self, version: Version, user: User) -> Project:
        return user.project_set.create(version=version)

    @pytest.fixture
    def section(self, version: Version) -> Section:
        return version.section_set.create(name="Project Info", code="1")

    @pytest.fixture
    def subsection(self, section: Section) -> Subsection:
        return section.subsection_set.create(name="Project Data", code="A")

    @pytest.fixture
    def group(self, subsection: Subsection) -> Group:
        return subsection.group_set.create(name="General Information")

    @pytest.fixture
    def row(self, group: Group) -> Row:
        return group.row_set.create()

    @pytest.fixture
    def field(self, row: Row) -> Field:
        return row.field_set.create(cell="ProjName", name="Project Name")

    @pytest.mark.vcr
    def test_get_project_value(
        self, client: Client, user: User, project: Project, field: Field
    ) -> None:
        value = project.value_set.create(field=field, value="Monterey LRT")
        client.force_login(user)
        response = client.get(
            reverse_lazy("project_value", kwargs={"project_pk": project.pk, "pk": value.pk})
        )
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Monterey LRT")
