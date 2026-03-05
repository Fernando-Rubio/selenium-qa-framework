from pages.orangehrm.login_page import OrangeHRMLoginPage

def test_valid_login(driver):

    login_page = OrangeHRMLoginPage(driver)
    login_page.open()
    login_page.login("Admin", "admin123")

    assert "dashboard" in driver.current_url.lower()