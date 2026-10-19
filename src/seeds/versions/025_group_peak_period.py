from functools import cached_property

import seeds.seed
from cal_bc.models.models.model import (
    Column,
    ColumnGroup,
    FieldDisplayType,
    Group,
    Subsection,
)


class Seed(seeds.seed.Seed):
    @cached_property
    def subsection(self) -> Subsection:
        return Subsection.objects.get(
            section__version__model__name="Cal-B/C Sketch",
            section__version__name="8.1",
            section__name="Model Inputs",
            name="Annual Person-Trips",
        )

    @cached_property
    def group(self) -> Group:
        group, _ = self.subsection.group_set.get_or_create(
            name="Peak Period",
            defaults={"position": 2}
        )
        return group

    @cached_property
    def column_group(self) -> ColumnGroup:
        column_group, _ = self.group.columngroup_set.get_or_create(position=1, name="")
        return column_group

    @cached_property
    def column_no_build(self) -> Column:
        column, _ = self.column_group.column_set.get_or_create(name="No Build", defaults={"position": 1})
        return column

    @cached_property
    def column_build(self) -> Column:
        column, _ = self.column_group.column_set.get_or_create(name="Build", defaults={"position": 2})
        return column

    @cached_property
    def column_induced(self) -> Column:
        column, _ = self.column_group.column_set.get_or_create(name="Induced", defaults={"position": 3})
        return column

    @property
    def columns(self) -> list[Column]:
        return [
            self.column_no_build,
            self.column_build,
            self.column_induced,
        ]

    def load(self) -> None:
        self.subsection.group_set.get_or_create(name="Year 1", defaults={"position": 1})

        row_1, _ = self.group.row_set.get_or_create(position=1, defaults={"name": "HOV Trips"})
        self.columns[0].fieldcolumn_set.get_or_create(
            field=row_1.field_set.get_or_create(name="No Build HOV Trips", defaults={"cell": "2) Model Inputs!AE9", "display_type": FieldDisplayType.READ_ONLY})[0]
        )
        self.columns[1].fieldcolumn_set.get_or_create(
            field=row_1.field_set.get_or_create(name="Build HOV Trips", defaults={"cell": "2) Model Inputs!AF9", "display_type": FieldDisplayType.READ_ONLY})[0]
        )


        row_2, _ = self.group.row_set.get_or_create(position=2, defaults={"name": "Non-HOV Trips"})
        self.columns[0].fieldcolumn_set.get_or_create(
            field=row_2.field_set.get_or_create(name="No Build Non-HOV Trips", defaults={"cell": "2) Model Inputs!AE10", "display_type": FieldDisplayType.READ_ONLY})[0]
        )
        self.columns[1].fieldcolumn_set.get_or_create(
            field=row_2.field_set.get_or_create(name="Build Non-HOV Trips", defaults={"cell": "2) Model Inputs!AF10", "display_type": FieldDisplayType.READ_ONLY})[0]
        )
        self.columns[2].fieldcolumn_set.get_or_create(
            field=row_2.field_set.get_or_create(name="Induced Non-HOV Trips", defaults={"cell": "PNT1Ind", "display_type": FieldDisplayType.READ_ONLY})[0]
        )


        row_3, _ = self.group.row_set.get_or_create(position=3, defaults={"name": "Truck Trips"})
        self.columns[0].fieldcolumn_set.get_or_create(
            field=row_3.field_set.get_or_create(name="No Build Truck Trips", defaults={"cell": "2) Model Inputs!AE11", "display_type": FieldDisplayType.READ_ONLY})[0]
        )
        self.columns[1].fieldcolumn_set.get_or_create(
            field=row_3.field_set.get_or_create(name="Build Truck Trips", defaults={"cell": "2) Model Inputs!AF11", "display_type": FieldDisplayType.READ_ONLY})[0]
        )
        self.columns[2].fieldcolumn_set.get_or_create(
            field=row_3.field_set.get_or_create(name="Induced Truck Trips", defaults={"cell": "PTT1Ind", "display_type": FieldDisplayType.READ_ONLY})[0]
        )
