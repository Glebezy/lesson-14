import allure
import pytest

from models.user import User
from pages.registration_page import RegistrationPage


@pytest.fixture
def user_full_info():
    return User("John", "Doe", "Male", "1234567890", "gte@mail.com",
                "7 August,2023", ["English", "Math"], ["Sports", "Music"],
                "pic.jpeg", "123 Main St, Haryana Karnal")


@pytest.fixture
def user_only_required_info():
    return User("John", "Doe", "Male", "1234567890")


@allure.epic("Student Registration Form")
@allure.story("Practice form")
@allure.feature("Register Student")
@allure.tag("UI")
@allure.label("owner", "Gleb T")
class TestFillForm:
    registration_page = RegistrationPage()

    @allure.title("Проверка регистрации студента")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_success_fill_form(self, setup_browser, user_full_info):
        (self.registration_page
         .open()
         .register(user_full_info)
         .should_have_registered(user_full_info))

    @allure.title("Проверка регистрации студента по обязательным полям")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_success_fill_only_required_fields(self, setup_browser, user_only_required_info):
        (self.registration_page
         .open()
         .register(user_only_required_info)
         .should_have_registered(user_only_required_info))

    @allure.title("Проверка регистрации студента без заполненных данных")
    @allure.severity(allure.severity_level.NORMAL)
    def test_submit_empty_form(self, setup_browser):
        (self.registration_page
         .open()
         .submit_form()
         .should_validation_visible())
