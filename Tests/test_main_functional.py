from helpers.data import Urls, TitleTexts
import allure

class TestMainFunction:

    @allure.title('Проверка перехода по кнопке "Лента заказов"')
    def test_click_order_feed(self, base_page):
        mp = base_page
        mp.open_main_page()
        mp.click_order_feed_button()
        url = mp.get_url()
        assert url == Urls.ORDERS_PAGE
        assert mp.check_heading_page() == TitleTexts.ORDERS_FEED_TITLE

    @allure.title('Проверка перехода по кнопке "Конструктор"')
    def test_click_constructor(self, base_page):
        mp = base_page
        mp.open_order_feed_page()
        mp.click_constructor_button()
        url = mp.get_url()
        assert url == Urls.MAIN_PAGE
        assert mp.check_heading_page() == TitleTexts.CONSTRUCTOR_TITLE

    @allure.title('Проверка всплывающего окна с деталями при нажатии на ингредиент')
    def test_modal_after_click_ingredient(self, base_page):
        mp = base_page
        mp.open_main_page()
        mp.open_random_ingredient()
        assert mp.check_modal_ingredient()

    @allure.title('Проверка закрытия всплывающего окна')
    def test_close_modal_window(self, base_page):
        mp = base_page
        mp.open_main_page()
        mp.open_random_ingredient()
        mp.click_close_modal_button()
        assert mp.check_invisibility_modal_ingredient()

    @allure.title('Проверка изменения счетчика выбранного ингредиента')
    def test_change_count(self, base_page):
        mp = base_page
        mp.open_main_page()
        mp.drag_and_drop_bread()
        count = mp.get_count()
        assert int(count) == 2

    @allure.title('Проверка оформления заказа пользователем')
    def test_create_user_order(self, login_page):
        lp = login_page
        lp.open_loging_page()
        lp.input_email()
        lp.input_password()
        lp.click_login_button()
        lp.click_constructor_button()
        lp.drag_and_drop_bread()
        lp.click_order_button()
        assert lp.check_modal_order()

class TestOrderFeed:

    @allure.title('Проверка всплывающего окна деталей заказа при выборе заказа')
    def test_modal_when_open_order(self, base_page):
        mp = base_page
        mp.open_order_feed_page()
        mp.open_random_order()
        assert mp.check_modal_details_of_order()

    @allure.title('Проверка увеличения счетчика выполненного за все время, после оформления заказа')
    def test_increase_count_all_orders(self, login_page):
        lp = login_page
        lp.open_loging_page()
        lp.input_email()
        lp.input_password()
        lp.click_login_button()
        lp.click_order_feed_button()
        number_orders = lp.get_number_all_orders()
        lp.click_constructor_button()
        lp.drag_and_drop_bread()
        lp.click_order_button()
        lp.open_order_feed_page()
        new_number_orders = lp.get_number_all_orders()
        assert int(new_number_orders) == int(number_orders)+1 or int(new_number_orders) > int(number_orders)

    @allure.title('Проверка увеличения счетчика выполненного за все сегодня, после оформления заказа')
    def test_increase_count_today_orders(self, login_page):
        lp = login_page
        lp.open_loging_page()
        lp.input_email()
        lp.input_password()
        lp.click_login_button()
        lp.click_order_feed_button()
        number_orders = lp.get_number_today_orders()
        lp.click_constructor_button()
        lp.drag_and_drop_bread()
        lp.click_order_button()
        lp.open_order_feed_page()
        new_number_orders = lp.get_number_today_orders()
        assert int(new_number_orders) == int(number_orders)+1

    @allure.title('Проверка отображения номера заказа в таблице "В работе:"')
    def test_create_order_in_work_list(self, login_page):
        lp = login_page
        lp.open_loging_page()
        lp.input_email()
        lp.input_password()
        lp.click_login_button()
        lp.click_constructor_button()
        lp.drag_and_drop_bread()
        lp.click_order_button()
        number_order = lp.get_number_create_order()
        lp.open_order_feed_page()
        assert lp.find_create_order_in_table_inwork(number_order)

    @allure.title('Проверка отображения заказов пользователя в ленте заказов')
    def test_user_orders_in_orders(self, login_page):
        lp = login_page
        lp.open_loging_page()
        lp.input_email()
        lp.input_password()
        lp.click_login_button()
        lp.click_constructor_button()
        lp.drag_and_drop_bread()
        lp.click_order_button()
        lp.click_close_modal_button()
        lp.click_personal_cabinet_button()
        lp.click_history_order_button()
        users_orders_numbers = lp.get_list_numbers_orders()
        lp.click_order_feed_button()
        orders_numbers = lp.get_list_numbers_orders()
        assert lp.check_users_order_in_orders(users_orders_numbers, orders_numbers)

