from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class InventoryPage(BasePage):
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack(self):
        self.click(self.ADD_BACKPACK)
    def add_bike_light(self):
        self.click(self.ADD_BIKE_LIGHT)
    def open_cart(self):
        self.click(self.CART_ICON)
        self.wait.until(EC.visibility_of_element_located((By.ID, "checkout")))