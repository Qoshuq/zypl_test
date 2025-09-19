import time
from playwright.sync_api import Page, expect


def test_page_has_title(page: Page):
    page.goto('https://www.google.com/')
    expect(page).to_have_title('Google')
