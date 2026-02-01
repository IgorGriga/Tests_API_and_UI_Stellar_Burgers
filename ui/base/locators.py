class Urls:
    BASE_URL = 'https://stellarburgers.education-services.ru/'
    LOGIN = f'{BASE_URL}login'


class MainPageLocators:
    account_btn = '//a[@href="/account"]'
    drop_area = '//div[contains(@class, "constructor-element_pos_top")]'
    basket_list_expect = 'div.constructor-element_pos_top'
    basket_list_element = '//span[@class="constructor-element__text"]'

    @staticmethod
    def ingredient_locator(name):
        return f'//p[text()="{name}"]'


class LoginLocators:
    email_field = '//input[@name="name"]'
    password_field = '//input[@name="Пароль"]'
    submit_btn = '//button[text()="Войти"]'
    registration_btn = '//a[@href="/register"]'


class AccountLocators:
    name_field = '//input[@name="Name"]'
    email_field = '//input[@type="text" and @name="name"]'
    exit_btn = '//button[text()="Выход"]'


class RegistrationLocators:
    name_field = '//label[text()="Имя"]/following-sibling::input'
    email_field = '//label[text()="Email"]/following-sibling::input'
    password_field = '//label[text()="Пароль"]/following-sibling::input'
    submit_btn = '//button[text()="Зарегистрироваться"]'
