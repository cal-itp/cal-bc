from functools import cached_property

import seeds.seed
from cal_bc.models.models.model import Section


class Seed(seeds.seed.Seed):
    @cached_property
    def section(self) -> Section:
        return Section.objects.get(
            version__model__name="Cal-B/C Sketch",
            version__name="8.1",
            name="Project Information"
        )

    def load(self) -> None:
        self.section.subsection_set.get_or_create(
            name="Project Costs",
            defaults={
                "code": "E",
                "description": "This subsection contains the project data.",
                "guide": """
                    <h2><strong>Setup Help</strong></h2>
                    <p>All values should be entered in thousands of dollars using today's constant dollars.</p>
                    <p>Project costs (including maintenance and operating costs) should be net of costs without project.</p>
                """
            }
        )
