from locators import StarBurgerMain
from config import URL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTransitionIngridients:

    def test_default_active_button_breads(self, driver):
        driver.get(URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerMain.INGRIDIENTS_SECTION))
        check = driver.find_element(*StarBurgerMain.CHECK_BREAD_BUTTON).get_attribute('class')
        assert 'tab_type_current' in check


    def test_transition_to_breads(self, driver):
        driver.get(URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerMain.INGRIDIENTS_SECTION))
        driver.find_element(*StarBurgerMain.SAUCE_BUTTON).click()
        driver.find_element(*StarBurgerMain.BREAD_BUTTON).click()
        check = driver.find_element(*StarBurgerMain.CHECK_BREAD_BUTTON).get_attribute('class')
        assert 'tab_type_current' in check


    def test_transition_to_souce(self, driver):
        driver.get(URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerMain.INGRIDIENTS_SECTION))
        driver.find_element(*StarBurgerMain.SAUCE_BUTTON).click()
        check = driver.find_element(*StarBurgerMain.CHECK_SAUCE_BUTTON).get_attribute('class')
        assert 'tab_type_current' in check


    def test_transition_to_toppings(self, driver):
        driver.get(URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StarBurgerMain.INGRIDIENTS_SECTION))
        driver.find_element(*StarBurgerMain.TOPPINGS_BUTTON).click()
        check = driver.find_element(*StarBurgerMain.CHECK_TOPPINGS_BUTTON).get_attribute('class')
        assert 'tab_type_current' in check



