from allure import step
from selene import browser, be

from pages.page import open_page


class StorePage:
    def open(self):
        with step("open browser"):
            open_page('/books')
            return self

    def search(self, query):
        with step("search book"):
            browser.element('#searchBox').clear()
            browser.element('#searchBox').type(query)
            return self

    def is_book_in_list(self, query):
        with step("Check if book is exists"):
            browser.element(f'//div[@role="gridcell" and descendant-or-self::text()="{query}"]').should(be.visible)
            return self

    def check_empty_list(self):
        with step("Check list is empty"):
            browser.element('.rt-noData').should(be.visible)
            return self
