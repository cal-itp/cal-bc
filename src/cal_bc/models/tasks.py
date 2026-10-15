import logging
from io import BytesIO

from django.core.files import File
from django.tasks import task

from cal_bc.models.models.model import (
    Version,
    VersionFile,
)
from cal_bc_calculator.downloader import Downloader

logger = logging.getLogger(__name__)


class RemoteWorkbook:
    def __init__(self, url: str) -> None:
        self.url = url

    @property
    def downloader(self) -> Downloader:
        return Downloader(url=self.url)

    @property
    def file(self) -> File:
        return File(BytesIO(self.downloader.to_bytes()), name=self.downloader.filename)


@task
def refresh_version_file(version_pk: int) -> None:
    version = Version.objects.get(id=version_pk)
    remote_workbook = RemoteWorkbook(url=version.url)
    VersionFile.objects.create(version=version, file=remote_workbook.file)
