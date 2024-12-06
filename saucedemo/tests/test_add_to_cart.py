import pytest
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.add_to_cart_page import AddToCartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def setup(driver):
    login_page = LoginPage(driver)
    add_to_cart_page = AddToCartPage(driver)
    checkout_page = CheckoutPage(driver)
    yield login_page, add_to_cart_page, checkout_page
    driver.quit()

def test_add_product_to_cart(setup):
    login_page, add_to_cart_page, checkout_page = setup
    login_page.open_base_page()
    login_page.login("standard_user", "secret_sauce")

    assert add_to_cart_page.driver.current_url == "https://www.saucedemo.com/inventory.html"

    add_to_cart_page.add_to_cart_button_first_item.click()
    add_to_cart_page.shopping_cart_link.click()

    assert len(checkout_page.all_products_in_cart) > 0

