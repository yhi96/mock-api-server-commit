import pytest
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.add_to_cart_page import AddToCartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def setup(driver):
    base_page = BasePage(driver)
    login_page = LoginPage(driver)
    add_to_cart_page = AddToCartPage(driver)
    checkout_page = CheckoutPage(driver)
    yield base_page, login_page, add_to_cart_page, checkout_page
    

def test_verify_fields_are_visible(setup):
    base_page, login_page, add_to_cart_page, checkout_page = setup
    base_page.open_base_page()
    login_page.login("standard_user", "secret_sauce")
    add_to_cart_page.add_to_cart_button_first_item.click()
    checkout_page.open_cart_url()
    checkout_page.checkout_button.click()

    assert checkout_page.first_name_checkout.is_displayed()
    assert checkout_page.last_name_checkout.is_displayed()
    assert checkout_page.postal_code_checkout.is_displayed()

def test_verify_function_of_cancel_button(setup):
    base_page, login_page, add_to_cart_page, checkout_page = setup
    base_page.open_base_page()
    login_page.login("standard_user", "secret_sauce")
    add_to_cart_page.add_to_cart_button_first_item.click()
    checkout_page.open_cart_url()
    checkout_page.checkout_button.click()
    checkout_page.cancel_checkout.click()

    assert checkout_page.driver.current_url == "https://www.saucedemo.com/cart.html"

def test_verify_function_of_continue_button_with_correct_info(setup):
    base_page, login_page, add_to_cart_page, checkout_page = setup
    base_page.open_base_page()
    login_page.login("standard_user", "secret_sauce")
    add_to_cart_page.add_to_cart_button_first_item.click()
    checkout_page.open_cart_url()
    checkout_page.checkout_button.click()

    checkout_page.enter_checkout_information("Test", "User", "96523")
    checkout_page.continue_checkout.click()

    assert checkout_page.driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"