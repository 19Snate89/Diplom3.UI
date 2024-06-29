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
    ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']") # Кнопка "Лента Заказов" перехода к разделу с начинками на главной форме
    ACCOUNT_ENTRY_BUTTON = (By.XPATH, "//button[text() = 'Войти в аккаунт']")  # Кнопка "Конструктор" перехода к разделу с начинками на главной форме
    INGREDIENTS_SECTION = (By.XPATH, "//div[contains(@class, 'BurgerIngredients_ingredients')]")
    PERSONAL_CABINET_BUTTON = (By.XPATH, "//a[@href='/account']")
    HEADING_PAGE = (By.XPATH, "//h1[contains(@class, 'text')]")
    INGREDIENT_NAME_LIST = (By.XPATH, "//a[contains(@class, 'BurgerIngredient')]/p")
    MODAL_INGREDIENT = (By.XPATH, "//h2[text()='Детали ингредиента']")
    MODAL_INGREDIENT_CLOSE_BUTTON = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]')
    INGREDIENT_COUNTER = (By.XPATH, '//div[contains(@class, "counter")]')
    BURGER_BASKET = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')
    BREAD = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]')
    ORDER_BUTTON = (By.XPATH, "//button[text() = 'Оформить заказ']")
    MODAL_ORDER = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")
    MODAL_ORDER_CLOSE_BUTTON = (By.XPATH, "//button[@type='button']")
    ORDER_HISTORY_LIST = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]")
    MODAL_ORDER_DETAILS = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]")
    COUNT_ALL_ORDER_FEED = (By.XPATH, "//div[@class='undefined mb-15']/p[contains(@class, 'OrderFeed_number')]")
    COUNT_TODAY_ORDER_FEED = (By.XPATH, "//div[contains(@class, 'OrderFeed_ordersData')]/div[last()]/p[last()]")
    NUMBER_ORDER = (By.XPATH, '//h2[contains(@class, "Modal_modal__title")]')
    ORDERS_IN_WORK = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li')
    NUMBERS_ORDERS_LIST = (By.XPATH, "//p[@class='text text_type_digits-default']")  # Список заказов пользователя
