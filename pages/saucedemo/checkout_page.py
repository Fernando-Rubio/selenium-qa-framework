from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    SUMMARY_CONTAINER = (By.CLASS_NAME, "checkout_summary_container")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def enter_info(self, first, last, postal):
        first_input = self.wait_for_element(self.FIRST_NAME)
        last_input = self.wait_for_element(self.LAST_NAME)
        postal_input = self.wait_for_element(self.POSTAL_CODE)

        first_input.clear()
        first_input.send_keys(first)

        last_input.clear()
        last_input.send_keys(last)

        postal_input.clear()
        postal_input.click()
        postal_input.send_keys(postal)

        print("First value:", first_input.get_attribute("value"))
        print("Last value:", last_input.get_attribute("value"))
        print("Postal value:", postal_input.get_attribute("value"))

        self.wait_for_clickable(self.CONTINUE_BUTTON)
        self.click(self.CONTINUE_BUTTON)

        print("URL after continue:", self.driver.current_url)

        self.wait_for_url("checkout-step-two.html")


    def finish_checkout(self):
        self.wait_for_url("checkout-step-two.html")

        button = self.wait_for_clickable(self.FINISH_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        self.driver.execute_script("arguments[0].click();", button)
        
        self.wait_for_url("checkout-complete.html")
        self.wait_for_element(self.COMPLETE_HEADER)