import time

import allure
from selenium import webdriver
from PageObject.BasePageLocator import StarBurgerMain
from helpers.data import Urls, helper
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
            return element
        except Exception:
            raise Exception(f'Не удалось найти элемент с локатором {element}')


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
                element.click()
        except Exception:
            raise Exception(f'Не удалось кликнуть по элементу с локатором {element}')


    @allure.step('Произвели клик по кнопке "Личный кабинет"')
    def click_personal_cabinet_button(self):
        self.click_element(StarBurgerMain.PERSONAL_CABINET_BUTTON)

    @allure.step('Произвели клик по кнопке "Конструктор"')
    def click_constructor_button(self):
        self.click_element(StarBurgerMain.CONSTRUCTOR)

    @allure.step('Произвели клик по кнопке "Лента Заказов"')
    def click_order_feed_button(self):
        self.click_element(StarBurgerMain.ORDER_FEED)

    @allure.step('Произвели клик по лого "Stellar Burgers"')
    def click_logo_button(self):
        self.click_element(StarBurgerMain.LOGO)

    @allure.step('Открываем главную страницу "Stellar Burgers"')
    def open_main_page(self):
        self.navigate(Urls.MAIN_PAGE)

    @allure.step('Открываем страницу "Лента заказов"')
    def open_order_feed_page(self):
        self.navigate(Urls.ORDERS_PAGE)

    @allure.step('Получаем текст заголовка главной страницы')
    def check_heading_page(self):
        text = self.get_text(StarBurgerMain.HEADING_PAGE)
        return text

    @allure.step('Открываем ингредиент')
    def open_random_ingredient(self):
        h = helper()
        ingredients = self.wait_located_elements(StarBurgerMain.INGREDIENT_NAME_LIST)
        ingredient = h.random_choose(ingredients)
        text = ingredient.text
        ingredient.click()
        return text

    @allure.step('Проверяем открытие модального окна ингредиента')
    def check_modal_ingredient(self):
        modal = self.find_element(StarBurgerMain.MODAL_INGREDIENT)
        return modal

    @allure.step('Проверяем закрытие модального окна ингредиента')
    def check_modal_ingredient(self):
        modal = self.find_element(StarBurgerMain.MODAL_INGREDIENT)
        if modal:
            return True
        else:
            return False

    @allure.step('Нажимаем кнопку закрытия модального окна ингредиента')
    def click_close_modal_button(self):
        self.click_element(StarBurgerMain.MODAL_INGREDIENT_CLOSE_BUTTON)

