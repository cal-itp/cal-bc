from functools import cached_property
from cal_bc.models.models.model import Subsection

class Seed:
    @cached_property
    def subsection(self) -> Subsection:
        return Subsection.objects.get(
            section__version__model__name="Cal-B/C Sketch",
            section__version__name="8.1",
            section__name="Project Data",
            name="Highway Design"
        )

    def load(self) -> None:
        group = self.subsection.group_set.get_or_create(
            name="Highway Design",
            defaults={"position": 1}
        )

        column_group = group.columngroup_set.get_or_create(position=1)
        column_no_build = column_group.column_set.get_or_create(name="No Build", defaults={"position": 1})
        column_build = column_group.column_set.get_or_create(name="Build", defaults={"position": 2})

        row_1 = group.row_set.get_or_create(position=1, defaults={"name": "Roadway Type"})
        field_no_build_type = row_1.field_set.get_or_create(name="Roadway Type No Build", defaults={"cell": "RoadTypeNB"})
        field_no_build_type.value_set.get_or_create(value="F", defaults={"name": "Freeway"})
        column_no_build.fieldcolumn_set.create(field=field_no_build_type)

        field_build_type = row_1.field_set.get_or_create(name="Roadway Type Build", defaults={"cell": "RoadTypeB"})
        field_build_type.value_set.get_or_create(value="E", defaults={"name": "Expressway"})
        column_build.fieldcolumn_set.create(field=field_build_type)

        row_2 = group.row_set.get_or_create(position=2, defaults={"name": "No. of General Traffic Lanes"})
        column_no_build.fieldcolumn_set.create(
            field=row_2.field_set.get_or_create(name="No. of General Traffic Lanes No Build", defaults={"cell": "GenLanesNB"})
        )
        column_build.fieldcolumn_set.create(
            field=row_2.field_set.get_or_create(name="No. of General Traffic Lanes Build", defaults={"cell": "GenLanesB"})
        )

        row_3 = group.row_set.get_or_create(position=3, defaults={"name": "No. of HOV/HOT Lanes"})
        column_no_build.fieldcolumn_set.create(
            field=row_2.field_set.get_or_create(name="No. of HOV/HOT Lanes No Build", defaults={"cell": "HOVLanesNB"})
        )
        column_build.fieldcolumn_set.create(
            field=row_2.field_set.get_or_create(name="No. of HOV/HOT Lanes Build", defaults={"cell": "HOVLanesB"})
        )

        row_4 = group.row_set.get_or_create(position=4, defaults={"name": "HOV Restriction"})
        field_hov_restriction = row_2.field_set.get_or_create(value="2", defaults={"name": "2"})
        field_hov_restriction.value_set.get_or_create(value="E", defaults={"name": "Expressway"})
        column_no_build.fieldcolumn_set.create(field=field_hov_restriction)

# field_exclusive_buses = create_field(
#     row=create_row(group=group_highway_design, name="Exclusive ROW for Buses", position=4),
#     name="Exclusive ROW for Buses No Build",
#     cell="Exclusive"
# )
# create_value(field=field_exclusive_buses, name="Yes", value="y")
# create_field_column(
#     field=field_exclusive_buses,
#     column=column_hwy_no_build
# )
# row_hwy_free_flow = create_row(group=group_highway_design, name="Highway Free-Flow Speed", position=5)
# create_field_column(
#     field=create_field(row=row_hwy_free_flow, name="Highway Free-Flow Speed No Build", cell="FFSpeedNB", unit="mph"),
#     column=column_hwy_no_build
# )
# create_field_column(
#     field=create_field(row=row_hwy_free_flow, name="Highway Free-Flow Speed Build", cell="FFSpeedB", unit="mph"),
#     column=column_hwy_build
# )
# row_ramp_design = create_row(group=group_highway_design, name="Ramp Design Speed", position=6)
# create_field_column(
#     field=create_field(row=row_ramp_design, name="Ramp Design Speed No Build", cell="RampFFSpdNB", unit="mph"),
#     column=column_hwy_no_build
# )
# create_field_column(
#     field=create_field(row=row_ramp_design, name="Ramp Design Speed Build", cell="RampFFSpdB", unit="mph"),
#     column=column_hwy_build
# )
# row_hwy_segment = create_row(group=group_highway_design, name="Highway Segment Length", position=7)
# create_field_column(
#     field=create_field(row=row_hwy_segment, name="Highway Segment Length No Build", cell="SegmentNB", unit="mi"),
#     column=column_hwy_no_build
# )
# create_field_column(
#     field=create_field(row=row_hwy_segment, name="Highway Segment Length Build", cell="SegmentB", unit="mi"),
#     column=column_hwy_build
# )
# row_impacted = create_row(group=group_highway_design, name="Impacted Length", position=8)
# create_field_column(
#     field=create_field(row=row_impacted, name="Impacted Length No Build", cell="ImpactedNB", unit="mi"),
#     column=column_hwy_no_build
# )
# create_field_column(
#     field=create_field(row=row_impacted, name="Impacted Length Build", cell="ImpactedB", unit="mi"),
#     column=column_hwy_build
# )
