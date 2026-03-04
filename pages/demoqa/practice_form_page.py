from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PracticeFormPage(BasePage):
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER_MALE = (By. XPATH, "//label[@for='gender-radio-1']")
    MOBILE = (By.ID, "userNumber")
    SUBMIT = (By.ID, "submit")
    MODAL = (By.CLASS_NAME, "modal-content")

    def open(self):
        self.driver.get("https://demoqa.com/automation-practice-form")

    def fill_form(self, first, last, email, mobile):
        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.EMAIL, email)
        self.click(self.GENDER_MALE)
        self.type(self.MOBILE, mobile)

    def submit_form(self):
        self.scroll_to_element(self.SUBMIT)
        element = self.driver.find_element(*self.SUBMIT)
        self.driver.execute_script("arguments[0].click();", element)

    def is_modal_displayed(self):
        return self.is_visible(self.MODAL)
    