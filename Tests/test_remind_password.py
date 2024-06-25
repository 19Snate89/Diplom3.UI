from Pages.LoginPage import LoginPage
from helpers.data import Urls
import allure


class TestRemindPassword:

    @allure.title('Проверка перехода на страницу восстановления')
    def test_redirect_to_remind_password(self, driver):
        lp = LoginPage(driver)
        lp.open_main_page()
        lp.click_personal_cabinet_button()
        lp.click_remind_password_button()
        url = lp.get_url()
        assert url == Urls.REMIND_PASSWORD_PAGE

    @allure.title('Проверка ввода Email и нажатия кнопки "Восстановить"')
    def test_enter_password_and_click_remind_button(self, driver):
        lp = LoginPage(driver)
        lp.open_forgot_password_page()
        lp.input_email()
        lp.click_remind_button()
        url = lp.get_url()
        assert url == Urls.RESET_PASSWORD_PAGE

    @allure.title('Проверка отображения пароля')
    def test_showing_password(self, driver):
        lp = LoginPage(driver)
        lp.open_forgot_password_page()
        lp.input_email()
        lp.click_remind_button()
        lp.enter_password_to_recovery_field()
        lp.click_show_password_button()
        assert lp.check_showing_password()



