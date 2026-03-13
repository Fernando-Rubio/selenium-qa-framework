import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.saucedemo.login_page import LoginPage

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("invalid_user", "wrong_password")
    error_message = WebDriverWait(driver, 15).until(EC.visibility_of_element_located(login_page.ERROR))
    
    assert "do not match" in error_message.text.lower().strip()