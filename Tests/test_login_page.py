from helpers.data import Urls, TitleTexts, UserData
import allure


class TestPersonalCabinet:

    @allure.title('Проверка захода в личный кабинет без авторизации')
    def test_personal_cabinet_page_without_authorisation(self, login_page):
        lp = login_page
        lp.open_main_page()
        lp.click_personal_cabinet_button()
        title, email, password = lp.check_loging_field()
        url = lp.get_url()
        assert url == Urls.LOGIN_PAGE
        assert title == TitleTexts.LOGIN_TITLE
        assert email, password

    @allure.title('Проверка захода в личный кабинет после авторизации')
    def test_personal_cabinet_page_with_authorisation(self, login_page):
        lp = login_page
        lp.open_loging_page()
        lp.input_email()
        lp.input_password()
        lp.click_login_button()
        lp.click_personal_cabinet_button()
        name, email = lp.check_personal_field()
        url = lp.get_url()
        assert url == Urls.PROFILE_PAGE
        assert name == UserData.USER_CREDS['name'] and email == UserData.USER_CREDS["email"]


    @allure.title('Проверка выхода из личного кабинета')
    def test_logout(self, login_page):
        lp = login_page
        lp.open_loging_page()
        lp.input_email()
        lp.input_password()
        lp.click_login_button()
        lp.click_personal_cabinet_button()
        lp.click_logout_button()
        title, email, password = lp.check_loging_field()
        url = lp.get_url()
        assert url == Urls.LOGIN_PAGE
        assert title == TitleTexts.LOGIN_TITLE
        assert email, password

    @allure.title('Проверка перехода на страницу "История заказов"')
    def test_open_user_history_orders(self, login_page):
        lp = login_page
        lp.open_loging_page()
        lp.input_email()
        lp.input_password()
        lp.click_login_button()
        lp.click_personal_cabinet_button()
        lp.click_history_order_button()
        url = lp.get_url()
        assert url == Urls.HISTORY_PAGE
        assert lp.check_order_list()




