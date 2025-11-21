# Инструкция по настройке и запуску тестов с Allure

## 1. Установка необходимых компонентов

### Установка Python пакетов:
pip install -r requirements.txt

Содержимое requirements.txt:
pytest
selenium
allure-pytest
pytest-html

### Установка Allure Framework:

Для Windows (через Scoop):
1. Установите Scoop: https://scoop.sh/
2. scoop install allure

Для MacOS:
1. brew install allure

Для Linux (Ubuntu/Debian):
1. sudo apt-add-repository ppa:qameta/allure
2. sudo apt-get update
3. sudo apt-get install allure

## 2. Структура проекта

project/
├── lesson_10/
│   ├── pages/
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   └── main_page.py
│   ├── tests/
│   │   └── test_ui.py
│   ├── conftest.py
│   └── README.md

## 3. Запуск тестов

### Базовый запуск всех тестов:
pytest lesson_10/tests/ --alluredir=lesson_10/allure-results

### Запуск с конкретным браузером:
pytest lesson_10/tests/ --browser=chrome --alluredir=lesson_10/allure-results
pytest lesson_10/tests/ --browser=firefox --alluredir=lesson_10/allure-results

### Запуск в headless режиме:
pytest lesson_10/tests/ --headless --alluredir=lesson_10/allure-results

### Запуск с указанием базового URL:
pytest lesson_10/tests/ --base-url=https://yourapp.com --alluredir=lesson_10/allure-results

### Запуск конкретных тестов:
pytest lesson_10/tests/test_login.py --alluredir=lesson_10/allure-results
pytest lesson_10/tests/test_login.py::TestLogin --alluredir=lesson_10/allure-results
pytest lesson_10/tests/test_login.py::TestLogin::test_successful_login --alluredir=lesson_10/allure-results

## 4. Генерация отчета Allure

### Генерация статического отчета:
allure generate lesson_10/allure-results -o lesson_10/allure-report --clean

### Просмотр сгенерированного отчета:
allure open lesson_10/allure-report

### Запуск сервера для просмотра отчета (без генерации):
allure serve lesson_10/allure-results

## 5. Дополнительные команды

### Запуск с детализированным выводом:
pytest lesson_10/tests/ -v --alluredir=lesson_10/allure-results

### Запуск с выводом print-сообщений:
pytest lesson_10/tests/ -s --alluredir=lesson_10/allure-results

### Запуск и остановка после первого упавшего теста:
pytest lesson_10/tests/ -x --alluredir=lesson_10/allure-results

### Параллельный запуск тестов:
pytest lesson_10/tests/ -n 2 --alluredir=lesson_10/allure-results

## 6. Просмотр отчета

После выполнения команды `allure serve` или `allure open` откроется браузер с отчетом, содержащим:

- Overview - общая статистика
- Suites - тестовые наборы
- Behaviors - группировка по функциональностям
- Graphs - графики и диаграммы
- Timeline - временная шкала выполнения

## 7. Очистка результатов

### Удаление предыдущих результатов:
rm -rf lesson_10/allure-results/
rm -rf lesson_10/allure-report/

### Или через очистку в одной команде:
allure generate --clean

## 8. Пример полного цикла выполнения

1. Запуск тестов:
   pytest lesson_10/tests/ --alluredir=lesson_10/allure-results

2. Генерация отчета:
   allure generate lesson_10/allure-results -o lesson_10/allure-report --clean

3. Просмотр отчета:
   allure open lesson_10/allure-report

## 9. Пояснения по опциям командной строки

--browser=chrome/firefox    Выбор браузера для тестов
--headless                  Запуск браузера без GUI
--base-url=URL              Базовый URL тестируемого приложения
--alluredir=DIR             Директория для сохранения результатов Allure
-v                          Детализированный вывод
-s                          Вывод print-сообщений
-x                          Остановка после первого упавшего теста
-n N                        Параллельный запуск в N потоков