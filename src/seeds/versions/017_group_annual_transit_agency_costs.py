from functools import cached_property

import seeds.seed
from cal_bc.models.models.model import Column, ColumnGroup, Group, Subsection


class Seed(seeds.seed.Seed):
    @cached_property
    def subsection(self) -> Subsection:
        return Subsection.objects.get(
            section__version__model__name="Cal-B/C Sketch",
            section__version__name="8.1",
            section__name="Project Information",
            name="Rail and Transit Data"
        )

    @cached_property
    def group(self) -> Group:
        group, _ = self.subsection.group_set.get_or_create(
            name="Annual Transit Agency Costs (if TMS project)",
            defaults={"position": 1}
        )
        return group

    @cached_property
    def column_group(self) -> ColumnGroup:
        column_group, _ = self.group.columngroup_set.get_or_create(position=1)
        return column_group

    @cached_property
    def column_no_build(self) -> Column:
        column_no_build, _ = self.column_group.column_set.get_or_create(name="No Build", defaults={"position": 1})
        return column_no_build

    @cached_property
    def column_build(self) -> Column:
        column_build, _ = self.column_group.column_set.get_or_create(name="Build", defaults={"position": 2})
        return column_build

    def load(self) -> None:
        row_1, _ = self.group.row_set.get_or_create(position=1, defaults={"name": "Capital Expenditure"})
        field_no_build_base, _ = row_1.field_set.get_or_create(name="Capital Expenditure No Build", defaults={"cell": "1) Project Information!P52", "unit": "$"})
        self.column_no_build.fieldcolumn_set.get_or_create(field=field_no_build_base)
        field_build_base, _ = row_1.field_set.get_or_create(name="Capital Expenditure Build", defaults={"cell": "1) Project Information!Q52", "unit": "$"})
        self.column_build.fieldcolumn_set.get_or_create(field=field_build_base)

        row_2, _ = self.group.row_set.get_or_create(position=2, defaults={"name": "Ops. & Maint. Expenditure"})
        field_no_build_base, _ = row_2.field_set.get_or_create(name="Ops. & Maint. Expenditure No Build", defaults={"cell": "1) Project Information!P53", "unit": "$"})
        self.column_no_build.fieldcolumn_set.get_or_create(field=field_no_build_base)
        field_build_base, _ = row_2.field_set.get_or_create(name="Ops. & Maint. Expenditure Build", defaults={"cell": "1) Project Information!Q53", "unit": "$"})
        self.column_build.fieldcolumn_set.get_or_create(field=field_build_base)
