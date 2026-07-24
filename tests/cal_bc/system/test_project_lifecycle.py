from pathlib import Path

import pytest
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from playwright.sync_api import Page, expect

from cal_bc.models.models.model import (
    Field,
    Group,
    Model,
    Row,
    Section,
    Subsection,
    Value,
    Version,
)


@pytest.mark.vcr
class TestProjectLifecycle(StaticLiveServerTestCase):
    @pytest.fixture(autouse=True)
    def setup(self, page: Page, tmp_path: Path):
        self.page = page
        self.tmp_path = tmp_path
        user = User.objects.create_user(username="caltrans")
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
        model = Model.objects.create(
            name="Cal-B/C Sketch",
        )
        version = Version.objects.create(
            model=model,
            name="8.1",
            url="https://dot.ca.gov/-/media/dot-media/programs/transportation-planning/documents/new-state-planning/transportation-economics/cal-bc/2023-cal-bc/2023-non-federal-model/cal-bc-8-1-sketch-a11y.xlsm",
        )
        section = Section.objects.create(
            version=version,
            name="Project Information",
            code="1",
        )
        subsection_1 = Subsection.objects.create(
            section=section,
            name="Project Data",
            code="A",
            guide="""
                # Setup Help
                All fields in this step are required.
            """,
        )
        group_1 = Group.objects.create(
            subsection=subsection_1, name="General Information", position=1
        )
        group_1_row_1 = Row.objects.create(
            group=group_1,
            position=1,
            guide="""
                # Project Name
                Enter a name for your project.
            """,
        )
        Field.objects.create(row=group_1_row_1, name="Project Name", position=1)
        group_1_row_2 = Row.objects.create(group=group_1, position=2)
        state_field = Field.objects.create(row=group_1_row_2, name="State", position=1)
        Value.objects.create(field=state_field, name="California", position=1)
        district_field = Field.objects.create(
            row=group_1_row_2, name="District", position=2
        )
        Value.objects.create(
            field=district_field,
            name="District 4 - Bay Area / Oakland",
            value="District 4",
            position=1,
        )
        subsection_2 = Subsection.objects.create(
            section=section, name="Traffic Data", code="B"
        )
        group_2 = Group.objects.create(
            subsection=subsection_2, name="Average daily traffic", position=1
        )
        group_2_row_1 = Row.objects.create(group=group_2, position=1)
        Field.objects.create(row=group_2_row_1, name="Cars per hour", position=1)

    def test_projects(self):
        self.page.goto(f"{self.live_server_url}/")
        expect(self.page.locator("body")).to_contain_text("My Cal B/C Projects")
        self.page.get_by_role("link", name="New project").click()
        self.page.get_by_role("button", name="Start project").click()
        expect(self.page.locator("body")).to_contain_text(
            "All fields in this step are required"
        )
        self.page.get_by_label("Project Name").click()
        expect(self.page.locator("body")).to_contain_text(
            "Enter a name for your project"
        )
        self.page.get_by_label("Project Name").fill("Geary Boulevard Light Rail")
        self.page.get_by_label("State").select_option("California")
        self.page.get_by_label("District").select_option(
            "District 4 - Bay Area / Oakland"
        )
        self.page.get_by_role("button", name="Save draft").click()
        expect(self.page.locator("body")).to_contain_text("Project successfully saved!")
        self.page.get_by_role("link", name="Projects").click()
        expect(self.page.locator("body")).to_contain_text("1 projects")
        expect(self.page.locator("body")).to_contain_text("Geary Boulevard Light Rail")
        self.page.get_by_role("link", name="Edit").click()
        self.page.get_by_label("Project Name").fill("New Geary Boulevard Light Rail")
        self.page.get_by_role("button", name="Save draft").click()
        self.page.get_by_role("button", name="1A - Project Data").click()
        self.page.get_by_role("menuitem", name="1B. Traffic Data").click()
        self.page.get_by_label("Cars per hour").fill("333")
        self.page.get_by_role("button", name="Save draft").click()
        self.page.get_by_role("link", name="Projects").click()
        expect(self.page.locator("body")).to_contain_text(
            "New Geary Boulevard Light Rail"
        )
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.page.get_by_role("button", name="Delete").click()
        expect(self.page.locator("body")).to_contain_text("0 projects")
        self.page.get_by_role("button", name="User").click()
        self.page.get_by_text("Sign out").click()
        expect(self.page.locator("body")).to_contain_text("Sign in with Microsoft")
        self.page.close()
