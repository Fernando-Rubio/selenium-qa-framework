import pytest
from pages.saucedemo.login_page import LoginPage
from pages.saucedemo.inventory_page import InventoryPage
from pages.saucedemo.cart_page import CartPage

def test_remove_item_from_cart(driver):

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack()
    inventory_page.open_cart()

    cart_page = CartPage(driver)
    cart_page.remove_backpack()

    assert "cart" in driver.current_url