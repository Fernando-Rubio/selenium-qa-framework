from selenium import webdriver
from datetime import datetime
import pytest
import os


@pytest.fixture
def driver():
    optons = webdriver.ChromeOptions()

    optons.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False})

    optons.add_argument("--disable-notifications")
    optons.add_argument("--disable-infobars")
    optons.add_argument("--disable-save-password-bubble")
    optons.add_argument("--disable-features=PasswordLeakDetection")
    optons.add_argument("--disable-features=PasswordCheck")

    optons.add_argument("--headless")
    optons.add_argument("--no-sandbox")
    optons.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=optons)

    driver.maximize_window()

    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name
            file_path = f"{screenshots_dir}/{test_name}_{timestamp}.png"

            driver.save_screenshot(file_path)
            print(f"\nScreenshot saved to {file_path}")