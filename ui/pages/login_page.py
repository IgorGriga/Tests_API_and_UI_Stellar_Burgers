import allure

from playwright.sync_api import Page

from ui.base.base_assertions import Assertions
from ui.base.base_page import BasePage
from ui.base.locators import (
    MainPageLocators as MPL,
    LoginLocators as LL,
    AccountLocators as AL,
    Urls
)


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, Urls.BASE_URL)
        self.assertions = Assertions(page, Urls.BASE_URL)

    @allure.step('Открыть главную страницу')
    def open_main_page(self):
        self.open(self.base_url)

    @allure.step('Нажать кнопку "Личный кабинет"')
    def click_account_button_on_main_page(self):
        self.click_on_element(MPL.account_btn)

    @allure.step('Заполнить поле "Email"')
    def fill_email_field(self, email):
        self.fill_field(LL.email_field, email)

    @allure.step('Заполнить поле "Пароль"')
    def fill_password_field(self, password):
        self.fill_field(LL.password_field, password)

    @allure.step('Нажать кнопку "Войти"')
    def submit_btn_click(self):
        self.click_on_element(LL.submit_btn)

    @allure.step('Проверка авторизации')
    def check_login(self, name, email):
        self.assertions.should_be_visible(MPL.basket_list_expect, err_msg='Ошибка загрузки главной страницы после авторизации')
        self.click_account_button_on_main_page()
        actual_name = self.get_attribute(AL.name_field, 'value')
        actual_email = self.get_attribute(AL.email_field, 'value')
        self.assertions.assert_equal(actual_name, name, err_msg='Фактическое имя пользователя не совпадает с ожидаемым')
        self.assertions.assert_equal(actual_email, email, err_msg='Фактический email не совпадает с ожидаемым')
