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

    def enter_info(self, first, last, zip_code):
          self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(first)
          self.wait.until(EC.visibility_of_element_located(self.LAST_NAME)).send_keys(last)
          self.wait.until(EC.visibility_of_element_located(self.POSTAL_CODE)).send_keys(zip_code)
          self.wait.until(EC.visibility_of_element_located(self.CONTINUE_BUTTON)).click()
    

    def finish_checkout(self):
            
            finish_btn = self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON))
            finish_btn.click()
            self.wait.until(EC.url_contains("complete"))
            self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER))
