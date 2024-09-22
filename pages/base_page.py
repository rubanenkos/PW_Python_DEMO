from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def navigate(self):
        self.page.goto(self.base_url, wait_until="networkidle")

    def check_page_link(self, page_url: str):
        expect(self.page).to_have_url(f"{self.base_url}{page_url}")

    def check_page_title(self, page_title: str):
        expect(self.page.locator("[data-test=\"title\"]")).to_have_text(page_title)
