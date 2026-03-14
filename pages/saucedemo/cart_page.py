from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def click_checkout(self):
        self.wait = WebDriverWait(self.driver, 15)
        self.wait.until(EC.url_contains("cart"))
        self.wait.until(EC.visibility_of_element_located(self.CHECKOUT_BUTTON)).click()