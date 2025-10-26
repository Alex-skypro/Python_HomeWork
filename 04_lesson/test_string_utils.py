import pytest
from string_utils import StringUtils

class TestCapitalize:
    """Тесты для функции capitalize"""
    
    # ПОЗИТИВНЫЙ СЦЕНАРИЙ
    def test_capitalize_positive_regular_string(self):
        """Позитивный: обычная строка 'тест' -> 'Тест'"""
        utils = StringUtils()
        assert utils.capitalize("тест") == "Тест"

    # НЕГАТИВНЫЙ СЦЕНАРИЙ
    def test_capitalize_negative_empty_string(self):
        """Негативный: пустая строка '' -> ''"""
        utils = StringUtils()
        assert utils.capitalize("") == ""


class TestTrim:
    """Тесты для функции trim"""
    
    # ПОЗИТИВНЫЙ СЦЕНАРИЙ
    def test_trim_positive_regular_string(self):
        """Позитивный: обычная строка с пробелами '   тест' -> 'тест'"""
        utils = StringUtils()
        assert utils.trim("   тест") == "тест"
    
    # НЕГАТИВНЫЙ СЦЕНАРИЙ     
    def test_trim_negative_space_string(self):
        """Негативный: строка с пробелом ' ' -> ''"""
        utils = StringUtils()
        assert utils.trim(" ") == ""


class TestContains:
    """Тесты для функции contains"""

    # ПОЗИТИВНЫЙ СЦЕНАРИЙ
    def test_contains_positive_numbers_string(self):
        """Позитивный: числа как строка содержит цифру '123' contains '2' -> True"""
        utils = StringUtils()
        assert utils.contains("123", "2") is True

    # НЕГАТИВНЫЙ СЦЕНАРИЙ
    def test_contains_negative_symbol_not_found(self):
        """Негативный: строка не содержит символ 'тест' contains 'x' -> False"""
        utils = StringUtils()
        assert utils.contains("тест", "x") is False


class TestDeleteSymbol:
    """Тесты для функции delete_symbol"""

    # ПОЗИТИВНЫЙ СЦЕНАРИЙ
    def test_delete_symbol_positive_numbers_string(self):
        """Позитивный: числа как строка удалить цифру '123' delete '2' -> '13'"""
        utils = StringUtils()
        assert utils.delete_symbol("123", "2") == "13"

    # НЕГАТИВНЫЙ СЦЕНАРИЙ
    def test_delete_symbol_negative_empty_string(self):
        """Негативный: пустая строка удалить символ '' delete 'a' -> ''"""
        utils = StringUtils()
        assert utils.delete_symbol("", "a") == ""

