from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage
from typing import Tuple
import allure


class MainPage(BasePage):
    """
    Класс для работы с главной страницей приложения.
    """
    
    # Локаторы элементов главной страницы
    WELCOME_MESSAGE: Tuple[str, str] = (By.ID, "welcome-message")
    USER_MENU: Tuple[str, str] = (By.ID, "user-menu")
    LOGOUT_BUTTON: Tuple[str, str] = (By.ID, "logout-btn")
    DASHBOARD_SECTION: Tuple[str, str] = (By.ID, "dashboard")
    
    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация главной страницы.
        
        Args:
            driver: WebDriver instance для управления браузером
        """
        super().__init__(driver)
    
    @allure.step("Получить приветственное сообщение")
    def get_welcome_message(self) -> str:
        """
        Получает текст приветственного сообщения.
        
        Returns:
            str: Текст приветственного сообщения
        """
        return self.get_element_text(self.WELCOME_MESSAGE)
    
    @allure.step("Нажать кнопку выхода")
    def click_logout_button(self) -> None:
        """
        Кликает по кнопке выхода из системы.
        """
        self.click_element(self.USER_MENU)
        self.click_element(self.LOGOUT_BUTTON)
    
    @allure.step("Проверить отображение dashboard")
    def is_dashboard_visible(self) -> bool:
        """
        Проверяет, отображается ли dashboard на странице.
        
        Returns:
            bool: True если dashboard видим
        """
        return self.is_element_visible(self.DASHBOARD_SECTION)
    
    @allure.step("Проверить, что пользователь авторизован")
    def is_user_logged_in(self) -> bool:
        """
        Проверяет, авторизован ли пользователь.
        
        Returns:
            bool: True если пользователь авторизован
        """
        return self.is_element_visible(self.USER_MENU)