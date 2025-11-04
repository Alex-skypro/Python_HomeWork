from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest


class TestForm:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()

    def test_form_validation(self):
        # Заполнение формы
        self.driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
        # Zip code оставляем пустым
        self.driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")
        
        # Нажатие кнопки Submit
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        # Ожидание применения стилей валидации
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert.py-2")))
        
        # Проверка, что поле Zip code подсвечено красным
        zip_code_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']")
        zip_code_class = zip_code_field.get_attribute("class")
        assert "is-invalid" in zip_code_class, "Поле Zip code не подсвечено красным"
        
        # Проверка, что остальные поля подсвечены зеленым
        fields_to_check = [
            "first-name", "last-name", "address", "e-mail", 
            "phone", "city", "country", "job-position", "company"
        ]
        
        for field_name in fields_to_check:
            field = self.driver.find_element(By.CSS_SELECTOR, f"input[name='{field_name}']")
            field_class = field.get_attribute("class")
            assert "is-valid" in field_class, f"Поле {field_name} не подсвечено зеленым"