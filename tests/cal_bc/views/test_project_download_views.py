from io import BytesIO

import pytest
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse_lazy

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
from cal_bc_calculator.calculator import Calculator


class TestProjectDownloadViews:
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

    @pytest.mark.vcr
    def test_get_project_download(
        self, client: Client, user: User, project: Project, name_field: Field
    ) -> None:
        ProjectValue.objects.create(
            project=project, field=name_field, value="Monterey LRT"
        )
        client.force_login(user)
        response = client.get(
            reverse_lazy("project_download", kwargs={"pk": project.pk})
        )
        assert response.status_code == 200
        with BytesIO(b"".join(response.streaming_content)) as buffer:
            evaluator = Calculator(buffer).compile()
        assert evaluator.evaluate("ProjName") == "Monterey LRT"
