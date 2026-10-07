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
            name="Queue Formation",
            defaults={"position": 7}
        )
        return group

    @cached_property
    def column_group(self) -> ColumnGroup:
        column_group, _ = self.group.columngroup_set.get_or_create(position=1)
        return column_group

    @cached_property
    def column_year_1(self) -> Column:
        column_year_1, _ = self.column_group.column_set.get_or_create(name="Year 1", defaults={"position": 1})
        return column_year_1

    @cached_property
    def column_year_20(self) -> Column:
        column_year_20, _ = self.column_group.column_set.get_or_create(name="Year 20", defaults={"position": 2})
        return column_year_20

    def load(self) -> None:
        row_1, _ = self.group.row_set.get_or_create(position=1, defaults={"name": "Arrival Rate"})
        field_year_1_arrivals, _ = row_1.field_set.get_or_create(name="Arrival Rate Year 1", defaults={"cell": "ArrRate1", "unit": "vph"})
        self.column_year_1.fieldcolumn_set.get_or_create(field=field_year_1_arrivals)
        field_year_20_arrivals, _ = row_1.field_set.get_or_create(name="Arrival Rate Year 20", defaults={"cell": "ArrRate20", "unit": "vph"})
        self.column_year_20.fieldcolumn_set.get_or_create(field=field_year_20_arrivals)

        row_2, _ = self.group.row_set.get_or_create(position=2, defaults={"name": "Departure Rate"})
        field_year_1_departures, _ = row_2.field_set.get_or_create(name="Departure Rate Year 1", defaults={"cell": "DepRate1", "unit": "vph"})
        self.column_year_1.fieldcolumn_set.get_or_create(field=field_year_1_departures)
        field_year_20_departures, _ = row_2.field_set.get_or_create(name="Departure Rate Year 20", defaults={"cell": "DepRate20", "unit": "vph"})
        self.column_year_20.fieldcolumn_set.get_or_create(field=field_year_20_departures)
