import logging
from functools import cached_property
from io import BytesIO

import openpyxl
from django.core.files import File
from django.db import transaction
from django.tasks import task
from openpyxl.workbook.workbook import Workbook

from cal_bc.models.models.model import (
    Version,
    VersionFile,
    VersionFileNamedCell,
    VersionFileSheet,
)
from cal_bc_calculator.downloader import Downloader

logger = logging.getLogger(__name__)


class RemoteWorkbook:
    def __init__(self, version: Version) -> None:
        self.version = version

    @property
    def downloader(self) -> Downloader:
        return Downloader(url=self.version.url)

    @property
    def file(self) -> File:
        return File(BytesIO(self.downloader.to_bytes()), name=self.downloader.filename)

    @cached_property
    def workbook(self) -> Workbook:
        return openpyxl.load_workbook(filename=BytesIO(self.downloader.to_bytes()), keep_vba=True)


class UploadedWorkbook:
    def __init__(self, version_file: VersionFile) -> None:
        self.version_file = version_file

    @property
    def file(self) -> File:
        with self.version_file.file.open() as f:
            return f.read()

    @cached_property
    def workbook(self) -> Workbook:
        return openpyxl.load_workbook(filename=BytesIO(self.file), keep_vba=True)

def update_file_details(version_file: VersionFile, workbook: Workbook) -> None:
        named_cells_set = [
            VersionFileNamedCell(version_file=version_file, name=name, cell=list(defn.destinations))
            for name, defn in workbook.defined_names.items()
            if not defn.is_reserved and list(defn.destinations)
        ]
        VersionFileNamedCell.objects.filter(version_file=version_file).delete()
        VersionFileNamedCell.objects.bulk_create(named_cells_set, update_conflicts=True, update_fields=("name",), unique_fields=("version_file", "name"))
        
        sheets_set = [
            VersionFileSheet(version_file=version_file, name=name)
            for name in workbook.sheetnames
        ]
        VersionFileSheet.objects.filter(version_file=version_file).delete()
        VersionFileSheet.objects.bulk_create(sheets_set, update_conflicts=True, update_fields=("name",), unique_fields=("version_file", "name"))

@task
def update_version_file(version_pk: int) -> None:
    version = Version.objects.get(id=version_pk)
    remote_workbook = RemoteWorkbook(version=version)
    
    with transaction.atomic():
        if hasattr(version, "versionfile"):
            version.versionfile.delete()
        version_file = VersionFile.objects.create(version=version, file=remote_workbook.file)
        update_file_details(version_file, remote_workbook.workbook)

@task
def refresh_version_file_details(version_file_pk: int) -> None:
    version_file = VersionFile.objects.get(id=version_file_pk)
    uploaded_workbook = UploadedWorkbook(version_file=version_file)
    
    with transaction.atomic():
        update_file_details(version_file, uploaded_workbook.workbook)
