
import pytest
from django.contrib.auth.models import User
from django.test import Client
from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import CreateContextCallback
from pytest_playwright_axe import Axe

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
    def subsection_2(self, section: Section) -> Subsection:
        return section.subsection_set.create(name="Traffic Data", code="B")

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

    @pytest.fixture
    def group_1_row_2(self, group_1: Group) -> Row:
        return group_1.row_set.create(position=2)

    @pytest.fixture
    def group_2(self, subsection_2: Subsection) -> Group:
        return subsection_2.group_set.create(name="Average daily traffic")

    @pytest.fixture
    def group_2_row_1(self, group_2: Group) -> Row:
        return group_2.row_set.create()

    @pytest.fixture(autouse=True)
    def project_name(self, group_1_row_1: Row) -> Field:
        return group_1_row_1.field_set.create(name="Project Name", cell="ProjName")

    @pytest.fixture(autouse=True)
    def district_field(self, group_1_row_2: Row) -> Field:
        return group_1_row_2.field_set.create(name="District", cell="1) Project Information!E2")

    @pytest.fixture(autouse=True)
    def cars_per_hour(self, group_2_row_1: Row) -> Field:
        return group_2_row_1.field_set.create(name="Annual Capital Expenditure", cell="ADT0", unit="$")

    @pytest.fixture(autouse=True)
    def district_4(self, district_field: Field) -> Value:
        return district_field.value_set.create(
            name="District 4 - Bay Area / Oakland",
            value="District 4",
        )

    def test_accessibility(self, first_page: Page, channels_live_server: ChannelsLiveServer):
        axe = Axe()
        msg = "Accessibility violations found. Check the report in 'axe-reports/'."

        first_page.goto(channels_live_server.http_url)
        axe_check = axe.run(first_page, filename="accessibility_report")
        assert len(axe_check["violations"]) == 0, f"{len(axe_check["violations"])} {msg}"

        first_page.get_by_role("link", name="New project").click()
        axe_check = axe.run(first_page, filename="accessibility_report")
        assert len(axe_check["violations"]) == 0, f"{len(axe_check["violations"])} {msg}"

        first_page.get_by_role("button", name="Start project").click()
        axe_check = axe.run(first_page, filename="accessibility_report")
        assert len(axe_check["violations"]) == 0, f"{len(axe_check["violations"])} {msg}"
        first_page.get_by_label("Project Name").fill("Geary Boulevard Light Rail")

        first_page.get_by_role("button", name="Continue to Subsection 1B").click()
        axe_check = axe.run(first_page, filename="accessibility_report")
        assert len(axe_check["violations"]) == 0, f"{len(axe_check["violations"])} {msg}"

        first_page.get_by_role("link", name="Projects").click()
        axe_check = axe.run(first_page, filename="accessibility_report")
        assert len(axe_check["violations"]) == 0, f"{len(axe_check["violations"])} {msg}"

        first_page.get_by_role("button", name="User").click()
        axe_check = axe.run(first_page, filename="accessibility_report")
        assert len(axe_check["violations"]) == 0, f"{len(axe_check["violations"])} {msg}"

        first_page.get_by_text("Sign out").click()
        axe_check = axe.run(first_page, filename="accessibility_report")
        assert len(axe_check["violations"]) == 0, f"{len(axe_check["violations"])} {msg}"

        first_page.close()
