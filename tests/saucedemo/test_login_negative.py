from pages.login_pages import LoginPage

def test_invalid_login(driver):
    login = LoginPage(driver)

    login.login("standard_user", "wrong_password")

    error_message = login.get_error_message()

    assert "Username and password do not match" in error_message