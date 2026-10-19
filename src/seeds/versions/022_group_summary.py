from functools import cached_property

import seeds.seed
from cal_bc.models.models.model import Group, Subsection


class Seed(seeds.seed.Seed):
    @cached_property
    def subsection(self) -> Subsection:
        return Subsection.objects.get(
            section__version__model__name="Cal-B/C Sketch",
            section__version__name="8.1",
            section__name="Results",
            name="Investment Analysis"
        )

    @cached_property
    def group(self) -> Group:
        group, _ = self.subsection.group_set.get_or_create(
            name="Summary",
            defaults={"position": 1, "is_summary": True}
        )
        return group

    def load(self) -> None:
        row_1, _ = self.group.row_set.get_or_create(position=1)
        row_1.field_set.get_or_create(name="Life-Cycle Costs (mil. $)", defaults={"cell": "3) Results!H13", "unit": "$"})
        row_1.field_set.get_or_create(name="Life-Cycle Benefits (mil. $)", defaults={"cell": "3) Results!H14", "unit": "$"})
        row_1.field_set.get_or_create(name="Net Present Value (mil. $)", defaults={"cell": "3) Results!H15", "unit": "$"})
        row_1.field_set.get_or_create(name="Benefit / Cost Ratio", defaults={"cell": "BeneCostRatio", "unit": "x"})
        row_1.field_set.get_or_create(name="Rate of Return on Investment", defaults={"cell": "3) Results!H19", "unit": "%"})
        row_1.field_set.get_or_create(name="Payback Period", defaults={"cell": "3) Results!H21", "unit": "years"})
