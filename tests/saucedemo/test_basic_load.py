from selenium import webdriver

def test_load_saucedemo():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    print(driver.title)
    assert "Swag Labs" in driver.title
    driver.quit()