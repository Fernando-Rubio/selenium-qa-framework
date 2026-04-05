from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class DemoBlazeLoginPage(BasePage):

    LOGIN_LINK = (By.ID, "login2")
    USERNAME = (By.ID, "loginusername")
    PASSWORD = (By.ID, "loginpassword")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[onclick='logIn()']")

    def open(self):
        self.driver.get("https://www.demoblaze.com/")
        self.wait_for_element(self.LOGIN_LINK)

    def open_login_modal(self):
        self.click(self.LOGIN_LINK)
        self.wait_for_element(self.USERNAME)

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON) 