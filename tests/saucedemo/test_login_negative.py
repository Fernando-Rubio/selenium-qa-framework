import pytest
from pages.saucedemo.login_page import LoginPage

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("invalid_user", "wrong_password")
    error_message = login_page.get_error_message()
    assert "do not match" in error_message.lower().strip()