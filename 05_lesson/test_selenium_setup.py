from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def test_selenium_installation():
    """Тест для проверки установки Selenium"""
    
    # Автоматическая установка и настройка ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        # Открываем страницу
        driver.get("https://www.google.com")
        
        # Проверяем заголовок страницы
        assert "Google" in driver.title
        print("✓ Selenium успешно установлен и работает!")
        print(f"✓ Заголовок страницы: {driver.title}")
        
        # Поиск элемента на странице
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium test")
        print("✓ Поисковая строка найдена и заполнена!")
        
    except Exception as e:
        print(f"✗ Ошибка: {e}")
    
    finally:
        # Закрываем браузер
        time.sleep(2)
        driver.quit()
        print("✓ Браузер закрыт.")

if __name__ == "__main__":
    test_selenium_installation()