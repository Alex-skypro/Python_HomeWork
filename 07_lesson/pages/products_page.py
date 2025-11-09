from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
    
    def add_to_cart(self, product_name):
        product_id = self._get_product_id(product_name)
        self.driver.find_element(By.CSS_SELECTOR, f"#add-to-cart-{product_id}").click()
    
    def go_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    
    def _get_product_id(self, product_name):
        product_ids = {
            "Sauce Labs Backpack": "sauce-labs-backpack",
            "Sauce Labs Bolt T-Shirt": "sauce-labs-bolt-t-shirt", 
            "Sauce Labs Onesie": "sauce-labs-onesie"
        }
        return product_ids.get(product_name)