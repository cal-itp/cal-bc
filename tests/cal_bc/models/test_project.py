import pytest
from cal_bc.projects.models.project import Project


@pytest.mark.django_db
class TestProject:
    def test_string_representation(self):
        project = Project.objects.create(name="Geary Boulevard MUNI Train")
        assert str(project) == "Geary Boulevard MUNI Train"
