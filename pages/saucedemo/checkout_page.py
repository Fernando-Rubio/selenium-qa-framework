from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    SUMMARY_INFO = (By.CLASS_NAME, "checkout_summary_container")

    def enter_info(self, first, last, postal):
        self.wait_for_element(self.FIRST_NAME)
        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.POSTAL_CODE, postal)
        
        button = self.wait_for_clickable(self.CONTINUE_BUTTON)
        self.driver.execute_script("arguments[0].click();", button)

        self.wait_for_url("checkout-step-two.html")

    def finish_checkout(self):
        button = self.wait_for_clickable(self.FINISH_BUTTON)
        self.driver.execute_script("arguments[0].click();", button)

        self.wait_for_url("checkout-complete.html")
        self.wait_for_element(self.COMPLETE_HEADER)