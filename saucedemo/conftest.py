import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.add_to_cart_page import AddToCartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_complete_page import CheckoutComplete


def clear_session(driver):
    
    driver.delete_all_cookies()

@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    #chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)

    clear_session(driver)

    yield driver

    driver.quit()

@pytest.fixture
def base_page(driver):
    return BasePage(driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def logout_page(driver):
    return LogoutPage(driver)

@pytest.fixture
def add_to_cart_page(driver):
    return AddToCartPage(driver)

@pytest.fixture
def checkout_page(driver):
    return CheckoutPage(driver)

@pytest.fixture
def checkout_complete_page(driver):
    return CheckoutComplete(driver)
