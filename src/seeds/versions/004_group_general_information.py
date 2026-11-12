from functools import cached_property

import seeds.seed
from cal_bc.models.models.model import FieldDisplayType, Group, Subsection


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
            name="General Information",
            defaults={"position": 1}
        )
        return group

    def load(self) -> None:
        row_1, _ = self.group.row_set.get_or_create(position=1)
        row_1.field_set.get_or_create(name="Project Name", defaults={"cell": "ProjName", "display_type": FieldDisplayType.REQUIRED})

        row_2, _ = self.group.row_set.get_or_create(position=2, defaults={"guide": "<p>Enter the Caltrans district, if available.</p>"})
        field_state, _ = row_2.field_set.get_or_create(name="State", defaults={"cell": "1) Project Information!F2", "display_type": FieldDisplayType.REQUIRED})
        field_state.choice_set.get_or_create(name="California", defaults={"value": "California", "is_selected": True})

        field_district, _ = row_2.field_set.get_or_create(name="District", defaults={"cell": "1) Project Information!E2", "display_type": FieldDisplayType.REQUIRED})
        field_district.choice_set.get_or_create(name="HQ", defaults={"value": "HQ", "is_selected": True})
        field_district.choice_set.get_or_create(name="District-1 - Eureka", defaults={"value": "District-1 - Eureka"})
        field_district.choice_set.get_or_create(name="District-2 - Redding", defaults={"value": "District-2 - Redding"})
        field_district.choice_set.get_or_create(name="District-3 - Marysville / Sacramento", defaults={"value": "District-3 - Marysville / Sacramento"})
        field_district.choice_set.get_or_create(name="District-4 - Bay Area / Oakland", defaults={"value": "District-4 - Bay Area / Oakland"})
