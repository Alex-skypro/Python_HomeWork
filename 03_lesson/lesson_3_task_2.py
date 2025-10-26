from smartphone import Smartphone

# Создаем каталог смартфонов
catalog = [
    Smartphone("Samsung", "Galaxy S23", "+79123456789"),
    Smartphone("Apple", "iPhone 15", "+79234567890"),
    Smartphone("Xiaomi", "Redmi Note 12", "+79345678901"),
    Smartphone("Google", "Pixel 7", "+79456789012"),
    Smartphone("OnePlus", "11 Pro", "+79567890123")
]

# Печатаем каталог
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")