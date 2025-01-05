import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from utils import attach


@pytest.fixture(scope="function")
def setup_browser(request):
    load_dotenv()

    selenoid_login = os.getenv('SELENOID_LOGIN')
    selenoid_password = os.getenv('SELENOID_PASS')
    selenoid_url = os.getenv('SELENOID_URL')

    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.base_url = 'https://demoqa.com'

    options = Options()

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "125.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    options.page_load_strategy = 'eager'

    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_password}@{selenoid_url}/wd/hub",
        options=options)

    browser.config.driver = driver

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
