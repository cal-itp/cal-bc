import pytest
from cal_bc.projects.models.model_version import ModelVersion


@pytest.mark.django_db
class TestModelVersion:
    def test_string_representation(self):
        model_version = ModelVersion.objects.create(
            name="Cal-B/C Sketch",
            version="8.1",
            url="https://example.com",
        )
        assert str(model_version) == "Cal-B/C Sketch v8.1"
