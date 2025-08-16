from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_logout(driver):
    login = LoginPage(driver); login.load(); login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver); assert inventory.is_loaded()
    assert inventory.logout()  # returns True when login button is visible
