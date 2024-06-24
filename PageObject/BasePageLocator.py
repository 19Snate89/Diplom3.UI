from selenium.webdriver.common.by import By
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
    INGREDIENTS_SECTION = (By.XPATH, "//div[contains(@class, 'BurgerIngredients_ingredients')]")
    PERSONAL_CABINET_BUTTON = (By.XPATH, "//a[@href='/account']")
