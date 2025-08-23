from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_add_to_cart(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    assert inventory.is_loaded()
    inventory.add_to_cart("Sauce Labs Backpack")
    inventory.open_cart()

    cart = CartPage(driver)
    assert "Sauce Labs Backpack" in cart.get_item_names()
