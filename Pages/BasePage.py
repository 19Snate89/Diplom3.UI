import datetime
import time

import allure
from selenium import webdriver
from PageObject.BasePageLocator import StarBurgerMain
from helpers.data import Urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver: webdriver):
        self.driver = driver

    def navigate(self, url: str):
        return self.driver.get(url)

    @allure.step('Получаем текущуй URL карточки')
    def get_url(self):
        time.sleep(1)
        return self.driver.current_url

    def find_element(self, locator: tuple):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        except Exception:
            raise Exception(f'Не удалось найти элемент с локатором {element}')
        return element

    def wait_clickable_element(self, locator: tuple):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        except Exception:
            raise Exception(f'Не удалось найти элемент с локатором {element}')
        return element

    def wait_located_elements(self, locator: tuple):
        try:
            elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        except Exception:
            raise Exception(f'Не удалось найти элементы с локатором {elements}')
        return elements

    def enter_text(self, locator: tuple, text: str):
        try:
            element = self.find_element(locator)
            if element:
                element.send_keys(text)
        except Exception:
            raise Exception(f'Не удалось ввести значение в элемент с локатором {element}')

    def get_text(self, locator: tuple):
        try:
            element = self.find_element(locator)
            if element:
                return element.text
        except Exception:
            raise Exception(f'Не удалось получить текст элемента с локатором {element}')

    def click_element(self, locator: tuple):
        try:
            element = self.wait_clickable_element(locator)
            if element:
                self.wait_located_elements(locator)
                element.click()
        except Exception:
            raise Exception(f'Не удалось кликнуть по элементу с локатором {element}')

    def close_cookies(self):
        self.click_element(HomePageLocators.CLOSE_COOKIES)

    def switch_window(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
        except Exception:
            raise Exception(f'Не удалось выполнить переход на другую вкладку')

    def redirect(self):
        try:
            self.switch_window()
            self.find_element(HomePageLocators.REDIRECT)
            url = self.get_url()
        except Exception:
            raise Exception('Не получилось')
        return url

    def get_date(self):
        get_date = datetime.datetime.now()
        new_date = get_date + datetime.timedelta(days=2)
        date = datetime.datetime.strftime(new_date, '%d.%m.%y')
        return date

    @allure.step('Произвели клик по кнопке "Личный кабинет"')
    def click_personal_cabinet_button(self):
        self.click_element(StarBurgerMain.PERSONAL_CABINET_BUTTON)

    @allure.step('Произвели клик по кнопке "Конструктор"')
    def click_constructor_button(self):
        self.click_element(StarBurgerMain.CONSTRUCTOR)

    @allure.step('Произвели клик по лого "Stellar Burgers"')
    def click_constructor_button(self):
        self.click_element(StarBurgerMain.LOGO)

    @allure.step('Открываем главную страницу "Stellar Burgers"')
    def open_main_page(self):
        self.navigate(Urls.MAIN_PAGE)
