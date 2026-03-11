from pages.demoqa.practice_form_page import PracticeFormPage
import pytest

def test_submit_form_success(driver):
    page = PracticeFormPage(driver)
    page.open()
    page.fill_form("Fernando", "Rubio", "test@email.com", "1234567890")
    page.submit_form()

    assert page.is_modal_displayed()

def test_submit_form_empty(driver):
    page = PracticeFormPage(driver)
    page.open()
    page.submit_form()

    assert not page.is_modal_displayed()