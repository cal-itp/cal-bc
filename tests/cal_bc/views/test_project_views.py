import pytest

from cal_bc.models.models.model import Model, Version
from cal_bc.projects.models.project import Project
from cal_bc.models.models.model import Section, Subsection, Group, Row, Field
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse_lazy
from unbrowsed import parse_html, query_by_text


class TestProjectViews:
    @pytest.fixture
    def user(self, django_user_model) -> User:
        return django_user_model.objects.create_user(username="caltrans", first_name="Maria", last_name="Mary")

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
        return Subsection.objects.create(section=section, name="Project Data", code="A", description="Project Data description")

    @pytest.fixture
    def group(self, subsection: Subsection) -> Group:
        return Group.objects.create(subsection=subsection, name="General Information", description="General Information description")

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

    def test_index(self, client: Client, user: User):
        client.force_login(user)
        response = client.get(reverse_lazy("projects"))
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Welcome, Maria")
        assert query_by_text(dom, "My Cal B/C Analyses")
        assert query_by_text(dom, "New analysis")
        assert query_by_text(dom, "0 analyses")
        assert query_by_text(dom, "No analyses yet")
        assert query_by_text(dom, "Create analysis")

    def test_index_with_projects(self, client: Client, user: User, project: Project):
        client.force_login(user)
        response = client.get(reverse_lazy("projects"))
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Welcome, Maria")
        assert query_by_text(dom, "My Cal B/C Analyses")
        assert query_by_text(dom, "New analysis")
        assert query_by_text(dom, "1 analyses")
        page = query_by_text(dom, "My Cal B/C Analyses", exact=False)
        assert page.to_have_text_content("1to1of1projects", exact=False)

    def test_edit(
        self,
        client: Client,
        user: User,
        project: Project,
        version: Version,
        section: Section,
        subsection: Subsection
    ) -> None:
        client.force_login(user)
        Subsection.objects.create(section=section, name="Highway Design", code="B")
        response = client.get(reverse_lazy("project_edit", kwargs={"pk": project.pk}))
        assert response.status_code == 302
        assert response.url == reverse_lazy("project_subsection_edit", kwargs={"project_pk": project.pk, "pk": subsection.pk})
