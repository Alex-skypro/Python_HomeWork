from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage
from typing import Tuple
import allure


class LoginPage(BasePage):
    """
    Класс для работы со страницей авторизации.
    """
    
    # Локаторы элементов страницы логина
    USERNAME_FIELD: Tuple[str, str] = (By.ID, "username")
    PASSWORD_FIELD: Tuple[str, str] = (By.ID, "password")
    LOGIN_BUTTON: Tuple[str, str] = (By.ID, "login-btn")
    ERROR_MESSAGE: Tuple[str, str] = (By.CLASS_NAME, "error-message")
    SUCCESS_MESSAGE: Tuple[str, str] = (By.CLASS_NAME, "success-message")
    
    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы логина.
        
        Args:
            driver: WebDriver instance для управления браузером
        """
        super().__init__(driver)
    
    @allure.step("Ввести логин: {username}")
    def enter_username(self, username: str) -> None:
        """
        Вводит логин в поле username.
        
        Args:
            username: Логин пользователя
        """
        self.enter_text(self.USERNAME_FIELD, username)
    
    @allure.step("Ввести пароль")
    def enter_password(self, password: str) -> None:
        """
        Вводит пароль в поле password.
        
        Args:
            password: Пароль пользователя
        """
        self.enter_text(self.PASSWORD_FIELD, password)
    
    @allure.step("Нажать кнопку входа")
    def click_login_button(self) -> None:
        """
        Кликает по кнопке входа в систему.
        """
        self.click_element(self.LOGIN_BUTTON)
    
    @allure.step("Выполнить полный процесс логина")
    def login(self, username: str, password: str) -> None:
        """
        Выполняет полный процесс авторизации.
        
        Args:
            username: Логин пользователя
            password: Пароль пользователя
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    @allure.step("Получить текст ошибки")
    def get_error_message(self) -> str:
        """
        Получает текст сообщения об ошибке.
        
        Returns:
            str: Текст ошибки или пустая строка если ошибки нет
        """
        try:
            return self.get_element_text(self.ERROR_MESSAGE)
        except:
            return ""
    
    @allure.step("Проверить наличие сообщения об ошибке")
    def is_error_message_displayed(self) -> bool:
        """
        Проверяет, отображается ли сообщение об ошибке.
        
        Returns:
            bool: True если сообщение об ошибке отображается
        """
        return self.is_element_visible(self.ERROR_MESSAGE)
    
    @allure.step("Проверить успешность авторизации")
    def is_login_successful(self) -> bool:
        """
        Проверяет, была ли авторизация успешной.
        
        Returns:
            bool: True если авторизация прошла успешно
        """
        return self.is_element_visible(self.SUCCESS_MESSAGE)