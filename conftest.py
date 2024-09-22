import pytest

@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getini("base_url")
