import pytest
import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.feature("Авторизация пользователя")
@allure.severity(allure.severity_level.CRITICAL)
class TestLogin:
    """
    Тесты для функциональности авторизации пользователя.
    """
    
    @allure.title("Успешная авторизация с валидными данными")
    @allure.description("""
    Тест проверяет успешную авторизацию пользователя 
    с корректными учетными данными.
    
    Steps:
    1. Открыть страницу логина
    2. Ввести валидный username
    3. Ввести валидный password
    4. Нажать кнопку Login
    5. Проверить успешную авторизацию
    """)
    def test_successful_login(self, login_page: LoginPage, main_page: MainPage) -> None:
        """
        Тест успешной авторизации пользователя.
        
        Args:
            login_page: Фикстура страницы логина
            main_page: Фикстура главной страницы
        """
        with allure.step("Открыть страницу логина"):
            login_page.open("https://example.com/login")
        
        with allure.step("Выполнить авторизацию с валидными данными"):
            login_page.login("valid_user", "valid_password")
        
        with allure.step("Проверить успешную авторизацию"):
            assert main_page.is_user_logged_in(), "Пользователь не авторизован"
            assert main_page.is_dashboard_visible(), "Dashboard не отображается"
            
        with allure.step("Проверить приветственное сообщение"):
            welcome_text = main_page.get_welcome_message()
            assert "Welcome" in welcome_text, f"Неверное приветствие: {welcome_text}"
    
    @allure.title("Неуспешная авторизация с невалидным паролем")
    @allure.description("""
    Тест проверяет поведение системы при вводе неверного пароля.
    
    Steps:
    1. Открыть страницу логина
    2. Ввести валидный username
    3. Ввести невалидный password
    4. Нажать кнопку Login
    5. Проверить сообщение об ошибке
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_invalid_password(self, login_page: LoginPage) -> None:
        """
        Тест авторизации с неверным паролем.
        
        Args:
            login_page: Фикстура страницы логина
        """
        with allure.step("Открыть страницу логина"):
            login_page.open("https://example.com/login")
        
        with allure.step("Выполнить авторизацию с невалидным паролем"):
            login_page.login("valid_user", "invalid_password")
        
        with allure.step("Проверить сообщение об ошибке"):
            assert login_page.is_error_message_displayed(), "Сообщение об ошибке не отображается"
            
            error_text = login_page.get_error_message()
            expected_error = "Invalid credentials"
            assert expected_error in error_text, f"Неверное сообщение об ошибке: {error_text}"
    
    @allure.title("Неуспешная авторизация с пустыми полями")
    @allure.description("""
    Тест проверяет поведение системы при попытке входа с пустыми полями.
    
    Steps:
    1. Открыть страницу логина
    2. Оставить поля пустыми
    3. Нажать кнопку Login
    4. Проверить сообщение о необходимости заполнения полей
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_empty_fields(self, login_page: LoginPage) -> None:
        """
        Тест авторизации с пустыми полями.
        
        Args:
            login_page: Фикстура страницы логина
        """
        with allure.step("Открыть страницу логина"):
            login_page.open("https://example.com/login")
        
        with allure.step("Нажать кнопку Login без заполнения полей"):
            login_page.click_login_button()
        
        with allure.step("Проверить сообщение об ошибке валидации"):
            assert login_page.is_error_message_displayed(), "Сообщение об ошибке не отображается"
            
            error_text = login_page.get_error_message()
            assert "required" in error_text.lower(), f"Неверное сообщение об ошибке: {error_text}"


@allure.feature("Выход из системы")
@allure.severity(allure.severity_level.CRITICAL)
class TestLogout:
    """
    Тесты для функциональности выхода из системы.
    """
    
    @allure.title("Успешный выход из системы")
    @allure.description("""
    Тест проверяет корректный выход авторизованного пользователя из системы.
    
    Steps:
    1. Выполнить успешную авторизацию
    2. Нажать кнопку выхода
    3. Проверить переход на страницу логина
    """)
    def test_successful_logout(self, login_page: LoginPage, main_page: MainPage) -> None:
        """
        Тест успешного выхода из системы.
        
        Args:
            login_page: Фикстура страницы логина
            main_page: Фикстура главной страницы
        """
        with allure.step("Выполнить предварительную авторизацию"):
            login_page.open("https://example.com/login")
            login_page.login("valid_user", "valid_password")
            assert main_page.is_user_logged_in(), "Пользователь не авторизован"
        
        with allure.step("Выполнить выход из системы"):
            main_page.click_logout_button()
        
        with allure.step("Проверить переход на страницу логина"):
            assert login_page.is_element_visible(login_page.USERNAME_FIELD), "Не произошел переход на страницу логина"
            assert login_page.is_element_visible(login_page.LOGIN_BUTTON), "Кнопка логина не отображается"