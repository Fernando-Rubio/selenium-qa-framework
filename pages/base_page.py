from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    def wait_for_url(self, url_fragment):
        self.wait.until(EC.url_contains(url_fragment))
    def open(self, url):
        self.driver.get(url)
    def wait_for_element(self, locator, timeout=15):
        return self.wait.until(EC.element_to_be_clickable(locator), (timeout))
    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    def click(self, locator, timeout=15):
        element = self.wait.until(EC.element_to_be_clickable(locator), (timeout))
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)
    def type(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def is_visible(self, locator):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
    
