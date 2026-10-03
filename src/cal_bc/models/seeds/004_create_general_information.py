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
            name="General Information",
            defaults={"position": 1}
        )

        row_1 = group.row_set.get_or_create(position=1)
        row_1.field_set.get_or_create(name="Project Name", defaults={"cell": "ProjName"})

        row_2 = group.row_set.get_or_create(position=2)
        field_state = row_2.field_set.get_or_create(name="State", defaults={"cell": "1) Project Information!F2"})
        field_state.value_set.get_or_create(name="California", defaults={"value": "California"})

        field_district = row_2.field_set.get_or_create(name="District", defaults={"cell": "1) Project Information!E2"})
        field_district.value_set.get_or_create(name="District 1", defaults={"value": "1"})
