from pages.saucedemo.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.saucedemo.inventory_page import InventoryPage

def test_add_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack()
    inventory_page.open_cart()

    WebDriverWait(driver,15).until(EC.url_contains("cart"))

    assert "cart" in driver.current_url