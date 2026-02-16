from pages.login_pages import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_complete_checkout(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_backpack()
    inventory.open_cart()

    cart = CartPage(driver)
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.enter_info("John", "Doe", "12345")
    checkout.finish_checkout()

    assert "checkout-complete" in driver.current_url