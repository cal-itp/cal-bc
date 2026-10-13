import pytest
from django.contrib.auth.models import User
from django.tasks import TaskResultStatus

from cal_bc.models.models.model import (
    Model,
    Version,
)
from cal_bc.models.tasks import refresh_version_file


@pytest.mark.django_db(transaction=True)
@pytest.mark.vcr
class TestModelTasks:
    @pytest.fixture
    def user(self, django_user_model) -> User:
        return django_user_model.objects.create_user(username="caltrans")

    @pytest.fixture
    def model(self) -> Model:
        return Model.objects.create(name="Testing")

    @pytest.fixture
    def version(self, model: Model) -> Version:
        return model.version_set.create(
            name="1",
            url="https://dot.ca.gov/-/media/dot-media/programs/transportation-planning/documents/new-state-planning/transportation-economics/cal-bc/2023-cal-bc/2023-non-federal-model/cal-bc-8-1-sketch-a11y.xlsm"
        )

    def test_refresh_project_dependent_fields(self, version: Version) -> None:
        result = refresh_version_file.enqueue(version.pk)
        assert result.status == TaskResultStatus.SUCCESSFUL
        assert version.versionfile.file.name == "cal-bc-8-1-sketch-a11y.xlsm"
        assert version.versionfile.file.size == 751_168
