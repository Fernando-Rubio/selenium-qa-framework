from pages.saucedemo.login_page import LoginPage
from pages.saucedemo.inventory_page import InventoryPage
from pages.saucedemo.cart_page import CartPage
from pages.saucedemo.checkout_page import CheckoutPage

def test_complete_checkout(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack()
    inventory_page.add_bike_light()
    inventory_page.open_cart()

    cart_page.click_checkout()

    checkout_page.enter_info("John", "Doe", "12345")

    checkout_page.finish_checkout()

    assert checkout_page.wait_for_element(checkout_page.COMPLETE_HEADER)