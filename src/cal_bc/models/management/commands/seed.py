import logging

from django.core.management.base import BaseCommand

from cal_bc.models.models.model import FieldColumn, FieldDisplayType, Model

logger = logging.getLogger(__name__)

# python manage.py seed --mode=reseed

MODE_RESEED = 'reseed'
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "Seed the database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        seed(self, options['mode'])


def clear():
    logger.info("Deleting all model data")
    Model.objects.all().delete()


def create_model():
    logger.info("Creating Sketch model")

    model = Model.objects.create(name="Cal-B/C Sketch", description="Best for early-stage highway or transit projects.", tags=["Transit", "Commuter Rail"])
    logger.info(f"{model} model created.")
    return model


def create_version(model):
    version = model.version_set.create(
        name="8.1",
        url="https://dot.ca.gov/-/media/dot-media/programs/transportation-planning/documents/new-state-planning/transportation-economics/cal-bc/2023-cal-bc/2023-non-federal-model/cal-bc-8-1-sketch-a11y.xlsm",
    )
    logger.info(f"{version} version created.")
    return version


def create_section(version):
    section = version.section_set.create(name="Project Information", code="1")
    logger.info(f"{section} section created.")
    return section


def create_subsection(section, name, code, description="", guide=None):
    subsection = section.subsection_set.create(
        name=name,
        code=code,
        description=description,
        guide=guide,
    )

    logger.info(f"{subsection} subsection created.")
    return subsection


def create_group(subsection, name, description="", is_summary=False):
    group = subsection.group_set.create(name=name, description=description, is_summary=is_summary)
    logger.info(f"{group} group created.")
    return group


def create_row(group, name=""):
    row = group.row_set.create(name=name)
    logger.info(f"{row} row created.")
    return row


def create_field(row, name, cell, unit="", display_type=FieldDisplayType.REQUIRED):
    field = row.field_set.create(name=name, cell=cell, unit=unit, display_type=display_type)
    logger.info(f"{field} field created.")
    return field


def create_value(field, name, value):
    value = field.value_set.create(name=name, value=value)
    logger.info(f"{value} value created.")
    return value


def create_column_group(group, name=""):
    column_group = group.columngroup_set.create(name=name)
    logger.info(f"{column_group} column_group created.")
    return column_group


def create_column(column_group, name=""):
    column = column_group.column_set.create(name=name)
    logger.info(f"{column} column created.")
    return column


def create_field_column(field, column):
    field_column = FieldColumn.objects.create(field=field, column=column)
    logger.info(f"{field_column} field column created.")
    return field_column


def seed(self, mode):
    self.stdout.write('Clearing data...')

    clear()
    if mode == MODE_CLEAR:
        self.stdout.write('Done.')
        return

    self.stdout.write('Seeding data...')
    self.stdout.write('Done.')

    model = create_model()
    version = create_version(model)

    section_project_information = create_section(version)

    subsection_project_data = create_subsection(
        section=section_project_information,
        name="Project Data",
        code="A",
        description="This subsection contains the project data.",
        guide="""
            # Setup Help
            All fields in this step are required.
        """
    )

    subsection_highway_traffic = create_subsection(
        section=section_project_information,
        name="Highway Design and Traffic Data",
        code="B",
        description="This subsection contains the project data.",
        guide="Setup Help\nAll fields in this step are required.\nClick on any field to see specific help and guidance for that input."
    )

    subsection_rail = create_subsection(section=section_project_information, name="Rail and Transit Data", code="D")

    subsection_project_costs = create_subsection(
        section=section_project_information,
        name="Project Costs",
        code="E",
        description="This subsection contains the project data.",
        guide="All values should be entered in thousands of dollars using today's constant dollars. Project costs (including maintenance and operating costs) should be net of costs without project."
    )

    group_general_information = create_group(subsection=subsection_project_data, name="General Information")
    create_field(row=create_row(group_general_information), name="Project Name", cell="ProjName")
    row_location = create_row(group_general_information)
    field_state = create_field(row=row_location, name="State", cell="1) Project Information!F2")
    create_value(field=field_state, name="California", value="California")
    field_district = create_field(row=row_location, name="District", cell="1) Project Information!E2")
    create_value(field=field_district, name="District 1", value="1")

    group_project_data = create_group(subsection=subsection_project_data, name="Project Data", description="Configure project analysis settings.")
    field_project_type = create_field(row=create_row(group_project_data), name="Project Type", cell="ProjType")
    create_value(field=field_project_type, name="• General Highway", value="    General Highway")
    field_project_location = create_field(row=create_row(group_project_data), name="Project Location", cell="ProjLoc")
    create_value(field=field_project_location, name="NorCal", value="2")
    create_field(row=create_row(group_project_data), name="Length of Construction Period", cell="Construct", unit="years")
    field_directions = create_field(row=create_row(group_project_data), name="One- or Two-Way Data", cell="NumDirections")
    create_value(field=field_directions, name="One-Way", value="1")
    create_field(row=create_row(group_project_data), name="Length of Peak Period(s) (up to 24 hrs)", cell="PeakLngthNB", unit="hours")

    group_highway_design = create_group(subsection=subsection_highway_traffic, name="Highway Design")
    column_group_hwy = create_column_group(group=group_highway_design)
    column_hwy_no_build = create_column(column_group=column_group_hwy, name="No Build")
    column_hwy_build = create_column(column_group=column_group_hwy, name="Build")
    row_roadway_type = create_row(group=group_highway_design, name="Roadway Type")
    field_roadway_type_no_build = create_field(row=row_roadway_type, name="Roadway Type No Build", cell="RoadTypeNB")
    create_value(field=field_roadway_type_no_build, name="Freeway", value="F")
    create_field_column(field=field_roadway_type_no_build, column=column_hwy_no_build)
    field_roadway_type_build = create_field(row=row_roadway_type, name="Roadway Type Build", cell="RoadTypeB")
    create_value(field=field_roadway_type_build, name="Expressway", value="E")
    create_field_column(field=field_roadway_type_build, column=column_hwy_build)
    row_general_traffic_lanes = create_row(group=group_highway_design, name="No. of General Traffic Lanes")
    create_field_column(
        field=create_field(row=row_general_traffic_lanes, name="No. of General Traffic Lanes No Build", cell="GenLanesNB"),
        column=column_hwy_no_build
    )
    create_field_column(
        field=create_field(row=row_general_traffic_lanes, name="No. of General Traffic Lanes Build", cell="GenLanesB"),
        column=column_hwy_build
    )
    row_hov_lanes = create_row(group=group_highway_design, name="No. of HOV/HOT Lanes")
    create_field_column(
        field=create_field(row=row_hov_lanes, name="No. of HOV/HOT Lanes No Build", cell="HOVLanesNB"),
        column=column_hwy_no_build
    )
    create_field_column(
        field=create_field(row=row_hov_lanes, name="No. of HOV/HOT Lanes Build", cell="HOVLanesB"),
        column=column_hwy_build
    )
    field_hov_restriction = create_field(
        row=create_row(group=group_highway_design, name="HOV Restriction"),
        name="HOV Restriction No Build",
        cell="HOVRest"
    )
    create_value(field=field_hov_restriction, name="2", value="2")
    create_field_column(
        field=field_hov_restriction,
        column=column_hwy_no_build
    )
    field_exclusive_buses = create_field(
        row=create_row(group=group_highway_design, name="Exclusive ROW for Buses"),
        name="Exclusive ROW for Buses No Build",
        cell="Exclusive"
    )
    create_value(field=field_exclusive_buses, name="Yes", value="y")
    create_field_column(
        field=field_exclusive_buses,
        column=column_hwy_no_build
    )
    row_hwy_free_flow = create_row(group=group_highway_design, name="Highway Free-Flow Speed")
    create_field_column(
        field=create_field(row=row_hwy_free_flow, name="Highway Free-Flow Speed No Build", cell="FFSpeedNB", unit="mph"),
        column=column_hwy_no_build
    )
    create_field_column(
        field=create_field(row=row_hwy_free_flow, name="Highway Free-Flow Speed Build", cell="FFSpeedB", unit="mph"),
        column=column_hwy_build
    )
    row_ramp_design = create_row(group=group_highway_design, name="Ramp Design Speed")
    create_field_column(
        field=create_field(row=row_ramp_design, name="Ramp Design Speed No Build", cell="RampFFSpdNB", unit="mph"),
        column=column_hwy_no_build
    )
    create_field_column(
        field=create_field(row=row_ramp_design, name="Ramp Design Speed Build", cell="RampFFSpdB", unit="mph"),
        column=column_hwy_build
    )
    row_hwy_segment = create_row(group=group_highway_design, name="Highway Segment Length")
    create_field_column(
        field=create_field(row=row_hwy_segment, name="Highway Segment Length No Build", cell="SegmentNB", unit="mi"),
        column=column_hwy_no_build
    )
    create_field_column(
        field=create_field(row=row_hwy_segment, name="Highway Segment Length Build", cell="SegmentB", unit="mi"),
        column=column_hwy_build
    )
    row_impacted = create_row(group=group_highway_design, name="Impacted Length")
    create_field_column(
        field=create_field(row=row_impacted, name="Impacted Length No Build", cell="ImpactedNB", unit="mi"),
        column=column_hwy_no_build
    )
    create_field_column(
        field=create_field(row=row_impacted, name="Impacted Length Build", cell="ImpactedB", unit="mi"),
        column=column_hwy_build
    )

    group_avg_traffic = create_group(subsection=subsection_highway_traffic, name="Average Daily Traffic")
    column_group_avg_traffic = create_column_group(group=group_avg_traffic)
    column_avg_traffic_no_build = create_column(column_group=column_group_avg_traffic, name="No Build")
    column_avg_traffic_build = create_column(column_group=column_group_avg_traffic, name="Build")
    create_field_column(
        field=create_field(row=create_row(group=group_avg_traffic, name="Current"), name="Current", cell="ADT0"),
        column=column_avg_traffic_no_build
    )
    row_base_year = create_row(group=group_avg_traffic, name="Base (Year 1)")
    create_field_column(
        field=create_field(row=row_base_year, name="Base (Year 1) No Build", cell="ADT1NB"),
        column=column_avg_traffic_no_build
    )
    create_field_column(
        field=create_field(row=row_base_year, name="Base (Year 1) Build", cell="ADT1B"),
        column=column_avg_traffic_build
    )
    row_forecast_year = create_row(group=group_avg_traffic, name="Forecast (Year 20)")
    create_field_column(
        field=create_field(row=row_forecast_year, name="Forecast (Year 20) No Build", cell="ADT20NB"),
        column=column_avg_traffic_no_build
    )
    create_field_column(
        field=create_field(row=row_forecast_year, name="Forecast (Year 20) Build", cell="ADT20B"),
        column=column_avg_traffic_build
    )

    group_hov_lane = create_group(subsection=subsection_highway_traffic, name="HOV/HOT Lane Traffic")
    column_group_hov_lane = create_column_group(group=group_hov_lane)
    column_hov_lane_no_build = create_column(column_group=column_group_hov_lane, name="No Build")
    column_hov_lane_build = create_column(column_group=column_group_hov_lane, name="Build")
    row_average_hourly = create_row(group=group_hov_lane, name="Average Hourly")
    create_field_column(
        field=create_field(row=row_average_hourly, name="Average Hourly No Build", cell="HOVvolNB"),
        column=column_hov_lane_no_build
    )
    create_field_column(
        field=create_field(row=row_average_hourly, name="Average Hourly Build", cell="HOVvolB"),
        column=column_hov_lane_build
    )
    create_field_column(
        field=create_field(row=create_row(group=group_hov_lane, name="Induced Trips"), name="Induced Trips", cell="PerIndHOV", unit="%"),
        column=column_hov_lane_build
    )

    group_weave = create_group(subsection=subsection_highway_traffic, name="Weave")
    column_group_weave = create_column_group(group=group_weave)
    column_weave_no_build = create_column(column_group=column_group_weave, name="No Build")
    column_weave_build = create_column(column_group=column_group_weave, name="Build")
    row_weave = create_row(group=group_weave, name="Traffic in Weave")
    create_field_column(
        field=create_field(row=row_weave, name="Traffic in Weave No Build", cell="PerWeaveNB", unit="%"),
        column=column_weave_no_build
    )
    create_field_column(
        field=create_field(row=row_weave, name="Traffic in Weave Build", cell="PerWeaveB", unit="%"),
        column=column_weave_build
    )

    group_trucks = create_group(subsection=subsection_highway_traffic, name="Trucks")
    column_group_trucks = create_column_group(group=group_trucks)
    column_trucks_no_build = create_column(column_group=column_group_trucks, name="No Build")
    column_trucks_build = create_column(column_group=column_group_trucks, name="Build")
    row_trucks = create_row(group=group_trucks, name="Trucks (incl. RVs, if appl.)")
    create_field_column(
        field=create_field(row=row_trucks, name="Trucks No Build", cell="PerTruckNB", unit="%"),
        column=column_trucks_no_build
    )
    create_field_column(
        field=create_field(row=row_trucks, name="Trucks Build", cell="PerTruckB", unit="%"),
        column=column_trucks_build
    )
    create_field_column(
        field=create_field(row=create_row(group=group_trucks, name="Truck Speed"), name="Truck Speed", cell="TruckSpeed", unit="mph"),
        column=column_trucks_no_build
    )

    group_onramp = create_group(subsection=subsection_highway_traffic, name="On-Ramp Volume")
    column_group_onramp = create_column_group(group=group_onramp)
    column_onramp_peak = create_column(column_group=column_group_onramp, name="Peak")
    column_onramp_nonpeak = create_column(column_group=column_group_onramp, name="Non-Peak")
    row_onramp = create_row(group=group_onramp, name="Hourly Ramp Volume")
    create_field_column(
        field=create_field(row=row_onramp, name="Hourly Ramp Volume Peak", cell="RampVolP"),
        column=column_onramp_peak
    )
    create_field_column(
        field=create_field(row=row_onramp, name="Hourly Ramp Volume Non-Peak", cell="RampVolNP"),
        column=column_onramp_nonpeak
    )
    field_metering = create_field(row=create_row(group=group_onramp, name="Metering Strategy"), name="Metering Strategy", cell="MeterStrat")
    create_field_column(
        field=field_metering,
        column=column_onramp_peak
    )
    create_value(field=field_metering, name="1", value="1")

    group_queue = create_group(subsection=subsection_highway_traffic, name="Queue Formation")
    column_group_queue = create_column_group(group=group_queue)
    column_queue_yr1 = create_column(column_group=column_group_queue, name="Year 1")
    column_queue_yr20 = create_column(column_group=column_group_queue, name="Year 20")
    row_arrival = create_row(group=group_queue, name="Arrival Rate")
    create_field_column(
        field=create_field(row=row_arrival, name="Arrival Rate Year 1", cell="ArrRate1", unit="vph"),
        column=column_queue_yr1
    )
    create_field_column(
        field=create_field(row=row_arrival, name="Arrival Rate Year 20", cell="ArrRate20", unit="vph"),
        column=column_queue_yr20
    )
    row_departure = create_row(group=group_queue, name="Departure Rate")
    create_field_column(
        field=create_field(row=row_departure, name="Departure Rate Year 1", cell="DepRate1", unit="vph"),
        column=column_queue_yr1
    )
    create_field_column(
        field=create_field(row=row_departure, name="Departure Rate Year 20", cell="DepRate20", unit="vph"),
        column=column_queue_yr20
    )

    group_pavement = create_group(subsection=subsection_highway_traffic, name="Pavement Condition")
    column_group_pavement = create_column_group(group=group_pavement)
    column_pavement_no_build = create_column(column_group=column_group_pavement, name="No Build")
    column_pavement_build = create_column(column_group=column_group_pavement, name="Build")
    row_iri_base = create_row(group=group_pavement, name="IRI Base (Year 1)")
    create_field_column(
        field=create_field(row=row_iri_base, name="IRI Base No Build", cell="IRI1NB"),
        column=column_pavement_no_build
    )
    create_field_column(
        field=create_field(row=row_iri_base, name="IRI Base Build", cell="IRI1B"),
        column=column_pavement_build
    )
    row_iri_forecast = create_row(group=group_pavement, name="IRI Forecast (Year 20)")
    create_field_column(
        field=create_field(row=row_iri_forecast, name="IRI Forecast No Build", cell="IRI20NB"),
        column=column_pavement_no_build
    )
    create_field_column(
        field=create_field(row=row_iri_forecast, name="IRI Forecast Build", cell="IRI20B"),
        column=column_pavement_build
    )

    group_avg_occupancy = create_group(subsection=subsection_highway_traffic, name="Average Vehicle Occupancy (AVO)")
    column_group_avg_occupancy = create_column_group(group=group_avg_occupancy)
    column_avg_occupancy_no_build = create_column(column_group=column_group_avg_occupancy, name="No Build")
    column_avg_occupancy_build = create_column(column_group=column_group_avg_occupancy, name="Build")
    row_general_nonpeak = create_row(group=group_avg_occupancy, name="General Non-Peak Traffic")
    create_field_column(
        field=create_field(row=row_general_nonpeak, name="General Non-Peak Traffic No Build", cell="AVONonNB"),
        column=column_avg_occupancy_no_build
    )
    create_field_column(
        field=create_field(row=row_general_nonpeak, name="General Non-Peak Traffic Build", cell="AVONonB"),
        column=column_avg_occupancy_build
    )
    row_general_peak = create_row(group=group_avg_occupancy, name="General Peak Traffic")
    create_field_column(
        field=create_field(row=row_general_peak, name="General Peak Traffic No Build", cell="AVOPeakNB"),
        column=column_avg_occupancy_no_build
    )
    create_field_column(
        field=create_field(row=row_general_peak, name="General Peak Traffic Build", cell="AVOPeakB"),
        column=column_avg_occupancy_build
    )
    row_high_occupancy = create_row(group=group_avg_occupancy, name="High Occupancy Vehicle")
    create_field_column(
        field=create_field(row=row_high_occupancy, name="High Occupancy Vehicle No Build", cell="AVOHovNB"),
        column=column_avg_occupancy_no_build
    )
    create_field_column(
        field=create_field(row=row_high_occupancy, name="High Occupancy Vehicle Build", cell="AVOHovB"),
        column=column_avg_occupancy_build
    )

    group_annual_agency_costs = create_group(subsection=subsection_rail, name="Annual Transit Agency Costs (if TMS project)")
    column_group_annual_agency_costs = create_column_group(group=group_annual_agency_costs)
    column_annual_agency_costs_no_build = create_column(column_group=column_group_annual_agency_costs, name="No Build")
    column_annual_agency_costs_build = create_column(column_group=column_group_annual_agency_costs, name="Build")
    row_capital_expenditure = create_row(group=group_annual_agency_costs, name="Capital Expenditure")
    create_field_column(field=create_field(row=row_capital_expenditure, name="Capital Expenditure No Build", unit="$", cell="1) Project Information!P52"), column=column_annual_agency_costs_no_build)
    create_field_column(field=create_field(row=row_capital_expenditure, name="Capital Expenditure Build", unit="$", cell="1) Project Information!Q52"), column=column_annual_agency_costs_build)
    row_ops_maint_expenditure =  create_row(group=group_annual_agency_costs, name="Ops. & Maint. Expenditure")
    create_field_column(field=create_field(row=row_ops_maint_expenditure, name="Ops. & Maint. Expenditure No Build", unit="$", cell="1) Project Information!P53"), column=column_annual_agency_costs_no_build)
    create_field_column(field=create_field(row=row_ops_maint_expenditure, name="Ops. & Maint. Expenditure Build", unit="$", cell="1) Project Information!Q53"), column=column_annual_agency_costs_build)

    group_costs_summary = create_group(subsection=subsection_project_costs, name="Summary", is_summary=True)
    row_costs_summary = create_row(group=group_costs_summary)
    create_field(row=row_costs_summary, name="Total Mitigation", cell="1) Project Information!AB44", display_type=FieldDisplayType.READ_ONLY)
    create_field(row=row_costs_summary, name="Total Transit Agency Cost Savings", cell="1) Project Information!AC44", display_type=FieldDisplayType.READ_ONLY)
    create_field(row=row_costs_summary, name="Total Costs in Constant Dollars", cell="1) Project Information!AD44", unit="$", display_type=FieldDisplayType.READ_ONLY)
    create_field(row=row_costs_summary, name="Total Costs as Present Value", cell="1) Project Information!AE44", unit="$", display_type=FieldDisplayType.READ_ONLY)

    group_construction_period_costs = create_group(subsection=subsection_project_costs, name="Construction Period Costs")
    column_group_initial_costs = create_column_group(group=group_construction_period_costs, name="Direct Project Initial Costs")
    column_project_support = create_column(column_group=column_group_initial_costs, name="Project Support")
    column_right_of_way = create_column(column_group=column_group_initial_costs, name="Right Of Way")
    column_construction = create_column(column_group=column_group_initial_costs, name="Construction")
    column_group_construction_period_costs = create_column_group(group=group_construction_period_costs, name="")
    column_mitigation = create_column(column_group=column_group_construction_period_costs, name="Mitigation")
    column_agency_savings = create_column(column_group=column_group_construction_period_costs, name="Transit AGY Cost SVGS")
    column_group_dollar_cost = create_column_group(group=group_construction_period_costs, name="Cost (in Dollars)")
    column_constant_dollars = create_column(column_group=column_group_dollar_cost, name="Constant Dollars")
    column_present_value = create_column(column_group=column_group_dollar_cost, name="Present Value")
    row_construction_period_costs_1 = create_row(group=group_construction_period_costs, name="Yr 1")
    create_field_column(field=create_field(row=row_construction_period_costs_1, name="Project Support Yr 1", cell="1) Project Information!W15"), column=column_project_support)
    create_field_column(field=create_field(row=row_construction_period_costs_1, name="Right of Way Yr 1", cell="1) Project Information!X15"), column=column_right_of_way)
    create_field_column(field=create_field(row=row_construction_period_costs_1, name="Construction Yr 1",
                                           cell="1) Project Information!Y15"), column=column_construction)
    create_field_column(field=create_field(row=row_construction_period_costs_1, name="Mitigation Yr 1",
                                           cell="1) Project Information!AB15"), column=column_mitigation)
    create_field_column(field=create_field(row=row_construction_period_costs_1, name="Transit Agy Cost Svgs Yr 1",
                                           cell="1) Project Information!AC15"), column=column_agency_savings)
    create_field_column(field=create_field(row=row_construction_period_costs_1, name="Constant Dollars Yr 1",
                                           cell="1) Project Information!AD15", display_type=FieldDisplayType.READ_ONLY), column=column_constant_dollars)
    create_field_column(field=create_field(row=row_construction_period_costs_1, name="Present Value Yr 1",
                                           cell="1) Project Information!AE15", display_type=FieldDisplayType.READ_ONLY),
                        column=column_present_value)
    row_construction_period_costs_2 = create_row(group=group_construction_period_costs, name="Yr 2")
    create_field_column(field=create_field(row=row_construction_period_costs_2, name="Project Support Yr 2", cell="1) Project Information!W16"), column=column_project_support)
    create_field_column(field=create_field(row=row_construction_period_costs_2, name="Right of Way Yr 2", cell="1) Project Information!X16"), column=column_right_of_way)
    create_field_column(field=create_field(row=row_construction_period_costs_2, name="Construction Yr 2",
                                           cell="1) Project Information!Y16"), column=column_construction)
    create_field_column(field=create_field(row=row_construction_period_costs_2, name="Mitigation Yr 2",
                                           cell="1) Project Information!AB16"), column=column_mitigation)
    create_field_column(field=create_field(row=row_construction_period_costs_2, name="Transit Agy Cost Svgs Yr 2",
                                           cell="1) Project Information!AC16"), column=column_agency_savings)
    create_field_column(field=create_field(row=row_construction_period_costs_2, name="Constant Dollars Yr 2",
                                           cell="1) Project Information!AD16", display_type=FieldDisplayType.READ_ONLY), column=column_constant_dollars)
    create_field_column(field=create_field(row=row_construction_period_costs_2, name="Present Value Yr 2",
                                           cell="1) Project Information!AE16", display_type=FieldDisplayType.READ_ONLY),
                        column=column_present_value)
    row_construction_period_costs_total = create_row(group=group_construction_period_costs, name="Total")
    create_field_column(field=create_field(row=row_construction_period_costs_total, name="Project Support Total", cell="1) Project Information!W44", display_type=FieldDisplayType.READ_ONLY), column=column_project_support)
    create_field_column(field=create_field(row=row_construction_period_costs_total, name="Right of Way Total", cell="1) Project Information!X44", display_type=FieldDisplayType.READ_ONLY), column=column_right_of_way)
    create_field_column(field=create_field(row=row_construction_period_costs_total, name="Construction Total",
                                           cell="1) Project Information!Y44", display_type=FieldDisplayType.READ_ONLY), column=column_construction)
    create_field_column(field=create_field(row=row_construction_period_costs_total, name="Mitigation Total",
                                           cell="1) Project Information!AB44", display_type=FieldDisplayType.READ_ONLY), column=column_mitigation)
    create_field_column(field=create_field(row=row_construction_period_costs_total, name="Transit Agy Cost Svgs Total",
                                           cell="1) Project Information!AC44", display_type=FieldDisplayType.READ_ONLY), column=column_agency_savings)
    create_field_column(field=create_field(row=row_construction_period_costs_total, name="Constant Dollars Total",
                                           cell="1) Project Information!AD44", display_type=FieldDisplayType.READ_ONLY), column=column_constant_dollars)
    create_field_column(field=create_field(row=row_construction_period_costs_total, name="Present Value Total",
                                           cell="1) Project Information!AE44", display_type=FieldDisplayType.READ_ONLY),
                        column=column_present_value)
