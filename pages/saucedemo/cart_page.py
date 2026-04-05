from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.saucedemo.checkout_page import CheckoutPage

class CartPage(BasePage):
    CART_LIST = (By.CLASS_NAME, "cart_list")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")

    def open_cart(self):
        self.wait_for_url("cart")
        self.wait_for_element(self.CART_LIST)

    def click_checkout(self):
        self.wait_for_element(self.CHECKOUT_BUTTON).click()
    
    def remove_backpack(self):
        self.click(self.REMOVE_BACKPACK)