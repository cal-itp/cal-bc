import django.test
import pytest
from cal_bc.projects.views import show

from cal_bc.projects.models.project import Project


@pytest.mark.django_db
class TestProjects:
    @pytest.fixture()
    def project(self) -> Project:
        result = Project(name="Test Project")
        result.save()
        return result

    def test_project(self, client: django.test.Client, project: Project):
        response = client.get(f"/projects/{project.id}")
        assert "Test Project" in response.content.decode()
