import allure
import pytest
from models.users import User
from pages.registration_page import RegistrationPage


@pytest.fixture
def registration_page():
    return RegistrationPage()


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

    @allure.title("Проверка регистрации студента")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_success_fill_form(self, setup_browser, registration_page, user_full_info):
        with allure.step("Open browser"):
            registration_page.open()
        with allure.step("Fill form"):
            registration_page.register(user_full_info)
        with allure.step("Check registration"):
            registration_page.should_have_registered(user_full_info)

    @allure.title("Проверка регистрации студента по обязательным полям")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_success_fill_only_required_fields(self, setup_browser, registration_page, user_only_required_info):
        with allure.step("open browser"):
            registration_page.open()
        with allure.step("Fill form"):
            registration_page.register(user_only_required_info)
        with allure.step("Check registration"):
            registration_page.should_have_registered(user_only_required_info)

    @allure.title("Проверка регистрации студента без заполненных данных")
    @allure.severity(allure.severity_level.NORMAL)
    def test_submit_empty_form(self, setup_browser, registration_page):
        with allure.step("open browser"):
            registration_page.open()
        with allure.step("submit empty form"):
            registration_page.submit()
        with allure.step("check validation"):
            registration_page.should_validation_visible()
