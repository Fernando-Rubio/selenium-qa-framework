from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class DemoBlazeCartPage(BasePage):

    FIRST_PRODUCT = (By.CSS_SELECTOR, ".card-title a")
    ADD_TO_CART = (By.LINK_TEXT, "Add to cart")

    def add_first_product_to_cart(self):
        self.click(self.FIRST_PRODUCT)
        self.wait_for_element(self.ADD_TO_CART)
        self.click(self.ADD_TO_CART)