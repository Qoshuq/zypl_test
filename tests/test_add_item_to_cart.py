import allure
from playwright.sync_api import expect, Page
from pages.product_page import ProductPage
from pages.cart_page import CartPage


@allure.feature('Добавление товара в корзину')
def test_add_item_to_cart(page: Page, login):
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    with allure.step('Добавляем товар в корзину'):
        product_page.add_item_to_cart()
    with allure.step('Переходим в корзину'):
        product_page.go_to_cart()
    with allure.step('Проверяем добавился ли выбранный товар в корзину'):
        cart_page.check_item_is_added('Sauce Labs Backpack')
