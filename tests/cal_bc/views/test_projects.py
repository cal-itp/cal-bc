from django.contrib.auth.models import User
from cal_bc.projects.models.model import Model
from cal_bc.projects.models.project import Project
from unbrowsed import parse_html, query_by_text, query_by_label_text
import pytest


class TestProjectsViews:
    @pytest.fixture
    def user(self, django_user_model) -> User:
        return django_user_model.objects.create_user(username="caltrans")

    @pytest.fixture
    def model(self) -> Model:
        return Model.objects.create(
            name="Testing 0.0",
            url="https://example.com",
        )

    @pytest.fixture
    def project(self, model: Model) -> Project:
        return Project.objects.create(
            name="Monterey LRT",
            district=Project.District.FIVE,
            model=model,
        )

    def test_projects(self, client, user):
        client.force_login(user)
        response = client.get("/projects/")
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Projects")
        assert query_by_text(dom, "New Project")
        page = query_by_text(dom, "Projects", exact=False)
        assert page.to_have_text_content("Showing1of1pages", exact=False)

    def test_new_project(self, client, user):
        client.force_login(user)
        response = client.get("/projects/new")
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Project Data")
        assert query_by_label_text(dom, "Project Name")
        assert query_by_label_text(dom, "District")
        assert query_by_label_text(dom, "Model")
        assert query_by_text(dom, "Save Project")

    def test_edit_project(self, client, user, model, project):
        client.force_login(user)
        response = client.get(f"/projects/{project.pk}/edit")
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Project Data")

        project_name_field = query_by_label_text(dom, "Project Name")
        district_field = query_by_label_text(dom, "District")
        model_field = query_by_label_text(dom, "Model")

        assert project_name_field.element.attrs["value"] == "Monterey LRT"
        assert district_field.element.select("[value='5'][selected]").any_matches
        assert model_field.element.select(f"[value='{model.pk}'][selected]").any_matches
        assert query_by_text(dom, "Save Project")

    def test_show_project(self, client, user, model, project):
        client.force_login(user)
        response = client.get(f"/projects/{project.pk}/")
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Project Data")

        project_name_field = query_by_label_text(dom, "Project Name")
        district_field = query_by_label_text(dom, "District")
        model_field = query_by_label_text(dom, "Model")

        assert project_name_field.element.attrs["value"] == "Monterey LRT"
        assert district_field.element.select("[value='5'][selected]").any_matches
        assert model_field.element.select(f"[value='{model.pk}'][selected]").any_matches
        assert query_by_text(dom, "Edit Project")
