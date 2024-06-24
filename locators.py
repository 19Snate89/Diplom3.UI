from selenium.webdriver.common.by import By

class StarBurgerRegistration:
    REG_TITLE = (By.XPATH, "//div[contains(@class, 'Auth_login')]/h2") # Заголовок страницы формы регистрации
    NAME_FIELD = (By.XPATH, "//label[text()='Имя']/../input") # Поле "Имя" на форме регистрации
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/../input") # Поле "Email" на форме регистрации
    PASS_FIELD = (By.XPATH, "//input[@name='Пароль']") # Поле "Пароль" на форме регистрации
    REG_BUTTON= (By.XPATH, "//button[text() = 'Зарегистрироваться']") # Кнопка "Зарегистрироваться" на форме регистрации
    ERROR_TEXT = (By.XPATH, "//p[@class = 'input__error text_type_main-default']")  # Ошибка ввода пароля на форме регистрации
    LOGIN_BUTTON = (By.XPATH, "//a[@href = '/login']")  # Кнопка "Войти" на форме регистрации

class StarBurgerLogin:
    LOGIN_TITLE = (By.XPATH, "//div[contains(@class, 'Auth_login')]/h2") # Заголовок страницы формы входа
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']") # Поле "Email" на форме входа
    PASS_FIELD = (By.XPATH, "//input[@name='Пароль']") # Поле "Пароль" на форме входа
    LOGIN_BUTTON = (By.XPATH, "//button[text() = 'Войти']") # Кнопка "Войти" на форме входа
    ERROR_TEXT = (By.XPATH, "//p[@class = 'input__error text_type_main-default']")  # Ошибка ввода пароля на форме входа
    REMIND_BUTTON = (By.XPATH, "//a[@href = '/forgot-password']")  # Кнопка "Восстановить пароль" на форме входа
    REG_BUTTON = (By.XPATH, "//a[@href = '/register']")  # Кнопка "Восстановить пароль" на форме входа

class StarBurgerMain:
    BREAD_BUTTON = (By.XPATH, "//span[text()='Булки']") # Кнопка "Булки" перехода к разделу с булками на главной форме
    CHECK_BREAD_BUTTON = (By.XPATH, "//span[text()='Булки']/..")  # Проверка активированной кнопки "Булки" перехода к разделу с булками на главной форме
    SAUCE_BUTTON = (By.XPATH, "//span[text()='Соусы']") # Кнопка "Соусы" перехода к разделу с соусами на главной форме
    CHECK_SAUCE_BUTTON = (By.XPATH, "//span[text()='Соусы']/..")  # Проверка активированной кнопки "Соусы" перехода к разделу с булками на главной форме
    TOPPINGS_BUTTON = (By.XPATH, "//span[text()='Начинки']") # Кнопка "Начинки" перехода к разделу с начинками на главной форме
    CHECK_TOPPINGS_BUTTON = (By.XPATH, "//span[text()='Начинки']/..")  # Проверка активированной кнопки "Начинки" перехода к разделу с булками на главной форме
    LOGO = (By.XPATH, "//div[contains(@class, 'logo')]")  # Лого на главной форме
    CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']") # Кнопка "Конструктор" перехода к разделу с начинками на главной форме
    ACCOUNT_ENTRY_BUTTON = (By.XPATH, "//button[text() = 'Войти в аккаунт']")  # Кнопка "Конструктор" перехода к разделу с начинками на главной форме
    INGRIDIENTS_SECTION = (By.XPATH, "//div[contains(@class, 'BurgerIngredients_ingredients')]")
    PERSONAL_CABINET_BUTTON = (By.XPATH, "//a[@href='/account']")

class StarBurgerRemindPassword:
    REMIND_TITLE = (By.XPATH, "//div[contains(@class, 'Auth_login')]/h2") # Заголовок страницы формы восстановления пароля
    EMAIL_FIELD = (By.XPATH, "//fieldset[1]//input") # Поле "Email" на форме восстановления пароля
    LOGIN_BUTTON = (By.XPATH, "//a[@href = '/login']")  # Кнопка "Войти" на форме восстановления пароля

class StarBurgerPersonalCabinet:
    ACCOUNT_TEXT = (By.XPATH, "//p[contains(@class, 'Account_text')]") # Заголовок страницы формы личного кабинета
    LOGOUT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")  # Кнопка "Войти" на форме личного кабинета
