from pages.demoblaze.home_page import DemoBlazeHomePage
from pages.demoblaze.cart_page import DemoBlazeCartPage

def text_add_product_to_cart(driver):

    home = DemoBlazeHomePage(driver)
    cart = DemoBlazeCartPage(driver)

    home.open()
    home.select_first_product()

    cart.add_product()

    assert True