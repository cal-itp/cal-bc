from pathlib import Path

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
    def page(self, session_cookie: dict, new_context: CreateContextCallback) -> Page:
        page = new_context().new_page()
        page.context.add_cookies([session_cookie])
        return page

    @pytest.fixture
    def cal_bc_sketch_xls(self) -> str:
        return str(Path(__file__).resolve().parent.parent.parent / "fixtures" / "cal-bc-8-1-sketch-a11y.xlsm")

    def test_models(self, page: Page, channels_live_server: ChannelsLiveServer, cal_bc_sketch_xls: str) -> None:
        page.goto(f"{channels_live_server.http_url}{reverse_lazy('admin:index')}")
        page.wait_for_selector("text=Cal-B/C Admin")
        page.wait_for_selector("text=Site administration")

        page.locator(".app-models").get_by_role(
            "rowheader", name="Models"
        ).get_by_role("link", name="Models", exact=True).click()
        page.get_by_role("link", name="Add model").click()
        page.get_by_label("Name").fill("Sketch")
        page.get_by_label("Description").fill("Caltrans’s California Benefit/Cost Analysis tool")
        page.get_by_label("Tags").fill("Highway, Transit")
        page.get_by_role("button", name="Save", exact=True).click()
        page.wait_for_selector("text=The model “Sketch” was added successfully")

        page.locator(".app-models").get_by_role(
            "link", name="Versions", exact=True
        ).click()
        page.get_by_role("link", name="Add version").click()
        page.get_by_label("Model").select_option("Sketch")
        page.get_by_label("Name").first.fill("8.1")
        page.get_by_label("Url").fill("https://dot.ca.gov/-/media/dot-media/programs/transportation-planning/documents/new-state-planning/transportation-economics/cal-bc/2023-cal-bc/2023-non-federal-model/cal-bc-8-1-sketch-a11y.xlsm")

        page.get_by_role("link", name="Add another Version File").click()
        with page.expect_file_chooser() as file_chooser:
            page.get_by_role("button", name="Choose File").click()
            file_chooser.value.set_files(cal_bc_sketch_xls)

        page.get_by_role("button", name="Save", exact=True).click()
        page.wait_for_selector(
            "text=The version “8.1” was added successfully"
        )

        page.locator(".app-models").get_by_role(
            "link", name="Versions", exact=True
        ).click()
        page.get_by_role("link", name="8.1", exact=True).click()
        page.locator(":text('Section: #1') + fieldset").get_by_label("Code").nth(
            0
        ).fill("1")
        page.locator(":text('Section: #1') + fieldset").get_by_label("Name").nth(
            0
        ).fill("Project Information")
        page.locator(":text('Subsection: #1') + fieldset").get_by_label(
            "Code"
        ).nth(0).fill("A")
        page.locator(":text('Subsection: #1') + fieldset").get_by_label(
            "Name"
        ).nth(0).fill("Project Data")
        page.locator(":text('Subsection: #1') + fieldset").get_by_label(
            "Description"
        ).nth(0).fill("This is the main info.")
        page.locator(":text('Subsection: #1') + fieldset").get_by_label(
            "Guide"
        ).locator("~ [contenteditable]").nth(0).fill(
            "Add basic project information here"
        )
        page.locator(":text('Groups') ~ table tbody tr").nth(0).locator("td").nth(
            1
        ).locator("input").fill("General Information")
        page.get_by_role("button", name="Save", exact=True).click()
        page.wait_for_selector(
            "text=The version “8.1” was changed successfully"
        )

        page.get_by_role("link", name="Home").click()
        page.locator(".app-models").get_by_role(
            "link", name="Groups", exact=True
        ).click()
        page.get_by_role(
            "link", name="General Information", exact=True
        ).click()
        page.locator(":text('Row: #1') + fieldset").get_by_label("Guide").locator(
            "~ [contenteditable]"
        ).fill("Complete this section")
        page.locator(":text('Field: #1') + fieldset").get_by_label("Name").nth(
            0
        ).fill("District")
        page.locator(":text('Field: #1') + fieldset").get_by_label("Cell").nth(
            0
        ).fill("ProjLoc")
        page.get_by_role("link", name="Add another Choice").click()
        page.locator(":text('Choices') ~ table tbody tr").nth(0).locator("td").nth(
            1
        ).locator("input").fill("District 4 - Bay Area")
        page.locator(":text('Choices') ~ table tbody tr").nth(0).locator("td").nth(
            2
        ).locator("input").fill("District 4")

        page.get_by_role("link", name="Add another Field", exact=True).click()
        page.locator(":text('Field: #2') + fieldset").get_by_label("Name").nth(
            0
        ).fill("Project Name")
        page.locator(":text('Field: #2') + fieldset").get_by_label("Cell").nth(
            0
        ).fill("ProjName")
        page.get_by_role("link", name="Add another Field Range").nth(1).click()
        expect(page.locator(":text('Field range') ~ table tbody tr").nth(0).locator("td").nth(
            1
        ).locator("input")).to_have_value("0")
        page.locator(":text('Field range') ~ table tbody tr").nth(0).locator("td").nth(
            1
        ).locator("input").press_sequentially("20")
        page.locator(":text('Field range') ~ table tbody tr").nth(0).locator("td").nth(
            2
        ).locator("input").press_sequentially("50")
        page.get_by_role("button", name="Save", exact=True).click()
        page.wait_for_selector(
            "text=The group “1 - General Information” was changed successfully"
        )

        page.get_by_role("link", name="Add group").click()
        page.get_by_label("subsection").select_option("A - Project Data")
        page.get_by_label("Name").nth(0).fill("Project Data")
        page.get_by_label("Description").fill("Configure project analysis settings.")
        page.locator(":text('Field: #1') + fieldset").get_by_label("Name").nth(
            0
        ).fill("Length of Construction Period")
        page.locator(":text('Field: #1') + fieldset").get_by_label("Cell").nth(
            0
        ).fill("1) Project Information!F14")
        page.locator(":text('Field: #1') + fieldset").get_by_label("Unit").nth(
            0
        ).fill("years")
        expect(page.locator(":text('Field: #1') + fieldset").get_by_label("Display Type").nth(
            0
        )).to_contain_text("Required")

        page.get_by_role("link", name="Add another row").click()
        page.locator(":text('Field: #1') + fieldset").nth(1).get_by_label("Name").nth(
            0
        ).fill("One- or Two-Way Data")
        page.locator(":text('Field: #1') + fieldset").nth(1).get_by_label("Cell").nth(
            0
        ).fill("1) Project Information!F15")
        page.locator(":text('Field: #1') + fieldset").nth(1).get_by_label("Display Type").nth(
            0
        ).select_option("Not Required")

        page.get_by_role("link", name="Add another row").click()
        page.locator(":text('Field: #1') + fieldset").nth(2).get_by_label("Name").nth(
            0
        ).fill("Length of Peak Period(s)")
        page.locator(":text('Field: #1') + fieldset").nth(2).get_by_label("Cell").nth(
            0
        ).fill("1) Project Information!F17")
        page.locator(":text('Field: #1') + fieldset").nth(2).get_by_label("Unit").nth(
            0
        ).fill("hours")
        page.locator(":text('Field: #1') + fieldset").nth(2).get_by_label("Display Type").nth(
            0
        ).select_option("Read-Only")
        page.get_by_role("button", name="Save", exact=True).click()
        page.wait_for_selector(
            "text=The group “1 - Project Data” was added successfully"
        )

        page.close()
