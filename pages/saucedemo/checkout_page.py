from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def enter_info(self, first, last, postal):
        self.wait_for_element(self.FIRST_NAME).send_keys(first)
        self.wait_for_element(self.LAST_NAME).send_keys(last)
        self.wait_for_element(self.POSTAL_CODE).send_keys(postal)
        self.wait_for_clickable(self.CONTINUE_BUTTON).click()
        print("Current URL before wait:", self.driver.current_url)
        self.wait_for_url("/checkout-step-two.html")

    def finish_checkout(self):
        self.wait_for_element(self.FINISH_BUTTON).click()
        self.wait_for_element_visible(self.COMPLETE_HEADER)