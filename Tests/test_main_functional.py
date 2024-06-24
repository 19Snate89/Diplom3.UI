import pytest

from Pages.BasePage import BasePage
from helpers.data import Urls
import allure

class TestMainFunction:

    @allure.title('Проверка перехода по кнопке "Лента заказов"')
    def test_click_order_feed(self, driver):
        mp = BasePage(driver)
        mp.open_main_page()
        mp.click_order_feed_button()
        url = mp.get_url()
        assert url == Urls.ORDERS_PAGE
        assert mp.check_heading_page() == 'Лента заказов'

    @allure.title('Проверка перехода по кнопке "Конструктор"')
    def test_click_constructor(self, driver):
        mp = BasePage(driver)
        mp.open_order_feed_page()
        mp.click_constructor_button()
        url = mp.get_url()
        assert url == Urls.MAIN_PAGE
        assert mp.check_heading_page() == 'Соберите бургер'

    @allure.title('Проверка всплывающего окна с деталями при нажатии на ингредиент')
    def test_modal_after_click_ingredient(self, driver):
        mp = BasePage(driver)
        mp.open_main_page()
        mp.open_random_ingredient()
        assert mp.check_modal_ingredient()

    @allure.title('Проверка закрытия всплывающего окна')
    def test_close_modal_window(self, driver):
        mp = BasePage(driver)
        mp.open_main_page()
        mp.open_random_ingredient()
        mp.click_close_modal_button()
        assert mp.check_modal_ingredient() == False

