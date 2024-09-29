import pytest

from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.fixture(scope="session")
def base_url(pytestconfig):
    BasePage.base_url = pytestconfig.getini("base_url")


@pytest.fixture(scope="session", autouse=True)
def setup_test_id_attribute(playwright):
    playwright.selectors.set_test_id_attribute("data-test")

@pytest.fixture
def login_page(page):
    login_page = LoginPage(page)
    login_page.navigate()
    return login_page

@pytest.fixture
def products_page(page):
    products_page = ProductsPage(page)
    return products_page


@pytest.fixture
def cart_page(page):
    return CartPage(page)
