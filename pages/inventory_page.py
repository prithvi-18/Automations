from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class InventoryPage(BasePage):
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    ITEM_ADD_BUTTON = (By.XPATH, "//div[text()='{}']/ancestor::div[@class='inventory_item']//button")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def is_loaded(self):
        """Check if inventory page loaded successfully."""
        return self.wait.until(
            EC.visibility_of_element_located(self.INVENTORY_CONTAINER)
        )

    def add_to_cart(self, item_name):
        locator = (self.ITEM_ADD_BUTTON[0], self.ITEM_ADD_BUTTON[1].format(item_name))
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def open_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_ICON)).click()

    def logout(self):
        # Click menu
        self.wait.until(EC.element_to_be_clickable(self.MENU_BUTTON)).click()
        # Click logout
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK)).click()

        # Wait until login button appears (more reliable than URL)
        self.wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
        return True
