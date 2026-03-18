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

        self.wait.until(EC.url_contains("checkout-step-one"))
        self.type(self.FIRST_NAME,first)
        self.type(self.LAST_NAME,last)
        self.type(self.POSTAL_CODE, postal)
        self.click(self.CONTINUE_BUTTON)
        self.wait_for_url("checkout-step-two")
        self.wait_for_element(self.FINISH_BUTTON)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)
        self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER))