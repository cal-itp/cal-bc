import pytest

from cal_bc.projects.models.model_version import ModelVersion
from cal_bc.projects.models.project import Project
from cal_bc_calculator.calculator import Calculator
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse_lazy
from io import BytesIO
from unbrowsed import parse_html, query_by_text, query_by_label_text


class TestProjectsViews:
    @pytest.fixture
    def user(self, django_user_model) -> User:
        return django_user_model.objects.create_user(username="caltrans")

    @pytest.fixture
    def model_version(self) -> ModelVersion:
        return ModelVersion.objects.create(
            name="Testing",
            version="1",
            url="https://dot.ca.gov/-/media/dot-media/programs/transportation-planning/documents/new-state-planning/transportation-economics/cal-bc/2023-cal-bc/2023-non-federal-model/cal-bc-8-1-sketch-a11y.xlsm",
        )

    @pytest.fixture
    def project(self, model_version: ModelVersion) -> Project:
        return Project.objects.create(
            name="Monterey LRT",
            model_version=model_version,
            district=Project.District.FIVE,
            type=Project.RailTransitCapacityType.LIGHT_RAIL,
            location=Project.Location.NO_CAL,
            construction_period_length=4,
        )

    def test_with_projects_index(self, client: Client, user: User):
        client.force_login(user)
        response = client.get(reverse_lazy("projects"))
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Projects")
        assert query_by_text(dom, "New Project")
        page = query_by_text(dom, "Projects", exact=False)
        assert page.to_have_text_content("Showing1of1pages", exact=False)

    def test_with_project_new(self, client: Client, user: User):
        client.force_login(user)
        response = client.get(reverse_lazy("project_new"))
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Project Data")
        assert query_by_label_text(dom, "Project Name")
        assert query_by_label_text(dom, "Model Version")
        assert query_by_label_text(dom, "District")
        assert query_by_label_text(dom, "Project Type")
        assert query_by_label_text(dom, "Project Location")
        assert query_by_label_text(dom, "Length of Construction Period")
        assert query_by_label_text(dom, "One- or Two-Way Data")
        assert query_by_label_text(dom, "Length of Peak Period(s) (up to 24 hrs)")
        assert query_by_text(dom, "Save Project")

    def test_with_project_edit(
        self,
        client: Client,
        user: User,
        project: Project,
        model_version: ModelVersion,
    ) -> None:
        client.force_login(user)
        response = client.get(reverse_lazy("project_edit", kwargs={"pk": project.pk}))
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Project Data")

        project_name = query_by_label_text(dom, "Project Name")
        model_version_select = query_by_label_text(dom, "Model Version")
        district = query_by_label_text(dom, "District")
        project_type = query_by_label_text(dom, "Project Type")
        project_location = query_by_label_text(dom, "Project Location")
        construction_length = query_by_label_text(dom, "Length of Construction Period")
        data_direction = query_by_label_text(dom, "One- or Two-Way Data")
        peak_period = query_by_label_text(
            dom, "Length of Peak Period(s) (up to 24 hrs)"
        )
        assert project_name.element.attrs["value"] == "Monterey LRT"
        assert district.element.select("[value='5'][selected]").any_matches
        assert model_version_select.element.select(
            f"[value='{model_version.pk}'][selected]"
        ).any_matches
        assert project_type.element.select("[value='light_rail'][selected]").any_matches
        assert project_location.element.select("[value='2'][selected]").any_matches
        assert construction_length.element.attrs["value"] == "4"
        assert data_direction.element.select("[value='2'][selected]").any_matches
        assert peak_period.element.attrs["value"] == "5"

        assert query_by_text(dom, "Save Project")

    def test_with_project_show(
        self,
        client: Client,
        user: User,
        project: Project,
        model_version: ModelVersion,
    ):
        client.force_login(user)
        response = client.get(reverse_lazy("project", kwargs={"pk": project.pk}))
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Project Data")

        project_name = query_by_label_text(dom, "Project Name")
        model_version_select = query_by_label_text(dom, "Model Version")
        district = query_by_label_text(dom, "District")
        project_type = query_by_label_text(dom, "Project Type")
        project_location = query_by_label_text(dom, "Project Location")
        construction_length = query_by_label_text(dom, "Length of Construction Period")
        data_direction = query_by_label_text(dom, "One- or Two-Way Data")
        peak_period = query_by_label_text(
            dom, "Length of Peak Period(s) (up to 24 hrs)"
        )
        assert project_name.element.attrs["value"] == "Monterey LRT"
        assert project_name.element.select("[disabled]").any_matches
        assert model_version_select.element.select(
            f"[value='{model_version.pk}'][selected]"
        ).any_matches
        assert district.element.select("[value='5'][selected]").any_matches
        assert district.element.select("[disabled]").any_matches
        assert project_type.element.select("[value='light_rail'][selected]").any_matches
        assert project_type.element.select("[disabled]").any_matches
        assert project_location.element.select("[value='2'][selected]").any_matches
        assert project_location.element.select("[disabled]").any_matches
        assert construction_length.element.attrs["value"] == "4"
        assert construction_length.element.select("[disabled]").any_matches
        assert data_direction.element.select("[value='2'][selected]").any_matches
        assert data_direction.element.select("[disabled]").any_matches
        assert peak_period.element.attrs["value"] == "5"
        assert peak_period.element.select("[disabled]").any_matches

        assert query_by_text(dom, "Download")
        assert query_by_text(dom, "Edit Project")

    @pytest.mark.vcr
    def test_get_project_download(
        self, client: Client, user: User, project: Project
    ) -> None:
        client.force_login(user)
        response = client.get(
            reverse_lazy("project_download", kwargs={"pk": project.pk})
        )
        assert response.status_code == 200
        with BytesIO(b"".join(response.streaming_content)) as buffer:
            evaluator = Calculator(buffer).compile()
        assert round(evaluator.evaluate("3) Results!H13"), 2) == 136.65
