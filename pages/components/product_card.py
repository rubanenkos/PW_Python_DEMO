import allure
from playwright.sync_api import Page, expect

class ProductCard:
    def __init__(self, page: Page, item_name: str):
        self.item_name = item_name
        self.card = page.get_by_test_id("inventory-item").filter(has_text=item_name)
        self.inventory_price = self.card.get_by_test_id("inventory-item-price")

    @allure.step("Get item price")
    def get_price(self)-> str:
        return self.inventory_price.text_content()

    @allure.step("Add to Cart")
    def add_to_cart(self):
        self.card.get_by_role("button").click()

    def check_is_card_present(self):
        with allure.step(f"Check is '{self.item_name}' present in cart"):
            expect(self.card).to_be_visible()



