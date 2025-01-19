import allure
import pytest

from models.book import Book
from pages.store_page import StorePage


@pytest.fixture
def book():
    return Book("Git Pocket Guide", "Richard E. Silverman", "O'Reilly Media")


@allure.epic("Book store application")
@allure.story("Book store")
@allure.feature("Book store search")
@allure.tag("UI")
@allure.label("owner", "Gleb T")
class TestSearchItem:
    store_page = StorePage()

    @allure.title("Проверка поиска книги по названию")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_success_search_book_by_title(self, setup_browser, book):
        (self.store_page
         .open()
         .search(book.title)
         .is_book_in_list(book.title))

    @allure.title("Проверка поиска книги по автору")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_success_search_book_by_author(self, setup_browser, book):
        (self.store_page
         .open()
         .search(book.author)
         .is_book_in_list(book.author))

    @allure.title("Проверка поиска книги по издателю")
    @allure.severity(allure.severity_level.MINOR)
    def test_success_search_book_by_publisher(self, setup_browser, book):
        (self.store_page
         .open()
         .search(book.publisher)
         .is_book_in_list(book.publisher))

    @allure.title("Проверка отображения пустого списка при отсутствии результата поиска")
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_book_list(self, setup_browser):
        (self.store_page
         .open()
         .search("1234")
         .check_empty_list())
