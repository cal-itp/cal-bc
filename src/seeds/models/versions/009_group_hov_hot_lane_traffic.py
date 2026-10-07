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
            name="HOV/HOT Lane Traffic",
            defaults={"position": 3}
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
        row_1, _ = self.group.row_set.get_or_create(position=1, defaults={"name": "Average Hourly"})
        field_no_build_hourly, _ = row_1.field_set.get_or_create(name="Average Hourly No Build", defaults={"cell": "HOVvolNB"})
        self.column_no_build.fieldcolumn_set.get_or_create(field=field_no_build_hourly)
        field_build_hourly, _ = row_1.field_set.get_or_create(name="Average Hourly Build", defaults={"cell": "HOVvolB"})
        self.column_build.fieldcolumn_set.get_or_create(field=field_build_hourly)

        row_2, _ = self.group.row_set.get_or_create(position=2, defaults={"name": "Induced Trips"})
        field_build_induced, _ = row_2.field_set.get_or_create(name="Induced Trips", defaults={"cell": "PerIndHOV", "unit": "%"})
        self.column_build.fieldcolumn_set.get_or_create(field=field_build_induced)
