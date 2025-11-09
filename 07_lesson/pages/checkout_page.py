from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(postal_code)
    
    def continue_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()
    
    def get_total_amount(self):
        total_element = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_total_label"))
        )
        return total_element.text