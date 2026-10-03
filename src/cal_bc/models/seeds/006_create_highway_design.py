from functools import cached_property
from cal_bc.models.models.model import Version

class Seed:
    @cached_property
    def section(self) -> Section:
        return Section.objects.get(
            version__model__name="Cal-B/C Sketch",
            version__name="8.1",
            name="Project Data"
        )

    def load(self) -> None:
        self.section.subsection_set.get_or_create(
            name="Highway Design and Traffic Data",
            defaults={
                "code": "B",
                "description": "This subsection contains the project data.",
                "guide": """
                    # Setup Help

                    All fields in this step are required.

                    Click on any field to see specific help and guidance for that input.
                """
            }
        )
