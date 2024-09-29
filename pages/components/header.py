import allure
from playwright.sync_api import Page

class Header:
    def __init__(self, page: Page):
        self.page = page
        self.page_url = "cart.html"
        self.cart_link = page.get_by_test_id("shopping-cart-link")
        self.burger_menu = page.get_by_test_id("open-menu")

    @allure.step("Open Cart")
    def open_cart(self)-> None:
        self.cart_link.click()
        self.page.wait_for_url(f"**/{self.page_url}")

    @allure.step("Open Menu")
    def open_burger_menu(self)-> None:
        self.burger_menu.click()
