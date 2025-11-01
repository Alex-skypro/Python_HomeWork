from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Переходим на сайт
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    
    # Ждем загрузки всех картинок - ожидаем, что у последней картинки появится атрибут src
    wait = WebDriverWait(driver, 10)
    
    # Ожидаем загрузки последней (4-й) картинки
    last_image = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#image-container img:nth-child(4)"))
    )
    
    # Дополнительная проверка - ждем пока у последней картинки появится непустой src
    wait.until(
        lambda driver: last_image.get_attribute("src") and len(last_image.get_attribute("src")) > 0
    )
    
    print("Все картинки загружены!")
    
    # Получаем 3-ю картинку (индексация с 1)
    third_image = driver.find_element(By.CSS_SELECTOR, "#image-container img:nth-child(3)")
    
    # Получаем значение атрибута src у 3-й картинки
    src_value = third_image.get_attribute("src")
    
    # Выводим значение в консоль
    print(f"SRC третьей картинки: {src_value}")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрываем браузер
    driver.quit()