from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def find_item_and_click_button(driver, item_name, timeout=10):
    """Find an inventory item by name and click its button (Add to Cart / Remove)."""
    items = WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
    for item in items:
        name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        if name == item_name:
            item.find_element(By.TAG_NAME, "button").click()
            return True
    raise Exception(f"Item ' {item_name}' not found")