import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from pages.components.product_card import ProductCard


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.inventory_item = page.get_by_test_id("inventory-item")

    @allure.step("Check if '{item_name}' product in Cart")
    def check_is_purchase_in_cart(self, item_name:str):
        product_card = ProductCard(self.page, item_name)
        product_card.check_is_card_present()

    @allure.step("Check if '{item_name}  price is '{expected_price}'")
    def check_is_purchase_has_correct_price(self, item_name:str, expected_price: str):
        product_card = ProductCard(self.page, item_name)
        actual_price = product_card.inventory_price
        expect(actual_price).to_have_text(expected_price)




