from functools import cached_property

import seeds.seed
from cal_bc.models.models.model import Group, Subsection


class Seed(seeds.seed.Seed):
    @cached_property
    def subsection(self) -> Subsection:
        return Subsection.objects.get(
            section__version__model__name="Cal-B/C Sketch",
            section__version__name="8.1",
            section__name="Project Information",
            name="Project Data"
        )

    @cached_property
    def group(self) -> Group:
        group, _ = self.subsection.group_set.get_or_create(
            name="Project Data",
            defaults={
                "description": "Configure project analysis settings.",
                "position": 2
            }
        )
        return group

    def load(self) -> None:
        row_1, _ = self.group.row_set.get_or_create(position=1)
        field_project_type, _ = row_1.field_set.get_or_create(name="Project Type", defaults={"cell": "ProjType"})
        field_project_type.value_set.get_or_create(value="    General Highway", defaults={"name": "• General Highway"})

        row_2, _ = self.group.row_set.get_or_create(position=2)
        field_project_location, _ = row_2.field_set.get_or_create(name="Project Location", defaults={"cell": "ProjLoc"})
        field_project_location.value_set.get_or_create(value="2", defaults={"name": "NorCal"})

        row_3, _ = self.group.row_set.get_or_create(position=3)
        row_3.field_set.get_or_create(name="Length of Construction Period", defaults={"cell": "Construct", "unit": "years"})

        _row_4, _ = self.group.row_set.get_or_create(position=4)
        field_direction, _ = row_3.field_set.get_or_create(name="One- or Two-Way Data", defaults={"cell": "NumDirections"})
        field_direction.value_set.get_or_create(value="1", defaults={"name": "One-Way"})

        row_5, _ = self.group.row_set.get_or_create(position=5)
        row_5.field_set.get_or_create(name="Length of Peak Period(s) (up to 24 hrs)", defaults={"cell": "PeakLngthNB", "unit": "hours"})
