import pytest
from cal_bc.projects.models.project import Project


class TestProject:
    def test_create(self):
        project = Project()
        assert project.name is not None
