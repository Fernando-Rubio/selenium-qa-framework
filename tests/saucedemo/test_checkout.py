from pages.saucedemo.login_page import LoginPage
from pages.saucedemo.inventory_page import InventoryPage
from pages.saucedemo.cart_page import CartPage
from pages.saucedemo.checkout_page import CheckoutPage

def test_complete_checkout(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack()
    inventory_page.open_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    print(driver.current_url)
    checkout_page.enter_info("John", "Doe", "12345")
    checkout_page.finish_checkout()

    assert checkout_page.is_visible(checkout_page.COMPLETE_HEADER)