from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from typing import Optional
import allure


class DriverFactory:
    """
    Фабрика для создания WebDriver instances.
    """
    
    @staticmethod
    @allure.step("Инициализировать WebDriver для браузера: {browser_name}")
    def get_driver(browser_name: str = "chrome") -> webdriver:
        """
        Создает и возвращает экземпляр WebDriver для указанного браузера.
        
        Args:
            browser_name: Название браузера ('chrome' или 'firefox')
            
        Returns:
            webdriver: Экземпляр WebDriver
            
        Raises:
            ValueError: Если указан неподдерживаемый браузер
        """
        browser_name = browser_name.lower()
        
        if browser_name == "chrome":
            service = ChromeService(ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")  # Для CI/CD
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            return webdriver.Chrome(service=service, options=options)
        
        elif browser_name == "firefox":
            service = FirefoxService(GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            return webdriver.Firefox(service=service, options=options)
        
        else:
            raise ValueError(f"Неподдерживаемый браузер: {browser_name}")