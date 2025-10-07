import pytest
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from playwright.sync_api import Page
from cal_bc.projects.models import Project


class TestProjects(StaticLiveServerTestCase):
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page

    def test_projects(self):
        self.page.goto(f"{self.live_server_url}/projects")
        self.page.wait_for_selector("text=Cal B/C")
        self.page.click("text=Log in with Microsoft")
        assert self.page.is_visible("text=Logout")
        self.page.close()
