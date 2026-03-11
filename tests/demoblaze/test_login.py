import pytest
from pages.demoblaze.login_page import DemoBlazeLoginPage

def test_login_modal_opens(driver):
    login_page = DemoBlazeLoginPage(driver)
    login_page.open()
    login_page.open_login_modal()
    
   
    assert "demoblaze" in driver.current_url.lower()