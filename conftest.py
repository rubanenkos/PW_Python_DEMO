import pytest

from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getini("base_url")

@pytest.fixture(scope="session", autouse=True)
def setup_test_id_attribute(playwright):
    playwright.selectors.set_test_id_attribute("data-test")

@pytest.fixture
def login_page(page, base_url):
    login_page = LoginPage(page, base_url)
    login_page.navigate()
    return login_page