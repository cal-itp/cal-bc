import pytest
from django.contrib.auth.models import User
from django.tasks import TaskResultStatus

from cal_bc.models.models.model import (
    Model,
    Version,
    VersionFile,
)
from cal_bc.models.tasks import (
    RemoteWorkbook,
    refresh_version_file_details,
    update_version_file,
)


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
    
    @pytest.fixture
    def cal_bc_corridor_url(self) -> str:
        return "https://dot.ca.gov/-/media/dot-media/programs/transportation-planning/documents/new-state-planning/transportation-economics/cal-bc/2023-cal-bc/2023-non-federal-model/cal-bc-8-1-corridor--a11y.xlsm"

    @pytest.fixture
    def version_file(self, version: Version) -> VersionFile:
        remote_workbook = RemoteWorkbook(version=version)
        return VersionFile.objects.create(version=version, file=remote_workbook.file)

    def test_create_version_file(self, version: Version) -> None:
        result = update_version_file.enqueue(version.pk)
        assert result.status == TaskResultStatus.SUCCESSFUL
        assert version.versionfile.file.name == "cal-bc-8-1-sketch-a11y.xlsm"
        assert version.versionfile.file.size == 751_168
        assert version.versionfile.versionfilesheet_set.count() == 12
        assert version.versionfile.versionfilenamedcell_set.count() == 387

    def test_upload_version_file(self, version_file: VersionFile) -> None:
        assert version_file.versionfilesheet_set.count() == 0
        assert version_file.versionfilenamedcell_set.count() == 0
        result = refresh_version_file_details.enqueue(version_file.id)
        assert result.status == TaskResultStatus.SUCCESSFUL
        assert version_file.file.name == "cal-bc-8-1-sketch-a11y.xlsm"
        assert version_file.file.size == 751_168
        assert version_file.versionfilesheet_set.count() == 12
        assert version_file.versionfilenamedcell_set.count() == 387

    def test_update_version_file_url(self, version: Version, cal_bc_corridor_url: str) -> None:
        result_before = update_version_file.enqueue(version.pk)
        assert result_before.status == TaskResultStatus.SUCCESSFUL
        assert version.versionfile.file.name == "cal-bc-8-1-sketch-a11y.xlsm"
        Version.objects.filter(pk=version.pk).update(url=cal_bc_corridor_url)
        version.refresh_from_db()
        result = update_version_file.enqueue(version.pk)
        assert result.status == TaskResultStatus.SUCCESSFUL
        assert version.versionfile.file.name == "cal-bc-8-1-corridor--a11y.xlsm"
        assert version.versionfile.file.size == 740_142
        assert version.versionfile.versionfilesheet_set.count() == 13
        assert version.versionfile.versionfilenamedcell_set.count() == 295

    def test_refresh_version_file_without_details(self, version_file: VersionFile) -> None:
        assert version_file.versionfilesheet_set.count() == 0
        assert version_file.versionfilenamedcell_set.count() == 0
        result = refresh_version_file_details.enqueue(version_file.id)
        assert result.status == TaskResultStatus.SUCCESSFUL
        assert version_file.versionfilesheet_set.count() == 12
        assert version_file.versionfilenamedcell_set.count() == 387

    def test_refresh_version_file_with_details(self, version_file: VersionFile) -> None:
        version_file.versionfilesheet_set.create(name="Test Sheet")
        version_file.versionfilenamedcell_set.create(name="test", cell="['Test Sheet'!'A1']")
        assert version_file.versionfilesheet_set.count() == 1
        assert version_file.versionfilenamedcell_set.count() == 1
        result = refresh_version_file_details.enqueue(version_file.id)
        assert result.status == TaskResultStatus.SUCCESSFUL
        assert not version_file.versionfilesheet_set.filter(name="Test Sheet").exists()
        assert not version_file.versionfilenamedcell_set.filter(name="test").exists()
        assert version_file.versionfilesheet_set.count() == 12
        assert version_file.versionfilenamedcell_set.count() == 387

    def test_refresh_version_file_with_sheet(self, version_file: VersionFile) -> None:
        version_file.versionfilesheet_set.create(name="Test Sheet")
        assert version_file.versionfilesheet_set.count() == 1
        assert version_file.versionfilenamedcell_set.count() == 0
        result = refresh_version_file_details.enqueue(version_file.id)
        assert result.status == TaskResultStatus.SUCCESSFUL
        assert not version_file.versionfilesheet_set.filter(name="Test Sheet").exists()
        assert version_file.versionfilesheet_set.count() == 12
        assert version_file.versionfilenamedcell_set.count() == 387

    def test_refresh_version_file_with_named_cell(self, version_file: VersionFile) -> None:
        version_file.versionfilenamedcell_set.create(name="test", cell="['Test Sheet'!'A1']")
        assert version_file.versionfilesheet_set.count() == 0
        assert version_file.versionfilenamedcell_set.count() == 1
        result = refresh_version_file_details.enqueue(version_file.id)
        assert result.status == TaskResultStatus.SUCCESSFUL
        assert not version_file.versionfilenamedcell_set.filter(name="test").exists()
        assert version_file.versionfilesheet_set.count() == 12
        assert version_file.versionfilenamedcell_set.count() == 387
