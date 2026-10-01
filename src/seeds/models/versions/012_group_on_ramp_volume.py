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
            name="On-Ramp Volume",
            defaults={"position": 6}
        )
        return group

    @cached_property
    def column_group(self) -> ColumnGroup:
        column_group, _ = self.group.columngroup_set.get_or_create(position=1)
        return column_group

    @cached_property
    def column_peak(self) -> Column:
        column_peak, _ = self.column_group.column_set.get_or_create(name="Peak", defaults={"position": 1})
        return column_peak

    @cached_property
    def column_non_peak(self) -> Column:
        column_non_peak, _ = self.column_group.column_set.get_or_create(name="Non-Peak", defaults={"position": 2})
        return column_non_peak

    def load(self) -> None:
        row_1, _ = self.group.row_set.get_or_create(position=1, defaults={"name": "Hourly Ramp Volume"})
        field_hourly_volume_peak, _ = row_1.field_set.get_or_create(name="Hourly Ramp Volume Peak", defaults={"cell": "RampVolP"})
        self.column_peak.fieldcolumn_set.get_or_create(field=field_hourly_volume_peak)
        field_hourly_volume_non_peak, _ = row_1.field_set.get_or_create(name="Hourly Ramp Volume Non-Peak", defaults={"cell": "RampVolNP"})
        self.column_non_peak.fieldcolumn_set.get_or_create(field=field_hourly_volume_non_peak)

        row_2, _ = self.group.row_set.get_or_create(position=2, defaults={"name": "Metering Strategy"})
        field_metering_strategy_peak, _ = row_2.field_set.get_or_create(name="Metering Strategy", defaults={"cell": "MeterStrat"})
        field_metering_strategy_peak.value_set.get_or_create(value="1", defaults={"name": "1"})
        self.column_peak.fieldcolumn_set.get_or_create(field=field_metering_strategy_peak)
