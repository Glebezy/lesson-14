import os

from selene import browser, be, have


class StorePage:
    def open(self):
        browser.open('/books')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def search(self, query):
        browser.element('#searchBox').clear()
        browser.element('#searchBox').type(query)

    def is_book_in_list(self, query):
        browser.element(f'//div[@role="gridcell" and descendant-or-self::text()="{query}"]').should(be.visible)

    def empty_list(self):
        browser.element('.rt-noData').should(be.visible)
