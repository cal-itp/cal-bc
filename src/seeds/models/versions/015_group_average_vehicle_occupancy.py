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
            name="Average Vehicle Occupancy (AVO)",
            defaults={"position": 9}
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
        row_1, _ = self.group.row_set.get_or_create(position=1, defaults={"name": "General Non-Peak Traffic"})
        field_no_build_base, _ = row_1.field_set.get_or_create(name="General Non-Peak Traffic No Build", defaults={"cell": "AVONonNB"})
        self.column_no_build.fieldcolumn_set.get_or_create(field=field_no_build_base)
        field_build_base, _ = row_1.field_set.get_or_create(name="General Non-Peak Traffic Build", defaults={"cell": "AVONonB"})
        self.column_build.fieldcolumn_set.get_or_create(field=field_build_base)

        row_2, _ = self.group.row_set.get_or_create(position=2, defaults={"name": "General Peak Traffic"})
        field_no_build_forecast, _ = row_2.field_set.get_or_create(name="General Peak Traffic No Build", defaults={"cell": "AVOPeakNB"})
        self.column_no_build.fieldcolumn_set.get_or_create(field=field_no_build_forecast)
        field_build_forecast, _ = row_2.field_set.get_or_create(name="General Peak Traffic Build", defaults={"cell": "AVOPeakB"})
        self.column_build.fieldcolumn_set.get_or_create(field=field_build_forecast)

        row_3, _ = self.group.row_set.get_or_create(position=3, defaults={"name": "High Occupancy Vehicle"})
        field_no_build_forecast, _ = row_3.field_set.get_or_create(name="High Occupancy Vehicle No Build", defaults={"cell": "AVOHovNB"})
        self.column_no_build.fieldcolumn_set.get_or_create(field=field_no_build_forecast)
        field_build_forecast, _ = row_3.field_set.get_or_create(name="High Occupancy Vehicle Build", defaults={"cell": "AVOHovB"})
        self.column_build.fieldcolumn_set.get_or_create(field=field_build_forecast)
