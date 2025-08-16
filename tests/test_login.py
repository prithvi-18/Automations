from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_success(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    assert inventory.is_loaded()
