from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    INVENTORY_TITLE = (By.CLASS_NAME, "title")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def is_loaded(self):
        return self.wait_for(self.INVENTORY_TITLE).is_displayed()

    def add_to_cart(self, item_name):
        button = self.driver.find_element(By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button")
        button.click()

    def open_cart(self):
        self.driver.find_element(*self.CART_LINK).click()

    def logout(self):
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        self.wait_for((By.ID, "logout_sidebar_link")).click()
