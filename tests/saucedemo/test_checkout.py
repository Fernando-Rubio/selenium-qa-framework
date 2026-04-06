from pages.saucedemo.login_page import LoginPage
from pages.saucedemo.inventory_page import InventoryPage

def test_complete_checkout(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack()
    inventory_page.add_bike_light()
    
    cart_page = inventory_page.open_cart()
    assert cart_page.is_loaded()

    checkout_page = cart_page.click_checkout()
    checkout_page.enter_info("John", "Doe", "12345")
    checkout_page.finish_checkout()

    assert checkout_page.is_visible(checkout_page.COMPLETE_HEADER)