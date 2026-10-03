from functools import cached_property
from cal_bc.models.models.model import Subsection

class Seed:
    @cached_property
    def subsection(self) -> Subsection:
        return Subsection.objects.get(
            section__version__model__name="Cal-B/C Sketch",
            section__version__name="8.1",
            section__name="Project Data",
            name="Project Information"
        )

    def load(self) -> None:
        group = self.subsection.group_set.get_or_create(
            name="Project Data",
            defaults={
                "description": "Configure project analysis settings.",
                "position": 2
            }
        )

        row_1 = group.row_set.get_or_create(position=1)
        field_project_type = row_1.field_set.get_or_create(name="Project Type", defaults={"cell": "ProjType"})
        field_project_type.value_set.get_or_create(value="    General Highway", defaults={"name": "• General Highway"})

        row_2 = group.row_set.get_or_create(position=2)
        field_project_location = row_2.field_set.get_or_create(name="Project Location", defaults={"cell": "ProjLoc"})
        field_project_location.value_set.get_or_create(value="2", defaults={"name": "NorCal"})

        row_3 = group.row_set.get_or_create(position=3)
        field_project_type = row_3.field_set.get_or_create(name="Length of Construction Period", defaults={"cell": "Construct", "unit": "years"})

        row_4 = group.row_set.get_or_create(position=4)
        field_direction = row_3.field_set.get_or_create(name="One- or Two-Way Data", defaults={"cell": "NumDirections"})
        field_direction.value_set.get_or_create(value="1", defaults={"name": "One-Way"})

        row_5 = group.row_set.get_or_create(position=5)
        row_5.field_set.get_or_create(name="Length of Peak Period(s) (up to 24 hrs)", defaults={"cell": "PeakLngthNB", "unit": "hours"})
