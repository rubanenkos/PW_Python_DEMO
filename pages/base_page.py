import allure
from playwright.sync_api import Page, expect
from typing import Literal


class BasePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def navigate(self, url: str="",
                 wait_until:Literal['commit', 'domcontentloaded', 'load', 'networkidle'] = 'networkidle' ) -> None:
        navigate_link = self.base_url if url.startswith(('http://', 'https://')) else self.base_url + url
        with allure.step(f"Navigate to URL: {navigate_link}"):
            self.page.goto(navigate_link, wait_until=wait_until)

    @allure.step("Check the page url is '{page_url}'")
    def check_page_link(self, page_url: str)-> None:
        expect(self.page).to_have_url(f"{self.base_url}{page_url}")

    @allure.step("Check the page title is {page_title}")
    def check_page_title(self, page_title: str)-> None:
        expect(self.page.locator("[data-test=\"title\"]")).to_have_text(page_title)

