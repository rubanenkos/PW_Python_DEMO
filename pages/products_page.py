import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from pages.components.header import Header
from pages.components.product_card import ProductCard


class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.inventory_item = page.get_by_test_id("inventory-item")
        self.header = Header(page)

    @allure.step("Pick the item '{item_name}' to buy")
    def pick_purchase(self, item_name: str)-> str:
        product_card = ProductCard(self.page, item_name)
        price_value = product_card.get_price()
        product_card.add_to_cart()
        return price_value
