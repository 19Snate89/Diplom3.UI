from selenium.webdriver.common.by import By

class LoginPageLocator:

    LOGIN_TITLE = (By.XPATH, "//div[contains(@class, 'Auth_login')]/h2")  # Заголовок страницы формы входа
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")  # Поле "Email" на форме входа
    PASS_FIELD = (By.XPATH, "//input[@name='Пароль']")  # Поле "Пароль" на форме входа
    LOGIN_BUTTON = (By.XPATH, "//button[text() = 'Войти']")  # Кнопка "Войти" на форме входа
    ERROR_TEXT = (By.XPATH, "//p[@class = 'input__error text_type_main-default']")  # Ошибка ввода пароля на форме входа
    REMIND_PASSWORD_BUTTON = (By.XPATH, "//a[@href = '/forgot-password']")  # Кнопка "Восстановить пароль" на форме входа
    REG_BUTTON = (By.XPATH, "//a[@href = '/register']")  # Кнопка "Восстановить пароль" на форме входа
    ACCOUNT_TEXT = (By.XPATH, "//p[contains(@class, 'Account_text')]")  # Заголовок страницы формы личного кабинета
    LOGOUT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")  # Кнопка "Войти" на форме личного кабинета
    ORDERS_HISTORY = (By.XPATH, "//a[@href='/account/order-history']") # Кнопка перехода в историю заказов пользователя
    USER_NUMBERS_ORDERS_LIST = (By.XPATH, "//p[@class='text text_type_digits-default']") # Список заказов пользователя

class RemindPassword:

    REMIND_TITLE = (By.XPATH, "//div[contains(@class, 'Auth_login')]/h2") # Заголовок страницы формы восстановления пароля
    REMIND_BUTTON = (By.XPATH, "//button[text() = 'Восстановить']") # Кнопка "Восстановить"
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")  # Поле "Email" на форме восстановления
    SHOW_PASSWORD = (By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default input_status_active"]')
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")  # Поле "Email" на форме входа
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[@class='input__icon input__icon-action']")  # Кнопка скрыть/открыть пароль
