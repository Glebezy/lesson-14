import os


def setup(options, webdriver, browser):
    selenoid_login = os.getenv('SELENOID_LOGIN')
    selenoid_password = os.getenv('SELENOID_PASS')
    selenoid_url = os.getenv('SELENOID_URL')

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "125.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_password}@{selenoid_url}/wd/hub",
        options=options)

    browser.config.driver = driver
