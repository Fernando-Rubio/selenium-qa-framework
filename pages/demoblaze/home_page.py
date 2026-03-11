from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DemoBlazeHomePage(BasePage):

    PRODUCT = (By.CSS_SELECTOR, ".card-title a")

    def open(self):
        self.driver.get("https://www.demoblaze.com/")

    def select_first_product(self):
        products = self.driver.find_elements(*self.PRODUCT)
        products[0].click()