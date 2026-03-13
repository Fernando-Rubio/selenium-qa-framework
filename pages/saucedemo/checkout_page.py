from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")


    def enter_info(self, first, last, zip_code):
        self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME))
        self.type(self.FIRST_NAME, first)
        self.wait.until(EC.element_to_be_clickable(self.LAST_NAME))
        self.type(self.LAST_NAME, last)
        postal_input = self.wait.until(EC.element_to_be_clickable(self.POSTAL_CODE))
        postal_input.clear()
        postal_input.send_keys(zip_code)
        print("URL before clicking continue", self.driver.current_url)
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON))
        self.click(self.CONTINUE_BUTTON)
        print("URL after clicking continue:", self.driver.current_url)
    
    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)