from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка драйвера
driver = webdriver.Chrome()

try:
    # Шаг 1: Перейдите на страницу
    driver.get("http://uitestingplayground.com/ajax")
    
    # Шаг 2: Нажмите на синюю кнопку
    blue_button = driver.find_element(By.ID, "ajaxButton")
    blue_button.click()
    
    # Шаг 3: Дождаться появления зеленой плашки и получить текст
    # Ждем пока элемент станет видимым
    green_banner = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
    )
    
    # Получаем текст из зеленой плашки
    banner_text = green_banner.text
    
    # Шаг 4: Вывести текст в консоль
    print(banner_text)

finally:
    # Закрываем браузер
    driver.quit()