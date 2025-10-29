from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time

def firefox_input_test():
    """
    Скрипт для работы с полем ввода в Firefox
    - Открывает Firefox
    - Переходит на страницу inputs
    - Вводит 'Sky'
    - Очищает поле
    - Вводит 'Pro'
    - Закрывает браузер
    """
    print("🦊 Запуск скрипта для Firefox...")
    
    try:
        # Настройка FirefoxDriver с автоматической установкой
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        
        # Открываем страницу
        print("📄 Открываем страницу http://the-internet.herokuapp.com/inputs...")
        driver.get("http://the-internet.herokuapp.com/inputs")
        
        # Ждем загрузки страницы
        time.sleep(2)
        
        # Ищем поле ввода (обычно это input[type='text'] или input[type='number'])
        # На этой странице поле ввода имеет type='number'
        input_field = driver.find_element(By.TAG_NAME, "input")
        
        print(f"🔍 Найдено поле ввода:")
        print(f"   Тип: {input_field.get_attribute('type')}")
        print(f"   Placeholder: {input_field.get_attribute('placeholder')}")
        
        # Вводим текст "Sky"
        print("⌨️  Вводим текст 'Sky'...")
        input_field.send_keys("Sky")
        
        # Проверяем что текст введен
        current_value = input_field.get_attribute('value')
        print(f"   Текущее значение поля: '{current_value}'")
        
        # Ждем секунду чтобы увидеть результат
        time.sleep(1)
        
        # Очищаем поле
        print("🧹 Очищаем поле...")
        input_field.clear()
        
        # Проверяем что поле очищено
        current_value = input_field.get_attribute('value')
        print(f"   Текущее значение поля после очистки: '{current_value}'")
        
        # Ждем секунду
        time.sleep(1)
        
        # Вводим текст "Pro"
        print("⌨️  Вводим текст 'Pro'...")
        input_field.send_keys("Pro")
        
        # Проверяем финальное значение
        current_value = input_field.get_attribute('value')
        print(f"   Финальное значение поля: '{current_value}'")
        
        # Ждем секунду чтобы увидеть результат
        time.sleep(1)
        
        print("✅ Все операции успешно выполнены!")
        
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")
        
    finally:
        # Закрываем браузер
        if 'driver' in locals():
            print("🔚 Закрываем браузер...")
            driver.quit()
            print("🦊 Браузер Firefox закрыт.")

if __name__ == "__main__":
    firefox_input_test()
    