from pages.login_pages import LoginPage
from pages.inventory_page import InventoryPage

def test_add_to_cart(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    inventory.add_backpack()
    inventory.open_cart()

    assert "cart" in driver.current_url