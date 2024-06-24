import allure
from selenium import webdriver
from helpers.data import UserData, Urls
from Pages.BasePage import BasePage
from PageObject.LoginPageLocator import LoginPageLocator, RemindPassword




class LoginPage(BasePage):

    def __init__(self, driver: webdriver):
        self.driver = driver

    @allure.step('Выполняем переход на страницу авторизации')
    def open_loging_page(self):
        self.navigate(Urls.LOGIN_PAGE)

    @allure.step('Вводим Email')
    def input_email(self):
        self.enter_text(LoginPageLocator.EMAIL_FIELD, UserData.USER_CREDS['email'])


    @allure.step('Вводим Пароль')
    def input_password(self):
        self.enter_text(LoginPageLocator.PASS_FIELD, UserData.USER_CREDS['password'])

    @allure.step('Нажимаем кнопку "Войти"')
    def click_login_button(self):
        self.click_element(LoginPageLocator.LOGIN_BUTTON)

    @allure.step('Нажимаем кнопку "Выйти"')
    def click_logout_button(self):
        self.click_element(LoginPageLocator.LOGOUT_BUTTON)

    @allure.step('Нажимаем кнопку "История заказов"')
    def click_history_order__button(self):
        self.click_element(LoginPageLocator.ORDERS_HISTORY)

    @allure.step('Нажимаем кнопку "Восстановления пароля"')
    def click_remind_password_button(self):
        self.click_element(LoginPageLocator.REMIND_PASSWORD_BUTTON)

    @allure.step('Нажимаем кнопку "Восстановить"')
    def click_remind_button(self):
        self.click_element(RemindPassword.REMIND_BUTTON)

    @allure.step('Выполняем переход на страницу авторизации')
    def open_forgot_password_page(self):
        self.navigate(Urls.REMIND_PASSWORD_PAGE)

    @allure.step('Вводим пароль на странице восстановления')
    def enter_password_to_recovery_field(self):
        self.enter_text(RemindPassword.PASSWORD_FIELD, 'Password1')

    @allure.step('Нажимаем кнопку "Скрыть/Открыть пароль"')
    def click_show_password_button(self):
        self.click_element(RemindPassword.SHOW_PASSWORD_BUTTON)


    @allure.step('Проверяем отображение скрытого пароля')
    def check_showing_password(self):
        self.find_element(RemindPassword.SHOW_PASSWORD_BUTTON)
