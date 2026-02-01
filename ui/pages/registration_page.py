import allure

from playwright.sync_api import Page

from ui.base.base_assertions import Assertions
from ui.base.base_page import BasePage
from ui.base.locators import (
    RegistrationLocators as RL,
    MainPageLocators as MPL,
    LoginLocators as LL,
    Urls
)


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, Urls.BASE_URL)
        self.assertions = Assertions(page, Urls.BASE_URL)

    @allure.step('Открыть страницу регистрации')
    def open_registration_page(self):
        self.open(self.base_url)
        self.click_on_element(MPL.account_btn)
        self.click_on_element(LL.registration_btn)

    @allure.step('Заполнить поле "Имя"')
    def fill_name_field(self, name):
        self.fill_field(RL.name_field, name)

    @allure.step('Заполнить поле "Email"')
    def fill_email_field(self, email):
        self.fill_field(RL.email_field, email)

    @allure.step('Заполнить поле "Пароль"')
    def fill_password_field(self, password):
        self.fill_field(RL.password_field, password)

    @allure.step('Нажать кнопку "Зарегистрироваться"')
    def submit_btn_click(self):
        self.click_on_element(RL.submit_btn)
