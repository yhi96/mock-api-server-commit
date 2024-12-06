import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    login_page = LoginPage(driver)
    yield login_page
    driver.quit()

def test_access_web_app_from_url(setup):
    login_page = setup
    login_page.open_base_page()
    assert login_page.driver.current_url == "https://www.saucedemo.com/"

def test_verify_contains_login_form(setup):
    login_page = setup
    login_page.open_base_page()
    assert login_page.driver.find_element(*login_page.user_name_field).is_displayed()
    assert login_page.driver.find_element(*login_page.password_field).is_displayed()
    assert login_page.driver.find_element(*login_page.login_button).is_displayed()

def test_login_with_correct_credentials(setup):
    login_page = setup
    login_page.open_base_page()
    login_page.login("standard_user", "secret_sauce")
    assert login_page.driver.current_url == "https://www.saucedemo.com/inventory.html"
    

def test_login_with_empty_username(setup):
    login_page = setup
    login_page.open_base_page()
    login_page.login("", "secret_sauce")
    assert login_page.get_error_message() == "Epic sadface: Username is required"

def test_login_with_empty_password(setup):
    login_page = setup
    login_page.open_base_page()
    login_page.login("standard_user", "")
    assert login_page.get_error_message() == "Epic sadface: Password is required"

def test_login_with_wrong_credentials(setup):
    login_page = setup
    login_page.open_base_page()
    login_page.login("invalid_user", "invalid_pass")
    assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"
