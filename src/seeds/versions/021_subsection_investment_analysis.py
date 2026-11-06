from functools import cached_property

import seeds.seed
from cal_bc.models.models.model import Section


class Seed(seeds.seed.Seed):
    @cached_property
    def section(self) -> Section:
        return Section.objects.get(
            version__model__name="Cal-B/C Sketch",
            version__name="8.1",
            name="Results"
        )

    def load(self) -> None:
        self.section.subsection_set.get_or_create(
            name="Investment Analysis",
            defaults={
                "code":"A",
                "description": "This is a summary section.",
                "guide": """
                    <h2><strong>Setup Help</strong></h2>
                    <p>Summary Fields</p>
                """
            }
        )
