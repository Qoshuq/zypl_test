import pytest
import allure
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


@allure.feature('Авторизация')
@allure.story('Авторизация с валидными и не валидными данными')
@pytest.mark.parametrize('case, username, password',
                         [('positive', 'standard_user', 'secret_sauce'),
                          ('negative', 'test', 'test')])
def test_login(page: Page, case, username, password):
    login_page = LoginPage(page)
    with allure.step(f'Заполняем логин: {username}'):
        login_page.fill_username_(username)
    with allure.step(f'Заполняем пароль: {password}'):
        login_page.fill_password_(password)
    with allure.step('Нажимаем кнопку Submit'):
        login_page.click_login_button()
    if case == 'positive':
        with allure.step('Проверяем наличие хедера'):
            login_page.check_if_login_success()
    else:
        with allure.step('Проверяем текст с ошибкой'):
            login_page.error_message_shown()
