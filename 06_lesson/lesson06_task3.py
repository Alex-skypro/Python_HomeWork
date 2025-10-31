from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка драйвера
driver = webdriver.Chrome()

try:
    # Шаг 1: Перейдите на сайт
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    
    # Шаг 2: Дождитесь загрузки всех картинок
    # Ждем пока все изображения загрузятся (атрибут complete станет True)
    images = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#image-container img"))
    )
    
    # Ждем пока все изображения полностью загрузятся
    WebDriverWait(driver, 15).until(
        lambda driver: all(image.get_attribute("complete") for image in images)
    )
    
    # Шаг 3: Получите значение атрибута src у 3-й картинки
    third_image_src = images[2].get_attribute("src")
    
    # Шаг 4: Выведите значение в консоль
    print(third_image_src)

finally:
    # Закрываем браузер
    driver.quit()