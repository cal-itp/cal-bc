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
            section__name="Project Information",
            name="Project Costs"
        )

    @cached_property
    def group(self) -> Group:
        group, _ = self.subsection.group_set.get_or_create(
            name="Construction Period Costs",
            defaults={"position": 1}
        )
        return group

    @cached_property
    def column_group_initial_costs(self) -> ColumnGroup:
        column_group, _ = self.group.columngroup_set.get_or_create(position=1, name="Direct Project Initial Costs")
        return column_group

    @cached_property
    def column_project_support(self) -> Column:
        column, _ = self.column_group_initial_costs.column_set.get_or_create(name="Project Support", defaults={"position": 1})
        return column

    @cached_property
    def column_right_of_way(self) -> Column:
        column, _ = self.column_group_initial_costs.column_set.get_or_create(name="Right Of Way", defaults={"position": 2})
        return column

    @cached_property
    def column_construction(self) -> Column:
        column, _ = self.column_group_initial_costs.column_set.get_or_create(name="Construction", defaults={"position": 3})
        return column

    @cached_property
    def column_group(self) -> ColumnGroup:
        column_group, _ = self.group.columngroup_set.get_or_create(position=2, name="")
        return column_group

    @cached_property
    def column_mitigation(self) -> Column:
        column, _ = self.column_group.column_set.get_or_create(name="Mitigation", defaults={"position": 1})
        return column

    @cached_property
    def column_agency_savings(self) -> Column:
        column, _ = self.column_group.column_set.get_or_create(name="Agency Cost Savings", defaults={"position": 2})
        return column

    @cached_property
    def column_group_cost(self) -> ColumnGroup:
        column_group, _ = self.group.columngroup_set.get_or_create(position=3, name="Cost (in Dollars)")
        return column_group

    @cached_property
    def column_constant_dollars(self) -> Column:
        column, _ = self.column_group_cost.column_set.get_or_create(name="Constant Dollars", defaults={"position": 1})
        return column

    @cached_property
    def column_present_value(self) -> Column:
        column, _ = self.column_group_cost.column_set.get_or_create(name="Present Value", defaults={"position": 2})
        return column

    @cached_property
    def column_no_build(self) -> Column:
        column, _ = self.column_group_period_costs.column_set.get_or_create(name="Build", defaults={"position": 1})
        return column

    @property
    def columns(self) -> list[Column]:
        return [
            self.column_project_support,
            self.column_right_of_way,
            self.column_construction,
            self.column_mitigation,
            self.column_agency_savings,
            self.column_constant_dollars,
            self.column_present_value,
        ]

    def load(self) -> None:
        row_1, _ = self.group.row_set.get_or_create(position=1, defaults={"name": "Yr 1"})
        self.columns[0].fieldcolumn_set.get_or_create(
            field=row_1.field_set.get_or_create(name="Project Support Yr 1", defaults={"cell": "1) Project Information!W15"})[0]
        )
        self.columns[1].fieldcolumn_set.get_or_create(
            field=row_1.field_set.get_or_create(name="Right of Way Yr 1", defaults={"cell": "1) Project Information!X15"})[0]
        )
        self.columns[2].fieldcolumn_set.get_or_create(
            field=row_1.field_set.get_or_create(name="Construction Yr 1", defaults={"cell": "1) Project Information!Y15"})[0]
        )
        self.columns[3].fieldcolumn_set.get_or_create(
            field=row_1.field_set.get_or_create(name="Mitigation Yr 1", defaults={"cell": "1) Project Information!AB15"})[0]
        )
        self.columns[4].fieldcolumn_set.get_or_create(
            field=row_1.field_set.get_or_create(name="Transit Agy Cost Svgs Yr 1", defaults={"cell": "1) Project Information!AC15"})[0]
        )
        self.columns[5].fieldcolumn_set.get_or_create(
            field=row_1.field_set.get_or_create(name="Constant Dollars Yr 1", defaults={"cell": "1) Project Information!AD15", "unit": "$", "display_type": FieldDisplayType.READ_ONLY})[0]
        )
        self.columns[6].fieldcolumn_set.get_or_create(
            field=row_1.field_set.get_or_create(name="Present Value Yr 1", defaults={"cell": "1) Project Information!AE15", "unit": "$", "display_type": FieldDisplayType.READ_ONLY})[0]
        )

        row_2, _ = self.group.row_set.get_or_create(position=2, defaults={"name": "Yr 2"})
        self.columns[0].fieldcolumn_set.get_or_create(
            field=row_2.field_set.get_or_create(name="Project Support Yr 2", defaults={"cell": "1) Project Information!W16"})[0]
        )
        self.columns[1].fieldcolumn_set.get_or_create(
            field=row_2.field_set.get_or_create(name="Right of Way Yr 2", defaults={"cell": "1) Project Information!X16"})[0]
        )
        self.columns[2].fieldcolumn_set.get_or_create(
            field=row_2.field_set.get_or_create(name="Construction Yr 2", defaults={"cell": "1) Project Information!Y16"})[0]
        )
        self.columns[3].fieldcolumn_set.get_or_create(
            field=row_2.field_set.get_or_create(name="Mitigation Yr 2", defaults={"cell": "1) Project Information!AB16"})[0]
        )
        self.columns[4].fieldcolumn_set.get_or_create(
            field=row_2.field_set.get_or_create(name="Transit Agy Cost Svgs Yr 2", defaults={"cell": "1) Project Information!AC16"})[0]
        )
        self.columns[5].fieldcolumn_set.get_or_create(
            field=row_2.field_set.get_or_create(name="Constant Dollars Yr 2", defaults={"cell": "1) Project Information!AD16", "unit": "$", "display_type": FieldDisplayType.READ_ONLY})[0]
        )
        self.columns[6].fieldcolumn_set.get_or_create(
            field=row_2.field_set.get_or_create(name="Present Value Yr 2", defaults={"cell": "1) Project Information!AE16", "unit": "$", "display_type": FieldDisplayType.READ_ONLY})[0]
        )


        row_total, _ = self.group.row_set.get_or_create(position=3, defaults={"name": "Total"})
        self.columns[0].fieldcolumn_set.get_or_create(
            field=row_total.field_set.get_or_create(name="Project Support Total", defaults={"cell": "1) Project Information!W44", "display_type": FieldDisplayType.READ_ONLY})[0]
        )
        self.columns[1].fieldcolumn_set.get_or_create(
            field=row_total.field_set.get_or_create(name="Right of Way Total", defaults={"cell": "1) Project Information!X44", "display_type": FieldDisplayType.READ_ONLY})[0]
        )
        self.columns[2].fieldcolumn_set.get_or_create(
            field=row_total.field_set.get_or_create(name="Construction Total", defaults={"cell": "1) Project Information!Y44", "display_type": FieldDisplayType.READ_ONLY})[0]
        )
        self.columns[3].fieldcolumn_set.get_or_create(
            field=row_total.field_set.get_or_create(name="Mitigation Total", defaults={"cell": "1) Project Information!AB44", "display_type": FieldDisplayType.READ_ONLY})[0]
        )
        self.columns[4].fieldcolumn_set.get_or_create(
            field=row_total.field_set.get_or_create(name="Transit Agy Cost Svgs Total", defaults={"cell": "1) Project Information!AC44", "display_type": FieldDisplayType.READ_ONLY})[0]
        )
        self.columns[5].fieldcolumn_set.get_or_create(
            field=row_total.field_set.get_or_create(name="Constant Dollars Total", defaults={"cell": "1) Project Information!AD44", "unit": "$", "display_type": FieldDisplayType.READ_ONLY})[0]
        )
        self.columns[6].fieldcolumn_set.get_or_create(
            field=row_total.field_set.get_or_create(name="Present Value Total", defaults={"cell": "1) Project Information!AE44", "unit": "$", "display_type": FieldDisplayType.READ_ONLY})[0]
        )
