import pytest
from django.contrib.auth.models import User
from django.test import Client
from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import CreateContextCallback

from cal_bc.models.models.model import (
    Column,
    ColumnGroup,
    Field,
    FieldDisplayType,
    Group,
    Model,
    Row,
    Section,
    Subsection,
    Version,
)
from cal_bc.projects.models.project import Value
from tests.channels_live_server_helper import ChannelsLiveServer


@pytest.mark.vcr
@pytest.mark.django_db(transaction=True)
class TestProjectSystem:
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
    def first_page(self, page: Page, cookie: dict) -> Page:
        first_page = page
        first_page.context.add_cookies([cookie])
        return first_page

    @pytest.fixture
    def second_page(self, cookie: dict, new_context: CreateContextCallback) -> Page:
        second_page = new_context().new_page()
        second_page.context.add_cookies([cookie])
        return second_page

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
            guide="""
                # Setup Help
                All fields in this step are required.
            """,
        )

    @pytest.fixture
    def general_info_1A_group(self, subsection_1A: Subsection) -> Group:
        return subsection_1A.group_set.create(
            name="General Information",
            description="This is the general information group.",
            position=1
        )

    @pytest.fixture
    def general_info_1A_group_row_1(self, general_info_1A_group: Group) -> Row:
        return general_info_1A_group.row_set.create(
            position=1,
            guide="""
                # Project Name
                Enter a descriptive name for your project.
            """
        )

    @pytest.fixture(autouse=True)
    def project_name_field(self, general_info_1A_group_row_1: Row) -> Field:
        return general_info_1A_group_row_1.field_set.create(name="Project Name", cell="ProjName")

    @pytest.fixture
    def general_info_1A_group_row_2(self, general_info_1A_group: Group) -> Row:
        return general_info_1A_group.row_set.create(position=2)

    @pytest.fixture
    def district_field(self, general_info_1A_group_row_2: Row) -> Field:
        return general_info_1A_group_row_2.field_set.create(name="District", cell="ProjLoc")

    @pytest.fixture(autouse=True)
    def district_4_value(self, district_field: Field) -> Value:
        return district_field.value_set.create(
            name="District 4 - Bay Area / Oakland",
            value="District 4",
        )

    @pytest.fixture
    def project_data_1A_group(self, subsection_1A: Subsection) -> Group:
        return subsection_1A.group_set.create(
            name="Project Data",
            description="Configure project analysis settings.",
            position=2
        )
    
    @pytest.fixture
    def project_data_1A_group_row(self, project_data_1A_group: Group) -> Row:
        return project_data_1A_group.row_set.create(position=5)

    @pytest.fixture(autouse=True)
    def length_peak_period_field(self, project_data_1A_group_row: Row) -> Field:
        return project_data_1A_group_row.field_set.create(name="Length of Peak Period(s)", cell="1) Project Information!F17", unit="hours", position=1, display_type=FieldDisplayType.READ_ONLY)

    @pytest.fixture
    def subsection_1E(self, section: Section) -> Subsection:
        return section.subsection_set.create(name="Project Costs", code="E")

    @pytest.fixture
    def summary_1E_group(self, subsection_1E: Subsection) -> Group:
        return subsection_1E.group_set.create(name="Summary", is_summary=True)

    @pytest.fixture
    def summary_1E_group_row(self, summary_1E_group: Group) -> Row:
        return summary_1E_group.row_set.create()

    @pytest.fixture(autouse=True)
    def total_project_support_summary_field(self, summary_1E_group_row: Row) -> Field:
        return summary_1E_group_row.field_set.create(name="Total Project Support", cell="1) Project Information!W44", unit="$", position=1)

    @pytest.fixture(autouse=True)
    def total_construction_summary_field(self, summary_1E_group_row: Row) -> Field:
        return summary_1E_group_row.field_set.create(name="Total Construction", cell="1) Project Information!Y44", unit="$", position=2)

    @pytest.fixture
    def costs_1E_group(self, subsection_1E: Subsection) -> Group:
        return subsection_1E.group_set.create(name="Construction Period Costs")

    @pytest.fixture(autouse=True)
    def costs_1E_group_project_column_group(self, costs_1E_group: Group) -> ColumnGroup:
        return costs_1E_group.columngroup_set.create(name="Direct Project Initial Costs", position=1)

    @pytest.fixture
    def costs_1E_group_project_column(self, costs_1E_group_project_column_group: ColumnGroup) -> Column:
        return costs_1E_group_project_column_group.column_set.create(name="Project Support", position=1)

    @pytest.fixture
    def costs_1E_group_construction_column(self, costs_1E_group_project_column_group: ColumnGroup) -> Column:
        return costs_1E_group_project_column_group.column_set.create(name="Construction", position=2)

    @pytest.fixture
    def costs_1E_group_costs_column_group(self, costs_1E_group: Group) -> ColumnGroup:
        return costs_1E_group.columngroup_set.create(name="Costs (in Dollars)", position=2)

    @pytest.fixture
    def costs_1E_group_constant_column(self, costs_1E_group_costs_column_group: ColumnGroup) -> Column:
        return costs_1E_group_costs_column_group.column_set.create(name="Constant Dollars", position=1)

    @pytest.fixture
    def costs_1E_group_present_column(self, costs_1E_group_costs_column_group: ColumnGroup) -> Column:
        return costs_1E_group_costs_column_group.column_set.create(name="Present Value", position=2)

    @pytest.fixture
    def costs_1E_group_year_1_row(self, costs_1E_group: Group) -> Row:
        return costs_1E_group.row_set.create(name="Yr 1", position=1)

    @pytest.fixture(autouse=True)
    def year_one_project_support_field(self, costs_1E_group_year_1_row: Row, costs_1E_group_project_column: Column) -> Field:
        field = costs_1E_group_year_1_row.field_set.create(name="Project Support Year 1", cell="1) Project Information!W15", position=1, display_type=FieldDisplayType.REQUIRED)
        costs_1E_group_project_column.fieldcolumn_set.create(field=field)
        return field

    @pytest.fixture(autouse=True)
    def year_one_construction_field(self, costs_1E_group_year_1_row: Row, costs_1E_group_construction_column: Column) -> Field:
        field = costs_1E_group_year_1_row.field_set.create(name="Construction Year 1", cell="1) Project Information!Y15", position=2, display_type=FieldDisplayType.REQUIRED)
        costs_1E_group_construction_column.fieldcolumn_set.create(field=field)
        return field

    @pytest.fixture(autouse=True)
    def year_one_constant_field(self, costs_1E_group_year_1_row: Row, costs_1E_group_constant_column: Column) -> Field:
        field = costs_1E_group_year_1_row.field_set.create(name="Constant Dollars Year 1", cell="1) Project Information!AD15", position=3, unit="$", display_type=FieldDisplayType.READ_ONLY)
        costs_1E_group_constant_column.fieldcolumn_set.create(field=field)
        return field

    @pytest.fixture(autouse=True)
    def year_one_present_field(self, costs_1E_group_year_1_row: Row, costs_1E_group_present_column: Column) -> Field:
        field = costs_1E_group_year_1_row.field_set.create(name="Present Value Year 1", cell="1) Project Information!AE15", position=4, unit="$", display_type=FieldDisplayType.READ_ONLY)
        costs_1E_group_present_column.fieldcolumn_set.create(field=field)
        return field

    @pytest.fixture
    def costs_1E_group_year_2_row(self, costs_1E_group: Group) -> Row:
        return costs_1E_group.row_set.create(name="Yr 2", position=2)

    @pytest.fixture(autouse=True)
    def year_two_project_support_field(self, costs_1E_group_year_2_row: Row, costs_1E_group_project_column: Column) -> Field:
        field = costs_1E_group_year_2_row.field_set.create(name="Project Support Year 2", cell="1) Project Information!W16", position=1, display_type=FieldDisplayType.NOT_REQUIRED)
        costs_1E_group_project_column.fieldcolumn_set.create(field=field)
        return field

    @pytest.fixture(autouse=True)
    def year_two_construction_field(self, costs_1E_group_year_2_row: Row, costs_1E_group_construction_column: Column) -> Field:
        field = costs_1E_group_year_2_row.field_set.create(name="Construction Year 2", cell="1) Project Information!Y16", position=2, display_type=FieldDisplayType.NOT_REQUIRED)
        costs_1E_group_construction_column.fieldcolumn_set.create(field=field)
        return field

    @pytest.fixture(autouse=True)
    def year_two_constant_field(self, costs_1E_group_year_2_row: Row, costs_1E_group_constant_column: Column) -> Field:
        field = costs_1E_group_year_2_row.field_set.create(name="Constant Dollars Year 2", cell="1) Project Information!AD16", position=3, unit="$", display_type=FieldDisplayType.READ_ONLY)
        costs_1E_group_constant_column.fieldcolumn_set.create(field=field)
        return field

    @pytest.fixture(autouse=True)
    def year_two_present_field(self, costs_1E_group_year_2_row: Row, costs_1E_group_present_column: Column) -> Field:
        field = costs_1E_group_year_2_row.field_set.create(name="Present Value Year 2", cell="1) Project Information!AE16", position=4, unit="$", display_type=FieldDisplayType.READ_ONLY)
        costs_1E_group_present_column.fieldcolumn_set.create(field=field)
        return field

    def test_projects(self, first_page: Page, second_page: Page, channels_live_server: ChannelsLiveServer):
        first_page.goto(channels_live_server.http_url)
        expect(first_page.locator("body")).to_contain_text("My Cal B/C Projects")

        second_page.goto(channels_live_server.http_url)
        expect(second_page.locator("body")).to_contain_text("My Cal B/C Projects")
        expect(first_page.locator("body")).to_contain_text("0 projects")

        first_page.get_by_role("link", name="New project").click()
        first_page.get_by_role("button", name="Start project").click()
        expect(first_page.locator("h1")).to_contain_text("1A. Project Data")
        expect(first_page.locator("h2").first).to_contain_text("General Information")
        expect(first_page.locator("body")).to_contain_text("This subsection contains the project data.")
        expect(first_page.locator("body")).to_contain_text("All fields in this step are required.")
        expect(first_page.locator("h2").nth(1)).to_contain_text("Project Data")
        expect(first_page.locator("body")).to_contain_text("Configure project analysis settings.")

        first_page.get_by_label("Project Name").click()
        expect(first_page.locator("body")).to_contain_text("Enter a descriptive name for your project.")
        expect(first_page.locator("dl dt").filter(has_text="Length of Peak Period(s)").locator("xpath=following-sibling::dd[1]")).to_contain_text("5 hours")

        first_page.get_by_role("button", name="Save draft").click()
        expect(first_page.locator("body")).to_contain_text("Select District.")

        expect(second_page.locator("body")).to_contain_text("Hypothetical Project", timeout=10_000)
        first_page.get_by_label("Project Name").fill("Geary Boulevard Light Rail")
        first_page.get_by_label("District").select_option("District 4 - Bay Area / Oakland")
        first_page.get_by_role("button", name="Save draft").click()
        expect(first_page.locator("body")).to_contain_text("Project successfully saved!")
        expect(second_page.locator("body")).to_contain_text("Geary Boulevard Light Rail")

        first_page.get_by_label("Project Name").fill("New Geary Boulevard Light Rail", timeout=10_000)
        first_page.get_by_role("button", name="Continue to Subsection 1E").click()
        expect(first_page.locator("body")).to_contain_text("Project successfully saved!")

        expect(second_page.locator("body")).to_contain_text("1 projects")
        second_page.get_by_role("link", name="Edit").click()
        expect(second_page.get_by_label("Project Name")).to_have_value("New Geary Boulevard Light Rail")

        expect(first_page.locator("dl dt").filter(has_text="Total Project Support").locator("xpath=following-sibling::dd[1]")).to_contain_text("$0")
        expect(first_page.locator("dl dt").filter(has_text="Total Construction").locator("xpath=following-sibling::dd[1]")).to_contain_text("$0")
        expect(first_page.locator("body")).to_contain_text("Yr 1*")
        expect(first_page.locator("dl dt").filter(has_text="Constant Dollars Year 1").locator("xpath=following-sibling::dd[1]")).to_contain_text("$0")
        expect(first_page.locator("dl dt").filter(has_text="Present Value Year 1").locator("xpath=following-sibling::dd[1]")).to_contain_text("$0")
        expect(first_page.locator("body")).to_contain_text("Yr 2")
        expect(first_page.locator("dl dt").filter(has_text="Constant Dollars Year 2").locator("xpath=following-sibling::dd[1]")).to_contain_text("$0")
        expect(first_page.locator("dl dt").filter(has_text="Present Value Year 2").locator("xpath=following-sibling::dd[1]")).to_contain_text("$0")
        
        first_page.get_by_role("button", name="Back to Subsection 1A").click()
        expect(first_page.locator("body")).to_contain_text("Enter Project Support Year 1, Enter Construction Year 1.")

        first_page.get_by_label("Project Support Year 1").fill("10000")
        first_page.get_by_label("Construction Year 1").fill("12000")
        first_page.get_by_label("Project Support Year 2").fill("15000")
        first_page.get_by_role("button", name="Save draft").click()
        expect(first_page.locator("body")).to_contain_text("Project successfully saved!")
        expect(first_page.locator("dl dt").filter(has_text="Total Project Support").locator("xpath=following-sibling::dd[1]")).to_contain_text("$25,000")
        expect(first_page.locator("dl dt").filter(has_text="Total Construction").locator("xpath=following-sibling::dd[1]")).to_contain_text("$12,000")
        expect(first_page.locator("dl dt").filter(has_text="Constant Dollars Year 1").locator("xpath=following-sibling::dd[1]")).to_contain_text("$22,000,000")
        expect(first_page.locator("dl dt").filter(has_text="Present Value Year 1").locator("xpath=following-sibling::dd[1]")).to_contain_text("$22,000,000")
        expect(first_page.locator("dl dt").filter(has_text="Constant Dollars Year 2").locator("xpath=following-sibling::dd[1]")).to_contain_text("$15,000,000")
        expect(first_page.locator("dl dt").filter(has_text="Present Value Year 2").locator("xpath=following-sibling::dd[1]")).to_contain_text("$14,423,076.92")

        first_page.get_by_role("button", name="Back to Subsection 1A").click()
        expect(first_page.locator("body")).to_contain_text("Project successfully saved!")

        first_page.get_by_role("button", name="1A - Project Data").click()
        first_page.get_by_role("menuitem", name="1E. Project Costs").click()
        expect(first_page.locator("dl dt").filter(has_text="Total Project Support").locator("xpath=following-sibling::dd[1]")).to_contain_text("25,000")

        first_page.get_by_role("button", name="Exit Project").click()
        first_page.get_by_role("link", name="Discard").click()
        expect(first_page.locator("body")).to_contain_text("New Geary Boulevard Light Rail")
        expect(first_page.locator("body")).to_contain_text("1 projects")
        first_page.on("dialog", lambda dialog: dialog.accept())
        first_page.get_by_role("button", name="Delete").click()
        expect(first_page.locator("body")).to_contain_text("0 projects")

        first_page.get_by_role("button", name="User").click()
        first_page.get_by_text("Sign out").click()
        expect(first_page.locator("body")).to_contain_text("Sign in with Microsoft")
        second_page.close()
        first_page.close()
