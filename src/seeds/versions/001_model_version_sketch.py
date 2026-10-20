import pathlib
from io import BytesIO

from django.core.files import File

import seeds.seed
from cal_bc.models.models.model import Model, VersionFile


class Seed(seeds.seed.Seed):
    @property
    def model(self) -> Model:
        model, _ = Model.objects.get_or_create(
            name="Cal-B/C Sketch",
            defaults={
                "description": "Best for early-stage highway or transit projects.",
                "tags": ["Transit", "Commuter Rail"]
            },
        )
        return model

    def load(self) -> None:
        version, _ = self.model.version_set.get_or_create(
            name="8.1",
            defaults={
                "url": "https://dot.ca.gov/-/media/dot-media/programs/transportation-planning/documents/new-state-planning/transportation-economics/cal-bc/2023-cal-bc/2023-non-federal-model/cal-bc-8-1-sketch-a11y.xlsm",
            }
        )
        workbook_bytes = pathlib.Path(__file__).parent.parent.joinpath("assets", "cal-bc-8-1-sketch-a11y.xlsm").read_bytes()
        VersionFile.objects.get_or_create(
            version=version,
            defaults={
                "file": File(BytesIO(workbook_bytes), name="cal-bc-8-1-sketch-a11y.xlsm"),
            }
        )
