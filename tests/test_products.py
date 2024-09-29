import pytest
from constants.users import Users

class TestProducts:

    def test_check_purchase_has_correct_price(self, login_page, products_page, cart_page):
        purchase_item = "Sauce Labs Backpack"
        login_page.login(Users.STANDARD_USER)
        purchase_price = products_page.pick_purchase(purchase_item)
        products_page.header.open_cart()
        cart_page.check_is_purchase_in_cart(purchase_item)
        cart_page.check_is_purchase_has_correct_price(purchase_item, purchase_price)




