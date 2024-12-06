from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    user_name_field = (By.XPATH, "//input[@id='user-name']")
    password_field = (By.XPATH, "//input[@id='password']")
    login_button = (By.XPATH, "//input[@id='login-button']")
    error_message = (By.XPATH, "//div[@class='error-message-container error']")

    def login(self, username, password):
        self.driver.find_element(*self.user_name_field).clear()
        self.driver.find_element(*self.user_name_field).send_keys(username)

        self.driver.find_element(*self.password_field).clear()
        self.driver.find_element(*self.password_field).send_keys(password)

        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        self.wait_for_element(*self.error_message)
        return self.driver.find_element(*self.error_message).text
