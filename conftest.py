import pytest
from selenium import webdriver


def browser_settings():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return options

@pytest.fixture
def driver():
    chrome = webdriver.Chrome(options=browser_settings())
    chrome.get('https://stellarburgers.nomoreparties.site')
    yield chrome
    chrome.quit()