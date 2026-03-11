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
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_LINK))

    def open_login_modal(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_LINK)).click()

    def login(self, username, password):
        self.click(self.LOGIN_BUTTON)
        self.wait.until(EC.visibility_of_element_located(self.USERNAME))
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON) 