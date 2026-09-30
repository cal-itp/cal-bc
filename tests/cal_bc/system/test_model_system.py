
import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse_lazy
from playwright.sync_api import Page
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
        page.set_viewport_size({ "width": 1440, "height": 900 })
        return page

    def test_models(self, first_page: Page, channels_live_server: ChannelsLiveServer) -> None:
        first_page.goto(f"{channels_live_server.http_url}{reverse_lazy('admin:index')}")
        first_page.wait_for_selector("text=Site administration")

        first_page.locator(".app-models").get_by_role(
            "rowheader", name="Models"
        ).get_by_role("link", name="Models", exact=True).click()
        first_page.get_by_role("link", name="Add model").click()
        first_page.get_by_label("Name").fill("Sketch")
        first_page.get_by_label("Description").fill("Caltrans’s California Benefit/Cost Analysis tool")
        first_page.get_by_label("Tags").fill("Highway, Transit")
        first_page.get_by_role("button", name="Save", exact=True).click()
        first_page.wait_for_selector(
            "text=The model “Sketch” was added successfully."
        )
        first_page.locator("nav").get_by_role("link", name="Versions").click()
        first_page.get_by_role("link", name="Add version").click()
        first_page.get_by_label("Name").first.fill("8.1")
        first_page.get_by_label("Url").fill("https://example.com")
        first_page.get_by_label("Model").select_option("Sketch")
        first_page.get_by_role("button", name="Save and continue editing").click()
        first_page.wait_for_selector(
            "text=The version “8.1” was added successfully. You may edit it again below."
        )
        first_page.locator("#id_section_set-0-code").fill("1")
        first_page.locator("#id_section_set-0-name").fill("Project Information")
        first_page.locator("#id_section_set-0-subsection_set-0-code").fill("A")
        first_page.locator("#id_section_set-0-subsection_set-0-name").fill("Project Data")
        first_page.locator("#id_section_set-0-subsection_set-0-description").fill("This is the main info.")
        first_page.get_by_label("Guide").locator("~ [contenteditable]").nth(0).fill(
            "Add basic project information here"
        )
        first_page.get_by_role("button", name="Save", exact=True).click()
        first_page.wait_for_selector(
            "text=The version “8.1” was changed successfully."
        )
        first_page.locator("nav").get_by_role("link", name="Subsections").click()
        first_page.get_by_role("link", name="Project Data").click()
        first_page.locator("#id_group_set-0-name").fill("General Information")
        first_page.get_by_role("link", name="Add another Group").click()
        first_page.locator("#id_group_set-1-name").fill("Project Data")
        first_page.locator("#id_group_set-1-description").fill("Configure project analysis settings.")
        first_page.get_by_role("button", name="Save", exact=True).click()
        first_page.wait_for_selector(
            "text=The subsection “A - Project Data” was changed successfully."
        )
        first_page.locator("nav").get_by_role("link", name="communities Groups").click()
        first_page.get_by_role("link", name="General Information").click()
        first_page.get_by_role("link", name="Rows").click()
        first_page.get_by_label("Guide").locator("~ [contenteditable]").fill("Complete this section")
        first_page.locator("#id_row_set-0-field_set-0-name").fill("District")
        first_page.locator("#id_row_set-0-field_set-0-cell").fill("ProjLoc")
        first_page.get_by_role("link", name="Add another Field").click()
        first_page.locator("#id_row_set-0-field_set-1-name").fill("Project Name")
        first_page.locator("#id_row_set-0-field_set-1-cell").fill("ProjName")
        first_page.get_by_role("button", name="Save", exact=True).click()
        first_page.wait_for_selector(
            "text=The group “1 - General Information” was changed successfully"
        )
        first_page.get_by_role("link", name="Project Data").click()
        first_page.get_by_role("link", name="Rows").click()
        first_page.locator("#id_row_set-0-name").fill("Length of Construction Period")
        first_page.locator("#id_row_set-0-field_set-0-name").fill("Length of Construction Period")
        first_page.locator("#id_row_set-0-field_set-0-cell").fill("Construct")
        first_page.locator("#id_row_set-0-field_set-0-unit").fill("years")
        first_page.locator("#id_row_set-0-field_set-0-display_type").select_option("Not Required")
        first_page.get_by_role("link", name="Add another row").click()
        first_page.locator("#id_row_set-1-name").fill("Length of Peak Period(s)")
        first_page.locator("#id_row_set-1-field_set-0-name").fill("Length of Peak Period(s)")
        first_page.locator("#id_row_set-1-field_set-0-cell").fill("1) Project Information!F17")
        first_page.locator("#id_row_set-1-field_set-0-unit").fill("hours")
        first_page.locator("#id_row_set-1-field_set-0-display_type").select_option("Read-Only")
        first_page.get_by_role("button", name="Save", exact=True).click()
        first_page.wait_for_selector(
            "text=The group “1 - Project Data” was changed successfully"
        )
        first_page.locator("nav").get_by_role("link", name="variable_insert Fields").click()
        first_page.get_by_role("link", name="District").click()
        first_page.locator("#id_value_set-0-name").fill("District 1 - Eureka")
        first_page.locator("#id_value_set-0-value").fill("1")
        first_page.get_by_role("link", name="Add another Value").click()
        first_page.locator("#id_value_set-1-name").fill("District 4 - Bay Area")
        first_page.locator("#id_value_set-1-value").fill("4")
        first_page.get_by_role("button", name="Save", exact=True).click()
        first_page.wait_for_selector(
            "text=The field “1 - District” was changed successfully"
        )
        first_page.get_by_role("link", name="Length of Construction Period").click()
        first_page.locator("#id_fieldrange-0-max_value").press_sequentially("10")
        first_page.get_by_role("button", name="Save", exact=True).click()
        first_page.wait_for_selector(
            "text=The field “1 - Length of Construction Period (years)” was changed successfully"
        )
        first_page.close()
