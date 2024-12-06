from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.cart_url = "https://www.saucedemo.com/cart.html"
    
    def open_cart_url(self):
        self.driver.get(self.cart_url)

    @property
    def remove_button(self):
        return self.driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-backpack']")

    @property
    def continue_shopping_button(self):
        return self.driver.find_element(By.XPATH, "//button[@id='continue-shopping']")

    @property
    def checkout_button(self):
        return self.driver.find_element(By.XPATH, "//button[@id='checkout']")
    
    @property
    def first_name_checkout(self):
        return self.driver.find_element(By.XPATH, "//input[@id='first-name']")

    @property
    def last_name_checkout(self):
        return self.driver.find_element(By.XPATH, "//input[@id='last-name']")

    @property
    def postal_code_checkout(self):
        return self.driver.find_element(By.XPATH, "//input[@id='postal-code']")

    @property
    def cancel_checkout(self):
        return self.driver.find_element(By.XPATH, "//button[@id='cancel']")

    @property
    def continue_checkout(self):
        return self.driver.find_element(By.XPATH, "//input[@id='continue']")
    
    @property
    def all_products_in_cart(self):
        return self.driver.find_elements(By.XPATH, "//div[@class='cart_item_label']")
    


    def enter_checkout_information(self, first_name, last_name, postal_code):
        self.first_name_checkout.send_keys(first_name)
        self.last_name_checkout.send_keys(last_name)
        self.postal_code_checkout.send_keys(postal_code)

