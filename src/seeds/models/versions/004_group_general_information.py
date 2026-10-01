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
            name="General Information",
            defaults={"position": 1}
        )
        return group

    def load(self) -> None:
        row_1, _ = self.group.row_set.get_or_create(position=1)
        row_1.field_set.get_or_create(name="Project Name", defaults={"cell": "ProjName"})

        row_2, _ = self.group.row_set.get_or_create(position=2)
        field_state, _ = row_2.field_set.get_or_create(name="State", defaults={"cell": "1) Project Information!F2"})
        field_state.value_set.get_or_create(name="California", defaults={"value": "California"})

        field_district, _ = row_2.field_set.get_or_create(name="District", defaults={"cell": "1) Project Information!E2"})
        field_district.value_set.get_or_create(name="District 1", defaults={"value": "1"})
