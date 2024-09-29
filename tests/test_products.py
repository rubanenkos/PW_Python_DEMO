import pytest
from constants.users import Users

class TestProducts:

    def test_check_product_price_in_cart_is_correct(self, login_page, products_page, cart_page):
        product_name = "Sauce Labs Backpack"
        login_page.login(Users.STANDARD_USER)
        product_price = products_page.pick_purchase(product_name)
        products_page.header.open_cart()
        cart_page.check_is_purchase_in_cart(product_name)
        cart_page.check_is_purchase_has_correct_price(product_name, product_price)




