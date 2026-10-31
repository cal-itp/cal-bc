import pytest
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse_lazy

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
from cal_bc.projects.models.project import Input, Project


@pytest.mark.django_db(transaction=True)
class TestProjectSubsectionFieldViews:
    @pytest.fixture
    def user(self, django_user_model) -> User:
        return django_user_model.objects.create_user(username="caltrans")

    @pytest.fixture
    def model(self) -> Model:
        return Model.objects.create(name="Cal-B/C Sketch")

    @pytest.fixture
    def version(self, model: Model) -> Version:
        return model.version_set.create(
            name="8.1",
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
        return version.section_set.create(name="Project Information", code="1")

    @pytest.fixture
    def subsection(self, section: Section) -> Subsection:
        return section.subsection_set.create(
            name="Project Data",
            code="A",
            description="This subsection contains the project data.",
        )

    @pytest.fixture
    def group(self, subsection: Subsection) -> Group:
        return subsection.group_set.create(
            name="General Information",
            position=1
        )

    @pytest.fixture
    def row(self, group: Group) -> Row:
        return group.row_set.create(
            position=1,
            guide="""
                # Project Name
                Enter a descriptive name for your project.
            """
        )

    @pytest.fixture
    def name_field(self, row: Row) -> Field:
        return row.field_set.create(name="Project Name", cell="ProjName", display_type=FieldDisplayType.REQUIRED)

    def test_subsection_field_submission_success(
            self,
            client: Client,
            user: User,
            project: Project,
            subsection: Subsection,
            name_field: Field,
    ):
        client.force_login(user)
        response = client.post(
            reverse_lazy(
                "project_subsection_field",
                kwargs={"project_pk": project.pk, "subsection_pk": subsection.pk, "pk": name_field.pk},
            ),
            data={
                f"field-{name_field.pk}-input-value": "Testing",
            },
        )

        assert response.status_code == 200
        assert "<span></span>" in str(response.content)
        assert Input.objects.filter(field=name_field)[0].value == "Testing"

    def test_subsection_field_submission_failure(
            self,
            client: Client,
            user: User,
            project: Project,
            subsection: Subsection,
            name_field: Field,
    ):
        client.force_login(user)
        response = client.post(
            reverse_lazy(
                "project_subsection_field",
                kwargs={"project_pk": project.pk, "subsection_pk": subsection.pk, "pk": name_field.pk},
            ),
            data={
                f"field-{name_field.pk}-input-value": "",
            },
        )

        assert response.status_code == 400
        assert "Enter Project Name" in str(response.content)
