from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.saucedemo.checkout_page import CheckoutPage

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")

    def click_checkout(self):
        self.wait.until(EC.url_contains("cart"))
        self.wait_for_element(self.CHECKOUT_BUTTON).click()
    
    def remove_backpack(self):
        self.click(self.REMOVE_BACKPACK)