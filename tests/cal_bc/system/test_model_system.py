
import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse_lazy
from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import CreateContextCallback

from tests.channels_live_server_helper import ChannelsLiveServer


@pytest.mark.django_db(transaction=True)
class TestModelSystem:
    @pytest.fixture
    def user(self) -> User:
        return User.objects.create_superuser(username="caltrans")

    @pytest.fixture
    def session_id(self, client: Client, user: User) -> bytes:
        client.force_login(user)
        return client.cookies["sessionid"].value

    @pytest.fixture
    def session_cookie(self, channels_live_server: ChannelsLiveServer, session_id: bytes) -> dict:
        return {
            "name": "sessionid",
            "value": session_id,
            "secure": False,
            "url": channels_live_server.http_url,
        }

    @pytest.fixture
    def first_page(self, session_cookie: dict, new_context: CreateContextCallback) -> Page:
        page = new_context().new_page()
        page.context.add_cookies([session_cookie])
        return page

    def test_models(self, first_page: Page, channels_live_server: ChannelsLiveServer) -> None:
        first_page.goto(f"{channels_live_server.http_url}{reverse_lazy('admin:index')}")
        first_page.wait_for_selector("text=Django administration")

        first_page.locator(".app-models").get_by_role(
            "rowheader", name="Models"
        ).get_by_role("link", name="Models", exact=True).click()
        first_page.get_by_role("link", name="Add model").click()
        first_page.get_by_label("Name").fill("Sketch")
        first_page.get_by_label("Description").fill("Caltrans’s California Benefit/Cost Analysis tool")
        first_page.get_by_label("Tags").fill("Highway, Transit")
        first_page.get_by_role("button", name="Save", exact=True).click()
        first_page.wait_for_selector("text=The model “Sketch” was added successfully")

        first_page.get_by_role("link", name="Home").click()
        first_page.locator(".app-models").get_by_role(
            "link", name="Versions", exact=True
        ).click()
        first_page.get_by_role("link", name="Add version").click()
        first_page.get_by_label("Name").first.fill("8.1")
        first_page.get_by_label("Url").fill("https://example.com")
        first_page.get_by_label("Model").select_option("Sketch")
        first_page.get_by_role("button", name="Save", exact=True).click()
        first_page.wait_for_selector(
            "text=The version “8.1” was added successfully"
        )

        first_page.get_by_role("link", name="Home").click()
        first_page.locator(".app-models").get_by_role(
            "link", name="Versions", exact=True
        ).click()
        first_page.get_by_role("link", name="8.1", exact=True).click()
        first_page.locator(":text('Section: #1') + fieldset").get_by_label("Name").nth(
            0
        ).fill("Project Information")
        first_page.locator(":text('Section: #1') + fieldset").get_by_label("Code").nth(
            0
        ).fill("1")
        first_page.locator(":text('Subsection: #1') + fieldset").get_by_label(
            "Name"
        ).nth(0).fill("Project Data")
        first_page.locator(":text('Subsection: #1') + fieldset").get_by_label(
            "Code"
        ).nth(0).fill("A")
        first_page.locator(":text('Subsection: #1') + fieldset").get_by_label(
            "Description"
        ).nth(0).fill("This is the main info.")
        first_page.locator(":text('Subsection: #1') + fieldset").get_by_label(
            "Guide"
        ).locator("~ [contenteditable]").nth(0).fill(
            "Add basic project information here"
        )
        first_page.locator(":text('Groups') ~ table tbody tr").nth(0).locator("td").nth(
            1
        ).locator("input").fill("General Information")
        first_page.get_by_role("button", name="Save", exact=True).click()
        first_page.wait_for_selector(
            "text=The version “8.1” was changed successfully"
        )

        first_page.get_by_role("link", name="Home").click()
        first_page.locator(".app-models").get_by_role(
            "link", name="Groups", exact=True
        ).click()
        first_page.get_by_role(
            "link", name="General Information", exact=True
        ).click()
        first_page.locator(":text('Row: #1') + fieldset").get_by_label("Guide").locator(
            "~ [contenteditable]"
        ).fill("Complete this section")
        first_page.locator(":text('Field: #1') + fieldset").get_by_label("Name").nth(
            0
        ).fill("District")
        first_page.locator(":text('Field: #1') + fieldset").get_by_label("Cell").nth(
            0
        ).fill("ProjLoc")
        first_page.get_by_role("link", name="Add another Value").click()
        first_page.locator(":text('Values') ~ table tbody tr").nth(0).locator("td").nth(
            1
        ).locator("input").fill("District 4 - Bay Area")
        first_page.locator(":text('Values') ~ table tbody tr").nth(0).locator("td").nth(
            2
        ).locator("input").fill("District 4")

        first_page.get_by_role("link", name="Add another Field", exact=True).click()
        first_page.locator(":text('Field: #2') + fieldset").get_by_label("Name").nth(
            0
        ).fill("Project Name")
        first_page.locator(":text('Field: #2') + fieldset").get_by_label("Cell").nth(
            0
        ).fill("ProjName")
        first_page.get_by_role("link", name="Add another Field Range").nth(1).click()
        expect(first_page.locator(":text('Field range') ~ table tbody tr").nth(0).locator("td").nth(
            1
        ).locator("input")).to_have_value("0")
        first_page.locator(":text('Field range') ~ table tbody tr").nth(0).locator("td").nth(
            1
        ).locator("input").press_sequentially("20")
        first_page.locator(":text('Field range') ~ table tbody tr").nth(0).locator("td").nth(
            2
        ).locator("input").press_sequentially("50")
        first_page.get_by_role("button", name="Save", exact=True).click()
        first_page.wait_for_selector(
            "text=The group “General Information” was changed successfully"
        )
        first_page.get_by_role("link", name="Add group").click()
        first_page.get_by_label("subsection").select_option("A - Project Data")
        first_page.get_by_label("Name").nth(0).fill("Project Data")
        first_page.get_by_label("Description").fill("Configure project analysis settings.")
        first_page.locator(":text('Field: #1') + fieldset").get_by_label("Name").nth(
            0
        ).fill("Length of Construction Period")
        first_page.locator(":text('Field: #1') + fieldset").get_by_label("Cell").nth(
            0
        ).fill("1) Project Information!F14")
        first_page.locator(":text('Field: #1') + fieldset").get_by_label("Unit").nth(
            0
        ).fill("years")
        first_page.get_by_role("button", name="Save", exact=True).click()
        first_page.wait_for_selector(
            "text=The group “Project Data” was added successfully"
        )

        first_page.close()
