from django.contrib.auth.models import User
from cal_bc.projects.models.model import Model
from cal_bc.projects.models.model_section import ModelSection
from cal_bc.projects.models.project import Project
from unbrowsed import parse_html, query_by_text
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
    def section(self, model: Model) -> ModelSection:
        return ModelSection.objects.create(
            name="1A",
            help_text="Please fill in this section",
            model=model,
        )

    @pytest.fixture
    def project(self, model: Model) -> Project:
        return Project.objects.create(
            name="Monterey LRT",
            district=Project.District.FIVE,
            model=model,
        )

    def test_edit_project_section(
        self,
        client,
        user: User,
        project: Project,
        section: ModelSection,
    ) -> None:
        client.force_login(user)
        response = client.get(f"/projects/{project.pk}/section/{section.pk}/edit")
        assert response.status_code == 200

        dom = parse_html(response.content)

        assert query_by_text(dom, "1A")
        assert query_by_text(dom, "Please fill in this section")
        assert query_by_text(dom, "Save Section")
