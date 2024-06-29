import allure
from selenium import webdriver
from helpers.data import UserData, Urls
from Pages.BasePage import BasePage
from Locators.LoginPageLocator import LoginPageLocator, RemindPassword, PersonalCabinetLocators




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
    def click_history_order_button(self):
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
        element = self.find_element(RemindPassword.SHOW_PASSWORD_BUTTON)
        return element

    @allure.step('Получаем список номеров заказа пользователя')
    def get_list_numbers_orders(self):
        list = []
        elements = self.wait_located_elements(LoginPageLocator.USER_NUMBERS_ORDERS_LIST)
        for element in elements:
            list.append(element.text)
        return list

    @allure.step('Проверяем отображение полей на странице входа')
    def check_loging_field(self):
        title = self.find_element(LoginPageLocator.LOGIN_TITLE).text
        email = self.find_element(LoginPageLocator.EMAIL_FIELD)
        password = self.find_element(LoginPageLocator.PASS_FIELD)
        return title, email, password

    @allure.step('Проверяем значения полей пользователя при входе в личный кабинет')
    def check_personal_field(self):
        name = self.find_element(PersonalCabinetLocators.NAME_FIELD).get_attribute('value')
        email = self.find_element(PersonalCabinetLocators.EMAIL_FIELD).get_attribute('value')
        return name, email

    @allure.step('Проверяем наличие списка заказов')
    def check_order_list(self):
        order = self.find_element(PersonalCabinetLocators.ORDERS_LIST)
        return order

    @allure.step('Проверяем поля и титул формы восстановления')
    def check_remind_password_fields(self):
        title = self.get_text(RemindPassword.REMIND_TITLE)
        email = self.find_element(RemindPassword.EMAIL_FIELD)
        button = self.find_element(RemindPassword.REMIND_BUTTON)
        return title, email, button

    @allure.step('Проверяем поля и титул формы отправки кода')
    def check_remind_code(self):
        title = self.get_text(RemindPassword.REMIND_TITLE)
        password = self.find_element(RemindPassword.PASSWORD_FIELD)
        code = self.find_element(RemindPassword.CODE_FIELD)
        button = self.find_element(RemindPassword.SAVE_BUTTON)
        return title, password, code, button