from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class InventoryPage(BasePage):
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack(self):
        self.click(self.ADD_BACKPACK)
    def open_cart(self):
        cart = self.wait.until(EC.element_to_be_clickable(self.CART_ICON))
        cart.click()
        self.wait.until(EC.url_contains("cart"))