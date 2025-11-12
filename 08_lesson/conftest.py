import pytest
import sys
import os

# Добавляем корневую директорию в путь Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture(autouse=True)
def setup_teardown():
    """Общая настройка и очистка для всех тестов"""
    # Setup
    yield
    # Teardown (при необходимости)