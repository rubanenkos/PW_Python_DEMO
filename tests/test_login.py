import pytest
from playwright.sync_api import Page, expect

from constants.page_info import PageInfo
from constants.users import Users
from pages.login_page import LoginPage

class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page, base_url):
        self.login_page = LoginPage(page, base_url)
        self.login_page.navigate()


    def test_registered_user_can_login(self, page: Page, base_url):
        self.login_page.login(Users.STANDARD_USER)
        self.login_page.check_page_link(PageInfo.INVENTORY.URL)
        self.login_page.check_page_title(PageInfo.INVENTORY.TITLE)


