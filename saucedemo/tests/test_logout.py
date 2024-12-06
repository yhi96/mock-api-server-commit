import pytest
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.base_page import BasePage

@pytest.fixture
def setup(driver):
    login_page = LoginPage(driver)
    logout_page = LogoutPage(driver)
    base_page = BasePage(driver)
    yield login_page, logout_page, base_page
    driver.quit()

def test_logout_user_from_the_system(setup):
    login_page, logout_page, base_page = setup
    base_page.open_base_page()
    login_page.login("standard_user", "secret_sauce")

    assert login_page.driver.current_url == "https://www.saucedemo.com/inventory.html"

    logout_page.logout()

    assert login_page.driver.current_url == "https://www.saucedemo.com/"

