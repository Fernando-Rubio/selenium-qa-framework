import pytest
from pages.login_pages import LoginPage

@pytest.mark.parametrize("username,password,expected_result" , [("standard_user", "secret_sauce", "success"), ("locked_out_user", "secret_sauce", "locked"), ("problem_user", "secret_sauce", "success"), ("performance_glitch_user", "secret_sauce", "success"),])
def test_login_scenarios(driver, username, password, expected_result):
    login_page = LoginPage(driver)
    login_page.login(username, password)

    if expected_result == "success":
        assert "inventory" in driver.current_url

    elif expected_result == "locked":
        error_message = login_page.get_error_message()
        assert "locked out" in error_message.lower()