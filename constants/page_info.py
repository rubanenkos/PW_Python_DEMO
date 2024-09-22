from enum import Enum

class PageInfo(Enum):
    INVENTORY = ("inventory.html", "Products")
    LOGIN = ("login.html", "Login Page")
    CHECKOUT_INFO = ("checkout-step-one.html", "Checkout: Your Information"),
    CHECKOUT_OVERVIEW = ( "checkout-step-two.html", "Checkout: Overview"),

    @property
    def URL(self):
        return self.value[0]

    @property
    def TITLE(self):
        return self.value[1]

