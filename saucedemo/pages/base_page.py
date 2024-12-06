from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        

    @property
    def base_url(self):
        return "https://www.saucedemo.com/"

    def open_base_page(self):
        self.driver.get(self.base_url)

    def wait_for_element(self, by, value):
        return self.driver.find_element(by, value)
