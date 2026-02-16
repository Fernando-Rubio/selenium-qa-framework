from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By. ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR = (By.CLASS_NAME, "error-message-container")
    
    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def wait_for_inventory(self):
        self.wait.until(EC.url_contains("inventory"))

    def get_error_message(self):
        return self.get_text(self.ERROR)