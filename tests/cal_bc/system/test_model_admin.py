from pathlib import Path

import pytest
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from playwright.sync_api import Page


class TestModelAdmin(StaticLiveServerTestCase):
    @pytest.fixture(autouse=True)
    def setup(self, page: Page, tmp_path: Path):
        self.page = page
        self.tmp_path = tmp_path
        user = User.objects.create_superuser(username="caltrans")
        self.client.force_login(user)
        cookie = self.client.cookies["sessionid"]
        self.page.context.add_cookies(
            [
                {
                    "name": "sessionid",
                    "value": cookie.value,
                    "secure": False,
                    "url": self.live_server_url,
                }
            ]
        )

    def test_model_admin(self):
        self.page.goto(f"{self.live_server_url}/admin/")
        self.page.wait_for_selector("text=Django administration")

        self.page.locator(".app-models").get_by_role(
            "rowheader", name="Models"
        ).get_by_role("link", name="Models", exact=True).click()
        self.page.get_by_role("link", name="Add model").click()
        self.page.get_by_label("Name").fill("Sketch")
        self.page.get_by_role("button", name="Save", exact=True).click()
        self.page.wait_for_selector("text=The model “Sketch” was added successfully")

        self.page.get_by_role("link", name="Home").click()
        self.page.locator(".app-models").get_by_role(
            "link", name="Versions", exact=True
        ).click()
        self.page.get_by_role("link", name="Add version").click()
        self.page.get_by_label("Name").first.fill("8.1")
        self.page.get_by_label("Url").fill("https://example.com")
        self.page.get_by_label("Model").select_option("Sketch")
        self.page.get_by_role("button", name="Save", exact=True).click()
        self.page.wait_for_selector(
            "text=The version “Sketch v8.1” was added successfully"
        )

        self.page.get_by_role("link", name="Home").click()
        self.page.locator(".app-models").get_by_role(
            "link", name="Versions", exact=True
        ).click()
        self.page.get_by_role("link", name="Sketch v8.1", exact=True).click()
        self.page.locator(":text('Section: #1') + fieldset").get_by_label("Name").nth(
            0
        ).fill("Project Information")
        self.page.locator(":text('Section: #1') + fieldset").get_by_label("Code").nth(
            0
        ).fill("1")
        self.page.locator(":text('Subsection: #1') + fieldset").get_by_label(
            "Name"
        ).nth(0).fill("Project Data")
        self.page.locator(":text('Subsection: #1') + fieldset").get_by_label(
            "Code"
        ).nth(0).fill("A")
        self.page.locator(":text('Subsection: #1') + fieldset").get_by_label(
            "Guide"
        ).locator("~ [contenteditable]").nth(0).fill(
            "Add basic project infomration here"
        )
        self.page.locator(":text('Groups') ~ table tbody tr").nth(0).locator("td").nth(
            1
        ).locator("input").fill("General Information")
        self.page.get_by_role("button", name="Save", exact=True).click()
        self.page.wait_for_selector(
            "text=The version “Sketch v8.1” was changed successfully"
        )

        self.page.get_by_role("link", name="Home").click()
        self.page.locator(".app-models").get_by_role(
            "link", name="Groups", exact=True
        ).click()
        self.page.get_by_role(
            "link", name="Sketch v8.1 § 1A General Information", exact=True
        ).click()
        self.page.locator(":text('Row: #1') + fieldset").get_by_label("Guide").locator(
            "~ [contenteditable]"
        ).fill("Complete this section")
        self.page.locator(":text('Field: #1') + fieldset").get_by_label("Name").nth(
            0
        ).fill("District")
        self.page.locator(":text('Field: #1') + fieldset").get_by_label("Cell").nth(
            0
        ).fill("ProjLoc")
        self.page.get_by_role("link", name="Add another Value").click()
        self.page.locator(":text('Values') ~ table tbody tr").nth(0).locator("td").nth(
            1
        ).locator("input").fill("District 4 - Bay Area")
        self.page.locator(":text('Values') ~ table tbody tr").nth(0).locator("td").nth(
            2
        ).locator("input").fill("District 4")
        self.page.get_by_role("button", name="Save", exact=True).click()
        self.page.wait_for_selector(
            "text=The group “Sketch v8.1 § 1A General Information” was changed successfully"
        )

        self.page.close()
