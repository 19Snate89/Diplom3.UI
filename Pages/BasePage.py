import time

import allure
from selenium import webdriver
from PageObject.BasePageLocator import StarBurgerMain
from helpers.data import Urls, helper
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

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
            raise Exception(f'Не удалось найти элемент с локатором {elements}')
        return elements

    def invisible_element(self, locator: tuple):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))
        except Exception:
            raise Exception(f'Не удалось обнаружить скрытый элемент с локатором {element}')
        return element

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
    def check_invisibility_modal_ingredient(self):
        modal = self.invisible_element(StarBurgerMain.MODAL_INGREDIENT)
        return modal


    @allure.step('Нажимаем кнопку закрытия модального окна ингредиента')
    def click_close_modal_button(self):
        self.click_element(StarBurgerMain.MODAL_INGREDIENT_CLOSE_BUTTON)


    def drag_and_drop_element(self, locator):
        element = self.find_element(locator)
        target = self.find_element(StarBurgerMain.BURGER_BASKET)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, target).perform()

    @allure.step('Перетаскиваем булку в корзину')
    def drag_and_drop_bread(self):
        element = self.find_element(StarBurgerMain.BREAD)
        target = self.find_element(StarBurgerMain.BURGER_BASKET)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, target).perform()

    @allure.step('Проверяем счетчик ингредианта')
    def get_count(self):
        counter = self.get_text(StarBurgerMain.INGREDIENT_COUNTER)
        return counter

    @allure.step('Нажимаем кнопку "Оформить заказ"')
    def click_order_button(self):
        self.click_element(StarBurgerMain.ORDER_BUTTON)


    @allure.step('Проверяем открытие модального окна оформленного заказа')
    def check_modal_order(self):
        modal = self.find_element(StarBurgerMain.MODAL_ORDER)
        return modal

    @allure.step('Проверяем открытие модального окна оформленного заказа')
    def check_modal_details_of_order(self):
        modal = self.find_element(StarBurgerMain.MODAL_ORDER_DETAILS)
        return modal

    @allure.step('Открываем ингредиент')
    def open_random_order(self):
        h = helper()
        orders = self.wait_located_elements(StarBurgerMain.ORDER_HISTORY_LIST)
        order = h.random_choose(orders)
        text = order.text
        order.click()
        return text

    @allure.step('Получаем число выполненных заказов за все время')
    def get_number_all_orders(self):
        number_order = self.get_text(StarBurgerMain.COUNT_ALL_ORDER_FEED)
        return number_order

    @allure.step('Получаем число выполненных заказов за сегодня')
    def get_number_today_orders(self):
        number_order = self.get_text(StarBurgerMain.COUNT_TODAY_ORDER_FEED)
        return number_order

    @allure.step('Получаем номер заказа, после оформления')
    def get_number_create_order(self):
        time.sleep(2)
        number_order = self.get_text(StarBurgerMain.NUMBER_ORDER)
        return number_order

    @allure.step('Сверяем номер созданного заказа в таблице "В работе"')
    def find_create_order_in_table_inwork(self, order_number):
        time.sleep(3)
        orders_in_work = self.wait_located_elements(StarBurgerMain.ORDERS_IN_WORK)
        for order in orders_in_work:
            text = order.text
            if order_number in text:
                return True

    @allure.step('Получаем список номеров заказов в ленте заказов')
    def get_list_numbers_orders(self):
        list = []
        elements = self.wait_located_elements(StarBurgerMain.NUMBERS_ORDERS_LIST)
        for element in elements:
            list.append(element.text)
        return list

    @allure.step('Получаем список номеров заказов в ленте заказов')
    def check_users_order_in_orders(self, users_order, orders):
        count = 0
        for order in users_order:
            if order in orders:
                count += 1
        if count >= 1:
            return True



