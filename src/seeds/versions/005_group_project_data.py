from functools import cached_property

import seeds.seed
from cal_bc.models.models.model import FieldDisplayType, FieldRange, Group, Subsection


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
        field_project_type, _ = row_1.field_set.get_or_create(name="Project Type", defaults={"cell": "ProjType", "display_type": FieldDisplayType.REQUIRED})
        choice_group_project_type, _ = field_project_type.choicegroup_set.get_or_create(name="Highway Capacity Expansion")
        choice_group_project_type.choice_set.get_or_create(value="    General Highway", defaults={"name": "• General Highway"})
        choice_group_project_type.choice_set.get_or_create(value="    HOV Lane Addition", defaults={"name": "• HOV Lane Addition"})

        row_2, _ = self.group.row_set.get_or_create(position=2)
        field_project_location, _ = row_2.field_set.get_or_create(name="Project Location", defaults={"cell": "ProjLoc", "display_type": FieldDisplayType.REQUIRED})
        choice_group_project_location, _ = field_project_location.choicegroup_set.get_or_create()
        choice_group_project_location.choice_set.get_or_create(value="1", defaults={"name": "SoCal"})
        choice_group_project_location.choice_set.get_or_create(value="2", defaults={"name": "NorCal"})
        choice_group_project_location.choice_set.get_or_create(value="3", defaults={"name": "Rural"})

        row_3, _ = self.group.row_set.get_or_create(position=3)
        row_3.field_set.get_or_create(name="Length of Construction Period", defaults={"cell": "Construct", "unit": "years", "position": 0, "display_type": FieldDisplayType.REQUIRED})
        field_direction, _ = row_3.field_set.get_or_create(name="One- or Two-Way Data", defaults={"cell": "NumDirections", "position": 1, "display_type": FieldDisplayType.REQUIRED})
        choice_group_direction, _ = field_direction.choicegroup_set.get_or_create()
        choice_group_direction.choice_set.get_or_create(value="1", defaults={"name": "One-Way"})
        choice_group_direction.choice_set.get_or_create(value="2", defaults={"name": "Two-Way", "is_selected": True})

        row_4, _ = self.group.row_set.get_or_create(position=4)
        field_peak_period, _ = row_4.field_set.get_or_create(name="Length of Peak Period(s) (up to 24 hrs)", defaults={"cell": "PeakLngthNB", "unit": "hours"})
        FieldRange.objects.get_or_create(field=field_peak_period, defaults={"min_value": 0, "max_value": 24})
