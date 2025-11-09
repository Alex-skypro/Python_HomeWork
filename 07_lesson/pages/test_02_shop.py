import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestShop:
    def test_shopping_cart_total(self, firefox_driver):
        # Инициализация страниц
        login_page = LoginPage(firefox_driver)
        products_page = ProductsPage(firefox_driver)
        cart_page = CartPage(firefox_driver)
        checkout_page = CheckoutPage(firefox_driver)
        
        # Открыть сайт магазина и авторизоваться
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        
        # Добавить товары в корзину
        products_page.add_to_cart("Sauce Labs Backpack")
        products_page.add_to_cart("Sauce Labs Bolt T-Shirt")
        products_page.add_to_cart("Sauce Labs Onesie")
        
        # Перейти в корзину и нажать Checkout
        products_page.go_to_cart()
        cart_page.checkout()
        
        # Заполнить форму данными
        checkout_page.fill_checkout_info("Иван", "Петров", "123456")
        checkout_page.continue_checkout()
        
        # Прочитать итоговую стоимость
        total_text = checkout_page.get_total_amount()
        
        # Проверить, что итоговая сумма равна $58.29
        assert total_text == "Total: $58.29", f"Ожидалась сумма $58.29, но получили {total_text}"