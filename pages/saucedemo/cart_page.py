from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.saucedemo.checkout_page import CheckoutPage

class CartPage(BasePage):
    CART_LIST = (By.CLASS_NAME, "cart_list")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")


    def is_loaded(self):
        return self.is_visible(self.CART_LIST)

    def click_checkout(self):
        self.wait_for_cart_page()
        self.click(self.CHECKOUT_BUTTON)
    
    def remove_backpack(self):
        self.click(self.REMOVE_BACKPACK)