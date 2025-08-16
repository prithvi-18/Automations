from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "inventory_item_name")

    def get_item_names(self):
        items = self.wait.until(
            EC.visibility_of_all_elements_located(self.CART_ITEMS)
        )
        return [i.text for i in items]
