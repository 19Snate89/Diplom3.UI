import pytest
from selenium import webdriver
from helpers.data import Urls

URL = 'https://stellarburgers.nomoreparties.site'

def browser_firefox_settings():
    options = webdriver.FirefoxOptions()
    options.add_argument("--start-maximized")
    return options

def browser_chrome_settings():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return options

@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None
    if request.param == 'firefox':
        browser = webdriver.Firefox(options=browser_firefox_settings())
    elif request.param == 'chrome':
        browser = webdriver.Chrome(options=browser_chrome_settings())
    browser.get(Urls.MAIN_PAGE)
    yield browser
    browser.quit()
