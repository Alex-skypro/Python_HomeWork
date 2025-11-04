from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pytest


class TestShop:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver.get("https://www.saucedemo.com/")
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()

    def test_shopping_cart_total(self):
        # Авторизация
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        
        # Добавление товаров в корзину
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        
        # Переход в корзину
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
        
        # Нажатие Checkout
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
        
        # Заполнение формы
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Иван")
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Петров")
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("123456")
        
        # Нажатие Continue
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()
        
        # Чтение итоговой стоимости
        total_element = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_total_label"))
        )
        total_text = total_element.text
        
        # Проверка итоговой суммы
        assert total_text == "Total: $58.29", f"Ожидалась сумма $58.29, но получили {total_text}"