from locators import StarBurgerMain, StarBurgerLogin, StarBurgerRegistration, StarBurgerRemindPassword
from config import URL, USER_DATA
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLoginBurger:

    def test_login_page(self, driver):
        driver.get(f'{URL}login')
        name_title = driver.find_element(*StarBurgerLogin.LOGIN_TITLE)
        assert name_title.text == 'Вход', f'Неверный заголовок формы авторизации: {name_title.text}'
        assert driver.find_element(*StarBurgerLogin.REG_BUTTON)
        assert driver.find_element(*StarBurgerLogin.REMIND_BUTTON)

    def test_login_positive_result(self, driver):
        driver.get(f'{URL}login')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerLogin.LOGIN_BUTTON))

        email = driver.find_element(*StarBurgerLogin.EMAIL_FIELD)
        email.send_keys(USER_DATA['email'])

        password = driver.find_element(*StarBurgerLogin.PASS_FIELD)
        password.send_keys(USER_DATA['password'])

        driver.find_element(*StarBurgerLogin.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerMain.INGRIDIENTS_SECTION))
        url = driver.current_url
        assert url == URL

    def test_login_with_incorrect_password(self, driver):
        driver.get(f'{URL}login')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerLogin.LOGIN_BUTTON))

        email = driver.find_element(*StarBurgerLogin.EMAIL_FIELD)
        email.send_keys('1234')

        password = driver.find_element(*StarBurgerLogin.PASS_FIELD)
        password.send_keys('12345')

        driver.find_element(*StarBurgerLogin.LOGIN_BUTTON).click()

        error_text = driver.find_element(*StarBurgerLogin.ERROR_TEXT)
        assert error_text

    def test_login_with_incorrect_data(self, driver):
        driver.get(f'{URL}login')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerLogin.LOGIN_BUTTON))

        email = driver.find_element(*StarBurgerLogin.EMAIL_FIELD)
        email.send_keys('1234')

        password = driver.find_element(*StarBurgerLogin.PASS_FIELD)
        password.send_keys('123456')

        driver.find_element(*StarBurgerLogin.LOGIN_BUTTON).click()

        url = driver.current_url
        assert url == f'{URL}login'

    def test_login_from_account_entry_button(self, driver):
        driver.get(URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerMain.ACCOUNT_ENTRY_BUTTON)).click()
        url = driver.current_url
        assert url == f'{URL}login'
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerLogin.LOGIN_BUTTON))

        email = driver.find_element(*StarBurgerLogin.EMAIL_FIELD)
        email.send_keys(USER_DATA['email'])

        password = driver.find_element(*StarBurgerLogin.PASS_FIELD)
        password.send_keys(USER_DATA['password'])

        driver.find_element(*StarBurgerLogin.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerMain.INGRIDIENTS_SECTION))
        url = driver.current_url
        assert url == URL

    def test_login_from_personal_cabinet_button(self, driver):
        driver.get(URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerMain.PERSONAL_CABINET_BUTTON)).click()
        url = driver.current_url
        assert url == f'{URL}login'

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerLogin.LOGIN_BUTTON))

        email = driver.find_element(*StarBurgerLogin.EMAIL_FIELD)
        email.send_keys(USER_DATA['email'])

        password = driver.find_element(*StarBurgerLogin.PASS_FIELD)
        password.send_keys(USER_DATA['password'])

        driver.find_element(*StarBurgerLogin.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerMain.INGRIDIENTS_SECTION))
        url = driver.current_url
        assert url == URL

    def test_login_from_registration_form(self, driver):
        driver.get(f'{URL}register')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerRegistration.LOGIN_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerLogin.LOGIN_BUTTON))

        email = driver.find_element(*StarBurgerLogin.EMAIL_FIELD)
        email.send_keys(USER_DATA['email'])

        password = driver.find_element(*StarBurgerLogin.PASS_FIELD)
        password.send_keys(USER_DATA['password'])

        driver.find_element(*StarBurgerLogin.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerMain.INGRIDIENTS_SECTION))
        url = driver.current_url
        assert url == URL

    def test_login_from_remind_password_form(self, driver):
        driver.get(f'{URL}login')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerLogin.REMIND_BUTTON)).click()
        url = driver.current_url
        assert url == f'{URL}forgot-password'

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerRemindPassword.LOGIN_BUTTON)).click()

        email = driver.find_element(*StarBurgerLogin.EMAIL_FIELD)
        email.send_keys(USER_DATA['email'])

        password = driver.find_element(*StarBurgerLogin.PASS_FIELD)
        password.send_keys(USER_DATA['password'])

        driver.find_element(*StarBurgerLogin.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerMain.INGRIDIENTS_SECTION))
        url = driver.current_url
        assert url == URL



