import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from constants.users import Users

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.user_name_field = page.locator("[data-test=\"username\"]")
        self.password_field = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-button\"]")
        self.error_message = page.get_by_test_id("error")

    def login(self, user: Users):
        user_data = user.value
        with allure.step(f"Login as a user: '{user_data["username"]}'"):
            self.fill_name_field(user_data["username"])
            self.fill_password_field(user_data["password"])
            self.click_login_button()

    def fill_name_field(self, value: str ):
        with allure.step(f"Fill name field with '{value}'"):
            self.user_name_field.fill(value)

    def fill_password_field(self, value):
        with allure.step(f"Fill password field with '{value}'"):
            self.password_field.fill(value)

    def click_login_button(self):
        with allure.step("Click 'Login' button"):
            self.login_button.click()

    def check_error_message(self, expected_message):
        with allure.step(f"Check the error message '{expected_message}' is shown"):
            expect(self.error_message).to_have_text(expected_message)



