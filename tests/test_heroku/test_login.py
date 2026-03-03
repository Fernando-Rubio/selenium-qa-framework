import pytest
from pages.heroku.login_page import HerokuLoginPage

def test_valid_login(driver):
    page = HerokuLoginPage(driver)
    page.open()
    page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in page.get_flash_message()

def test_invalid_login(driver):
    page = HerokuLoginPage(driver)
    page.open()
    page.login("wrong", "wrong")
    assert "Your username is invalid!" in page.get_flash_message()