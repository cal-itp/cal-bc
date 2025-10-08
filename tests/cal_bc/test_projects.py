import pytest
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from playwright.sync_api import Page


class TestProjects(StaticLiveServerTestCase):
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page

    def test_projects(self):
        self.page.goto(f"{self.live_server_url}/")
        self.page.wait_for_selector("text=Cal B/C")
        self.page.click("text=Sign in with Microsoft")
        assert self.page.is_visible("text=Logout")
        self.page.close()
