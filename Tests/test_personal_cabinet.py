from Pages.LoginPage import LoginPage
from helpers.data import Urls
import allure


class TestPersonalCabinet:

    @allure.title('Проверка захода в личный кабинет без авторизации')
    def test_personal_cabinet_page_without_authorisation(self, driver):
        lp = LoginPage(driver)
        lp.open_main_page()
        lp.click_personal_cabinet_button()
        url = lp.get_url()
        assert url == Urls.LOGIN_PAGE

    @allure.title('Проверка захода в личный кабинет после авторизации')
    def test_personal_cabinet_page_with_authorisation(self, driver):
        lp = LoginPage(driver)
        lp.open_loging_page()
        lp.input_email()
        lp.input_password()
        lp.click_login_button()
        lp.click_personal_cabinet_button()
        url = lp.get_url()
        assert url == Urls.PROFILE_PAGE

    @allure.title('Проверка выхода из личного кабинета')
    def test_logout(self, driver):
        lp = LoginPage(driver)
        lp.open_loging_page()
        lp.input_email()
        lp.input_password()
        lp.click_login_button()
        lp.click_personal_cabinet_button()
        lp.click_logout_button()
        url = lp.get_url()
        assert url == Urls.LOGIN_PAGE

    @allure.title('Проверка выхода из личного кабинета')
    def test_logout(self, driver):
        lp = LoginPage(driver)
        lp.open_loging_page()
        lp.input_email()
        lp.input_password()
        lp.click_login_button()
        lp.click_personal_cabinet_button()
        lp.click_history_order__button()
        url = lp.get_url()
        assert url == Urls.HISTORY_PAGE



