import allure
import pytest

from ui.data.test_data import TestData
from ui.pages.main_page import MainPage


@allure.title('Создание бургера')
@allure.description('Успешное создание бургера')
@pytest.mark.smoke
@pytest.mark.burger_build
def test_burger_build(authorized_user):
    page = MainPage(authorized_user['page'])
    page.open_main_page()
    page.set_item('accessToken', authorized_user['accessToken'])
    page.set_item('refreshToken', authorized_user['refreshToken'])

    page.build_burger(TestData.burger)
    actual_burger = page.get_basket_list()
    page.assertions.assert_equal(actual_burger, TestData.burger)


@allure.title('Авторизация после создания бургера')
@allure.description('Бургер не изменился после авторизации')
@pytest.mark.smoke
@pytest.mark.burger_build_and_login
def test_burger_build_and_login(deferred_authorization):
    page = MainPage(deferred_authorization['page'])
    page.open_main_page()
    page.build_burger(TestData.burger)
    page.login(
        deferred_authorization['email'],
        deferred_authorization['password'])
    actual_burger = page.get_basket_list()
    page.assertions.assert_equal(actual_burger, TestData.burger)
