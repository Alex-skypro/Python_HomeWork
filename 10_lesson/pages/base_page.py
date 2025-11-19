from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure
from typing import Optional, Tuple


class BasePage:
    """
    Базовый класс для всех страниц приложения.
    Содержит общие методы для работы с веб-элементами.
    """
    
    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        """
        Инициализация базовой страницы.
        
        Args:
            driver: WebDriver instance для управления браузером
            timeout: Время ожидания элементов в секундах (по умолчанию 10)
        """
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)
    
    @allure.step("Открыть страницу по URL: {url}")
    def open(self, url: str) -> None:
        """
        Открывает указанный URL в браузере.
        
        Args:
            url: Строка с URL для открытия
        """
        self.driver.get(url)
    
    @allure.step("Найти элемент по локатору: {locator}")
    def find_element(self, locator: Tuple[str, str]) -> WebDriver:
        """
        Находит элемент на странице по указанному локатору.
        
        Args:
            locator: Кортеж (By, локатор) для поиска элемента
            
        Returns:
            WebElement: Найденный веб-элемент
            
        Raises:
            TimeoutException: Если элемент не найден за указанное время
        """
        return self.wait.until(EC.presence_of_element_located(locator))
    
    @allure.step("Кликнуть по элементу с локатором: {locator}")
    def click_element(self, locator: Tuple[str, str]) -> None:
        """
        Кликает по элементу после проверки его кликабельности.
        
        Args:
            locator: Кортеж (By, локатор) для поиска элемента
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    @allure.step("Ввести текст '{text}' в элемент с локатором: {locator}")
    def enter_text(self, locator: Tuple[str, str], text: str) -> None:
        """
        Вводит текст в поле ввода.
        
        Args:
            locator: Кортеж (By, локатор) для поиска поля ввода
            text: Текст для ввода
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    @allure.step("Получить текст элемента с локатором: {locator}")
    def get_element_text(self, locator: Tuple[str, str]) -> str:
        """
        Получает текст из элемента.
        
        Args:
            locator: Кортеж (By, локатор) для поиска элемента
            
        Returns:
            str: Текст элемента
        """
        element = self.find_element(locator)
        return element.text
    
    @allure.step("Проверить видимость элемента: {locator}")
    def is_element_visible(self, locator: Tuple[str, str]) -> bool:
        """
        Проверяет, видим ли элемент на странице.
        
        Args:
            locator: Кортеж (By, локатор) для поиска элемента
            
        Returns:
            bool: True если элемент видим, False в противном случае
        """
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    @allure.step("Получить заголовок страницы")
    def get_page_title(self) -> str:
        """
        Получает заголовок текущей страницы.
        
        Returns:
            str: Заголовок страницы
        """
        return self.driver.title