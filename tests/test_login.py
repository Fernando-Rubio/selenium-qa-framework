from pages.login_pages import LoginPage

def test_valid_login(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url 

