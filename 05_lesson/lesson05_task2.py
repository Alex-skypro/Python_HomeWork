from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def click_dynamic_button():
    """
    Скрипт для клика на синюю кнопку с динамическим ID
    на странице uitestingplayground.com/dynamicid
    """
    print("🚀 Запуск скрипта для кнопки с динамическим ID...")
    
    # Настройка ChromeDriver с автоматической установкой
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        # Открываем страницу
        print("📄 Открываем страницу uitestingplayground.com/dynamicid...")
        driver.get("http://uitestingplayground.com/dynamicid")
        
        # Явное ожидание загрузки страницы
        wait = WebDriverWait(driver, 10)
        
        # Ищем синюю кнопку по классу (динамический ID меняется, но класс остается)
        # Кнопка имеет класс 'btn-primary'
        blue_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
        )
        
        # Альтернативные способы поиска (на случай если класс изменится):
        # 1. По XPath с частичным совпадением класса
        # blue_button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn')]")
        
        # 2. По тексту кнопки
        # blue_button = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")
        
        print(f"🔵 Найдена кнопка с динамическим ID")
        print(f"   Текст кнопки: '{blue_button.text}'")
        print(f"   Класс кнопки: '{blue_button.get_attribute('class')}'")
        print(f"   ID кнопки: '{blue_button.get_attribute('id')}'")
        
        # Кликаем на синюю кнопку
        print("🖱️ Кликаем на синюю кнопку...")
        blue_button.click()
        
        # Ждем обработки клика
        time.sleep(2)
        
        print("✅ Скрипт успешно выполнен!")
        
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")
        
    finally:
        # Закрываем браузер
        driver.quit()
        print("🔚 Браузер закрыт.\n")
        print("-" * 50)

if __name__ == "__main__":
    click_dynamic_button()
    