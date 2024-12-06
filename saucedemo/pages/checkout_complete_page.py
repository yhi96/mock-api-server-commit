from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage

class CheckoutComplete(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_complete_url = "https://www.saucedemo.com/checkout-step-two.html"

    @property
    def back_home_button(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//button[@data-test='back-to-products']")

    @property
    def checkout_complete(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//span[@data-test='title']")
    
    @property
    def finish_button(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//button[@id='finish']")

    @property
    def cart_items(self) -> list[WebElement]:
        return self.driver.find_elements(By.XPATH, "//div[@class='cart_item']")

    @property
    def cancel_button(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//button[@id='cancel']")

    @property
    def quantity(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[@class='cart_quantity']")

    @property
    def description(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[@class='inventory_item_desc']")

    @property
    def item_name(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[@class='inventory_item_name']")

    @property
    def item_price(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")

    @property
    def payment_information(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[@data-test='payment-info-value']")

    @property
    def delivery_information(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[@data-test='shipping-info-value']")

    @property
    def item_total_price(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[@data-test='subtotal-label']")

    @property
    def thank_you_order(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//h2[@data-test='complete-header']")

