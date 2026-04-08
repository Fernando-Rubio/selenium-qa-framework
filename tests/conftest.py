from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import pytest
import os


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")

    prefs = { 
        "credentials_enable_service": False, 
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False, 
        "autofill.profile_enabled": False,
        "autofill.credit_card_enabled": False
    }
    options.add_experimental_option("prefs", prefs)

    options.add_argument("--disable-features=PasswordLeakDetection,PasswordCheck,PasswordManagerOnboarding,AutofillServerCommunication,OptimizationHints")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1920, 1080)

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