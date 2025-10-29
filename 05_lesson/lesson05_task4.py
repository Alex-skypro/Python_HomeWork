from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time

def firefox_login_test():
    """
    Скрипт для авторизации на сайте и получения сообщения об успехе
    - Открывает Firefox
    - Переходит на страницу логина
    - Вводит логин и пароль
    - Нажимает кнопку Login
    - Получает текст с зеленой плашки
    - Выводит текст в консоль
    - Закрывает браузер
    """
    print("🦊 Запуск скрипта авторизации для Firefox...")
    
    try:
        # Настройка FirefoxDriver с автоматической установкой
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        
        # Открываем страницу логина
        print("📄 Открываем страницу http://the-internet.herokuapp.com/login...")
        driver.get("http://the-internet.herokuapp.com/login")
        
        # Ждем загрузки страницы
        time.sleep(2)
        
        # Ищем поле username
        print("🔍 Ищем поле username...")
        username_field = driver.find_element(By.ID, "username")
        
        # Вводим логин
        print("⌨️  Вводим логин 'tomsmith'...")
        username_field.send_keys("tomsmith")
        
        # Ищем поле password
        print("🔍 Ищем поле password...")
        password_field = driver.find_element(By.ID, "password")
        
        # Вводим пароль
        print("⌨️  Вводим пароль 'SuperSecretPassword!'...")
        password_field.send_keys("SuperSecretPassword!")
        
        # Ждем секунду чтобы увидеть введенные данные
        time.sleep(1)
        
        # Ищем кнопку Login
        print("🔍 Ищем кнопку Login...")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        # Нажимаем кнопку Login
        print("🖱️  Нажимаем кнопку Login...")
        login_button.click()
        
        # Ждем редиректа и появления зеленой плашки
        print("⏳ Ожидаем загрузки страницы после логина...")
        time.sleep(3)
        
        # Ищем зеленую плашку с сообщением об успехе
        # Зеленая плашка имеет класс 'flash success'
        print("🔍 Ищем зеленую плашку с сообщением...")
        flash_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
        
        # Получаем текст из плашки
        success_text = flash_message.text
        print("=" * 60)
        print("💚 ТЕКСТ С ЗЕЛЕНОЙ ПЛАШКИ:")
        print(success_text)
        print("=" * 60)
        
        # Ждем чтобы увидеть результат
        time.sleep(2)
        
        print("✅ Авторизация успешно выполнена!")
        
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")
        
    finally:
        # Закрываем браузер
        if 'driver' in locals():
            print("🔚 Закрываем браузер с помощью quit()...")
            driver.quit()
            print("🦊 Браузер Firefox закрыт.")

if __name__ == "__main__":
    firefox_login_test()
    