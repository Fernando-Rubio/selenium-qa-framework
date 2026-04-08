from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.saucedemo.cart_page import CartPage

class InventoryPage(BasePage):
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack(self):
        self.click(self.ADD_BACKPACK)

    def add_bike_light(self):
        self.click(self.ADD_BIKE_LIGHT)
        
    def open_cart(self):
      self.click(self.CART_LINK)
      self.wait_for_url("cart.html")
      return CartPage(self.driver)