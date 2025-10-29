from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def click_blue_button():
    """
    Скрипт для клика на синюю кнопку на странице uitestingplayground.com/classattr
    """
    print("🚀 Запуск скрипта...")
    
    # Настройка ChromeDriver с автоматической установкой
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        # Открываем страницу
        print("📄 Открываем страницу...")
        driver.get("http://uitestingplayground.com/classattr")
        
        # Ждем загрузки страницы
        time.sleep(2)
        
        # Ищем синюю кнопку по классу (синяя кнопка имеет класс 'btn-primary')
        blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
        
        # Кликаем на синюю кнопку
        print("🔵 Кликаем на синюю кнопку...")
        blue_button.click()
        
        # Ждем немного чтобы увидеть результат
        time.sleep(2)
        
        print("✅ Скрипт успешно выполнен!")
        
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")
        
    finally:
        # Закрываем браузер
        driver.quit()
        print("🔚 Браузер закрыт.\n")

if __name__ == "__main__":
    click_blue_button()
    