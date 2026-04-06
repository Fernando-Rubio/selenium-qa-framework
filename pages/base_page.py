from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=20):
       self.driver = driver
       self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def wait_for_url(self, url_fragment):
        return self.wait.until(EC.url_contains(url_fragment))
    
    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def click(self, locator):
        element = self.wait_for_clickable(locator)
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait_for_element(locator).text
   
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def is_visible(self, locator):
        try:
            self.wait_for_element(locator)
            return True
        except:
            return False
    
