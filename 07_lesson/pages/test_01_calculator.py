import pytest
from pages.calculator_page import CalculatorPage

class TestCalculator:
    def test_slow_calculator(self, chrome_driver):
        calculator_page = CalculatorPage(chrome_driver)
        
        # Открыть страницу калькулятора
        calculator_page.open()
        
        # Ввести значение 45 в поле задержки
        calculator_page.set_delay(45)
        
        # Нажать кнопки: 7, +, 8, =
        calculator_page.click_button("7")
        calculator_page.click_button("+")
        calculator_page.click_button("8")
        calculator_page.click_button("=")
        
        # Проверить, что в окне отобразится результат 15 через 45 секунд
        result = calculator_page.get_result()
        assert result == "15", f"Ожидался результат 15, но получили {result}"