import pytest
from pages.login_page import LoginPage
from pages.add_to_cart_page import AddToCartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_complete_page import CheckoutComplete


@pytest.fixture
def setup(driver):
    login_page = LoginPage(driver)
    add_to_cart_page = AddToCartPage(driver)
    checkout_page = CheckoutPage(driver)
    checkout_complete_page = CheckoutComplete(driver)
    yield login_page, add_to_cart_page, checkout_page, checkout_complete_page

def test_verify_function_of_back_home_button(setup):
    login_page, add_to_cart_page, checkout_page, checkout_complete_page = setup
    login_page.open_base_page()
    login_page.login("standard_user", "secret_sauce")

    add_to_cart_page.add_to_cart_button_first_item.click()
    add_to_cart_page.shopping_cart_link.click()
    checkout_page.checkout_button.click()
    checkout_page.enter_checkout_information("Yoana", "Ivanova", "6163")
    checkout_page.continue_checkout.click()

    checkout_complete_page.finish_button.click()

    checkout_complete_page.back_home_button.click()

    assert checkout_complete_page.driver.current_url == f"{checkout_complete_page.base_url}inventory.html"

def test_verify_message_checkout_complete(setup):
    login_page, add_to_cart_page, checkout_page, checkout_complete_page = setup
    login_page.open_base_page()
    login_page.login("standard_user", "secret_sauce")

    add_to_cart_page.add_to_cart_button_first_item.click()
    add_to_cart_page.shopping_cart_link.click()
    checkout_page.checkout_button.click()
    checkout_page.enter_checkout_information("Yoana", "Ivanova", "6163")
    checkout_page.continue_checkout.click()

    checkout_complete_page.finish_button.click()

    assert checkout_complete_page.checkout_complete.text == "Checkout: Complete!"


