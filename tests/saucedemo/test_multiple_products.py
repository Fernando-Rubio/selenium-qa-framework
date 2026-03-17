import pytest
from pages.saucedemo.login_page import LoginPage
from pages.saucedemo.inventory_page import InventoryPage

def test_add_multiple_items_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)

    inventory_page.add_backpack()
    inventory_page.add_bike_light()

    inventory_page.open_cart()

    assert "cart" in driver.current_url 