import allure
import pytest

from ui.pages.registration_page import RegistrationPage


@allure.title('Регистрация нового пользователя')
@allure.description('Успешная регистрация')
@pytest.mark.smoke
@pytest.mark.registration
def test_registration(for_registration):
    page = RegistrationPage(for_registration['page'])
    name = for_registration['name']
    email = for_registration['email']
    password = for_registration['password']
    page.open_registration_page()
    page.fill_name_field(name)
    page.fill_email_field(email)
    page.fill_password_field(password)
    page.submit_btn_click()
