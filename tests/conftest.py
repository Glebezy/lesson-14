import allure_commons
import pytest
import selene
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach, selenoid


def pytest_addoption(parser):
    parser.addoption('--context', action='store', default='local')


@pytest.fixture(scope="function")
def setup_browser(request):
    context = request.config.getoption('--context')

    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.base_url = 'https://demoqa.com'

    options = Options()
    options.page_load_strategy = 'eager'

    browser.config._wait_decorator = selene.support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    if context == 'selenoid':
        selenoid.setup(options, webdriver, browser)

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
