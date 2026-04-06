from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.saucedemo.checkout_page import CheckoutPage

class CartPage(BasePage):
    CART_LIST = (By.CLASS_NAME, "cart_list")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")


    def is_loaded(self):
        return self.is_visible(self.CART_LIST)

    def click_checkout(self):
        button = self.wait_for_clickable(self.CHECKOUT_BUTTON)
        self.driver.execute_script("arguments[0].click();", button)
        self.wait_for_url("checkout-step-one.html")
        return CheckoutPage(self.driver)
    
    def remove_backpack(self):
        self.click(self.REMOVE_BACKPACK)