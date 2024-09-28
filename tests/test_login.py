import pytest
import allure
from playwright.sync_api import Page, expect

from constants.page_info import PageInfo
from constants.users import Users

class TestLogin:

    def test_registered_user_can_login(self, login_page):
        login_page.login(Users.STANDARD_USER)
        login_page.check_page_link(PageInfo.INVENTORY.URL)
        login_page.check_page_title(PageInfo.INVENTORY.TITLE)

    @pytest.mark.parametrize(
        "username, password, expected_error",
        [
            (
                    Users.STANDARD_USER.USERNAME,
                    Users.UNREGISTERED_USER.PASSWORD,
                    "Epic sadface: Username and password do not match any user in this service",
            ),
            (
                    Users.LOCKED_OUT_USER.USERNAME,
                    Users.LOCKED_OUT_USER.PASSWORD,
                    "Epic sadface: Sorry, this user has been locked out.",
            ),
        ],
        ids=["invalid_password", "locked_user"],
    )
    def test_failed_login_for_user(self, login_page, page: Page, username: str, password: str, expected_error: str):
        login_page.fill_name_field(username)
        login_page.fill_password_field(password)
        login_page.click_login_button()
        login_page.check_error_message(expected_error)


