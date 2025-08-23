from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "inventory_item_name")

    def get_item_names(self):
        return [e.text for e in self.driver.find_elements(*self.CART_ITEMS)]
