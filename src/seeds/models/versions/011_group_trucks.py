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
            name="Trucks",
            defaults={"position": 5}
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
        row_1, _ = self.group.row_set.get_or_create(position=1, defaults={"name": "Trucks (incl. RVs, if appl.)"})
        field_no_build_trucks, _ = row_1.field_set.get_or_create(name="Trucks No Build", defaults={"cell": "PerTruckNB", "unit": "%"})
        self.column_no_build.fieldcolumn_set.get_or_create(field=field_no_build_trucks)
        field_build_trucks, _ = row_1.field_set.get_or_create(name="Trucks Build", defaults={"cell": "PerTruckB", "unit": "%"})
        self.column_build.fieldcolumn_set.get_or_create(field=field_build_trucks)

        row_2, _ = self.group.row_set.get_or_create(position=2, defaults={"name": "Truck Speed"})
        field_no_build_speed, _ = row_2.field_set.get_or_create(name="Truck Speed", defaults={"cell": "TruckSpeed", "unit": "mph"})
        self.column_no_build.fieldcolumn_set.get_or_create(field=field_no_build_speed)
