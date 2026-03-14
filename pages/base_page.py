from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    def wait_for_url(self, text):
        self.wait.until(EC.url_contains(text))
    def open(self, url):
        self.driver.get(url)
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
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
        
    def open(self,url):
        self.driver.get(url)
