from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.goto('https://www.saucedemo.com/')
        self.username_input = page.locator('#user-name')
        self.password_input = page.locator('#password')
        self.login_button = page.get_by_role('button')
        self.error_message = page.locator('#error')
        self.header = page.locator('#menu_button_container')

    def fill_username_(self, username):
        self.username_input.fill(username)

    def fill_password_(self, password):
        self.password_input.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def error_message_shown(self):
        self.error_message.is_visible()

    def check_if_login_success(self):
        self.header.is_visible()

