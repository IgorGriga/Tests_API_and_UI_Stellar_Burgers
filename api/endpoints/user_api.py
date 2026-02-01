import allure
import requests

from api.endpoints.assertions import Assertions
from api.endpoints.endpoints import Endpoints, Headers


class UserAPI(Assertions):

    def __init__(self):
        super().__init__()
        self.access_token = None
        self.refresh_token = None

    @allure.step('Авторизация существующего пользователя')
    def authorization(self, email, password):
        self.response = requests.post(
            url = Endpoints.LOGIN_USER,
            json = {
                'email': email,
                'password': password
            },
            headers = Headers.COMMON
        )

        self.response_json = self.response.json()
        self.check_success('Ошибка авторизации: неправильный email или пароль')
        self.access_token = self.response_json['accessToken']
        self.refresh_token = self.response_json['refreshToken']

    def assert_if_user_authorized(self, err_msg = 'Пользователь авторизован'):
        assert (self.access_token is None and
                self.refresh_token is None), err_msg

    def assert_if_user_not_authorized(self, err_msg = 'Пользователь не авторизован'):
        assert (self.access_token is not None or
                self.refresh_token is not None), err_msg

    @allure.step('Проверка существования пользователя')
    def is_user_exists(self, name, email, password):
        self.assert_if_user_authorized('При проверке существования пользователя требуется отсутствие авторизации')

        response = requests.post(
            url = Endpoints.REGISTER_USER,
            json = {
                'email': email,
                'password': password,
                'name': name
            },
            headers = Headers.COMMON
        )

        is_exists = (not response.json()['success']
            and response.json()['message'] == 'User already exists')

        if not is_exists:
            self.authorization(email, password)
            self.user_delete()

        return is_exists

    @allure.step('Регистрация нового пользователя')
    def registration(self, name, email, password):
        self.response = requests.post(
            url = Endpoints.REGISTER_USER,
            json = {
                'email': email,
                'password': password,
                'name': name
            },
            headers = Headers.COMMON
        )

        self.response_json = self.response.json()
        self.check_success()

    @allure.step('Выход пользователя из системы')
    def logout(self):
        self.assert_if_user_not_authorized('Для выхода из системы пользователь должен быть авторизован')

        self.response = requests.post(
            url = Endpoints.LOGOUT,
            json = {
                'token': self.refresh_token
            },
            headers = Headers.COMMON
        )

        self.access_token = None
        self.refresh_token = None

    @allure.step('Запрос accessToken авторизованного пользователя')
    def get_access_token(self):
        return self.access_token

    @allure.step('Запрос refreshToken авторизованного пользователя')
    def get_refresh_token(self):
        return self.refresh_token

    @allure.step('Запрос данных пользователя')
    def userdata(self):
        self.assert_if_user_not_authorized('Для запроса данных пользователь должен быть авторизован')

        headers_with_access_token = {
            **Headers.COMMON,
            'Authorization': self.access_token
        }
        self.response = requests.get(
            url = Endpoints.USER_DATA,
            headers = headers_with_access_token
        )

        self.response_json = self.response.json()
        self.check_success()

        return self.response_json['user']

    @allure.step('Удаление пользователя')
    def user_delete(self):
        self.assert_if_user_not_authorized('Для удаления пользователь должен быть авторизован')

        headers_with_access_token = {
            **Headers.COMMON,
            'Authorization': self.access_token
        }
        self.response = requests.delete(
            url = Endpoints.USER_DELETE,
            headers = headers_with_access_token
        )

        self.response_json = self.response.json()
        self.check_success()
        self.access_token = None
        self.refresh_token = None

        return 'User deleted'
