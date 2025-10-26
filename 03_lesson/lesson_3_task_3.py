from address import Address
from mailing import Mailing

# Создаем адреса
to_address = Address("123456", "Москва", "Ленина", "15", "25")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "42", "13")

# Создаем почтовое отправление
mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=250,
    track="TRACK123456789"
)

# Выводим информацию об отправлении
print(mailing)