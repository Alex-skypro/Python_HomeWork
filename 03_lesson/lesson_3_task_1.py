from user import User

# Создаем экземпляр класса User
my_user = User("Иван", "Петров")

# Вызываем методы и выводим результаты
print(my_user.get_first_name())    # Ожидаемый результат: "Иван"
print(my_user.get_last_name())     # Ожидаемый результат: "Петров"
print(my_user.get_full_name())     # Ожидаемый результат: "Иван Петров"