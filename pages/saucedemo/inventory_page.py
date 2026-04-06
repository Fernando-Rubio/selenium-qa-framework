from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.saucedemo.cart_page import CartPage

class InventoryPage(BasePage):
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    CART_BUTTON = (By.ID, "shopping_cart_container")

    def add_backpack(self):
        self.click(self.ADD_BACKPACK)

    def add_bike_light(self):
        self.click(self.ADD_BIKE_LIGHT)
        
    def open_cart(self):
       self.scroll_to_element(self.CART_BUTTON)
       self.click(self.CART_BUTTON)
       self.wait_for_element((By.CLASS_NAME, "cart_list"), timeout=20)
       return CartPage(self.driver)