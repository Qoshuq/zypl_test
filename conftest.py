import pytest
from playwright.sync_api import Playwright
from pages.login_page import LoginPage


@pytest.fixture(scope='session')
def browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)

    yield browser

    browser.close()


@pytest.fixture(scope='function')
def page(browser):
    context = browser.new_context()
    page = context.new_page()

    yield page

    context.close()


@pytest.fixture(scope='function')
def login(page):
    login_page = LoginPage(page)
    login_page.fill_username_('standard_user')
    login_page.fill_password_('secret_sauce')
    login_page.click_login_button()
