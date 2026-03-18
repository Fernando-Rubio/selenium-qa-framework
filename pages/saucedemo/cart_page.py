from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        self.wait.until(EC.url_contains("checkout-step-one"))

    def remove_backpack(self):
        self.click(self.REMOVE_BACKPACK)