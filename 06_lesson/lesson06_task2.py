from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка драйвера
driver = webdriver.Chrome()

try:
    # Шаг 1: Перейдите на страницу
    driver.get("http://uitestingplayground.com/textinput")
    
    # Шаг 2: Укажите в поле ввода текст SkyPro
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "newButtonName"))
    )
    input_field.clear()
    input_field.send_keys("SkyPro")
    
    # Шаг 3: Нажмите на синюю кнопку
    blue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "updatingButton"))
    )
    blue_button.click()
    
    # Шаг 4: Получите текст кнопки и выведите в консоль
    updated_button = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )
    
    button_text = driver.find_element(By.ID, "updatingButton").text
    print(button_text)

finally:
    # Закрываем браузер
    driver.quit()