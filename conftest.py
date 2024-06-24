import pytest
from selenium import webdriver

URL = 'https://stellarburgers.nomoreparties.site'

def browser_settings():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return options

@pytest.fixture
def driver():
    chrome = webdriver.Chrome(options=browser_settings())
    chrome.get(URL)
    yield chrome
    chrome.quit()