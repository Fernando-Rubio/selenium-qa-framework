from pages.saucedemo.login_page import LoginPage
from pages.saucedemo.inventory_page import InventoryPage

def test_add_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart()
    inventory_page.open_cart()

    assert "cart" in driver.current_url