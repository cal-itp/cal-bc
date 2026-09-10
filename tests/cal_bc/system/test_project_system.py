import os
from pathlib import Path

import pytest
from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import Client
from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import CreateContextCallback

from tests.channels_live_server_helper import ChannelsLiveServer

BASE_DIR = Path(__file__).resolve().parent

@pytest.mark.vcr
@pytest.mark.django_db(transaction=True)
class TestProjectSystem:
    @pytest.fixture
    def user(self) -> User:
        return User.objects.create_user(username="caltrans")

    @pytest.fixture
    def session_id(self, client: Client, user: User) -> bytes:
        client.force_login(user)
        return client.cookies["sessionid"].value

    @pytest.fixture
    def cookie(self, channels_live_server: ChannelsLiveServer, session_id: bytes) -> dict:
        return {
            "name": "sessionid",
            "value": session_id,
            "secure": False,
            "url": channels_live_server.http_url,
        }

    @pytest.fixture
    def first_page(self, page: Page, cookie: dict) -> Page:
        first_page = page
        first_page.context.add_cookies([cookie])
        return first_page

    @pytest.fixture
    def second_page(self, cookie: dict, new_context: CreateContextCallback) -> Page:
        second_page = new_context().new_page()
        second_page.context.add_cookies([cookie])
        return second_page

    @pytest.fixture(autouse=True)
    def load_model_sketch(self):
        call_command('loaddata', os.path.join(BASE_DIR, '../../seeds/tags.json'))
        call_command('loaddata', os.path.join(BASE_DIR, '../../seeds/model_sketch.json'))
        call_command('loaddata', os.path.join(BASE_DIR, '../../seeds/model_sketch_sub1A.json'))
        call_command('loaddata', os.path.join(BASE_DIR, '../../seeds/model_sketch_sub1D.json'))
        call_command('loaddata', os.path.join(BASE_DIR, '../../seeds/model_sketch_sub1E.json'))

    def test_projects(self, first_page: Page, second_page: Page, channels_live_server: ChannelsLiveServer):
        first_page.goto(channels_live_server.http_url)
        expect(first_page.locator("body")).to_contain_text("My Cal B/C Projects")

        second_page.goto(channels_live_server.http_url)
        expect(second_page.locator("body")).to_contain_text("My Cal B/C Projects")
        expect(first_page.locator("body")).to_contain_text("0 projects")

        first_page.get_by_role("link", name="New project").click()
        first_page.get_by_role("button", name="Start project").click()
        expect(first_page.locator("body")).to_contain_text(
            "All fields in this step are required"
        )

        first_page.get_by_label("Project Name").click()
        expect(first_page.locator("body")).to_contain_text(
            "Enter a descriptive name for your project."
        )
        expect(first_page.locator("body")).to_contain_text(
            "Configure project analysis settings."
        )

        first_page.get_by_role("button", name="Save draft").click()
        expect(first_page.locator("body")).to_contain_text("This field is required")

        first_page.get_by_label("Project Name").fill("Geary Boulevard Light Rail")
        first_page.get_by_label("State").select_option("California")
        first_page.get_by_label("District").select_option(
            "District 4 - Bay Area / Oakland"
        )
        first_page.get_by_label("Project Type").select_option("• General Highway")
        first_page.get_by_label("Project Location").select_option("NorCal")
        expect(first_page.get_by_label("Length of Construction Period").locator("//following-sibling::span")).to_contain_text("years")
        first_page.get_by_label("Length of Construction Period").fill("3")
        first_page.get_by_label("One- or Two-Way Data").select_option("One-Way")
        expect(first_page.get_by_label("Length of Peak Period").locator("//following-sibling::span")).to_contain_text("hours")
        first_page.get_by_label("Length of Peak Period").fill("4")

        expect(second_page.locator("body")).to_contain_text("Hypothetical Project")
        first_page.get_by_role("button", name="Save draft").click()
        expect(first_page.locator("body")).to_contain_text("Project successfully saved!")
        expect(second_page.locator("body")).to_contain_text("Geary Boulevard Light Rail")

        first_page.get_by_label("Project Name").fill("New Geary Boulevard Light Rail")
        first_page.get_by_role("button", name="Continue to Subsection 1D").click()
        expect(first_page.locator("body")).to_contain_text("Project successfully saved!")

        expect(second_page.locator("body")).to_contain_text("1 projects")
        second_page.get_by_role("link", name="Edit").click()
        expect(second_page.get_by_label("Project Name")).to_have_value("New Geary Boulevard Light Rail")

        first_page.get_by_role("button", name="Save draft").click()
        expect(first_page.locator("body")).to_contain_text("This field is required")
        expect(first_page.get_by_label("Capital Expenditure No Build").locator("//following-sibling::span")).to_contain_text("$")
        expect(first_page.get_by_label("Capital Expenditure Build").locator("//following-sibling::span")).to_contain_text("$")
        expect(first_page.get_by_role("spinbutton", name="Capital Expenditure Build" )).to_have_value("0.0")
        expect(first_page.get_by_label("Ops. & Maint. Expenditure No Build").locator("//following-sibling::span")).to_contain_text("$")
        expect(first_page.get_by_label("Ops. & Maint. Expenditure Build").locator("//following-sibling::span")).to_contain_text("$")
        expect(first_page.get_by_role("spinbutton", name="Ops. & Maint. Expenditure Build" )).to_have_value("0.0")
        first_page.get_by_label("Capital Expenditure No Build").fill("250")
        first_page.get_by_label("Ops. & Maint. Expenditure No Build").fill("30")
        first_page.get_by_role("button", name="Back to Subsection 1A").click()
        expect(first_page.locator("body")).to_contain_text("Project successfully saved!")

        first_page.get_by_role("button", name="1A - Project Data").click()
        first_page.get_by_role("menuitem", name="1E. Project Costs").click()

        expect(first_page.get_by_label("Total Mitigation")).to_contain_text("0", use_inner_text=True)
        expect(first_page.get_by_label("Total Transit Agency Cost Savings")).to_contain_text("0", use_inner_text=True)
        expect(first_page.get_by_label("Total Costs in Constant Dollars")).to_contain_text("$0", use_inner_text=True)
        expect(first_page.get_by_label("Total Costs as Present Value")).to_contain_text("$0", use_inner_text=True)

        expect(first_page.get_by_label("Constant Dollars Year 1")).to_contain_text("$0", use_inner_text=True)
        expect(first_page.get_by_label("Present Value Year 1")).to_contain_text("$0", use_inner_text=True)
        expect(first_page.get_by_label("Constant Dollars Year 2")).to_contain_text("$0", use_inner_text=True)
        expect(first_page.get_by_label("Present Value Year 2")).to_contain_text("$0", use_inner_text=True)

        expect(first_page.get_by_label("Project Support Total")).to_contain_text("0", use_inner_text=True)
        expect(first_page.get_by_label("Right of Way Total")).to_contain_text("0", use_inner_text=True)
        expect(first_page.get_by_label("Construction Total")).to_contain_text("0", use_inner_text=True)
        expect(first_page.get_by_label("Mitigation Total")).to_contain_text("0", use_inner_text=True)
        expect(first_page.get_by_label("Transit AGY Cost SVGS Total")).to_contain_text("0", use_inner_text=True)
        expect(first_page.get_by_label("Constant Dollars Total")).to_contain_text("$0", use_inner_text=True)
        expect(first_page.get_by_label("Present Value Total")).to_contain_text("$0", use_inner_text=True)

        first_page.get_by_label("Project Support Year 1").fill("10000")
        first_page.get_by_label("Right of Way Year 1").fill("11000")
        first_page.get_by_label("Construction Year 1").fill("12000")
        first_page.get_by_label("Mitigation Year 1").fill("13000")
        first_page.get_by_label("Transit AGY Cost SVGS Year 1").fill("14000")

        first_page.get_by_label("Project Support Year 2").fill("21000")
        first_page.get_by_label("Right of Way Year 2").fill("22000")
        first_page.get_by_label("Construction Year 2").fill("23000")
        first_page.get_by_label("Mitigation Year 2").fill("24000")
        first_page.get_by_label("Transit AGY Cost SVGS Year 2").fill("25000")

        first_page.get_by_role("button", name="Save draft").click()

        expect(first_page.get_by_label("Constant Dollars Year 1")).to_contain_text("$60,000,000", use_inner_text=True, timeout=10_000)
        expect(first_page.get_by_label("Present Value Year 1")).to_contain_text("$60,000,000", use_inner_text=True)
        expect(first_page.get_by_label("Constant Dollars Year 2")).to_contain_text("$115,000,000", use_inner_text=True)
        expect(first_page.get_by_label("Present Value Year 2")).to_contain_text("$110,576,923", use_inner_text=True)

        expect(first_page.get_by_label("Project Support Total")).to_contain_text("31,000", use_inner_text=True)
        expect(first_page.get_by_label("Right of Way Total")).to_contain_text("33,000", use_inner_text=True)
        expect(first_page.get_by_label("Construction Total")).to_contain_text("35,000", use_inner_text=True)
        expect(first_page.get_by_label("Mitigation Total")).to_contain_text("37,000", use_inner_text=True)
        expect(first_page.get_by_label("Transit AGY Cost SVGS Total")).to_contain_text("39,000", use_inner_text=True)
        expect(first_page.get_by_label("Constant Dollars Total")).to_contain_text("$175,000,000", use_inner_text=True)
        expect(first_page.get_by_label("Present Value Total")).to_contain_text("$170,576,923", use_inner_text=True)

        first_page.get_by_role("link", name="Projects").click()
        expect(first_page.locator("body")).to_contain_text(
            "New Geary Boulevard Light Rail"
        )

        expect(first_page.locator("body")).to_contain_text("1 projects")
        first_page.on("dialog", lambda dialog: dialog.accept())
        first_page.get_by_role("button", name="Delete").click()
        expect(first_page.locator("body")).to_contain_text("0 projects")

        first_page.get_by_role("button", name="User").click()
        first_page.get_by_text("Sign out").click()
        expect(first_page.locator("body")).to_contain_text("Sign in with Microsoft")
        first_page.close()
