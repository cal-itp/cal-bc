from django.contrib.auth.models import User
from unbrowsed import parse_html, query_by_text, query_by_label_text
import pytest


class TestProjectsViews:
    @pytest.fixture
    def user(self, django_user_model) -> User:
        return django_user_model.objects.create_user(username="caltrans")

    def test_with_projects_index(self, client, user):
        client.force_login(user)
        response = client.get("/projects/")
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Projects")
        assert query_by_text(dom, "New Project")
        page = query_by_text(dom, "Projects", exact=False)
        assert page.to_have_text_content("Showing1of1pages", exact=False)

    def test_with_projects_new(self, client, user):
        client.force_login(user)
        response = client.get("/projects/new")
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "New Project")
        assert query_by_label_text(dom, "Project name")
        assert query_by_text(dom, "Save Project")
