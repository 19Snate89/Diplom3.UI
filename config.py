import faker
import random

URL = 'https://stellarburgers.nomoreparties.site/'
USER_DATA = {'name': 'Mary', 'email': 'luisli@example.com', 'password': 'mrRdbaNt_5'}
NAMES = ["John", "Mary", "Peter", "Susan", "David"]

def registration_data():
    fake = faker.Faker()
    email = fake.email()
    password = fake.password()
    random_number = random.randint(0, len(NAMES)-1)
    name = NAMES[random_number]
    return name, email, password
