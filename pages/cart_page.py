from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page

    cart_item = '.cart_item'

    def check_item_is_added(self, expected_name: str):
        item_name = self.page.locator(self.cart_item + " .inventory_item_name")
        expect(item_name).to_have_text(expected_name)
