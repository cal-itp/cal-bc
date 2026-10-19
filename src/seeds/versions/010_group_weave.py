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
            name="Highway Design and Traffic Data"
        )

    @cached_property
    def group(self) -> Group:
        group, _ = self.subsection.group_set.get_or_create(
            name="Weave",
            defaults={"position": 4}
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
        row_1, _ = self.group.row_set.get_or_create(position=1, defaults={"name": "Traffic in Weave"})
        field_no_build_weave, _ = row_1.field_set.get_or_create(name="Traffic in Weave No Build", defaults={"cell": "PerWeaveNB", "unit": "%"})
        self.column_no_build.fieldcolumn_set.get_or_create(field=field_no_build_weave)
        field_build_weave, _ = row_1.field_set.get_or_create(name="Traffic in Weave Build", defaults={"cell": "PerWeaveB", "unit": "%"})
        self.column_build.fieldcolumn_set.get_or_create(field=field_build_weave)
