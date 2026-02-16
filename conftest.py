from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enable": False, "profile.password_manager_leak_detection": False},)
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-features=PasswordLeakDetection")
    options.add_argument("--disable-features=PasswordCheck")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")

    yield driver
    driver.quit()