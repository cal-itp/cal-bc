import os.path
from pathlib import Path
import pytest

from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from playwright.sync_api import Page

from cal_bc.projects.models.model_version import ModelVersion


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
        ModelVersion.objects.create(
            name="Cal-B/C Sketch",
            version="8.1",
            url="https://dot.ca.gov/-/media/dot-media/programs/transportation-planning/documents/new-state-planning/transportation-economics/cal-bc/2023-cal-bc/2023-non-federal-model/cal-bc-8-1-sketch-a11y.xlsm",
        )

    def test_projects(self):
        self.page.goto(f"{self.live_server_url}/")
        self.page.wait_for_selector("text=Cal B/C")
        self.page.get_by_role("link", name="Sign in with Microsoft").click()
        self.page.wait_for_selector("text=Projects")
        self.page.get_by_role("link", name="New Project").click()
        self.page.get_by_label("Project Name").fill("Geary Boulevard Light Rail")
        self.page.get_by_label("Model Version").select_option("Cal-B/C Sketch v8.1")
        self.page.get_by_label("District").select_option(
            "District 4 - Bay Area / Oakland"
        )
        self.page.get_by_label("Project Type").select_option("Light Rail (LRT)")
        self.page.get_by_label("Project Location").select_option("Northern California")
        self.page.get_by_label("Length of Construction Period").fill("3")
        self.page.get_by_label("One- or Two-Way Data").select_option("Two-Way")
        self.page.get_by_label("Length of Peak Period(s) (up to 24 hrs)").fill("3")
        self.page.get_by_role("button", name="Save Project").click()
        self.page.wait_for_selector("text=Cal-B/C Sketch v8.1")
        self.page.get_by_role("link", name="Show").click()
        self.page.wait_for_selector("text=Life-Cycle Costs")
        self.page.wait_for_selector("text=$136.6")
        with self.page.expect_download() as download_info:
            self.page.get_by_role("link", name="Download").click()
        download = download_info.value
        filename = self.tmp_path / download.suggested_filename
        download.save_as(filename)
        assert os.path.exists(filename)
        self.page.get_by_role("button", name="Sign out caltrans").click()
        assert self.page.get_by_role("link", name="Sign in with Microsoft")
        self.page.close()
