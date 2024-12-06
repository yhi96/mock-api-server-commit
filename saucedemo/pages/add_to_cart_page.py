from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AddToCartPage(BasePage):
    inventory_url = "https://www.saucedemo.com/inventory.html"

    def open_inventory_page(self):
        self.driver.get(self.inventory_url)

    @property
    def add_to_cart_button_first_item(self):
        return self.wait_for_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")

    @property
    def all_inventory_products(self):
        return self.driver.find_elements(By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory']")

    @property
    def shopping_cart_link(self):
        return self.wait_for_element(By.XPATH, "//a[@class='shopping_cart_link']")

    @property
    def remove_from_cart_button_first_item(self):
        return self.wait_for_element(By.XPATH, "//button[@class='btn btn_secondary btn_small btn_inventory']")



