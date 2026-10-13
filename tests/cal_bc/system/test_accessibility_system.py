
import pytest
from django.contrib.auth.models import User
from django.test import Client
from playwright.sync_api import Page
from pytest_playwright_axe import Axe

from cal_bc.models.models.model import (
    FieldDisplayType,
    Group,
    GroupDisplayType,
    Model,
    Section,
    Subsection,
    Version,
)
from tests.channels_live_server_helper import ChannelsLiveServer


@pytest.mark.vcr
@pytest.mark.django_db(transaction=True)
class TestAccessibilitySystem:
    @pytest.fixture
    def user(self) -> User:
        return User.objects.create_user(username="caltrans")

    @pytest.fixture
    def session_id(self, client: Client, user: User) -> bytes:
        client.force_login(user)
        return client.cookies["sessionid"].value

    @pytest.fixture
    def cookie(self, channels_live_server: ChannelsLiveServer, session_id: bytes) -> dict:
        return {
            "name": "sessionid",
            "value": session_id,
            "secure": False,
            "url": channels_live_server.http_url,
        }

    @pytest.fixture
    def first_window(self, page: Page, cookie: dict) -> Page:
        first_window = page
        first_window.context.add_cookies([cookie])
        return first_window

    @pytest.fixture
    def model(self) -> Model:
        return Model.objects.create(name="Cal-B/C Sketch", description="Best for early-stage highway or transit projects.", tags=["Transit", "Commuter Rail"])

    @pytest.fixture
    def version(self, model: Model) -> Version:
        return model.version_set.create(
            name="8.1",
            url="https://dot.ca.gov/-/media/dot-media/programs/transportation-planning/documents/new-state-planning/transportation-economics/cal-bc/2023-cal-bc/2023-non-federal-model/cal-bc-8-1-sketch-a11y.xlsm",
        )

    @pytest.fixture
    def section(self, version: Version) -> Section:
        return version.section_set.create(name="Project Information", code="1")

    @pytest.fixture
    def subsection_1A(self, section: Section) -> Subsection:
        return section.subsection_set.create(
            name="Project Data",
            code="A",
            description="This subsection contains the project data.",
            guide="All fields in this step are required."
        )

    @pytest.fixture(autouse=True)
    def group_1A_general_info(self, subsection_1A: Subsection) -> None:
        group = subsection_1A.group_set.create(
            name="General Information",
            description="This is the general information group.",
            position=1
        )
        row_1 = group.row_set.create(
            position=1,
            guide="Enter a descriptive name for your project."
        )
        row_1.field_set.create(name="Project Name", cell="ProjName", display_type=FieldDisplayType.REQUIRED)
        field_district = row_1.field_set.create(name="District", cell="1) Project Information!E2", display_type=FieldDisplayType.REQUIRED)
        field_district.choice_set.create(
            name="District 4 - Bay Area / Oakland",
            value="District 4",
        )

    @pytest.fixture(autouse=True)
    def group_1A_project_data(self, subsection_1A: Subsection) -> Group:
        group = subsection_1A.group_set.create(
            name="Project Data",
            description="Configure project analysis settings.",
            position=2
        )
        row_1 = group.row_set.create(position=1)
        field_project_type = row_1.field_set.create(name="Project Type", cell="ProjType", display_type=FieldDisplayType.REQUIRED)
        field_project_type.choice_set.create(
            name="General Highway",
            value="    General Highway",
        )

        row_2 = group.row_set.create(position=2)
        field_project_location = row_2.field_set.create(name="Project Location", cell="ProjLoc", display_type=FieldDisplayType.REQUIRED)
        field_project_location.choice_set.create(
            name="NorCal",
            value="2",
        )

        row_3 = group.row_set.create(position=3)
        row_3.field_set.create(name="Length of Construction Period", cell="Construct", unit="years", display_type=FieldDisplayType.REQUIRED)


    @pytest.fixture
    def subsection_1B(self, section: Section) -> Subsection:
        return section.subsection_set.create(
            name="Highway Design and Traffic Data",
            code="B",
        )

    @pytest.fixture(autouse=True)
    def group_1B_highway_design(self, subsection_1B: Subsection) -> None:
        group = subsection_1B.group_set.create(name="Highway Design", position=1)
        column_group = group.columngroup_set.create()
        column_no_build = column_group.column_set.create(name="No Build")
        column_build = column_group.column_set.create(name="Build")

        row_number_general_traffic_lanes = group.row_set.create(name="Number of General Traffic Lanes", position=1)
        column_no_build.fieldcolumn_set.create(field = row_number_general_traffic_lanes.field_set.create(name="Number of General Traffic Lanes No Build", cell="GenLanesNB", display_type=FieldDisplayType.REQUIRED))
        column_build.fieldcolumn_set.create(field=row_number_general_traffic_lanes.field_set.create(name="Number of General Traffic Lanes Build", cell="GenLanesB", display_type=FieldDisplayType.REQUIRED))

        row_number_hov = group.row_set.create(name="Number of HOV/HOT Lanes", position=2)
        column_no_build.fieldcolumn_set.create(field=row_number_hov.field_set.create(name="Number of HOV/HOT Lanes No Build", cell="HOVLanesNB", display_type=FieldDisplayType.REQUIRED))
        column_build.fieldcolumn_set.create(field=row_number_hov.field_set.create(name="Number of HOV/HOT Lanes Build", cell="HOVLanesB", display_type=FieldDisplayType.REQUIRED))

        row_hov_restriction = group.row_set.create(name="HOV Restriction", position=3)
        column_no_build.fieldcolumn_set.create(field=row_hov_restriction.field_set.create(name="HOV Restriction No Build", cell="HOVRest", display_type=FieldDisplayType.REQUIRED))

        row_highway_freeflow = group.row_set.create(name="Highway Free-Flow Speed", position=4)
        column_no_build.fieldcolumn_set.create(field=row_highway_freeflow.field_set.create(name="Highway Free-Flow Speed No Build", cell="FFSpeedNB", display_type=FieldDisplayType.REQUIRED))

        row_highway_segment_length = group.row_set.create(name="Highway Segment Length", position=5)
        column_no_build.fieldcolumn_set.create(field=row_highway_segment_length.field_set.create(name="Highway Segment Length No Build", cell="SegmentNB", display_type=FieldDisplayType.REQUIRED))

    @pytest.fixture(autouse=True)
    def group_1B_average_daily_traffic(self, subsection_1B: Subsection) -> None:
        group = subsection_1B.group_set.create(name="Average Daily Traffic", position=2)
        column_group = group.columngroup_set.create()
        column_no_build = column_group.column_set.create(name="No Build")
        column_build = column_group.column_set.create(name="Build")

        row_current = group.row_set.create(name="Current", position=1)
        row_current.field_set.create(name="Current", cell="ADT0", display_type=FieldDisplayType.REQUIRED)

        row_base = group.row_set.create(name="Base (Year 1)", position=2)
        column_no_build.fieldcolumn_set.create(field=row_base.field_set.create(name="Base No Build", cell="ADT1NB", display_type=FieldDisplayType.REQUIRED))
        column_build.fieldcolumn_set.create(field=row_base.field_set.create(name="Base Build", cell="ADT1B", display_type=FieldDisplayType.REQUIRED))

        row_forecast = group.row_set.create(name="Forecast (Year 20)", position=3)
        column_no_build.fieldcolumn_set.create(field=row_forecast.field_set.create(name="Forecast No Build", cell="ADT20NB", display_type=FieldDisplayType.REQUIRED))
        column_build.fieldcolumn_set.create(field=row_forecast.field_set.create(name="Forecast Build", cell="ADT20B", display_type=FieldDisplayType.REQUIRED))

    @pytest.fixture
    def subsection_1E(self, section: Section) -> Subsection:
        return section.subsection_set.create(name="Project Costs", code="E", guide="Subsection 1E Help")

    @pytest.fixture(autouse=True)
    def group_1E_summary(self, subsection_1E: Subsection) -> None:
        group = subsection_1E.group_set.create(name="Summary", is_summary=True)
        row = group.row_set.create()
        row.field_set.create(name="Total Project Support", cell="1) Project Information!W44", unit="$", position=1)
        row.field_set.create(name="Total Construction", cell="1) Project Information!Y44", unit="$", position=2)

    @pytest.fixture(autouse=True)
    def group_1E_costs(self, subsection_1E: Subsection) -> None:
        group = subsection_1E.group_set.create(name="Construction Period Costs", guide="Construction Period Costs Instructions")
        column_group_direct_initial = group.columngroup_set.create(name="Direct Project Initial Costs", position=1)
        column_project_support = column_group_direct_initial.column_set.create(name="Project Support", position=1)
        column_construction = column_group_direct_initial.column_set.create(name="Construction", position=2)
        column_group_costs = group.columngroup_set.create(name="Costs (in Dollars)", position=2)
        column_constant_dollars = column_group_costs.column_set.create(name="Constant Dollars", position=1)
        column_present_value = column_group_costs.column_set.create(name="Present Value", position=2)

        row = group.row_set.create(name="Yr 1", position=1)
        field_project_support_yr_1 = row.field_set.create(name="Project Support Year 1", cell="1) Project Information!W15", position=1, display_type=FieldDisplayType.REQUIRED)
        column_project_support.fieldcolumn_set.create(field=field_project_support_yr_1)
        field_construction_yr_1 = row.field_set.create(name="Construction Year 1", cell="1) Project Information!Y15", position=2, display_type=FieldDisplayType.REQUIRED)
        column_construction.fieldcolumn_set.create(field=field_construction_yr_1)
        field_constant_dollars_yr_1 = row.field_set.create(name="Constant Dollars Year 1", cell="1) Project Information!AD15", position=3, unit="$", display_type=FieldDisplayType.READ_ONLY)
        column_constant_dollars.fieldcolumn_set.create(field=field_constant_dollars_yr_1)
        field_present_value_yr_1 = row.field_set.create(name="Present Value Year 1", cell="1) Project Information!AE15", position=4, unit="$", display_type=FieldDisplayType.READ_ONLY)
        column_present_value.fieldcolumn_set.create(field=field_present_value_yr_1)

    @pytest.fixture
    def section_3(self, version: Version) -> Section:
        return version.section_set.create(code="3", name="Investment Analysis")

    @pytest.fixture
    def subsection_3(self, section_3: Section) -> Subsection:
        return section_3.subsection_set.create(code="A", name="Investment Analysis")

    @pytest.fixture(autouse=True)
    def group_3_summary(self, subsection_3: Subsection) -> None:
        group = subsection_3.group_set.create(name="Investment Analysis Summary", display_type=GroupDisplayType.SUMMARY)
        row = group.row_set.create()
        row.field_set.create(name="Life-Cycle Costs (mil. $)", cell="3) Results!H13", unit="$", display_type=FieldDisplayType.READ_ONLY)
        row.field_set.create(name="Life-Cycle Benefits (mil. $)", cell="3) Results!H14", unit="$", display_type=FieldDisplayType.READ_ONLY)
        row.field_set.create(name="Benefit / Cost Ratio", cell="BeneCostRatio", display_type=FieldDisplayType.READ_ONLY)
        group_2 = subsection_3.group_set.create(name="Emissions Reduction")
        row_2 = group_2.row_set.create()
        row_2.field_set.create(name="Emission Cost Savings Passenger", cell="3) Results!O18", display_type=FieldDisplayType.READ_ONLY)

    def test_accessibility(self, first_window: Page, channels_live_server: ChannelsLiveServer):
        axe = Axe()
        msg = "Accessibility violations found. Check the report in 'axe-reports/'."

        first_window.goto(channels_live_server.http_url)
        axe_check = axe.run(first_window, filename="accessibility_report")
        assert len(axe_check["violations"]) == 0, f"{len(axe_check["violations"])} {msg}"

        first_window.get_by_role("link", name="New project").click()
        axe_check = axe.run(first_window, filename="accessibility_report")
        assert len(axe_check["violations"]) == 0, f"{len(axe_check["violations"])} {msg}"

        first_window.get_by_role("button", name="Start project").click()
        axe_check = axe.run(first_window, filename="accessibility_report")
        assert len(axe_check["violations"]) == 0, f"{len(axe_check["violations"])} {msg}"

        first_window.get_by_role("button", name="Save draft").click()
        axe_check = axe.run(first_window, filename="accessibility_report")
        assert len(axe_check["violations"]) == 0, f"{len(axe_check["violations"])} {msg}"

        first_window.get_by_label("Project Name").click()
        axe_check = axe.run(first_window, filename="accessibility_report")
        assert len(axe_check["violations"]) == 0, f"{len(axe_check["violations"])} {msg}"

        first_window.get_by_label("Project Name").fill("Geary Boulevard Light Rail")
        first_window.get_by_label("District").select_option("District 4 - Bay Area / Oakland")
        first_window.get_by_label("Project Type").select_option("General Highway")
        first_window.get_by_label("Project Location").select_option("NorCal")
        first_window.get_by_label("Length of Construction Period").fill("1")
        first_window.get_by_role("button", name="Save draft").click()
        axe_check = axe.run(first_window, filename="accessibility_report")
        assert len(axe_check["violations"]) == 0, f"{len(axe_check["violations"])} {msg}"

        first_window.get_by_role("button", name="Continue to Subsection 1B").click()
        axe_check = axe.run(first_window, filename="accessibility_report")
        assert len(axe_check["violations"]) == 0, f"{len(axe_check["violations"])} {msg}"

        first_window.get_by_label("Number of General Traffic Lanes No Build").fill("10")
        first_window.get_by_label("Number of General Traffic Lanes Build").fill("4")
        first_window.get_by_label("Number of HOV/HOT Lanes No Build").fill("0")
        first_window.get_by_label("Number of HOV/HOT Lanes Build").fill("2")
        first_window.get_by_label("HOV Restriction No Build").fill("3")
        first_window.get_by_label("Highway Free-Flow Speed No Build").fill("55")
        first_window.get_by_label("Highway Segment Length No Build").fill("30")
        first_window.get_by_label("Current").fill("500000")
        first_window.get_by_label("Base No Build").fill("500000")
        first_window.get_by_label("Base Build").fill("300000")
        first_window.get_by_label("Forecast No Build").fill("600000")
        first_window.get_by_label("Forecast Build").fill("400000")

        first_window.get_by_role("button", name="Continue to Subsection 1E").click()
        axe_check = axe.run(first_window, filename="accessibility_report")
        assert len(axe_check["violations"]) == 0, f"{len(axe_check["violations"])} {msg}"

        first_window.get_by_label("Project Support Year 1").fill("3000000")
        first_window.get_by_label("Construction Year 1").fill("1")

        first_window.get_by_role("button", name="Continue to Subsection 3").click()
        axe_check = axe.run(first_window, filename="accessibility_report")
        assert len(axe_check["violations"]) == 0, f"{len(axe_check["violations"])} {msg}"

        first_window.get_by_role("link", name="Exit Project").click()
        axe_check = axe.run(first_window, filename="accessibility_report")
        assert len(axe_check["violations"]) == 0, f"{len(axe_check["violations"])} {msg}"

        first_window.get_by_role("button", name="User").click()
        axe_check = axe.run(first_window, filename="accessibility_report")
        assert len(axe_check["violations"]) == 0, f"{len(axe_check["violations"])} {msg}"

        first_window.get_by_text("Sign out").click()
        axe_check = axe.run(first_window, filename="accessibility_report")
        assert len(axe_check["violations"]) == 0, f"{len(axe_check["violations"])} {msg}"

        first_window.close()
