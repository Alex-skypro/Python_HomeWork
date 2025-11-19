import pytest
import allure
from selenium import webdriver
from utils.drivers import DriverFactory
from typing import Generator


@pytest.fixture(scope="function")
def driver() -> Generator[webdriver, None, None]:
    """
    Фикстура для инициализации и закрытия WebDriver.
    
    Yields:
        webdriver: Экземпляр WebDriver
        
    Notes:
        Закрывает браузер после завершения теста
    """
    driver_instance = None
    try:
        driver_instance = DriverFactory.get_driver("chrome")
        driver_instance.implicitly_wait(10)
        driver_instance.maximize_window()
        yield driver_instance
    finally:
        if driver_instance:
            driver_instance.quit()


@pytest.fixture
def login_page(driver: webdriver) -> 'LoginPage':
    """
    Фикстура для создания экземпляра LoginPage.
    
    Args:
        driver: WebDriver instance из фикстуры driver
        
    Returns:
        LoginPage: Экземпляр страницы логина
    """
    from pages.login_page import LoginPage
    return LoginPage(driver)


@pytest.fixture
def main_page(driver: webdriver) -> 'MainPage':
    """
    Фикстура для создания экземпляра MainPage.
    
    Args:
        driver: WebDriver instance из фикстуры driver
        
    Returns:
        MainPage: Экземпляр главной страницы
    """
    from pages.main_page import MainPage
    return MainPage(driver)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук для создания скриншотов при падении тестов.
    """
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )