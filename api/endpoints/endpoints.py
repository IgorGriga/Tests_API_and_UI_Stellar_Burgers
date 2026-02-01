class Url:
    BASE_URL = 'https://stellarburgers.education-services.ru/api'


class Endpoints:
    REGISTER_USER = f'{Url.BASE_URL}/auth/register'
    LOGIN_USER = f'{Url.BASE_URL}/auth/login'
    USER_DATA = f'{Url.BASE_URL}/auth/user'
    USER_DELETE = f'{Url.BASE_URL}/auth/user'
    LOGOUT = f'{Url.BASE_URL}/auth/logout'


class Headers:
    COMMON = {
        'Content-Type': 'application/json'
    }
