from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from constants.users import Users

class LoginPage(BasePage):
    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.user_name_field = page.locator("[data-test=\"username\"]")
        self.password_field = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-button\"]")

    def login(self, user: Users):
        user_data = user.value
        self.user_name_field.fill(user_data["username"])
        self.password_field.fill(user_data["password"])
        self.login_button.click()


