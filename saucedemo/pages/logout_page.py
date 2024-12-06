from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class LogoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    inventory_url = "https://www.saucedemo.com/inventory.html"

    def open_inventory_page(self):
        self.driver.get(self.inventory_url)

    @property
    def hamburger_menu(self):
        return self.driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")

    @property
    def logout_button(self):
        return self.driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']")

    def logout(self):
        self.hamburger_menu.click()
        self.logout_button.click()