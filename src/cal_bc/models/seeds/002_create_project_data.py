from functools import cached_property
from cal_bc.models.models.model import Version

class Seed:
    @cached_property
    def version(self) -> Version:
        return Version.objects.get(
            model__name="Cal-B/C Sketch",
            name="8.1",
        )

    def load(self) -> None:
        self.version.section_set.get_or_create(
            name="Project Information",
            defaults={"code":"1"}
        )
