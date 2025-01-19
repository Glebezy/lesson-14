from selene import browser


def remove_banner():
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")


def open_page(endpoint: str):
    browser.open(endpoint)
    remove_banner()
