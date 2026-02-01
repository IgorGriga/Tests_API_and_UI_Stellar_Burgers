import allure
import pytest

from ui.pages.login_page import LoginPage


@allure.title('Авторизация пользователя')
@allure.description('Успешная авторизация')
@pytest.mark.smoke
@pytest.mark.authorization
def test_login(for_authorization):
    page = LoginPage(for_authorization['page'])
    name = for_authorization['name']
    email = for_authorization['email']
    password = for_authorization['password']
    page.open_main_page()
    page.click_account_button_on_main_page()
    page.fill_email_field(email)
    page.fill_password_field(password)
    page.submit_btn_click()
    page.check_login(name, email)
