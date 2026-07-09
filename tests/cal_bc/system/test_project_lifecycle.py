from pathlib import Path
import pytest

from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from playwright.sync_api import Page

from cal_bc.models.models.model import Model, Version, Section, Subsection, Group, Row, Field, Value


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
        subsection = Subsection.objects.create(
            section=section,
            name="Project Data",
            code="A",
        )
        group = Group.objects.create(
            subsection=subsection,
            name="General Information",
            position=1
        )
        row_1 = Row.objects.create(
            group=group,
            position=1
        )
        Field.objects.create(
            row=row_1,
            name="Project Name",
            position=1
        )
        row_2 = Row.objects.create(
            group=group,
            position=2
        )
        state_field = Field.objects.create(
            row=row_2,
            name="State",
            position=1
        )
        Value.objects.create(
            field=state_field,
            name="California",
            position=1
        )
        district_field = Field.objects.create(
            row=row_2,
            name="District",
            position=2
        )
        Value.objects.create(
            field=district_field,
            name="District 4 - Bay Area / Oakland",
            value="District 4",
            position=1
        )

    def test_projects(self):
        self.page.goto(f"{self.live_server_url}/")
        self.page.wait_for_selector("text=My Cal B/C Analyses")
        self.page.get_by_role("link", name="New analysis").click()
        self.page.get_by_role("button", name="Cal-B/C Sketch v8.1").click()
        self.page.get_by_label("Project Name").fill("Geary Boulevard Light Rail")
        self.page.get_by_label("State").select_option("California")
        self.page.get_by_label("District").select_option(
            "District 4 - Bay Area / Oakland"
        )
        self.page.get_by_role("button", name="Save draft").click()
        self.page.wait_for_selector("text=Project successfully saved!")
        self.page.wait_for_selector("text=Project successfully saved!")
        self.page.get_by_role("button", name="User").click()
        self.page.wait_for_selector("text=Sign out").click()
        self.page.wait_for_selector("text=Sign in with Microsoft")
        self.page.close()
