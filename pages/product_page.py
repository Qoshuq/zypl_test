from playwright.sync_api import Page


class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = page.locator('#add-to-cart-sauce-labs-backpack')
        self.go_to_cart_button = page.locator('[data-test="shopping-cart-link"]')

    def add_item_to_cart(self):
        self.add_to_cart_button.first.click()

    def go_to_cart(self):
        self.go_to_cart_button.click()
