from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrangeHRMLoginPage(BasePage):
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def open(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)