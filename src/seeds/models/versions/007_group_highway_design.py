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
            name="Highway Design",
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
        row_1, _ = self.group.row_set.get_or_create(position=1, defaults={"name": "Roadway Type"})
        field_no_build_type, _ = row_1.field_set.get_or_create(name="Roadway Type No Build", defaults={"cell": "RoadTypeNB"})
        field_no_build_type.value_set.get_or_create(value="F", defaults={"name": "Freeway"})
        self.column_no_build.fieldcolumn_set.get_or_create(field=field_no_build_type)

        field_build_type, _ = row_1.field_set.get_or_create(name="Roadway Type Build", defaults={"cell": "RoadTypeB"})
        field_build_type.value_set.get_or_create(value="E", defaults={"name": "Expressway"})
        self.column_build.fieldcolumn_set.get_or_create(field=field_build_type)

        row_2, _ = self.group.row_set.get_or_create(position=2, defaults={"name": "No. of General Traffic Lanes"})
        field_no_build_lanes, _ = row_2.field_set.get_or_create(name="No. of General Traffic Lanes No Build", defaults={"cell": "GenLanesNB"})
        self.column_no_build.fieldcolumn_set.get_or_create(field=field_no_build_lanes)
        field_build_lanes, _ = row_2.field_set.get_or_create(name="No. of General Traffic Lanes Build", defaults={"cell": "GenLanesB"})
        self.column_build.fieldcolumn_set.get_or_create(field=field_build_lanes)

        row_3, _ = self.group.row_set.get_or_create(position=3, defaults={"name": "No. of HOV/HOT Lanes"})
        field_no_build_hov_lanes, _ = row_3.field_set.get_or_create(name="No. of HOV/HOT Lanes No Build", defaults={"cell": "HOVLanesNB"})
        self.column_no_build.fieldcolumn_set.get_or_create(field=field_no_build_hov_lanes)
        field_build_hov_lanes, _ = row_3.field_set.get_or_create(name="No. of HOV/HOT Lanes Build", defaults={"cell": "HOVLanesB"})
        self.column_build.fieldcolumn_set.get_or_create(field=field_build_hov_lanes)

        row_4, _ = self.group.row_set.get_or_create(position=4, defaults={"name": "HOV Restriction"})
        field_no_build_hov_restriction, _ = row_4.field_set.get_or_create(name="HOV Restriction No Build", defaults={"cell": "HOVRest"})
        field_no_build_hov_restriction.value_set.get_or_create(value="2", defaults={"name": "2"})
        self.column_no_build.fieldcolumn_set.get_or_create(field=field_no_build_hov_restriction)

        row_5, _ = self.group.row_set.get_or_create(position=5, defaults={"name": "Exclusive ROW for Buses"})
        field_no_build_exclusive_buses, _ = row_5.field_set.get_or_create(name="Exclusive ROW for Buses No Build", defaults={"cell": "Exclusive"})
        field_no_build_exclusive_buses.value_set.get_or_create(value="y", defaults={"name": "Yes"})
        self.column_no_build.fieldcolumn_set.get_or_create(field=field_no_build_exclusive_buses)

        row_6, _ = self.group.row_set.get_or_create(position=6, defaults={"name": "Highway Free-Flow Speed"})
        field_no_build_free_flow, _ = row_6.field_set.get_or_create(name="Highway Free-Flow Speed No Build", defaults={"cell": "FFSpeedNB", "unit": "mph"})
        self.column_no_build.fieldcolumn_set.get_or_create(field=field_no_build_free_flow)
        field_build_free_flow, _ = row_6.field_set.get_or_create(name="Highway Free-Flow Speed Build", defaults={"cell": "FFSpeedB", "unit": "mph"})
        self.column_build.fieldcolumn_set.get_or_create(field=field_build_free_flow)

        row_7, _ = self.group.row_set.get_or_create(position=7, defaults={"name": "Ramp Design Speed"})
        field_no_build_ramp_speed, _ = row_7.field_set.get_or_create(name="Ramp Design Speed No Build", defaults={"cell": "RampFFSpdNB", "unit": "mph"})
        self.column_no_build.fieldcolumn_set.get_or_create(field=field_no_build_ramp_speed)
        field_build_ramp_speed, _ = row_7.field_set.get_or_create(name="Ramp Design Speed Build", defaults={"cell": "RampFFSpdB", "unit": "mph"})
        self.column_build.fieldcolumn_set.get_or_create(field=field_build_ramp_speed)

        row_8, _ = self.group.row_set.get_or_create(position=8, defaults={"name": "Highway Segment Length"})
        field_no_build_segment_length, _ = row_8.field_set.get_or_create(name="Highway Segment Length No Build", defaults={"cell": "SegmentNB", "unit": "mi"})
        self.column_no_build.fieldcolumn_set.get_or_create(field=field_no_build_segment_length)
        field_build_segment_length, _ = row_8.field_set.get_or_create(name="Highway Segment Length Build", defaults={"cell": "SegmentB", "unit": "mi"})
        self.column_build.fieldcolumn_set.get_or_create(field=field_build_segment_length)

        row_9, _ = self.group.row_set.get_or_create(position=9, defaults={"name": "Impacted Length"})
        field_no_build_impacted_length, _ = row_9.field_set.get_or_create(name="Impacted Length No Build", defaults={"cell": "ImpactedNB", "unit": "mi"})
        self.column_no_build.fieldcolumn_set.get_or_create(field=field_no_build_impacted_length)
        field_build_impacted_length, _ = row_9.field_set.get_or_create(name="Impacted Length Build", defaults={"cell": "ImpactedB", "unit": "mi"})
        self.column_build.fieldcolumn_set.get_or_create(field=field_build_impacted_length)
