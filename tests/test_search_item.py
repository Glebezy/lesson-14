import allure
import pytest

from models.book import Book
from pages.store_page import StorePage


@pytest.fixture
def store_page():
    return StorePage()


@pytest.fixture
def book():
    return Book("Git Pocket Guide", "Richard E. Silverman", "O'Reilly Media")


@allure.epic("Book store application")
@allure.story("Book store")
@allure.feature("Book store search")
@allure.tag("UI")
@allure.label("owner", "Gleb T")
class TestSearchItem:

    @allure.title("Проверка поиска книги по названию")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_success_search_book_by_title(self, setup_browser, store_page, book):
        with allure.step("Open browser"):
            store_page.open()
        with allure.step("Search book by title"):
            store_page.search(book.title)
        with allure.step("Check if book is exists"):
            store_page.is_book_in_list(book.title)

    @allure.title("Проверка поиска книги по автору")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_success_search_book_by_author(self, setup_browser, store_page, book):
        with allure.step("Open browser"):
            store_page.open()
        with allure.step("Search book by author"):
            store_page.search(book.author)
        with allure.step("Check if book is exists"):
            store_page.is_book_in_list(book.author)

    @allure.title("Проверка поиска книги по издателю")
    @allure.severity(allure.severity_level.MINOR)
    def test_success_search_book_by_publisher(self, setup_browser, store_page, book):
        with allure.step("Open browser"):
            store_page.open()
        with allure.step("Search book by publisher"):
            store_page.search(book.publisher)
        with allure.step("Check if book is exists"):
            store_page.is_book_in_list(book.publisher)

    @allure.title("Проверка отображения пустого списка при отсутствии результата поиска")
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_book_list(self, setup_browser, store_page):
        with allure.step("Open browser"):
            store_page.open()
        with allure.step("Search invalid book"):
            store_page.search('1234')
        with allure.step("Check list is empty"):
            store_page.empty_list()
