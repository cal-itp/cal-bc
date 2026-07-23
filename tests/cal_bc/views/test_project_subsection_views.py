import pytest
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse_lazy
from unbrowsed import parse_html, query_by_role, query_by_text

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
from cal_bc.projects.models.project import Value as ProjectValue


class TestProjectSubsectionViews:
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
            url="https://dot.ca.gov/-/media/dot-media/programs/transportation-planning/documents/new-state-planning/transportation-economics/cal-bc/2023-cal-bc/2023-non-federal-model/cal-bc-8-1-sketch-a11y.xlsm",
        )

    @pytest.fixture
    def project(self, version: Version, user: User) -> Project:
        return Project.objects.create(
            version=version,
            user=user,
        )

    @pytest.fixture
    def section(self, version: Version) -> Section:
        return Section.objects.create(version=version, name="Project Info", code="1")

    @pytest.fixture
    def subsection(self, section: Section) -> Subsection:
        return Subsection.objects.create(section=section, name="Project Data", code="A")

    @pytest.fixture
    def group(self, subsection: Subsection) -> Group:
        return Group.objects.create(subsection=subsection, name="General Information")

    @pytest.fixture
    def row(self, group: Group) -> Row:
        return Row.objects.create(group=group)

    @pytest.fixture
    def name_field(self, row: Row) -> Field:
        return Field.objects.create(row=row, cell="ProjName", name="Project Name")

    @pytest.fixture
    def district_field(self, row: Row) -> Field:
        field = Field.objects.create(row=row, cell="ProjLoc", name="District")
        field.value_set.create(name="District 1", value="1")
        return field

    def test_subsection_edit(
        self,
        client: Client,
        user: User,
        project: Project,
        version: Version,
        subsection: Subsection,
        name_field: Field,
        district_field: Field
    ):
        client.force_login(user)
        response = client.get(reverse_lazy("project_subsection_edit", kwargs={"project_pk": project.pk, "pk": subsection.pk}))
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_role(dom, "heading", name="1A. Project Data")
        assert query_by_text(dom, "General Information")

        assert query_by_role(dom, "textbox", name="Project Name")
        assert query_by_role(dom, "combobox", name="District")

    def test_subsection_edit_submission(
        self,
        client: Client,
        user: User,
        project: Project,
        version: Version,
        subsection: Subsection,
        name_field: Field,
        district_field: Field
    ):
        client.force_login(user)
        response = client.post(
            reverse_lazy("project_subsection_edit", kwargs={"project_pk": project.pk, "pk": subsection.pk}),
            data={
                'value-0-field': name_field.pk,
                'value-0-value': 'Testing',
                'value-1-field': district_field.pk,
                'value-1-value': '1',
                'value-TOTAL_FORMS': 2,
                'value-INITIAL_FORMS': 0,
            }
        )

        assert response.status_code == 302
        assert response.url == reverse_lazy("project_subsection_edit", kwargs={"project_pk": project.pk, "pk": subsection.pk})

        assert ProjectValue.objects.filter(field=name_field)[0].value == "Testing"
        assert ProjectValue.objects.filter(field=district_field)[0].value == "1"
