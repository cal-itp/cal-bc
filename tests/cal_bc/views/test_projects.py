from django.contrib.auth.models import User
from cal_bc.projects.models.project import Project
from unbrowsed import parse_html, query_by_text, query_by_label_text
import pytest


class TestProjectsViews:
    @pytest.fixture
    def user(self, django_user_model) -> User:
        return django_user_model.objects.create_user(username="caltrans")

    @pytest.fixture
    def project(self) -> Project:
        return Project.objects.create(
            name="Monterey LRT",
            district=Project.District.FIVE,
            type=Project.RailTransitCapacityType.LIGHT_RAIL,
            location=Project.Location.NO_CAL,
            construction_period_length=4,
        )

    def test_with_projects_index(self, client, user):
        client.force_login(user)
        response = client.get("/projects/")
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Projects")
        assert query_by_text(dom, "New Project")
        page = query_by_text(dom, "Projects", exact=False)
        assert page.to_have_text_content("Showing1of1pages", exact=False)

    def test_with_project_new(self, client, user):
        client.force_login(user)
        response = client.get("/projects/new")
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Project Data")
        assert query_by_label_text(dom, "Project Name")
        assert query_by_label_text(dom, "District")
        assert query_by_label_text(dom, "Project Type")
        assert query_by_label_text(dom, "Project Location")
        assert query_by_label_text(dom, "Length of Construction Period")
        assert query_by_label_text(dom, "One- or Two-Way Data")
        assert query_by_label_text(dom, "Length of Peak Period(s) (up to 24 hrs)")
        assert query_by_text(dom, "Save Project")

    def test_with_project_edit(self, client, user, project):
        client.force_login(user)
        response = client.get(f"/projects/{project.pk}/edit")
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Project Data")

        project_name = query_by_label_text(dom, "Project Name")
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
        assert project_type.element.select("[value='light_rail'][selected]").any_matches
        assert project_location.element.select("[value='2'][selected]").any_matches
        assert construction_length.element.attrs["value"] == "4"
        assert data_direction.element.select("[value='2'][selected]").any_matches
        assert peak_period.element.attrs["value"] == "5"

        assert query_by_text(dom, "Save Project")

    def test_with_project_show(self, client, user, project):
        client.force_login(user)
        response = client.get(f"/projects/{project.pk}/show")
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Project Data")

        project_name = query_by_label_text(dom, "Project Name")
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

        assert query_by_text(dom, "Edit Project")
