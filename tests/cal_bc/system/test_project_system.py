
import pytest
from django.contrib.auth.models import User
from django.test import Client
from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import CreateContextCallback

from cal_bc.models.models.model import (
    Field,
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
    def subsection_1(self, section: Section) -> Subsection:
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
    def group_1(self, subsection_1: Subsection) -> Group:
        return subsection_1.group_set.create(name="General Information", description="All fields are required.")

    @pytest.fixture
    def group_1_row_1(self, group_1: Group) -> Row:
        return group_1.row_set.create(
            position=1,
            guide="""
                # Project Name
                Enter a name for your project.
            """
        )

    @pytest.fixture(autouse=True)
    def project_name(self, group_1_row_1: Row) -> Field:
        return group_1_row_1.field_set.create(name="Project Name", cell="ProjName")

    @pytest.fixture
    def group_1_row_2(self, group_1: Group) -> Row:
        return group_1.row_set.create(position=2)

    @pytest.fixture(autouse=True)
    def district_field(self, group_1_row_2: Row) -> Field:
        return group_1_row_2.field_set.create(name="District", cell="1) Project Information!E2")

    @pytest.fixture
    def subsection_2(self, section: Section) -> Subsection:
        return section.subsection_set.create(name="Traffic Data", code="B")

    @pytest.fixture
    def group_2(self, subsection_2: Subsection) -> Group:
        return subsection_2.group_set.create(name="Project Costs")

    @pytest.fixture
    def group_2_row_1(self, group_2: Group) -> Row:
        return group_2.row_set.create()

    @pytest.fixture(autouse=True)
    def current_daily_traffic(self, group_2_row_1: Row) -> Field:
        return group_2_row_1.field_set.create(name="Year 1 Project Support", cell="1) Project Information!W15", unit="$")

    @pytest.fixture(autouse=True)
    def base_daily_traffic(self, group_2_row_1: Row) -> Field:
        return group_2_row_1.field_set.create(name="Total Project Support", cell="1) Project Information!W44", unit="$", read_only=True)

    @pytest.fixture(autouse=True)
    def district_4(self, district_field: Field) -> Value:
        return district_field.value_set.create(
            name="District 4 - Bay Area / Oakland",
            value="District 4",
        )

    def test_projects(self, first_page: Page, second_page: Page, channels_live_server: ChannelsLiveServer):
        first_page.goto(channels_live_server.http_url)
        expect(first_page.locator("body")).to_contain_text("My Cal B/C Projects")

        second_page.goto(channels_live_server.http_url)
        expect(second_page.locator("body")).to_contain_text("My Cal B/C Projects")

        first_page.get_by_role("link", name="New project").click()
        first_page.get_by_role("button", name="Start project").click()
        expect(first_page.locator("body")).to_contain_text(
            "All fields in this step are required"
        )

        first_page.get_by_label("Project Name").click()
        expect(first_page.locator("body")).to_contain_text(
            "Enter a name for your project"
        )
        first_page.get_by_label("Project Name").fill("Geary Boulevard Light Rail")
        first_page.get_by_label("District").select_option(
            "District 4 - Bay Area / Oakland"
        )

        expect(second_page.locator("body")).to_contain_text("Hypothetical Project")
        first_page.get_by_role("button", name="Save draft").click()
        expect(second_page.locator("body")).to_contain_text("Geary Boulevard Light Rail")

        second_page.get_by_role("link", name="Edit").click()

        expect(first_page.locator("body")).to_contain_text("Project successfully saved!")
        first_page.get_by_role("link", name="Projects").click()
        expect(first_page.locator("body")).to_contain_text("1 projects")
        expect(first_page.locator("body")).to_contain_text("Geary Boulevard Light Rail")
        first_page.get_by_role("link", name="Edit").click()
        first_page.get_by_label("Project Name").fill("New Geary Boulevard Light Rail")
        first_page.get_by_role("button", name="Continue to Subsection 1B").click()

        expect(second_page.get_by_label("Project Name")).to_have_value("New Geary Boulevard Light Rail", timeout=240_000)

        first_page.get_by_role("button", name="Save draft").click()
        expect(first_page.locator("body")).to_contain_text("This field is required")
        expect(first_page.get_by_label("Year 1 Project Support").locator("//following-sibling::span")).to_contain_text("$")
        first_page.get_by_label("Year 1 Project Support").fill("10")
        expect(first_page.get_by_label("Total Project Support").locator("//following-sibling::span")).to_contain_text("$")
        expect(first_page.get_by_label("Total Project Support")).to_be_disabled()
        expect(first_page.get_by_label("Total Project Support")).to_have_value("0.0")
        first_page.get_by_role("button", name="Save draft").click()
        expect(first_page.get_by_label("Total Project Support")).to_have_value("10.0")

        first_page.get_by_role("button", name="Back to Subsection 1A").click()
        first_page.get_by_role("button", name="1A - Project Data").click()
        first_page.get_by_role("menuitem", name="1B. Traffic Data").click()
        first_page.get_by_role("link", name="Projects").click()
        expect(first_page.locator("body")).to_contain_text(
            "New Geary Boulevard Light Rail"
        )

        first_page.on("dialog", lambda dialog: dialog.accept())
        first_page.get_by_role("button", name="Delete").click()
        expect(first_page.locator("body")).to_contain_text("0 projects")
        first_page.get_by_role("button", name="User").click()
        first_page.get_by_text("Sign out").click()
        expect(first_page.locator("body")).to_contain_text("Sign in with Microsoft")
        first_page.close()
