from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By. ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR = (By.CSS_SELECTOR,"h3[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        super().open("https://www.saucedemo.com/")
    
    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR)