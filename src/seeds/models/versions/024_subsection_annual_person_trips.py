from functools import cached_property

import seeds.seed
from cal_bc.models.models.model import Section


class Seed(seeds.seed.Seed):
    @cached_property
    def section(self) -> Section:
        return Section.objects.get(
            version__model__name="Cal-B/C Sketch",
            version__name="8.1",
            name="Model Inputs",
        )

    def load(self) -> None:
        self.section.subsection_set.get_or_create(
            name="Annual Person-Trips",
            defaults={
                "code":"D",
                "guide": """
                    <h2><strong>Setup Help</strong></h2>
                    <p>For HOV and HOT lane projects that affect average vehicle occupancy</p>
                """
            }
        )
