from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def enter_info(self, first, last, postal):
        
            first_input = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME))
            first_input.clear()
            first_input.send_keys(first)

            last_input = self.wait.until(EC.element_to_be_clickable(self.LAST_NAME))
            last_input.clear()
            last_input.send_keys(last)

            postal_input = self.wait.until(EC.element_to_be_clickable(self.POSTAL_CODE))
            postal_input.clear()
            postal_input.send_keys(postal)

            continue_btn = self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON))
            continue_btn.click()
    

    def finish_checkout(self):
            
            finish_btn = self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON))
            finish_btn.click()
            self.wait.until(EC.url_contains("complete"))
            self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER))
