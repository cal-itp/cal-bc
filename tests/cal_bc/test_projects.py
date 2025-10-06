import pytest
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from playwright.sync_api import Page


class TestProjects(StaticLiveServerTestCase):
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page

    def test_projects(self):
        self.page.goto(f"{self.live_server_url}/admin/")
        self.page.wait_for_selector("text=Django administration")
        self.page.fill("[name=username]", "myuser")
        self.page.fill("[name=password]", "secret")
        self.page.click("text=Log in")
        assert len(self.page.eval_on_selector(".errornote", "el => el.innerText")) > 0
        self.page.close()
