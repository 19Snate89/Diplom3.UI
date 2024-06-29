import random

class UserData:
    USER_CREDS = {
        'email': 'user.testovich@gmail.com',
        'password': 'Password2',
        'name': 'test1'
        }

class Urls:
    MAIN_PAGE = 'https://stellarburgers.nomoreparties.site/'
    ORDERS_PAGE = f'{MAIN_PAGE}feed'
    LOGIN_PAGE = f'{MAIN_PAGE}login'
    REGISTER_PAGE = f'{MAIN_PAGE}register'
    REMIND_PASSWORD_PAGE = f'{MAIN_PAGE}forgot-password'
    RESET_PASSWORD_PAGE = f'{MAIN_PAGE}reset-password'
    PROFILE_PAGE = f'{MAIN_PAGE}account/profile'
    HISTORY_PAGE = f'{MAIN_PAGE}account/order-history'

class TitleTexts:
    LOGIN_TITLE = "Вход"
    ORDERS_FEED_TITLE = "Лента заказов"
    CONSTRUCTOR_TITLE = "Соберите бургер"


class helper:
    def random_choose(self, list_len):
        number = random.randint(0, len(list_len)-1)
        return list_len[number]

